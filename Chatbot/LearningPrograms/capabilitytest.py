#This program takes input from the user with the capabilities of:
# - solving simple maths problems
# - Telling the time

# The Logic adapaters seem to take priority in responses rather than the training data.

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

#Naming the Chatbot
chatbot = ChatBot('Chatty', 
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                    'chatterbot.logic.MathematicalEvaluation',
                    'chatterbot.logic.TimeLogicAdapter'
                  ],
                  database_uri='sqlite:///database.sqlite3')

#New Trainer instanse
trainer = ListTrainer(chatbot)


trainer.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])


while True:
    try:
        chatbot_input = chatbot.get_response(input())
        print(chatbot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

