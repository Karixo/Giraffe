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
    score = 0                               # wartość podstawowa dla wyniku - score
    for question in questions:              # dla kazdego obiektu question obecnego na liście w questions
        answer = input(question.prompt)     # answer = wpis uzytkownika
        if answer == question.answer:       # jeśli answer jest tożsamy z question.answer to
            score += 1                      # dodaje 1 dla wyniku
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)  # odpala funkcję run_test dla zmiennej questions*


"""
Pytania:
1. Jak działa wyświetlanie pytań
Odpowiedź: Pytanie nowa_linia Odpowiedź nowa_linia

2. Czy pytania stworzone są w liście
Odpowiedź: Tak, bo nazwa_listy = []

3. Czy questions to również lista
Odpowiedź: questions = [...], też lista, tylko że zawiera obiekty: 
Question(question_prompts[0], "a") 
- Question - obiekt 
- question_prompts[0] - "wartość" elementu prompt(self.prompt) z klasy Question, przypisanie pytania(element listy typu string) 
- "a" - wartość dla answer

4. Czemu dodajemy str(score) zamiast samo score
Odpowiedź:
can only concatenate str (not "int") to str - komunikat błędu
Czyli nie mozna łączyć int ze string
String do stringa, 
int do inta(ale na intach to juz działania wychodzą)

5. Co robi len() i dlaczego jest w str()
Odpowiedź:
len(np. nazwa_listy) - pokaże ilość elementów tej listy
 - Tutaj jest wykorzystane do sprytnego wyświetlenia ilości zdobytych punktów: 
 score/len(questions)
 ilość punktów/ilość pytań
 
 str(len(questions)) - w str żeby móc wyświetlić w konsoli z resztą tego co w print'cie

6. Co znaczy słowo prompt i jaką tu ma funkcję
Odpowiedź: 
prompt(czasownik) – wywołać – tak jakby zachęcić, „szturchnąć do zrobienia czegos”

Czyli prompt jako zachęcenie do działania
question_prompts - pytanie prowokujące(zachęcające) do reakcji
self.prompt - prompt - pytanie z odpowiedzią abc
"""
