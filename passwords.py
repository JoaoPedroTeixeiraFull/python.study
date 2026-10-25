# User inputs during a hypothetical registration
#username = "dev_user"
#password_input = "12345"

# Checking the minimum length requirement
#if len(password_input) >= 8:
    #print("Registration successful! Password meets security standards.")
#else:
    #print("Registration failed: Password must be at least 8 characters long.")

correct_password = "SecretPassword"
max_attempts = 3
attempts_used = 0

# The loop keeps running while the user has attempts left
while attempts_used < max_attempts:
    # input() allows the user to type something directly into the terminal
    user_input = input("Enter your password: ")
    
    if user_input == correct_password:
        print("Access granted! Welcome.")
        break  # The 'break' command stops the loop immediately because the user got it right
    else:
        attempts_used = attempts_used + 1
        remaining = max_attempts - attempts_used
        print(f"Wrong password. Remaining attempts: {remaining}\n")

# If the loop finished and the user used all attempts without hitting 'break'
if attempts_used == max_attempts:
    print("ALERT: Account locked!")

