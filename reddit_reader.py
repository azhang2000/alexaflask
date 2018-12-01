from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(_name_)
ask = Ask(app, "/reddit_reader")
def get_headlines():
    pass

@app.route('/')
def homepage()
    return "hello world"

@ask.launch
def start_skill():
    welcome_message = 'Hello, would you like the news?'
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headline_msg = 'Current world news headliens are {}.format(headlines)'
    return statement(headline_message)

if __name__ == '__main__':
    app.run(debug=True)
