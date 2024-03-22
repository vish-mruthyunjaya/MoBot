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

- **OpenAI API Key Configuration**: The chatbot utilizes OpenAI's GPT models for generating responses and processing queries, requiring an OpenAI API key for access. For your convenience and security, the API key should now be specified in a configuration file rather than embedded directly in the code. Follow these steps to set it up:

  1. Navigate to the `config/` directory within the project folder. You will find a JSON configuration file named `open_ai_config.json`.

  2. Open the `config.json` file in a text editor. Look for the placeholder that says `"open_ai_key": "YOUR_API_KEY_HERE"`.

  3. Replace `"YOUR_API_KEY_HERE"` with your actual OpenAI API key, ensuring to keep the quotation marks. For example: `"open_ai_key": "sk-youractualapikeyhere"`.
  
  4. Save the changes to `open_ai_config.json`. The chatbot will now use this key to authenticate with OpenAI's API for all operations requiring AI processing.

### 2. Running the Chatbot

With the environment set up and the API key in place, you can now run the chatbot. Navigate to the directory containing the chatbot's Python script and execute:

```sh
python main.py
```

### 3 Exiting the Chatbot

To exit the chatbot conversation, simply type `exit` at any point. The chatbot will terminate the session and return control to your terminal.

## Additional Information

Refer [MoBot Documentation](docs/MoBot.md) for detailed information. For further assistance or to report issues, please submit an issue on the project's repository.

---
