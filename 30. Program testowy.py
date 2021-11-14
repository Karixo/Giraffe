"""print("What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n")
score = 1
x = 2
print(str(score) + str(x))"""


from MultipleChoiceQuiz_class import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
    "Czy to działa?\n(a) Działa\n(b) Red\n(c) Blue\n\n",
]


def run_test(questions):
    score = 0                               # wartość podstawowa dla wyniku - score
    for question in questions:              # dla kazdego obiektu question obecnego na liście w questions
        answer = input(question.prompt)     # answer = wpis uzytkownika
        if answer == question.answer:       # jeśli answer jest tożsamy z question.answer to
            score += 1                      # dodaje 1 dla wyniku
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


def main():
    questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "c"),
        Question(question_prompts[2], "b"),
        Question(question_prompts[3], "a")
    ]
    run_test(questions)


main()

# poprawiona wersja kodu z 30.MultipleChoiceQuiz - naprawiony błąd shadowingu
# błąd shadowingu naprawiony poprzez wrzucenie listy questions do funkcji main
