from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
import streamlit as st

def create_template():
    template = """
    You are an expert quiz maker for technical fields.
    Create a quiz with {num_questions} multiple-choice questions about the following concepts: {quiz_context}.
    Increase the difficulty if I answer correctly and decrease it if I answer wrong.
    """
    prompt = PromptTemplate.from_template(template)
    return prompt

def create_chain(prompt_template, llm):
    return LLMChain(llm=llm, prompt=prompt_template)

def main():
    st.title("MCQ's")
    st.write("Generating MCQ,s")
    openai_api_key="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"
    
    
    llm = ChatOpenAI(api_key=openai_api_key)
    
    prompt_template = create_template()
    chain = create_chain(prompt_template, llm)
    
    context = st.text_area("Enter the contents of the quiz")
    num_questions = st.number_input("Enter number of questions", min_value=1, max_value=100, step=1)
    
    if st.button("Generate Quiz"):
        quiz_response = chain.run(num_questions=num_questions, quiz_context=context)
        st.write(quiz_response)

if __name__ == "__main__":
    main()
