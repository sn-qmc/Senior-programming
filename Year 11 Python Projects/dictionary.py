q = "question"
a = "answers"
quiz_questions_answers = [
    {q:"3 x 5 = ",
    a: "15"},
    {q:"7 + 2 = ",
    a: "9"},
    {q:"4 - 3 = ",
    a: "1"},
    {q:"8 / 4 = ",
    a: "2"},
    {q:"9 x 11 = ",
    a: "99"},
    {q:"16 / 2 = ",
    a: "8"},
]
"""
quiz_questions_answers = [
    {"question":"3 x 5 = ",
    "answer": "15"},
    {"question":"7 + 2 = ",
    "answer": "9"},
    {"question":"4 - 3 = ",
    "answer": "1"},
    {"question":"8 / 4 = ",
    "answer": "2"},
    {"question":"9 x 11 = ",
    "answer": "99"},
    {"question":"16 / 2 = ",
    "answer": "8"},
]
"""
score = 0

for question in quiz_questions_answers:
    answer = input(question[q])
    if(answer == question[a]):
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        score -= 2
        
print(score)