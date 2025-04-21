def transform_c_file(input_path):
    with open(input_path, 'r') as f:
        source_code = f.read()
    return source_code


# === Example ===
source = transform_c_file("sample_input.c")

import torch
from transformers import Trainer, TrainingArguments
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer
model_path = "./codeT5-nested-if"  # Path to your saved model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

# Inference function
def predict(input_text):
    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    
    # Perform inference
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"], 
            attention_mask=inputs["attention_mask"],
            max_length=128,
            num_beams=5,  # Optional: Adjust the number of beams for beam search
            early_stopping=True
        )
    
    # Decode the output and return
    predicted_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return predicted_text

#input
predicted_code = predict(source)

# Print the predicted output
print("Predicted Nested If Code:\n", predicted_code)

