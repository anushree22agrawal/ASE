import random
import json

# Generate a logical expression with parentheses
def generate_expression():
    vars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x', 'y']
    ops = ['>', '<', '==', '!=', '<=', '>=']
    logical = ['&&', '||']
    expr = [f"({random.choice(vars)} {random.choice(ops)} {random.randint(0, 9)})"]
    for _ in range(random.randint(1, 2)):
        expr.append(random.choice(logical))
        expr.append(f"({random.choice(vars)} {random.choice(ops)} {random.randint(0, 9)})")
    return ' '.join(expr)

# Convert a compound if condition into nested if statements
def to_nested_if(expr, action="doSomething();"):
    parts_and = expr.split('&&')
    code = ""
    indent = ""

    for i, part in enumerate(parts_and):
        part = part.strip()
        if '||' in part:
            parts_or = part.split('||')
            code += f"{indent}if ({parts_or[0].strip()}) {{\n"
            code += f"{indent}    {action}\n"
            code += f"{indent}}}\n"
            for sub_part in parts_or[1:]:
                code += f"{indent}else if ({sub_part.strip()}) {{\n"
                code += f"{indent}    {action}\n"
                code += f"{indent}}}\n"
        else:
            code += f"{indent}if ({part}) {{\n"
            indent += "    "

    for _ in parts_and:
        indent = indent[:-4]
        code += f"{indent}}}\n"

    return code

# Generate a dataset of C programs
def generate_dataset(n=1000):
    data = []
    for _ in range(n):
        cond = generate_expression()
        compound_if = f"if ({cond}) {{ doSomething(); }}"
        nested_if = to_nested_if(cond)
        
        full_input = f"""#include <stdio.h>

int main() {{
    int a=1,b=2,c=3,d=4,e=5,f=6,g=7,x=5,y=10;
    {compound_if}
    return 0;
}}"""
        
        full_output = f"""#include <stdio.h>

int main() {{
    int a=1,b=2,c=3,d=4,e=5,f=6,g=7,x=5,y=10;
    {nested_if}
    return 0;
}}"""
        data.append({'input': full_input, 'output': full_output})
    return data

# Generate the dataset
dataset = generate_dataset(400)

# Save the dataset to a JSON file
output_path = "nested_if_full_c_code.json"
with open(output_path, "w") as f:
    json.dump(dataset, f, indent=4)
