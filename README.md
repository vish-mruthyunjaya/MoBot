# MoBot: Q&A Chatbot that Queries Movie Database using Natural Language

This README provides instructions for setting up and running MoBOt, a Simple Memory Chatbot project, which includes a Python-based chatbot capable of conversing with users and performing various tasks based on user input. Please follow the steps outlined below to ensure a smooth setup and execution of the chatbot.

## Prerequisites

- [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) must be installed on your system.
- An active OpenAI API key is required for certain operations within the chatbot. You can obtain an API key by creating an account at [OpenAI](https://openai.com/api/).

## Installation

### 1. Installing the Environment

A Conda environment file named `environment.yml` is provided with this project to facilitate easy setup of the necessary Python environment and dependencies. To install this environment, navigate to the project directory in your terminal and run the following command:

```sh
conda env create -f environment.yml
```

This command will create a new Conda environment named `mobot` with all the dependencies specified in `environment.yml`.

### 2. Activating the Conda Environment

After successfully creating the environment, activate it by running:

```sh
conda activate mobot
```

You should now be in the `mobot` environment, indicated by the environment's name in your terminal prompt.

## Running the Python Code

### 1. Update Pre-requisites

Before running the chatbot, ensure you have updated the necessary configurations within the code:

- **OpenAI API Key**: Locate the placeholder for the `open_ai_key` in the code. Replace it with your actual OpenAI API key. This key is essential for the chatbot to access OpenAI's API for processing and generating responses.

### 2. Running the Chatbot

With the environment set up and the API key in place, you can now run the chatbot. Navigate to the directory containing the chatbot's Python script and execute:

```sh
python mobot.py
```

### 3 Exiting the Chatbot

To exit the chatbot conversation, simply type `exit` at any point. The chatbot will terminate the session and return control to your terminal.

## Additional Information

For further assistance or to report issues, please submit an issue on the project's repository.

---
