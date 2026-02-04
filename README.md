Le Gourmet | Culinary Discovery App 🍳
A premium full-stack web application designed for refined recipe discovery. Users can search by ingredients or dish names to find high-resolution recipes with real-time nutritional data.

🌟 Key Features

Ingredient-based Search: Find what to cook based on what's in your pantry.


Health Score Integration: Real-time health indicators for every recipe.


Premium UI: Minimalist, gastronomy-inspired design using Playfair Display typography.


Responsive Grid: Fluid layout that works perfectly on mobile and desktop.

🛠️ Technical Stack

Frontend: HTML5, CSS3 (Flexbox/Grid), and Vanilla JavaScript.


Backend: Python + Flask.


External API: Spoonacular API (Complex Search & Bulk Information endpoints).

⚙️ Architecture: The "API Bridge"
This project uses Flask as a secure bridge. The backend centralizes API calls to:


Protect Credentials: The SPOON_API_KEY stays on the server and is never exposed to the client-side browser.


Shape Responses: Flask filters the massive data from Spoonacular to return only the fields the UI needs, like healthScore and readyInMinutes.

🚀 Getting Started
Prerequisites
Python 3.7+ 

Spoonacular API Key 

Installation
Clone the repository:

Bash
git clone https://github.com/your-username/le-gourmet.git
Install dependencies:

Bash
pip install flask requests
Run the application:

Bash
python app.py
Access the UI: Open http://localhost:5000 in your browser.
