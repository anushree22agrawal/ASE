
sample_c_code = """
#include <stdio.h>

int main() {
    int x = 10, y = 5, z = 15;

    if ((x > 5 || y < 10) || z == 15) {
        printf("Compound condition met.\\n");
    }
    return 0;
}
"""

input_file_path = "sample_input.c"
with open(input_file_path, "w") as f:
    f.write(sample_c_code)

# Read the saved file to verify content
with open(input_file_path, "r") as f:
    sample_content = f.read()

input_file_path, sample_content[:300]  # show path and a preview of the content
