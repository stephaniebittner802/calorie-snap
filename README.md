
# CalorieSnap

**CalorieSnap** is an easy way to check the calories in your food on the go! Whether you are in a restaurant, at home, or shopping for groceries, CalorieSnap lets you instantly estimate the calories of any food by simply snapping a picture or typing its name. It’s your go-to tool for making informed, healthy choices — all within seconds.

---

## Features

- **Instant Food Calorie Estimation**: Upload a photo or type the food name, and let CalorieSnap provide an estimate of the calories in your food.
- **AI-Powered**: CalorieSnap uses AI to estimate food calories with impressive accuracy.
- **Quick Results**: Get results within seconds — perfect for those busy moments when you need to make quick, informed decisions.

---

## **Technologies Used**
- **Frontend**: 
  - React.js
  - React Router (for routing between pages)
  - CSS for styling and transitions
- **Backend**:
  - Flask (Python)
  - Google Cloud Vision API (for object detection)
  - OpenAI GPT-3.5 (for estimating calories and nutritional information)
  - dotenv (for environment variable management)

---

## **Setup Instructions**

### 1. **Clone the repository**

```bash
git clone https://github.com/stephaniebittner802/calorie-snap.git
cd caloriesnap
```

### 2. **Frontend Setup (React)**

- Navigate to the `frontend` directory:

```bash
cd frontend
```

- Install dependencies:

```bash
npm install
```

- To start the development server:

```bash
npm start
```

- The app will now be running on `http://localhost:3000`.

### 3. **Backend Setup (Flask)**

- Navigate to the `backend` directory:

```bash
cd backend
```

- Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

- Make sure you have the **Google Cloud Vision API** and **OpenAI API** keys set up in your environment:

1. Create a `.env` file in the `backend` directory with the following:

```env
GOOGLE_APPLICATION_CREDENTIALS=path_to_your_google_cloud_credentials_json
OPENAI_API_KEY=your_openai_api_key
```

- Run the backend server:

```bash
python app.py
```

- The backend will now be running on `http://localhost:5000`.

### 4. **Google Cloud Vision Setup**

- Sign up for **Google Cloud** and enable the **Vision API**.
- Create a new project and download the **JSON key file**.
- Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to this key.

### 5. **OpenAI Setup**

- Sign up for **OpenAI** and get your **API key**.
- Make sure to use **GPT-3.5** or the latest available model for your requests.

### 6. **Testing the App**

1. Open the app in your browser at `http://localhost:3000`.
2. You can:
   - Enter a food name (e.g., "Apple Pie") and click **Submit**.
   - Upload a food image or take a picture using the camera, and click **Submit**.
3. The app will display the estimated calories and nutritional information for the food item.

---

## **License**

This project is open-source and available under the MIT License.