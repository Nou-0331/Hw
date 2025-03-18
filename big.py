import random

def guess_number_game():
    print("Welcome to the number guessing game")
    
    while True:
        # 生成隨機數 (0 到 1000)
        number_to_guess = random.randint(0, 1000)
        attempts = 0
        print("Please guess a number between 0 to 1000")
        
        while True:
            try:
                # 玩家輸入
                guess = int(input("Enter your number:"))
                attempts += 1
                
                # 檢查猜測
                if guess < number_to_guess:
                    print(f"Too small your {abs(number_to_guess - guess)} away from the answer")
                elif guess > number_to_guess:
                    print(f"Too big your {abs(number_to_guess - guess)} away from the answer")
                else:
                    print(f"Congrats you got it right , you guessed {attempts} times")
                    break
            except ValueError:
                print("Please enter the number")
        
        # 問是否重新開始
        play_again = input("You wanna play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing , Goodbye!")
            break

# 遊戲開始
guess_number_game()