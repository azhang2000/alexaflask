from flask import Flask
from flask_ask import Ask, statement, question, session

import json
import requests
import time
import unidecode
import os


app = Flask(__name__)
ask = Ask(app, "/reddit_reader")
def get_headlines():
    user_pass_dict = {'user': 'USERNAME', 'passwd': 'PASSWORD', 'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update({'User-Agent': 'Im testing Alexa: Sentdex'})
    sess.post('https://www.reddit.com/api/login', data = user_pass_dict)
    time.sleep(1)
    url = 'https://reddit.com/r/askreddit/.json?limit=10'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title'])for listing in data['data']['children']]
    titles = '...'.join([i for i in titles])
    return titles

titles = get_headlines()
print(titles)

@app.route('/')
def homepage():
    return "hello world"

@ask.launch
def start_skill():
    welcome_message = 'Hello, would you like the news?'
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headline_msg = 'Current world news headlines are {}.format(headlines)'
    return statement(headline_msg)

@ask.intent("NoIntent")
def no_intent():
        bye_text = 'I am not sure why you requested me to run'
        return (bye_text)

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run(debug=True)
