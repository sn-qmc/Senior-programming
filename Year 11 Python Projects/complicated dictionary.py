question = "Question"
answer = "Answer"
potential_answers = "Potential Answers"
quiz_values = [
    {question: "11 ^ 2",
     potential_answers: {"a": "22", "b": "212", "c": "121"},
     answer: "b"},
    {question: "33 / 11",
     potential_answers: {"a": "3", "b": "1", "c": "5"},
     answer: "a"},
    {question: "5 * 7",
     potential_answers: {"a": "42", "b": "99", "c": "35"},
     answer: "c"}
]

possible_answers = ["a", "b", "c"]

for question_set in quiz_values:
    print(question_set[question])
    
    for key, value in question_set[potential_answers].items():
        print(f"{key}: {value}")
    
    while True:
        user_answer = input("Please enter your choice, a, b or c: ").strip().lower()
        if(user_answer in possible_answers):
            break
        else:
            print("Please choose between: a, b or c")
    
    if(user_answer == question_set[answer]):
        print("Correct!")
    else:
        print("Fool!")