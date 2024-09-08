questions = [
    "what is my name ? ",
    "how old am i ? ",
    "what is my favorite food ?",
    "what is my favorite club ?",
    "what is the most country i hate ?"
]
options = [
    ("A .john","B. achraf","C. david","D. loufi"),
    ("A. 23", "B. 17","C. 27","D. 21"),
    ("A. pizza", "B. kouskous", "C. meat","D. potato"),
    ("A. RMA","B. FCB","C. bayern","D. MAN-united"),
    ("A. Iran & Türkiye","B. Israel & US ","C. France & UK","D. All")
]
answers = ['B','D','C','A','D']
guesses = []
i = 0
score = 0

for question in questions:
    print(question)
    for option in options[i]:
        print(option)
    guess = input("Choose (A, B, C, D) : ").upper()
    guesses.append(guess)
    if guess == answers[i]:
        print("CORRECT !\n")
        score +=1
    else:
        print(f"INCORRECT , the correct answer is {answers[i]}\n")
    i+=1

print("------------------------------------------------------")

print("Guesses : ")
for guess in guesses:
    print(guess)

print("Answers :")
for answer in answers:
    print(answer)


print(f"your final score {score}/5")
