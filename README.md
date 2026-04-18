# 🧠 Mental Health Assistant

A machine learning–powered mental health assistant built using NLP and Streamlit. This project analyzes user input and generates supportive, context-aware responses, including PHQ-9–based assessment insights.

---

## 🌐 Live Demo

👉 Try the app here:
🔗 https://huggingface.co/spaces/CheboluGayatri/MentalHealth-Assistant

---

## 🚀 Features

* 💬 Interactive chatbot interface using Streamlit
* 🧠 Fine-tuned NLP model (T5) for mental health response generation
* 📊 PHQ-9–based evaluation support
* 🧪 Model training and evaluation scripts included
* 🐳 Docker support for deployment

---

## 🏗️ Project Structure

```
Mental_Healthcare/
│
├── Backend/
│   ├── data/                # Dataset files
│   ├── script/              # Training and model scripts
│   │   ├── datacollection.py
│   │   ├── finetune.py
│   │   └── model.py
│
├── Frontend/
│   └── app.py               # Streamlit app
│
├── evaluation.py            # Model evaluation script
├── requirements.txt         # Dependencies
├── Dockerfile               # Container setup
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/CheboluGayatri/-MentalHealth-Assistant.git
cd Mental_Healthcare
```

### 2. Create virtual environment

```
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```
streamlit run Frontend/app.py
```

Then open the local URL shown in your terminal (usually http://localhost:8501).

---

## 🧠 Model Information

* Uses a fine-tuned T5 model for generating mental health responses
* Based on PHQ-9 style evaluation patterns
* Designed for conversational emotional support

⚠️ Model files are **not included** due to size limits.

### 📥 Add Model Files

Place your trained model inside:

```
Backend/models/
```

---

## 🧪 Training the Model

```
python Backend/script/finetune.py
```

---

## 📊 Evaluation

```
python evaluation.py
```

---

## 🐳 Docker Support

Build and run with Docker:

```
docker build -t mental-health-app .
docker run -p 7860:7860 mental-health-app
```

---

## ⚠️ Disclaimer

This project is for educational and research purposes only.
It is **not a substitute for professional medical advice, diagnosis, or treatment**.

---

## 📌 Future Improvements

* Improve model accuracy with larger datasets
* Add multilingual support
* Enhance UI/UX
* Integrate professional mental health resources
* Add user authentication

---

## 👩‍💻 Author

**Gayatri Chebolu**

---

## ⭐ Contributing

Contributions are welcome. Feel free to fork the repo and submit a pull request.
