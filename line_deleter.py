import re
#To be adjustable
input_file = 'text.txt'
output_file = 'less_text.txt'
#in this case lines before 202X need to be deleted
keyword = r'.*202[0-9].*$'
lines_to_delete_before = 4
encoding = 'utf-8'  
try:
    with open(input_file, 'r', encoding=encoding) as input_f, \
         open(output_file, 'w', encoding=encoding) as output_f:
        buffer = []
        for line in input_f:
            buffer.append(line)
            if len(buffer) > lines_to_delete_before:
                if re.match(keyword, buffer[-1].strip()):
                    del buffer[:lines_to_delete_before]
                    output_f.writelines(buffer)
                    buffer = []
                else:
                    output_f.write(buffer.pop(0))
        output_f.writelines(buffer)
    print(f"Every {lines_to_delete_before} lines before lines matching the pattern '{keyword}' were deleted from '{input_file}', and the result is saved in '{output_file}'.")
except FileNotFoundError:
    print(f"File '{input_file}' not found.")
except Exception as e:
    print(f"line deleter ERROR!: {e}")
