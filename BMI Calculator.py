def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    # Categorize BMI
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    # Get user input
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        
        # Validation for positive values
        if weight <= 0 or height <= 0:
            print("Error: Please enter positive values for weight and height.")
            return

        # Calculate BMI and classify
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        # Display the result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Error: Invalid input! Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()