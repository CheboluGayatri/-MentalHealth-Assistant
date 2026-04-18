# ============================================
# PHQ-9 Chatbot (VS Code Version)
# ============================================

import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# ============================================
# LOAD MODEL
# ============================================
MODEL_PATH = "../Backend/models/t5_phq9_model"

tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()

# ============================================
# QUESTIONS
# ============================================
phq9_questions = [
    "Little interest or pleasure in doing things?",
    "Feeling down or hopeless?",
    "Trouble sleeping?",
    "Feeling tired?",
    "Poor appetite or overeating?",
    "Feeling bad about yourself?",
    "Trouble concentrating?",
    "Moving or speaking slowly/restless?",
    "Thoughts of self-harm?"
]

answer_score_map = {
    "Not At All": 0,
    "Several Days": 1,
    "More Than Half The Days": 2,
    "Nearly Every Day": 3
}

number_to_answer = {
    "0": "Not At All",
    "1": "Several Days",
    "2": "More Than Half The Days",
    "3": "Nearly Every Day"
}

# ============================================
# CHAT
# ============================================
print("\n🔹 PHQ-9 Chatbot 🔹\n")

total_score = 0

for i, question in enumerate(phq9_questions):
    while True:
        print(f"\nQ{i+1}: {question}")
        ans = input("Answer (0-3 or text): ").strip()

        if ans.lower() == "exit":
            exit()

        ans = number_to_answer.get(ans, ans.title())

        if ans in answer_score_map:
            total_score += answer_score_map[ans]
            break
        else:
            print("Invalid input!")

print(f"\nTotal Score: {total_score}/27")