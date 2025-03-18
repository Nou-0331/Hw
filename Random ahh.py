import random

def guess_number_game():
    # 生成一個1到100之間的隨機數字
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the guess the random number , guess a number between 1 to 100")
    
    while True:
        try:
            # 玩家輸入猜測的數字
            guess = int(input("Please enter your guess: "))
            attempts += 1
            
            # 檢查猜測結果
            if guess < number_to_guess:
                print("Too small Try again")
            elif guess > number_to_guess:
                print("Too big Try again")
            else:
                print(f"Congrats you got it right , you guessed {attempts} times")
                break
        except ValueError:
            print("Please enter the number")

# 遊戲開始
guess_number_game()