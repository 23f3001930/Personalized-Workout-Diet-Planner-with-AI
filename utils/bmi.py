def calculate_bmi(weight, height_cm):
    if height_cm <= 0 or weight <= 0:
        return 0, "Enter valid height & weight"

    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 24.9:
        status = "Normal"
    elif bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obese"

    return round(bmi, 2), status

