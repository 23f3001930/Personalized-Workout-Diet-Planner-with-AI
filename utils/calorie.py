def calorie_estimation(weight, height, age, goal):
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    if goal == "Weight Loss":
        return int(bmr - 300)
    elif goal == "Muscle Gain":
        return int(bmr + 400)
    else:
        return int(bmr)
