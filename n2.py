import streamlit as st


quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_option": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_option": "Mars",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Giraffe", "Elephant", "Blue Whale", "Hippopotamus"],
        "correct_option": "Blue Whale",
    },
]

quiz_score = 0
current_question = 0

st.title("Streamlit Quiz")

def display_question(question_data):
    global quiz_score

    st.write(f"**Question {current_question + 1}:** {question_data['question']}")
    selected_option = st.radio("Select an option:", question_data["options"])

    if selected_option == question_data["correct_option"]:
        quiz_score += 1

while current_question < len(quiz_data):
    display_question(quiz_data[current_question])

    if st.button("Next"):
        current_question += 1



st.write("Quiz completed!")    
st.write(f"Your Score: {quiz_score}/{len(quiz_data)}")