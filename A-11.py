height = input("Height(m)? > ")
weight = input("Weight(kg)? > ")
bmi = float(weight) / (float(height) ** 2)
print(f"Your BMI is {round(bmi, 2)}")
