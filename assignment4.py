filename = "sample.txt"

try:
    with open(filename, "r") as file:
        print("Reading file content:")
        line_number = 1
        for line in file:
            # strip() removes the trailing newline character
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1


except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

filename = "output.txt"


text_to_write = input("Enter text to write to the file: ")
with open(filename, "w") as f:
    f.write(text_to_write + "\n")
print(f"Data successfully written to {filename}.")

text_to_append = input("Enter additional text to append: ")
with open(filename, "a") as f:
    f.write(text_to_append + "\n")
print("Data successfully appended.")



