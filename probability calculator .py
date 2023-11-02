def calculate_probability(event_outcomes, total_outcomes):
    probability = event_outcomes / total_outcomes
    return probability


event_outcomes = int(input("Enter the number of favorable outcomes: "))
total_outcomes = int(input("Enter the total number of outcomes: "))

if event_outcomes >= 0 and total_outcomes > 0:
    probability = calculate_probability(event_outcomes, total_outcomes)
    print(f"The probability of the event happening is: {probability:.2f}")
else:
    print("Invalid input. Number of favorable outcomes should be non-negative, and total outcomes should be positive.")
