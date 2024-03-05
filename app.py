import streamlit as st
import os
import google.generativeai as genai

# Setup the google Gemini AI API Key
google_api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=google_api_key)


prompt = """ You are an advanced Code Comment Generator AI model engineered to generate informative and well-structured comments for code snippets. The model should support multiple programming languages and diverse comment types based on the user's input. The primary goal is to enhance code readability, foster collaboration, and streamline the documentation process.

**Key Features:**
1. **Language Support:** Engineer the model to support a wide range of programming languages.
2. **Comment Types:** Implement the capability to generate different comment types, such as single-line comments, multi-line comments, and docstrings. Users should be able to specify the comment type based on their preferences and coding conventions.
3. **Context Awareness:** Enhance the model to be context-aware, understanding the code's functionality and purpose to generate comments that provide meaningful insights.
4. **Customization Options:** Provide users with customization options for template strings, enabling them to tailor the generated comments to align with project-specific coding standards.
5. **Edge Case Handling:** Engineer the model to intelligently handle edge cases and common scenarios, such as complex logic, nested structures, and diverse coding styles.
6. **Natural Language Fluency:** Ensure that the generated comments are written in natural and fluent language, contributing to improved code comprehension.

**Input Validation:**
Before executing, the model checks if the user's input contains a valid code snippet and ensures the absence of malicious code. If the input is not a proper code snippet, the user receives a reply asking for a valid code snippet and emphasizing the exclusion of malicious code.

**Example Usage:**
The user inputs a code snippet along with the desired comment type (e.g., explaining functionality, marking assumptions) and the programming language. The Code Comment Generator AI model then processes this input and produces a well-crafted comment that effectively communicates the purpose and details of the code.

**Evaluation Criteria:**
1. **Clarity and Informativeness:** Assess the generated comments for clarity and informativeness, ensuring they contribute significantly to code comprehension.
2. **Language Accuracy:** Evaluate the model's ability to generate comments that adhere to the syntax and conventions of the chosen programming language.
3. **Flexibility:** Measure the flexibility of the model in accommodating various coding styles, contexts, and user preferences.

The Code Comment Generator should stand as an intelligent tool that elevates code documentation practices, promoting collaboration and enhancing the overall developer experience.

Here is the code snippet: 


"""

# Function to load OpenAI model and get responses
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt + question, generation_config=genai.types.GenerationConfig(
                                            candidate_count=1,temperature=temperature))
        return response.text
    except Exception as e:
        st.warning("An error occurred. Please press Generate again or check logs for more details.")
        return None

# Initialize the Streamlit app
st.set_page_config(page_title="Code Comment Generator")
st.header("Code Comment Generator")
st.warning('''The generated output may not always meet your expectations. 
           If you find that the result is not up to the mark or doesn't meet your requirements, please consider hitting the generate button again for an improved outcome.
           Use the generated code at your own discretion, and feel free to refine the input or adjust any parameters to achieve the desired comments for your code.''')

st.sidebar.write("Adjust the parameters to control the creativity of the generated comments:")
st.sidebar.write("\n")
st.sidebar.write("Temperature: Controls the randomness of the generated text. Higher values (e.g., 1.0) make the output more creative but less focused.")
temperature = st.slider("Temperature", 0.1, 1.0, 0.7, step=0.1, key="temperature")

# Input text area
input_text = st.text_area("Input:", key="input")

# Generate button
submit_button = st.button("Generate")

# If the Generate button is clicked
if submit_button:
    response = get_gemini_response(input_text)
    if response is not None:
        st.subheader("The Response is")
        st.write(response)

# Footer
footer = """
    <div style="position: fixed; bottom: 10px; width: 100%; text-align: center; color: #888;">
        <p style="margin: 0 auto; padding: 10px; display: inline-block;">
            Made with ❤️ by <a href="https://twitter.com/ishubhamsah" target="_blank" style="text-decoration: none; color: #888;">Shubham</a>
        </p>
    </div>
"""

st.markdown(footer, unsafe_allow_html=True)
