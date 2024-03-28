from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    "My Chatbot",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, I do not understand.',
            'maximum_similarity_threshold': 0.7
        },
    ],
)

trainer = ListTrainer(chatbot)

trainer.train([
    "hi",
    "Hello! If you want to learn a new song - just ask me!",
    "i ask you",
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
    "style",
    "How long have you played the guitar?",
    "4 years",
    "Then, I would suggest you to learn to play \"Take On Me\", it's a great song of intermediate difficulty"
])

trainer.train([
    "hello",
    "Hello! If you want to learn a new song - just ask me!",
    "what song do you recommend",
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
    "fignerlyst ig",
    "How long have you played the guitar?",
    "7 days",
    "Then, I suggest you to learn to play \"Greensleeves\". It is fingerstyle song great for beginners!"
])

trainer.train([
    "Hi, which song should I learn?",
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
    "does not matter",
    "OK, I will choose on my own. How long have you played the guitar?",
    "for 6 weeks",
    "Then, I suggest you to learn to play \"Riptide\". It is strumming song great for beginners!"
])

trainer.train([
    "which song should I learn?",
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
    "fingerstyle",
    "How long have you played the guitar?",
    "I haven't played yet",
    "Then, I suggest you to learn to play \"Greensleeves\". It is fingerstyle song great for beginners!"
])

trainer.train([
    "what song",
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
    "fingerstyle",
    "How long have you played the guitar?",
    "1 year",
    "Then, I suggest you to learn to play \"Helplessly Hoping\". It is fingerstyle song of intermedeate difficulty"
])

trainer.train([
    "Hi, which song should I learn?",
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
    "i dont know",
    "OK, I will choose on my own. How long have you played the guitar?",
    "2 days",
    "Then, I suggest you to learn to play \"I see fire\". It is strumming song great for beginners!"
])

trainer.train([
    "so what music should i learn",
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
    "i dunno",
    "OK, I will choose on my own. How long have you played the guitar?",
    "0",
    "Then, I suggest you to learn to play \"Knocking On Heavens Door\"."
    " It is strumming song great for absolute beginners!"
])

trainer.train([
    "so what music should i learn",
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
    "strum",
    "How long have you played the guitar?",
    "10 years",
    "Then, I suggest you to learn to play \"Knocking On Heavens Door\"."
    " It is strumming song great for absolute beginners!"
])

trainer.train([
    "Ok, something else?",
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
])
trainer.train([
    "song",
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
])

trainer.train([
    "gimme a song",
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
])

trainer.train([
    "i want to choose a song",
    "You are at a right place! "
    "Do you want to learn a fingerstyle song (picking string directly by fingertips) or a strum (sweeping over "
    + "several string)?",
])


def conversation_handler():
    query = input("> ")
    if query in exit_conditions:
        print("Goodbye!")
        return False
    print(f"< {chatbot.get_response(query)}")
    return True


exit_conditions = (":q", "quit", "exit")
print("\nHi, this chatbot is for choosing a song to learn to play on an acoustic guitar!\n"
      + "To exit, enter one of the following expressions:", exit_conditions)

should_continue = True
if __name__ == "__main__":
    while should_continue:
        should_continue = conversation_handler()
