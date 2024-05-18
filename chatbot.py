# Importing libraries
from nltk.chat.util import Chat, reflections

#Creating a list of responses
responses = [
    
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there","Hello user", "Hello friend"]
    ],
    
    [
        r"(.*) your name ?",
        ["My name is Ninja and I'm a chatbot.",]
    ],


    [
        r"(.*)help(.*) ",
        ["I can help you.",]
    ],


    [
        r"how are you (.*) ?",
        ["i am great !, i am fine., i am good."]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],


    [
        r"quit",
        ["Bye. See you soon :) ","Have a great day. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]


#Generating reflections
print(reflections)

#Output
{'i': 'you',
'your': 'my',
'yours': 'mine',
'i was': 'you were',
'you were': 'I was',
"i'll": 'you will',
"you'll": 'I will',
'you are': 'I am',
"you've": 'I have',
"i'd": 'you would'
}

#default message
print("Hi, I'm a bot, and my name is Ninja. \nPlease type your query. Type quit to leave. ")
#Creating Chat Bot
chat = Chat(responses, reflections)