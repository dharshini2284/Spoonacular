from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)

url = "https://api.apilayer.com/spoonacular/recipes/complexSearch?query=query"

payload = {}
headers= {
  "apikey": "90J6OxApoDi5K3Sh6w8yTEr9kMAMo22b"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        response = requests.request("GET", url, headers=headers, data = payload)
        status_code = response.status_code
        result = response.text
        #if result:
        #    return render_template('index.html', dish=result)
        #else:
        #    error = f"No dish found with title: {name}"
        return render_template('index.html',result=result)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
