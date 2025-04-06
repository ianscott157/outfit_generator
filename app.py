from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_outfit_image(description):
    response = openai.images.generate(
        prompt = description,
        model="dall-e-3",
        size="1024x1024",
        n=1
    )

    return response.data[0].url

@app.route("/", methods=["GET", "POST"])
def home_page():
     image_url = None
     if request.method == "POST":
         description = request.form["description"]
         image_url = generate_outfit_image(description)
     return render_template("index.html", image_url=image_url)

@app.route("/about")
def about_page():
    return render_template("about.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)

# Example usage
user_description = "A modern grey streetwear outfit with a hoodie, cargo pants, and sneakers."
image_url = generate_outfit_image(user_description)

print("Generated Outfit Image URL:", image_url)

