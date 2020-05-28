{"intents": [
        {"tag": "greeting",
         "patterns": ["Hi", "Is anyone there?", "Hello", "Good day", "Are you there?"],
         "responses": ["Hello!", "Good to see you again!", "Hi there, how can I help?", "I'm here"],
         "context_set": ""
        },
        {"tag": "goodbye",
         "patterns": ["cya", "See you later", "Goodbye", "I am Leaving", "Have a Good day", "Bye"],
         "responses": ["Sad to see you go :(", "Talk to you later", "Goodbye!"],
         "context_set": ""
        },
        {"tag": "age",
         "patterns": ["How old?", "How old are you?", "What is your age?", "Age?"],
         "responses": ["I don't have an age", "You tell me, I'm a bot."],
         "context_set": ""
        },
        {"tag": "name",
         "patterns": ["What is your name?", "What should I call you?"],
         "responses": ["You can call me whatever you want.", "I'm Chatbot!", "I'm a bot aka NLP Chatbot."],
         "context_set": ""
        },
        {"tag": "inquire",
         "patterns": ["How are you?", "Are you ok?", "What are you doing?", "What's up?"],
         "responses": ["I'm good, how are you?", "I'm feeling good, what about you?", "I don't know right now.", "I'm neutral", "I've never been this good before"],
         "context_set": ""
        },
        {"tag": "questions",
         "patterns": ["Are you a girl?", "What is your gender?"],
         "responses": ["My sound look like a girl but I don't have a gender.", "I'm not a girl or a boy", "I don't know right now.", "I don't want to tell you that", "I'm not a human"],
         "context_set": ""
        },
	    {"tag": "website",
         "patterns": ["open"],
         "responses": ["Okay I'm opening","Here it is"],
         "context_set": ""
        },
        {"tag": "weather",
         "patterns": ["weather","How is the weather today?","What's the weather like?","Tell me the weather"],
         "responses": ["Here it is","Let me check","I'm looking at"],
         "context_set": ""
        },
        {"tag": "closing",
         "patterns": ["quit","exit","shut down"],
         "responses": ["See you later boss","Don't forget me","Have a nice day"],
         "context_set": ""
        },
        {"tag": "email",
         "patterns": ["send","email","I want to send an email","Send an email for me."],
         "responses": ["OK, give me a min.","I need a min.","Give me a second"],
         "context_set": ""
        }
   ]
}
