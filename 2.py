input = "input.txt"

message = ''
with open(input,'r') as fp:
    for line in fp:
        for char in line:
            if ord(char) >= 97 and ord(char) <= 122:
                message = message + char    

print(message)
