from MultipleChoiceQuiz_class import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
    "Czy to działa?\n(a) Działa\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)


"""
Pytania:
1. Jak działa wyświetlanie pytań
2. Czy pytania stworzone są w liście
3. Czy questions to również lista
4. Czemu dodajemy str(score) zamiast samo score
5. Co robi len() i dlaczego jest w str()
6. Co znaczy słowo prompt i jaką tu ma funkcję

"""
