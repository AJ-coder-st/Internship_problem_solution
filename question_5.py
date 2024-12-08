def strongest_trainees(strength_levels):
    # Check for invalid inputs
    for strength in strength_levels:
        if strength < 1 or strength > 200:
            return "INVALID INPUT"
    
    # Organize input into a 2D list (4 trainees x 3 rounds)
    trainees = [strength_levels[i:i+4] for i in range(0, len(strength_levels), 4)]
    
    # Calculate the average strength for each trainee
    averages = [round(sum(rounds) / 3) for rounds in zip(*trainees)]
    
    # Find the maximum average strength
    max_average = max(averages)
    
    # Check if all trainees are unfit
    if max_average < 100:
        return "All trainees are unfit"
    
    # Find trainees with the maximum average strength
    strongest = [i + 1 for i, avg in enumerate(averages) if avg == max_average]
    
    # Prepare the output
    result = [f"Trainee Number : {trainee}" for trainee in strongest]
    return "\n".join(result)

# Input processing
strength_levels = []
for _ in range(12):  # 4 trainees x 3 rounds = 12 inputs
    strength_levels.append(int(input()))

# Output the result
print("Output :")
print(strongest_trainees(strength_levels))
