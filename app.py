from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import google.generativeai as genai
import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown



prompt=""" Develop an advanced Code Comment Generator AI model engineered to generate informative and well-structured comments for code snippets. The model should support multiple programming languages and diverse comment types based on the user's input. The primary goal is to enhance code readability, foster collaboration, and streamline the documentation process.

**Key Features:**
1. **Language Support:** Engineer the model to support a range of programming languages, including but not limited to Python, Java, JavaScript, C++, and Ruby.
2. **Comment Types:** Implement the capability to generate different comment types, such as single-line comments, multi-line comments, and docstrings. Users should be able to specify the comment type based on their preferences and coding conventions.
3. **Context Awareness:** Enhance the model to be context-aware, understanding the code's functionality and purpose to generate comments that provide meaningful insights.
4. **Customization Options:** Provide users with customization options for template strings, enabling them to tailor the generated comments to align with project-specific coding standards.
5. **Edge Case Handling:** Engineer the model to intelligently handle edge cases and common scenarios, such as complex logic, nested structures, and diverse coding styles.
6. **Natural Language Fluency:** Ensure that the generated comments are written in natural and fluent language, contributing to improved code comprehension.

**Example Usage:**
The user inputs a code snippet along with the desired comment type (e.g., explaining functionality, marking assumptions) and the programming language. The Code Comment Generator AI model then processes this input and produces a well-crafted comment that effectively communicates the purpose and details of the code.

**Evaluation Criteria:**
1. **Clarity and Informativeness:** Assess the generated comments for clarity and informativeness, ensuring they contribute significantly to code comprehension.
2. **Language Accuracy:** Evaluate the model's ability to generate comments that adhere to the syntax and conventions of the chosen programming language.
3. **Flexibility:** Measure the flexibility of the model in accommodating various coding styles, contexts, and user preferences.

The Code Comment Generator should stand as an intelligent tool that elevates code documentation practices, promoting collaboration and enhancing the overall developer experience.


Please Generate code comments for the following code snippet:


"""


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    print(prompt+question)
    response = model.generate_content(prompt + question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Code Comment Generator")

st.header("Code Comment Generator")

input=st.text_area("Input: ",key="input")


submit=st.button("Generate")

## If ask button is clicked

if submit: 
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
