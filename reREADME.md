# 🔄 Compound `if` to Nested `if` Converter for C Code

This Python script transforms C code by converting compound `if` statements with logical `&&` and `||` operators into equivalent nested `if` blocks. This can be useful for simplifying complex conditions, aiding code analysis, or preparing for logic-based transformations (e.g., in machine learning or code translation tools).

---

📁 Features

- Detects `if` statements with compound conditions using regex.
- Converts `&&` (AND) to nested `if` blocks.
- Converts `||` (OR) to `else`-based conditional branches.
- Supports file input and output for easy integration.

---

🚀 Usage

1. Prepare your C source file with compound `if` conditions.
2. Run the script using Python.
3. The transformed code will be saved in a new output file.

---

🧠 How It Works

- **Regex Matching**: Finds compound `if` blocks.
- **Tokenization**: Breaks logical expressions into tokens.
- **Parsing**: Builds a tree-like structure based on logical operators and parentheses.
- **Code Generation**: Recursively generates equivalent nested `if` blocks.

---

## 📜 Function Overview

- `convert_compound_ifs_to_nested(source_code)`: Main function that identifies and converts compound `if` statements.
- `logical_to_nested_if_body(expr, action_code)`: Processes logical expressions and prepares for nesting.
- `parse_tokens(tokens)`: Converts expressions into structured logical units.
- `generate_code(parsed, action_code)`: Generates properly indented nested `if` statements.
- `transform_c_file(input_path, output_path)`: Reads input and writes transformed output to a file.

---

## 🧪 Example

Place a C file named `sample_input.c` in the same directory, run the script, and view the output in `output.c`.

---

## 🛠️ Requirements

- Python 3.x
- No external dependencies required

---

