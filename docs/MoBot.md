# MoBot: A Simple Memory Chatbot Project

## Introduction

This document provides a detailed overview of MoBOt, a Simple Memory Chatbot project, designed to interact with users by answering questions-- dynamically generating queries in Cypher format to interact with a Neo4J database and extract answers for user queries in natural language. The chatbot integrates OpenAI's GPT models for enhanced conversation and query generation capabilities, including the use of conversational context for co-reference resolution.

---

## Project Objectives

1. **Terminal-Based Interaction**: Develop a chatbot capable of running directly in a terminal, providing an interactive command-line interface for users.

2. **Neo4J Database Integration**: Create a sandbox Neo4J database using the link [here](https://neo4j.com/developer/example-data/). The chatbot should be able to query and answer questions from the “Movie” toy database.

3. **Dynamic User Queries**: The chatbot must seek input from users about their questions or the information they seek, demonstrating the ability to understand and respond to a wide range of queries related to the database content.

4. **Memory Functionality**: Implement simple memory capabilities, allowing the chatbot to recall and reference previous messages within the conversation. This enhances the chatbot's ability to maintain context and continuity in discussions.

5. **Feedback Mechanism**: Incorporate a feedback mechanism within the chatbot's interaction flow, asking users to rate the quality of responses received. This feedback should influence the chatbot's future responses and learning, improving over time.

6. **Language and Tools**: Use any programming language of your choice, but we recommend Python. Feel free to use a chat bot framework such as LangChain, Rasa, or ChatterBot to build your chat bot.

7. **Advanced Language Models** (Optional): Integrate advanced language models, specifically recommending GPT-4 or GPT-4-Turbo, for dynamic query generation, natural language understanding, and generating coherent, contextually relevant responses.

---

## Requirements

Before you begin, ensure you have the following prerequisites met:

- **Python 3.8+**: The programming language used for development.
- **Neo4J Database**: Essential for storing and querying movie data.
- **OpenAI API Key**: Required for accessing GPT models for dynamic query generation and conversation understanding.
- **Anaconda or Miniconda**: For managing Python environments and dependencies, ensuring isolated and reproducible setups.

---

## Project Setup Steps

Follow these steps to set up and start the chatbot project:

1. **Install Python 3.8 or Higher**: Download and install the appropriate version for your operating system from [python.org](https://www.python.org/downloads/).

2. **Set Up Neo4J Database**:
   - Install Neo4J following the instructions on the [Neo4J website](https://neo4j.com/download/).
   - Populate the database with the "Movie" example data as described in the [Neo4J documentation](https://neo4j.com/developer/example-data/).

3. **Obtain an OpenAI API Key**:
   - Create an account at [OpenAI](https://openai.com/api/).
   - Follow the instructions to generate an API key.

4. **Install Anaconda or Miniconda**:
   - Choose and install Anaconda or Miniconda from their respective websites. This will be used for managing your project's environment.

5. **Create and Activate the Conda Environment**:
   - Use the `environment.yml` file provided with the project to create an environment named `smc-rilla`: `conda env create -f environment.yml`.
   - Activate the environment: `conda activate smc-rilla`.

6. **Update Configuration with OpenAI API Key**:
   - Locate the configuration section in the chatbot's code.
   - Replace the placeholder with your OpenAI API key.

7. **Run the Chatbot**:
   - Navigate to the project directory in your terminal.
   - Run the chatbot script: `python chatbot.py`.
   - Interact with the chatbot through your terminal.

8. **Exiting the Chatbot**:
   - To exit the chatbot conversation at any time, type `exit`. The chatbot will terminate the session.

---

## Data Overview

The chatbot utilizes a Neo4J database populated with movie-related data. This includes information on movies, actors, directors, and their relationships (e.g., acted in, directed by). The data model is designed to support complex queries about movie industry relationships and filmography. The database schema below provides a comprehensive overview of the Movie database.

### Database Schema

    Nodes:

        - Person: Represents an individual who can have various relationships with movies and other people.
            Properties:
                id: Unique identifier for the person.
                born: The year the person was born.
                name: The name of the person.
        
        - Movie: Represents a film that can have various people related to it in different capacities (e.g., actors, directors).
            Properties:
                id: Unique identifier for the movie.
                released: The year the movie was released.
                tagline: A short text introducing the theme or appeal of the movie.
                title: The title of the movie.
                votes: The number of votes or ratings the movie has received.

    Relationships:

        ACTED_IN: Connects a Person to a Movie to indicate that the person acted in that movie.
        REVIEWED: Connects a Person to a Movie to indicate that the person reviewed that movie.
        PRODUCED: Connects a Person to a Movie to indicate that the person produced that movie.
        WROTE: Connects a Person to a Movie to indicate that the person wrote the movie.
        FOLLOWS: Connects a Person to another Person to indicate that one follows the other (this represents some form of professional or personal relationship).
        DIRECTED: Connects a Person to a Movie to indicate that the person directed the movie.

---

## Chatbot Setup with OpenAI for Dynamic Query Generation

### Overview

The chatbot leverages OpenAI's GPT models to dynamically generate Cypher queries based on user input. This approach allows for natural language processing and understanding, enabling the chatbot to construct and execute database queries without predefined templates.

### Co-reference Resolution

Utilizing the last five conversations, the chatbot enhances query accuracy and relevance through co-reference resolution. This process helps the chatbot understand pronouns and references in the conversation, ensuring that responses are contextually appropriate.

### Steps

1. **Environment Setup**: Follow the README instructions to set up your Python environment and install necessary dependencies.
2. **API Key Configuration**: Insert your OpenAI API key in the designated placeholder within the chatbot's code.
3. **Running the Chatbot**: Execute the chatbot script and begin interacting with it through the terminal.

---

## Pros and Cons

### Pros

- **Dynamic Interaction**: Ability to generate queries on-the-fly allows for a flexible and engaging user experience.
- **Advanced NLP**: Integration with GPT models provides sophisticated natural language understanding and response generation.
- **Contextual Awareness**: Uses recent conversation history for co-reference resolution, improving response relevance.

### Cons

- **Dependency on OpenAI API**: Requires access to OpenAI API and valid API key, potentially incurring costs.
- **Multihop Query Generation**: While ChatGPT is effective in generating dynamic queries from user input, it currently struggles to build multiple queries for complex requests.

---

## Examples

### Example 1

![Example-1](example-1.png)

In example-1, we can observe context tracking in user input. Here, the main entity "Tom Hanks" has multiple attributes, and the chatbot is capable of tracking the user's questions related to the registered entity "Tom Hanks" and providing appropriate answers.

### Example 2

![Example-2](example-1.png)

---

## Improvements and Future Work

- **User Interface Enhancements**: Developing a web-based interface for the chatbot could make it more accessible and user-friendly.
- **Expansion of Database**: Including more data points and relationships in the Neo4J database would allow for richer interactions and responses.
- **Personalization**: Implementing user profiles and personalized recommendations based on past interactions could enhance user engagement.
- **Offline Functionality**: Reducing dependency on the OpenAI API for certain operations could improve performance and reduce costs.

---
