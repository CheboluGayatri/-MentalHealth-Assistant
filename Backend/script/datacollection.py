import random
import json

# Severity function
def get_severity(score):
    if score <= 4:
        return "Minimal Depression"
    elif score <= 9:
        return "Mild Depression"
    elif score <= 14:
        return "Moderate Depression"
    elif score <= 19:
        return "Moderately Severe Depression"
    else:
        return "Severe Depression"

# Suggestions
def get_suggestion(severity):
    return {
        "Minimal Depression": "You're doing well. Maintain a healthy lifestyle.",
        "Mild Depression": "Try exercise, meditation, and talking to friends.",
        "Moderate Depression": "Consider consulting a therapist.",
        "Moderately Severe Depression": "Seek professional mental health support.",
        "Severe Depression": "Immediate professional help is strongly recommended."
    }[severity]

# Storage
dataset = []
seen = set()

# Target samples per class (balanced dataset)
target_per_class = 1500

class_counts = {
    "Minimal Depression": 0,
    "Mild Depression": 0,
    "Moderate Depression": 0,
    "Moderately Severe Depression": 0,
    "Severe Depression": 0
}

# Generate until balanced
while min(class_counts.values()) < target_per_class:

    responses = tuple(random.randint(0,3) for _ in range(9))  # tuple for hash
    if responses in seen:
        continue

    seen.add(responses)

    score = sum(responses)
    severity = get_severity(score)

    # Balance control
    if class_counts[severity] >= target_per_class:
        continue

    class_counts[severity] += 1

    suggestion = get_suggestion(severity)

    # Better input variations
    user_formats = [
        "PHQ-9 responses: " + ", ".join([f"Q{i+1}={responses[i]}" for i in range(9)]),
        "My PHQ9 answers are: " + ", ".join(map(str, responses)),
        f"I feel low, here are my scores: {list(responses)}",
        f"Depression test answers: {responses}",
        f"Q1 to Q9 responses: {responses}"
    ]

    user_input = random.choice(user_formats)

    assistant_output = f"""Total Score: {score}
Severity: {severity}
Suggestion: {suggestion}"""

    dataset.append({
        "messages": [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": assistant_output}
        ]
    })

# Save file
file_path = "/content/drive/MyDrive/phq9_finetune_clean.jsonl"

with open(file_path, "w") as f:
    for item in dataset:
        f.write(json.dumps(item) + "\n")

print("✅ Clean dataset created:", file_path)
print("📊 Class distribution:", class_counts)
print("📦 Total samples:", len(dataset))