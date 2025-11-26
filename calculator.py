import logging

# Logging setup
logging.basicConfig(
    filename="calc_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

num1 = int(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

logging.info(f"Inputs received: {num1} {op} {num2}")

if op == '+':
    result = num1 + num2
    print("Result:", result)
    logging.info(f"Performed addition: {result}")

elif op == '-':
    result = num1 - num2
    print("Result:", result)
    logging.info(f"Performed subtraction: {result}")

elif op == '*':
    result = num1 * num2
    print("Result:", result)
    logging.info(f"Performed multiplication: {result}")

elif op == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        logging.error("Division by zero attempted")
    else:
        result = num1 / num2
        print("Result:", result)
        logging.info(f"Performed division: {result}")

else:
    print("Invalid operator")
    logging.error(f"Invalid operator entered: {op}")