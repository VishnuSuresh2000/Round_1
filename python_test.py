input_number = int(input("Enter the number: "))

apl = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

for i in range(1, input_number + 1):
    print(" " * (input_number - i), " ".join(apl[:i]))
for i in range(input_number - 1, 0, -1):
    print(" " * (input_number - i), " ".join(apl[:i]))
