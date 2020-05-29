# NLP Term Project

Python-based NLP Audio Chatbot for term project on Windows

# Installing Packages & Configuring Settings

Before starting you need to download a few python packages. Please note as of writing this these packages will ONLY WORK IN PYTHON 3.6. You can use the requirements.txt for installing the packages by using: 
  
```sh
pip install -r requirements.txt
```

Yet, you need to download some of the packages manually if you get an error while starting the chatbot.
  
# How To Use

After installing the required packages, you can start the chatbot via:

```sh
python NLPChatbot.py
```

After training is done and  Laurel welcomes you, you can answer to her by: 

> Hi
> Is anyone there?
> Hello
> Good day
> Are you there?

Also, you can ask these questions:

> How old are you?
> What is your age?
> Age?
> What is your name?
> What should I call you?
> How are you?
> Are you ok?
> What are you doing?
> What's up?

The chatbot will answer you randomly from its dataset according to the type of questions.

# Special Features

### Opening a Website

You can make the bot open a website with ".com" extension via:

> open "Name of the Web Site You Want to Redirect"

For Example,

> open google
>open youtube

### Asking The Weather

You can learn the present weather via asking:

For Example,

> What is the weather like?

### Sending Mails

After configuring the mail part in the py file you can make the chatbot send mail to the person you want to via:

> send mail

After this the chatbot will ask you "Who is the recipient?"
In this case, you should say "teacher" (it is default and you can change this in the py file).

After telling who will be the recipient, the chatbot will ask you "What should I say?". You can tell whatever you want, it will automatically send the mail to the recipient and let you know when it sends.

## Closing The Chatbot

When you want to close the chatbot you can say:

> shutdown
> exit
> quit
