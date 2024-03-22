# Import system libraries
import os

# Third-party imports
from neo4j import GraphDatabase
from openai import OpenAI

# Local application imports
from utils.gpt_helper import get_gpt_message
from utils.data_processing import process_cypher_output, read_json

# Gloabl variables: config files
__location__ = os.path.realpath(os.path.join(os.getcwd()))
__neo4j_config__ = "movies_db_config.json"
__open_ai_config__ = "open_ai_config.json"
__gpt_prompt_file__ = "movie_query_instruction.txt"


class MovieChatbot:
    def __init__(self, 
                 config_path: str = os.path.join(__location__, 'config/'),
                 utils_path: str = os.path.join(__location__, 'utils/')):
        # Get config filepath
        self.neo4j_config_json_file = str(config_path + __neo4j_config__)
        self.open_ai_config_json_file = str(config_path + __open_ai_config__)
        self.gpt_prompt_file = str(utils_path + __gpt_prompt_file__)
        # Load connfig files
        self.neo4j_config_data = read_json(self.neo4j_config_json_file)
        self.open_ai_config_data = read_json(self.open_ai_config_json_file)
        # Load neo4j DB parameters
        self.neo4j_uri = self.neo4j_config_data.get("neo4j_uri", "neo4j+ssc://demo.neo4jlabs.com")
        self.neo4j_username = self.neo4j_config_data.get("neo4j_username", "movies")
        self.neo4j_password = self.neo4j_config_data.get("neo4j_password", "movies")
        # Load open_ai key
        self.open_ai_key = self.open_ai_config_data.get("open_ai_key", "")
        if not self.open_ai_key or self.open_ai_key == "YOUR_API_KEY_HERE": 
            print("WARNING! Please provide OpenAI API key here: config/open_ai.json and re-run MoBot! Thank you.")
            exit(1)
        # Initialise graph DB driver for querying neo4j
        self.driver = GraphDatabase.driver(uri=self.neo4j_uri, 
                                           auth=(self.neo4j_username, 
                                                 self.neo4j_password))
        # Initialise OpenAI client
        self.open_ai_client = OpenAI(api_key=self.open_ai_key)
        # Param to store user input, bot responses, and user feedback
        self.memory = []

    def close(self):
        self.driver.close()
    
    def remember(self, user_input, bot_response, user_feedback=None):
        interaction = {
            "user_input": user_input,
            "bot_response": bot_response,
            "user_feedback": user_feedback
        }
        self.memory.append(interaction)

    def query_database(self, query):
        with self.driver.session() as session:
            try:
                result = session.run(query)
            except Exception as e:
                return None
            return [record for record in result]

    def respond(self, user_input):
        # Dynamically creates Cypher queries from natural language input
        cypher_query = get_gpt_message(client=self.open_ai_client, 
                                       prompt_file=self.gpt_prompt_file,
                                       user_input=user_input, 
                                       past_conversations=self.memory[-5:])
        if cypher_query == "query not available": 
            self.remember(user_input=user_input, bot_response={})
            return "MoBot: Could not produce query for your input. Try a different question, please?"
        else:
            query_results = self.query_database(query=cypher_query)
            if query_results:
                formatted_results, processed_results = process_cypher_output(query_results=query_results)
                self.remember(user_input=user_input, bot_response=processed_results)
                return formatted_results
            return "MoBot: No results were found. Sorry!"

    def get_feedback(self):
        feedback = input("MoBot: Was my response helpful? (yes/no): ")
        if self.memory:
            self.memory[-1]["user_feedback"] = feedback
        if feedback.lower() == "yes":
            print("MoBot: Great! I'm glad I could help. ")
        elif feedback.lower() == "no":
            print("MoBot: I'm sorry. I'll try to do better next time.")
        else:
            print("MoBot: I'm sorry. I only accept yes/no feedback, currently!")
        

    def start_chat(self):
        print("\n--------------------------------------------------------------------------------------\n")
        print("Hello, there! My name is MoBot and I know a little bit about movies.")
        print("So, ask me about things related movies, please. (To end the chat type: 'exit')")
        print("\n--------------------------------------------------------------------------------------\n")
        counter = 1
        while True:
            print("\n*** ", counter, " ***")
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("MoBot: Goodbye!")
                break
            bot_response = self.respond(user_input)
            print("MoBot: ", bot_response)
            self.get_feedback()
            counter += 1
