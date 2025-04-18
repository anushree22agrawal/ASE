from transformers import AutoTokenizer, T5ForConditionalGeneration,TrainingArguments, DataCollatorForSeq2Seq
from datasets import load_dataset
from transformers import Trainer, TrainingArguments, AutoModelForCausalLM
# Load model & tokenizer
model_name = "Salesforce/codet5p-220m"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

#dataset loading
# Load dataset
data = load_dataset("json", data_files="nested_if_full_c_code.json", split="train")
