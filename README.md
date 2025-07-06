
# CalorieSnap

**CalorieSnap** is an easy way to check the calories in your food on the go! Whether you are in a restaurant, at home, or shopping for groceries, CalorieSnap lets you instantly estimate the calories of any food by taking a picture or typing its name. Snap a picture, and see it for yourself!

## Demo

<p align="center">
  <img src="assets/demo.gif" alt="CalorieSnap Demo" width="300" />
</p>

## Features

- **Instant Food Calorie Estimation**: Upload a photo or type the food name, and let CalorieSnap provide an estimate of the calories in your food.
- **AI-Powered**: CalorieSnap uses AI to identify the images and estimate the food calories.
- **Quick Results**: Get results within seconds — perfect for those busy moments when you need to make quick, informed decisions.



## **Technologies Used**
- **Frontend**: 
  - React.js
  - CSS for styling and transitions
  - Netlify
- **Backend**:
  - Flask (Python)
  - Google Cloud Vision API (for object detection)
  - OpenAI API (for estimating calories and nutritional information)
  - Render



## **Setup Instructions**

### 1. **Clone the repository**

```bash
git clone https://github.com/stephaniebittner802/calorie-snap.git
cd caloriesnap
```

### 2. **Set up Frontend**

```bash
cd frontend
npm install
npm start
```

### 3. **Set up Backend**

```bash
cd backend
pip install -r requirements.txt
```

Make sure you have the **Google Cloud Vision API** and **OpenAI API** keys set up in your environment. To do this, create a `.env` file in the `backend` directory with the following:

```env
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_google_cloud_credentials_json
OPENAI_API_KEY=your_openai_api_key
```

Run the backend:

```bash
python app.py
```

### 4. **Google Cloud Vision Setup**

- Sign up for **Google Cloud** and enable the **Vision API**.
- Create a new project and download the **JSON key file**.
- Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to this key.

### 5. **OpenAI Setup**

- Sign up for **OpenAI** and get your **API key**.
- Make sure to use **GPT-3.5** or the latest available model for your requests.


## **License**

This project is open-source and available under the MIT License.