from dotenv import load_dotenv
load_dotenv()

import os
import openai
from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import vision
import base64

# Set OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
vision_client = vision.ImageAnnotatorClient()

# Set up Flask
app = Flask(__name__)
CORS(app)

# Route: Predict from Text
@app.route("/predict_text", methods=["POST"])
def predict_text():
    data = request.get_json()
    food = data.get("food", "").strip()

    if not food:
        print("No food name provided.")
        return jsonify({"error": "No food name provided"}), 400

    prompt = f"""
    Estimate the number of calories in one serving of {food}.
    Then provide one or two sentences of nutritional or general information about it.
    Provide only the calorie amount in the form of a number or a range (e.g., 100 or 100-200). Do not include the word "calories".
    Respond in this format:
    Calories: [calories]
    Info: [short description]
    """

    print(f"Sending prompt to OpenAI:\n{prompt}")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful nutrition assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        content = response.choices[0].message.content
        print("Response from OpenAI:\n", content)

        calories = "Unknown"
        info = "AI info not available."
        for line in content.splitlines():
            if line.lower().startswith("calories:"):
                calories = line.split(":", 1)[1].strip()
            elif line.lower().startswith("info:"):
                info = line.split(":", 1)[1].strip()

        print(f"Parsed Calories: {calories}")
        print(f"Parsed Info: {info}")

        return jsonify({
            "calories": calories,
            "info": info
        })

    except Exception as e:
        print("OpenAI error:", e)
        return jsonify({"calories": "Unknown", "info": "AI info not available."}), 500



# Route: Predict from Image
@app.route("/predict_image", methods=["POST"])
def predict_image():
    data = request.get_json()

    if not data.get("image"):
        print("No image data received.")  # Debugging line
        return jsonify({"error": "No image provided"}), 400

    image_data = data["image"]
    if not image_data.strip():
        print("Received empty image data.")  # Debugging line
        return jsonify({"error": "Image data is empty"}), 400

    # Decode the base64 image data
    try:
        image_bytes = base64.b64decode(image_data)
        image = vision.Image(content=image_bytes)
        print("Image successfully decoded.")  # Debugging line
    except Exception as e:
        print(f"Error decoding image: {str(e)}")  # Debugging line
        return jsonify({"error": f"Failed to decode image: {str(e)}"}), 400

    # Perform object localization (detection) on the image
    response = vision_client.object_localization(image=image)

    # Debugging: Print the response from Google Cloud Vision
    print("Response from Google Cloud Vision API:")
    print(response)

    if response.error.message:
        print(f"Google Vision API error: {response.error.message}")  # Debugging line
        return jsonify({"error": response.error.message}), 500
    
    detected_objects = []
    detected_food = None  # Store the detected food object name
    
    # Loop through the localized_object_annotations to get detected objects
    for obj in response.localized_object_annotations:
        print(f"Detected object: {obj.name}, Confidence: {obj.score}")  # Debugging line
        detected_objects.append({
            "object": obj.name,
            "confidence": obj.score,
            "bounding_box": str(obj.bounding_poly)
        })
        
        # Store the first object with confidence greater than 0.7 as the detected food
        if obj.score > 0.7 and not detected_food:
            detected_food = obj.name  # Extract the detected object name (e.g., "Hot dog")

    # Check if a food item was detected with high enough confidence
    if not detected_food:
        print("No objects detected with sufficient confidence.")  # Debugging line
        return jsonify({"error": "No food item detected with high confidence."}), 400

    # Send the detected food name to OpenAI for nutritional information
    prompt = f"""
    Estimate the number of calories in one serving of {detected_food}.
    Then provide one or two sentences of nutritional or general information about it.
    Provide only the calorie amount in the form of a number or a range (e.g., 100 or 100-200). Do not include the word "calories".
    Respond in this format:
    Calories: [calories]
    Info: [short description]
    """

    print(f"Sending prompt to OpenAI:\n{prompt}")  # Debugging line

    try:
        openai_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful nutrition assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        content = openai_response.choices[0].message.content
        print("Response from OpenAI:\n", content)  # Debugging line

        calories = "Unknown"
        info = "AI info not available."
        for line in content.splitlines():
            if line.lower().startswith("calories:"):
                calories = line.split(":", 1)[1].strip()
            elif line.lower().startswith("info:"):
                info = line.split(":", 1)[1].strip()

        print(f"Parsed Calories: {calories}")
        print(f"Parsed Info: {info}")

        return jsonify({
            "calories": calories,
            "info": info,
            "objects": detected_objects
        })

    except Exception as e:
        print("OpenAI error:", e)
        return jsonify({"calories": "Unknown", "info": "AI info not available."}), 500

# Run Server
if __name__ == "__main__":
    app.run(debug=True)