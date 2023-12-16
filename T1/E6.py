##BMI Calculator: Develop a Body Mass Index (BMI) calculator that takes a person's weight and
##height and calculates their BMI
## 
## Ref -- https://www.calculatorsoup.com/calculators/health/bmi-calculator.php
##

def calculate_bmi(weight_kg, height_m):
    try:
        # Calcular el BMI utilizando la fórmula: BMI = peso (kg) / (altura (m) * altura (m))
        bmi = weight_kg / (height_m * height_m)
        return bmi
    except ZeroDivisionError:
        return print("Height cannot be zero. Please enter a valid height.")

def main():
    print("Welcome to the BMI Calculator!")
    try: 
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_m = float(input("Enter your height in meters: "))

        bmi = calculate_bmi(weight_kg, height_m)

        if isinstance(bmi, float):
            print(f"Your BMI is: {bmi:.2f}")
        else:
            print(bmi)
    
    except ValueError:
        return print("Values must be a float. Please enter a valid value.")

    if bmi< 18.5:
        print("Underweight")
    elif bmi>=18.5 and bmi<24.5:
        print("healthy")
    elif bmi>=24.5 and bmi<30:
        print("overweight")
    else:
        print("obese")

if __name__ == "__main__":
    main()
