import re

def convert_compound_ifs_to_nested(source_code):
    # Adjust regex pattern to match 'if' statements with compound conditions
    pattern = re.compile(r'if\s*\((.*?)\)\s*{(.*?)}', re.DOTALL)

    def replace_if(match):
        condition = match.group(1).strip()
        action_block = match.group(2).strip()
        nested_code = logical_to_nested_if_body(condition, action_block)
        return nested_code

    return pattern.sub(replace_if, source_code)


def logical_to_nested_if_body(expr, action_code):
    # Replace '&&' with ' AND ' and '||' with ' OR ' for easier parsing
    expr = expr.replace('&&', ' AND ').replace('||', ' OR ')
    tokens = re.findall(r'\(|\)|AND|OR|!=|==|<=|>=|[<>]|[A-Za-z_][A-Za-z0-9_]*|\d+', expr)
    parsed = parse_tokens(tokens)
    return generate_code(parsed, action_code)


def parse_tokens(tokens):
    def parse_group(index):
        items = []
        while index < len(tokens):
            token = tokens[index]
            if token == '(':
                subgroup, index = parse_group(index + 1)
                items.append(subgroup)
            elif token == ')':
                return items, index + 1
            elif token in {'AND', 'OR'}:
                items.append(token)
                index += 1
            else:
                items.append(parse_condition(tokens, index))
                index += 3
        return items, index

    def parse_condition(tokens, index):
        # Parse conditions like x == 10 or x > 5 etc.
        if index + 2 < len(tokens) and tokens[index+1] in {'>', '<', '==', '!=', '<=', '>='}:
            return f"{tokens[index]} {tokens[index+1]} {tokens[index+2]}"
        return tokens[index]

    parsed, _ = parse_group(0)
    return parsed


def generate_code(parsed, action_code, indent=1):
    code = []
    i = 0
    while i < len(parsed):
        item = parsed[i]
        if isinstance(item, list):
            code.append(generate_code(item, action_code, indent))
            i += 1
        elif item == 'AND':
            left = code.pop()
            right = generate_code([parsed[i+1]], action_code, indent + 1)
            code.append(f"{left}\n{right}")
            i += 2
        elif item == 'OR':
            left = code.pop()
            right = generate_code([parsed[i+1]], action_code, indent)
            code.append(f"{left}\n{'    '*indent}else {{\n{right}\n{'    '*indent}}}")
            i += 2
        else:
            code.append(f"{'    '*indent}if ({item}) {{\n{'    '*(indent+1)}{action_code.strip()}\n{'    '*indent}}}")
            i += 1
    return '\n'.join(code)


# === File-based usage ===

def transform_c_file(input_path, output_path):
    with open(input_path, 'r') as f:
        source_code = f.read()

    transformed_code = convert_compound_ifs_to_nested(source_code)

    with open(output_path, 'w') as f:
        f.write(transformed_code)

    print(f"Transformed C code saved to: {output_path}")
    return transformed_code


# === Example ===
output = transform_c_file("sample_input.c", "output.c")

# Print output code as well
print(output)
