from neo4j import GraphDatabase
from openai import OpenAI
from gpt_helper import get_gpt_message


class MovieChatbot:
    def __init__(self, neo4j_uri, neo4j_username, neo4j_password, open_ai_key):
        self.driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))
        self.memory = []
        self.open_ai_client = OpenAI(api_key=open_ai_key)

    def close(self):
        self.driver.close()

    def remember(self, message):
        self.memory.append(message)
    
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
        
    def process_cypher_output(self, query_results):
        """
        Processes a list of neo4j.Record objects, extracting and formatting
        the data based on available keys in each Record. Handles cases where
        the data includes lists by converting all elements to strings.

        :param results: List of neo4j.Record objects.
        :return: A string representing the extracted data, formatted for display.
        """
        if not query_results:
            return "MoBot: No results found."
        # Initialize a dictionary to hold the data extracted from each record.
        processed_data = {}
        for record in query_results:
            for key in record.keys():
                # Ensure the key exists in the dictionary and initialize if not.
                if key not in processed_data:
                    processed_data[key] = []
                value = record[key]
                # Check if the value is a list and convert elements to strings if so.
                if isinstance(value, list):
                    value = [str(element) for element in value]
                # Append the possibly converted value to the list under its key.
                processed_data[key].append(value)
        # Format the extracted data for display.
        formatted_responses = []
        for key, values in processed_data.items():
            # Convert all elements to strings, handling both flat and nested lists.
            formatted_values = [
                ", ".join(str(item) for item in value) if isinstance(value, list) else str(value) 
                for value in values
            ]
            formatted_response = f"{key}: " + ", ".join(formatted_values)
            formatted_responses.append(formatted_response)
        return "\n".join(formatted_responses), processed_data

    def respond(self, user_input):
        # Dynamically creates Cypher queries from natural language input
        cypher_query = get_gpt_message(client=self.open_ai_client, user_input=user_input, past_conversations=self.memory[-5:])
        if cypher_query == "query not available": 
            self.remember(user_input=user_input, bot_response={})
            return "MoBot: Could not produce query for your input. Try a different question, please?"
        else:
            query_results = self.query_database(query=cypher_query)
            if query_results:
                formatted_results, processed_results = self.process_cypher_output(query_results=query_results)
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

if __name__ == "__main__":
    db_uri = "neo4j+ssc://demo.neo4jlabs.com"
    db_usr = "movies"
    db_pwd = "movies" 
    open_ai_key = ""  # ENTER YOUR OPENAI API KEY HERE
    chatbot = MovieChatbot(neo4j_uri=db_uri, 
                           neo4j_username=db_usr, 
                           neo4j_password=db_pwd, 
                           open_ai_key=open_ai_key)
    try:
        chatbot.start_chat()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    finally:
        chatbot.close()
