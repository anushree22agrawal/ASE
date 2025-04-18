from transformers import Trainer, TrainingArguments, DataCollatorForSeq2Seq
from datasets import load_dataset
import time

# Tokenization functions
def tokenize(batch):
    return tokenizer(batch["input"], padding="max_length", truncation=True, max_length=128)

def preprocess(example):
    input_enc = tokenizer(example["input"], padding="max_length", truncation=True, max_length=128)
    target_enc = tokenizer(example["output"], padding="max_length", truncation=True, max_length=128)

    return {
        "input_ids": input_enc["input_ids"],
        "attention_mask": input_enc["attention_mask"],
        "labels": target_enc["input_ids"]
    }

# Training arguments
args = TrainingArguments(
    output_dir="./codeT5-nested-if",
    per_device_train_batch_size=4,
    num_train_epochs=5,           
    save_total_limit=2,
    logging_steps=10,                      
    report_to="none",              
    logging_strategy="steps",     
    save_strategy="steps",        
)

# Data collator
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

# Load and preprocess dataset
dataset = load_dataset("json", data_files="nested_if_full_c_code.json")["train"]
dataset = dataset.train_test_split(test_size=0.1)
tokenized_data = dataset.map(preprocess, remove_columns=["input", "output"])

# Trainer
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized_data["train"],
    eval_dataset=tokenized_data["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
)

for epoch in range(args.num_train_epochs):
    trainer.train()  # Train the model for one epoch
    
   
    print(f"Evaluating at the end of epoch {epoch + 1}...")
    eval_results = trainer.evaluate()
    
    
    print(f"Evaluation Results: {eval_results}")
    
    
    trainer.save_model()

    
    time.sleep(1)  
