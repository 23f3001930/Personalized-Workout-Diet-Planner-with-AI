def generate_workout(profile):
    goal = profile["goal"]

    if goal == "Weight Loss":
        return """
        • 10 min warm-up
        • Jumping Jacks – 3×20
        • Squats – 3×15
        • Walking / Jogging – 20 min
        • Stretching – 10 min
        """

    if goal == "Muscle Gain":
        return """
        • Push-ups – 4×10
        • Squats – 4×15
        • Plank – 3×30 sec
        • Resistance training (if available)
        """

    return "Daily yoga + walking for 30 minutes"
