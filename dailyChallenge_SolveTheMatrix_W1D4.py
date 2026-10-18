
MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''    

matrix = [line.strip() for line in MATRIX_STR.strip().split("\n")]

decoded_message = ""

for col in range(len(matrix[0])):
    for row in matrix:
        if col < len(row):
            char = row[col]
            if char.isalpha():
                decoded_message += char
            else:
                decoded_message += " "

print(decoded_message)

# print(matrix[0][0]) # first number is the number OF the row, second is the number IN the row


