import random 
def guess_number():
    to_guess= random.randint(1,100)
    attempts=0
    print("welcome to number guessing game!")
    while True:
        user_guess=int(input("please enter your guess(between 1 and 100): "))
        attempts+=1
        try:
            if user_guess < 1 or user_guess > 100:
                raise ValueError("Guess must be between 1 and 100.")
            if user_guess< to_guess:
                print("Lower Guess! Guess Higher")
            if user_guess> to_guess:
                print("Higher Guess! Guess Lower")
            if user_guess== to_guess:               
                print(f"Congratulations! You've guessed the number {to_guess} in {attempts} attempts.")
                break
                
        except ValueError:
            print("Invalid Input.Please Enter valid number")
            continue
            
if __name__ =="__main__":
    guess_number()
         
        
                
            
            
        