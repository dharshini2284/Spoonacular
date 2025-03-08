from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "pyFSslDK5mfNjc0xl5sEnWcjET8tNH9E"
API_URL = "https://api.apilayer.com/spoonacular/recipes/complexSearch"

@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query") 
        params = {
            "query": query,
            "number": 10, 
        }
        headers = {"apikey": API_KEY}
        try:
            response = requests.get(API_URL, headers=headers, params=params,timeout=10)
            response.raise_for_status()
            data = response.json()
            print("API Response JSON:", data)
            recipes = data.get("results", []) 
        except requests.exceptions.RequestException as e:
            print("Error:", e) 
            return f"Error: {e}"
    return render_template("index.html", recipes=recipes, query=query)

if __name__ == "__main__":
    app.run(debug=True)
