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

'''
#Train unsing English corpus
trainer.train('chatterbot.corpus.english')

#Get a reponse from teh chatbot
reponse = chatbot.get_response('Hello, how are you?')

print(reponse)
'''

train_list = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

#Train the chatbot with the coversation list
trainer.train(train_list)
'''
#Get a response from the chatbot
response1 = chatbot.get_response("How are you?")
response2 = chatbot.get_response("That is good to hear.")
response3 = chatbot.get_response("Thank you")

#Print responses
print("Response to 'How are you?':", response1)
print("Response to 'That is good to hear.':", response2)
print("Response to 'Thank you':", response3)
'''
response = chatbot.get_response("Good morning!")
print(response)
