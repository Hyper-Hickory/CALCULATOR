def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error! Division by zero."
        result /= num
    return result

print("Select an operation to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = int(input("Enter the operation: "))
numbers = [int(num) for num in input("Enter the numbers separated by space: ").split()]

if operation == 1:
    print(add(numbers))
elif operation == 2:
    print(subtract(numbers))
elif operation == 3:
    print(multiply(numbers))
elif operation == 4:
    print(divide(numbers))
else:
    print("Invalid output")
