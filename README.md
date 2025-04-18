# ASE
C-Code Refactoring with CodeT5+

Transform Compound If Statements into Nested Ifs using a Fine-Tuned CodeT5+ Model

  

—

Overview

This project leverages the Salesforce CodeT5+ model to transform C code containing compound if statements into logically equivalent nested if constructs. The goal is to make complex conditions more readable and structurally easier to analyze or teach.

—

Features

Automatically convert compound logical expressions in C into nested ifs

Fine-tuned CodeT5+ (220M) on synthetic examples

Token-level training using Hugging Face’s Trainer API

End-to-end pipeline: data generation → training → evaluation → inference


—

Folder Structure

├── nested_if_full_c_code.json     # Synthetic dataset
├── sample_input.c                 # Sample source code (compound ifs)
├── output.c                       # Transformed code (nested ifs)
├── codeT5-nested-if/              # Trained model checkpoint
├── generate_dataset.py            # Code to create synthetic dataset
├── train_and_evaluate.py          # Fine-tuning pipeline
├── inference.py                   # Inference script
├── transform.py                   # File-level C code transformer
└── README.md                      # This file

—

Setup & Installation

1. Clone the repo:



git clone https://github.com/your-username/code-nested-if-transformer.git
cd code-nested-if-transformer

2. Install dependencies:



pip install transformers datasets torch

—

Step-by-Step Pipeline

1. Dataset Generation

Generate synthetic C code samples with compound and nested ifs:

python generate_dataset.py

This creates a JSON file: nested_if_full_c_code.json with 400 input-output pairs.

—

2. Model Fine-Tuning

Use Hugging Face’s Trainer to fine-tune CodeT5+:

python train_and_evaluate.py

Training uses the dataset and saves the model to ./codeT5-nested-if with evaluation at each epoch.

—

3. Inference

Use the fine-tuned model to transform new C code:

from inference import predict

compound_if_code = "...your code..."
nested_if_code = predict(compound_if_code)
print(nested_if_code)

—

4. File Transformation Utility

Transform a real C file:

from transform import transform_c_file

transform_c_file("sample_input.c", "output.c")

—

Example

Input (sample_input.c):

if ((a > 10 || b < 5) && c == 3) {
    printf("Run\n");
}

Output (output.c):

if (a > 10) {
    if (c == 3) {
        printf("Run\n");
    }
} else if (b < 5) {
    if (c == 3) {
        printf("Run\n");
    }
}

—

Future Work

Add transformation for if-else and switch-case logic

Use static code parsers for robust AST generation

Build a web-based UI for code uploading and transformation


—

License

This project is licensed under the MIT License.

—

Acknowledgements

CodeT5+ by Salesforce

Hugging Face Transformers & Datasets

GitHub Copilot inspiration for AST ideas





