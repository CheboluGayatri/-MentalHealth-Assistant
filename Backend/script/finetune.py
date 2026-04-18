import json
import torch
import os
from datasets import Dataset
from transformers import (
    T5Tokenizer,
    T5ForConditionalGeneration,
    Trainer,
    TrainingArguments
)

# =========================
# PATH SETUP (FIXED)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "../data/phq9_t5_dataset_3000_clean.json")
)

OUTPUT_MODEL_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "../models/t5_phq9_finetuned_model")
)

# =========================
# LOAD DATASET
# =========================
with open(DATASET_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

print("✅ Original Samples:", len(data))

# =========================
# REMOVE DUPLICATES
# =========================
unique_data = []
seen = set()

for item in data:
    pair = (item["input"].lower(), item["output"].lower())
    if pair not in seen:
        seen.add(pair)
        unique_data.append(item)

data = unique_data
print("✅ After Cleaning:", len(data))

dataset = Dataset.from_list(data)

# =========================
# LOAD MODEL
# =========================
tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

# =========================
# TOKENIZATION
# =========================
def tokenize_function(batch):
    inputs = tokenizer(
        batch["input"],
        padding="max_length",
        truncation=True,
        max_length=64
    )

    labels = tokenizer(
        batch["output"],
        padding="max_length",
        truncation=True,
        max_length=64
    )

    labels["input_ids"] = [
        [(l if l != tokenizer.pad_token_id else -100) for l in label]
        for label in labels["input_ids"]
    ]

    inputs["labels"] = labels["input_ids"]
    return inputs

tokenized_dataset = dataset.map(
    tokenize_function,
    batched=True,
    remove_columns=["input", "output"]
)

# =========================
# TRAINING CONFIG
# =========================
training_args = TrainingArguments(
    output_dir=OUTPUT_MODEL_PATH,
    per_device_train_batch_size=8,
    num_train_epochs=3,
    learning_rate=3e-4,
    logging_steps=50,
    save_strategy="epoch",
    save_total_limit=2,
    report_to="none",
    fp16=torch.cuda.is_available()
)

# =========================
# TRAINER (FIXED)
# =========================
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset
)

# =========================
# TRAIN MODEL
# =========================
print("🚀 Training started...")
trainer.train()

# =========================
# SAVE MODEL
# =========================
trainer.save_model(OUTPUT_MODEL_PATH)
tokenizer.save_pretrained(OUTPUT_MODEL_PATH)

print("\n🎉 Model saved at:", OUTPUT_MODEL_PATH)