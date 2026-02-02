import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

SPOON_API_KEY = "633effcb8bb14984aa5cfffa4fbfbf6d"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    query = data.get('ingredients')
    
    search_url = f"https://api.spoonacular.com/recipes/complexSearch"
    params = {"apiKey": SPOON_API_KEY, "query": query, "number": 6}
    
    try:
        search_response = requests.get(search_url, params=params)
        search_data = search_response.json()
        
        if not search_data.get('results'):
            return jsonify({"error": "No recipes found."}), 404

        recipe_ids = ",".join([str(r['id']) for r in search_data['results']])
        details_url = f"https://api.spoonacular.com/recipes/informationBulk"
        details_params = {"apiKey": SPOON_API_KEY, "ids": recipe_ids}
        
        details_response = requests.get(details_url, params=details_params)
        meals = details_response.json()
        
        return jsonify({"meals": meals})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

# oblg for Vercel
app = app