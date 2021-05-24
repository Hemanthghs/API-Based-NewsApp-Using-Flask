from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def get_data(url):
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    return articles



@app.route('/')
def home():
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=6a0368b0121547d89cfb017d702b37ca')
    articles = get_data(url)
    return render_template("index.html",articles=articles)

@app.route('/search-results',methods=['POST'])
def search():
    try:
        key = str(request.form['key'])
        url = ('https://newsapi.org/v2/everything?q='+key+'&apiKey=65729ab9862c408a85621220be43ee5f')
        article = get_data(url)
        
        return render_template("results.html",articles=article, key=key)
    
    except:
        return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True, port=8001)
    