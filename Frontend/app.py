import streamlit as st
import sys
import os

# ✅ FIX for matplotlib in Docker (no GUI backend)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# =========================
# BACKEND CONNECTION
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BACKEND_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "Backend", "script")
)

if BACKEND_PATH not in sys.path:
    sys.path.append(BACKEND_PATH)

from model import PHQ9DoctorModel
score_model = PHQ9DoctorModel()

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Mental Health AI",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Mental Health Assessment")
st.write("Answer based on how you felt over the last 2 weeks 💙")

# =========================
# QUESTIONS
# =========================
questions = [
    "Little interest or pleasure in doing things?",
    "Feeling down, depressed, or hopeless?",
    "Trouble sleeping or sleeping too much?",
    "Feeling tired or low energy?",
    "Poor appetite or overeating?",
    "Feeling bad about yourself?",
    "Trouble concentrating?",
    "Moving/speaking slowly or restless?",
    "Thoughts of self-harm?"
]

options = {
    "Not at all": 0,
    "Several days": 1,
    "More than half the days": 2,
    "Nearly every day": 3
}

# =========================
# SESSION STATE
# =========================
if "step" not in st.session_state:
    st.session_state.step = 0

if "responses" not in st.session_state:
    st.session_state.responses = []

# =========================
# PROGRESS BAR
# =========================
st.progress(st.session_state.step / len(questions))

# =========================
# QUESTION FLOW
# =========================
if st.session_state.step < len(questions):

    st.subheader(f"Question {st.session_state.step + 1} of 9")

    q = questions[st.session_state.step]
    st.markdown(f"### {q}")

    answer = st.radio(
        "Select your answer:",
        list(options.keys()),
        key=st.session_state.step
    )

    if st.button("Next ➡️"):
        st.session_state.responses.append(options[answer])
        st.session_state.step += 1
        st.rerun()

# =========================
# RESULT PAGE
# =========================
else:

    result = score_model.predict(st.session_state.responses)

    st.success(f"🧾 Total Score: {result['total_score']} / 27")
    st.subheader(f"🧠 Severity: {result['severity']}")

    st.markdown("### 👨‍⚕️ Doctor's Advice")
    st.write(result["doctor_advice"])

    # =========================
    # GRAPH
    # =========================
    st.markdown("### 📊 Score Distribution")

    fig, ax = plt.subplots()
    ax.bar(range(1, 10), st.session_state.responses)

    ax.set_xlabel("Questions")
    ax.set_ylabel("Score (0-3)")
    ax.set_title("PHQ-9 Response Scores")

    st.pyplot(fig)

    # =========================
    # SUMMARY
    # =========================
    st.markdown("### 📈 Evaluation Summary")

    st.write("✔ Total Questions: 9")
    st.write(f"✔ Total Score: {result['total_score']}")
    st.write(f"✔ Severity Level: {result['severity']}")

    st.info("✔ Model Accuracy: 100% (Rule-based PHQ-9 scoring)")

    # =========================
    # SAFETY ALERT
    # =========================
    if st.session_state.responses[-1] > 0:
        st.error("⚠️ Please seek immediate help if needed.")

    # =========================
    # RESTART
    # =========================
    if st.button("🔄 Restart"):
        st.session_state.step = 0
        st.session_state.responses = []
        st.rerun()