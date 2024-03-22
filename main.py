from mobot import MovieChatbot

if __name__ == "__main__":
    chatbot = MovieChatbot()
    try:
        chatbot.start_chat()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    finally:
        chatbot.close()
