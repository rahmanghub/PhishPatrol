from flask import Flask, render_template, request
import os
import numpy as np
import re
import requests
import time
import pickle

app = Flask(__name__)


phish = pickle.load(open('phishPred.pkl','rb'))

def get_url_features(url):
    domain = re.findall(r'://(.[^/]+)', url)[0]
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    try:
        start_time = time.time()
        response = requests.get(url, allow_redirects=True)
        end_time = time.time()
        time_response = round(end_time - start_time, 3)
        qty_redirects = len(response.history)
    except:
        time_response = 0
        qty_redirects = 0
    tls_ssl_certificate = int(bool(re.match(r'^https', url)))
    return [url.count("-"), url.count("_"), url.count("="), domain.count("."), domain.count("-"),domain.count("_"), domain.count("/"), domain.count("?"), domain.count("@"), domain.count("&"),domain.count("!"), domain.count(" "), sum(domain.count(vowel) for vowel in "aeiouAEIOU"), len(domain), int(bool(re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', domain))),int(any(keyword in domain for keyword in ["cdn", "cloud", "content", "static", "server", "client"])), int(bool(re.search(email_regex, url))), time_response, qty_redirects, tls_ssl_certificate]

def vald(url):
    regex = re.compile(
                r'^(?:http|ftp)s?://'
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
                r'localhost|'
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                r'(?::\d+)?'
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, url) != None:
        return url
    else:
        print('Invalid Url')




def predict(url):
    try:
        # if phish.predict(np.array([get_url_features(vald(url))])) == 0:
        #     return "Safe"
        # else:
        #     return "Danger"
        return phish.predict(np.array([get_url_features(vald(url))]))
    except:
        return 'Error'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        result = predict(url)
    return render_template('main.html', result=result)
    
if __name__ == '__main__':
    app.run()
