import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle
import webbrowser
from gtts import gTTS
import speech_recognition as sr
import os
import re
import smtplib
import requests
import pyowm

#Taking the Tags, Patterns and Responses from JSON File:

with open("intents.json") as file:
    data = json.load(file)

#Creating a Data with the Information by NLTK:

try:
    with open("data.pickle", "wb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

#Tokenizing part:

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)


    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

try:
    model.load('model.tflearn')
except:
    tensorflow.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")

#TextToSpeech Function:

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    text_to_speech = gTTS(text=audio, lang='en-US')
    text_to_speech.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#The Function that Gathers Together Input Words:

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)   

#The Main Function for Activating ChatBot

def chat():
    talkToMe("Hello Master, I'm your personal assistant and I'm at your service")
    while True:

        #Speech Recognition Part:

        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.pause_threshold = 0.7
            r.adjust_for_ambient_noise(source, duration=0.7)
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()

            inp = command
            print(inp) #For watching what we said

            results = model.predict([bag_of_words(inp, words)])[0]
            results_index = numpy.argmax(results)
            tag = labels[results_index]

            if results[results_index] > 0.9:
                for tg in data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']

                talkToMe(random.choice(responses))
            else:
                talkToMe("I didn't get that, tell me again.")

            #Quit Commands:

            if inp.lower() == 'quit' or inp.lower() == 'exit' or inp.lower() == 'shut down':
                break

            #Browser Commands:     

            elif 'open ' in inp:
                reg_ex = re.search('open (.+)', inp)
                if reg_ex:
                    domain = reg_ex.group(1)
                    url = 'https://www.' + domain + '.com'
                    webbrowser.open(url)
                else:
                    pass

            #Weather Commands:

            elif 'weather' in inp:
                res = requests.get('https://ipinfo.io/')
                info = res.json()
                country = info['country']
                zipcode = info['postal']

                degree_sign = u'\N{DEGREE SIGN}'
                owm = pyowm.OWM('58c31a987f2c5387dab8e3a11c9a18ae')
                observation = owm.weather_at_zip_code(zipcode, country)
                weather = observation.get_weather()
                status = str(weather.get_status())
                temperature = str(round(weather.get_temperature('celsius')['temp']))

                talkToMe("The weather status is: " + status + " and the temperature is: " + temperature + degree_sign + ". You can look for more information from this website.")
                url = 'https://weather.com/weather/today'
                webbrowser.open(url)

            #Email Commands:            

            elif 'email' in inp:
                talkToMe('Who is the recipient?')

                #Command Sub Function for Mailing:
                def myCommand():

                    r = sr.Recognizer()

                    with sr.Microphone() as source:
                        r.pause_threshold = 0.7
                        r.adjust_for_ambient_noise(source, duration=0.7)
                        audio = r.listen(source)

                    try:
                        command = r.recognize_google(audio).lower()
                        inp = command
                        print(inp) #For watching what we said

                    except sr.UnknownValueError:
                        talkToMe("I didn't get that, tell me again.")
                        inp = myCommand();                        

                    return inp

                recipient = myCommand()

                if 'teacher' in recipient:
                    talkToMe('What should I say?')
                    content = myCommand()

                    #init gmail SMTP
                    mail = smtplib.SMTP('smtp.gmail.com', 587)

                    #identify to server
                    mail.ehlo()

                    #encrypt session
                    mail.starttls()

                    #login
                    mail.login('your gmail id', 'your gmail password')

                    #send message
                    mail.sendmail('name of the recipient', 'mail of the recipient', content)

                    #end mail connection
                    mail.close()

                    talkToMe('Mail sent.')

                else:
                    talkToMe("I didn't get that")                          

        #loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            talkToMe("Hey are you here? I can't hear you")

        

chat()
