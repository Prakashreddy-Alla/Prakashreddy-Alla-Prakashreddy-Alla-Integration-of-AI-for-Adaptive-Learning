import streamlit as st
st.header("Questions:")

math_questions_list_easy = {
    1:[
        "What is the rank of the following 2x3 matrix?\n| 1  2  3 |\n| 4  5  6 |",
        ["A) 2", "B) 3", "C) 1", "D) 0"],
        "A"
    ],
    2:[
        "Which of the following is an example of a scalar in linear algebra?",
        ["A) A vector", "B) A matrix", "C) A real number", "D) A complex number"],
        "C"
    ],
    3:[
        "What is the trace of a 3x3 identity matrix?",
        ["A) 3", "B) 0", "C) 1", "D) 2"],
        "A"
    ],
    4:[
        "In a matrix multiplication AB, if A is an m x n matrix and B is an n x p matrix, what is the size of the resulting matrix AB?",
        ["A) m x p", "B) n x n", "C) p x m", "D) n x m"],
        "A"
    ],
    5:[
        "The determinant of a 2x2 matrix [a b; c d] is calculated as:",
        ["A) ad - bc", "B) ac - bd", "C) ab - cd", "D) bc - ad"],
        "A"
    ],
}
math_questions_list_hard={
    1: [
        "Question: What is the determinant of a 3x3 matrix with the following entries?\n| 2  0  1 |\n| 3  1 -2 |\n| 4  3  5 |",
        ["A) -26", "B) 26", "C) 34", "D) -34"],
        "A"
    ],
    2: [
        "Question: Which of the following matrices is not invertible (i.e., has no inverse)?",
        ["A) Identity matrix (3x3)", "B) A matrix with all elements equal to zero", "C) A matrix with all elements equal to one", "D) A matrix with zero determinant"],
        "D"
    ],
    3: [
        "Question: The eigenvectors of a matrix are linearly independent when:",
        ["A) They are orthogonal to each other", "B) They have different eigenvalues", "C) They are linearly dependent", "D) None of the above"],
        "B"
    ],
    4: [
        "Question: Which of the following operations changes the rank of a matrix?",
        ["A) Adding a multiple of one row to another row", "B) Multiplying all elements in a row by a non-zero constant", "C) Swapping two rows", "D) None of the above"],
        "D"
    ],
    5: [
        "Question: The transpose of a row matrix results in a:",
        ["A) Row matrix", "B) Column matrix", "C) Diagonal matrix", "D) Square matrix"],
        "B"
    ],
}


easy_crct=0
hard_crct=0
easy_wrng=0
hard_wrng=0

x=1

while(x<=len(math_questions_list_easy)):
    st.write(math_questions_list_easy[x][0])
    #ans= st.radio("Select an option:", ["Option A", "Option B", "Option C"])
    ans= st.radio("Select an option:", math_questions_list_easy[x][1])

    st.write("You selected:",ans)

    #st.write(easy_crct,easy_wrng)

    if st.button("Submit"):
        if ans[0]==math_questions_list_easy[x][-1]:
            easy_crct+=1
        else:
            easy_wrng+=1
        x+=1




