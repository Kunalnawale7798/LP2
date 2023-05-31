def apply_bitwise_operation(string, operation):
    result = ""
    for char in string:
        if operation == '&':
            result += chr(ord(char) & 127)
        elif operation == '^':
            result += chr(ord(char) ^ 127)
    return result

string = "Hello World"
print("Original String:", string)

# Apply bitwise AND operation
and_result = apply_bitwise_operation(string, '&')
print("After AND Operation:", and_result)

# Apply bitwise XOR operation
xor_result = apply_bitwise_operation(string, '^')
print("After XOR Operation:", xor_result)
