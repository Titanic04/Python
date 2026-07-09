questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter","Saturn", "None", 2
  ],
  [
    "Who was the first President of the United States?", "Thomas Jefferson", "Abraham Lincoln", "George Washington","John Adams", "None", 3
  ],
  [
    "Which of the following is the longest river in the world?", "Amazon River", "Nile River", "Yangtze River","Mississippi River", "None", 2
  ],
  [
    "What chemical element has the symbol 'K' on the periodic table?", "Krypton", "Potassium", "Calcium","Phosphorus", "None", 2
  ],
  [
    "Which video game is officially recognized as the best-selling video game of all time?", " Tetris", "Grand Theft Auto V", "Minecraft","Wii Sports", "None", 3
  ]
]


levels = [0,1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i+1]}")
  print(question[0])
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i+1-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i+1]}")
    
    if(i == 4):
      money = 10000
    elif(i == 11):
      money = 320000
    elif(i == 15):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")