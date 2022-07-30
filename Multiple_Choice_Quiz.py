'''
File 1 called "Question.py"
'''
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
        
#file 2

from Question import Question

Question_prompts = [
    "What pokemon is yellow with a lightning bolt shaped tail?\n(a) Garydose\n(b) Pikachu\n(c) Meowth\n\n",
    "Which pokemon is the sickest?\n(a) Weezing\n(b) Coffing\n(c) Arcanine\n\n",
    "Which pokemon is the biggest?\n(a) Snorlax\n(b) Mew\n(c) Mew2\n\n",
]

Questions = [
    Question(Question_prompts[0], "b"),
    Question(Question_prompts[1], "c"),
    Question(Question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for Question in Questions:
        answer = input(Question.prompt)
        if answer == Question.answer:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(Questions)
