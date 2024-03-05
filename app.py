import streamlit as st
import os
import google.generativeai as genai

from PIL import Image
# Loading Image using PIL
im = Image.open('./content/App_Icon.png')


# Setup the google Gemini AI API Key
google_api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=google_api_key)


prompt = """ You are an advanced Code Comment Generator AI model engineered to generate informative and well-structured comments for code snippets. The model should support multiple programming languages and diverse comment types based on the user's input. The primary goal is to enhance code readability, foster collaboration, and streamline the documentation process.

*Input Validation:*
Before executing, the model checks if the user's input contains a valid code snippet and ensures the absence of malicious code. If the input is not a proper code snippet, the user receives a reply asking for a valid code snippet.

*Example Usage:*
The user inputs a code snippet along with the desired comment type (e.g., explaining functionality, marking assumptions) and the programming language. The Code Comment Generator AI model then processes this input and produces a well-crafted comment that effectively communicates the purpose and details of the code.

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
st.set_page_config(page_title="Code Comment Generator", page_icon = im)
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
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
footer = ''' Made with <svg viewBox="0 0 1792 1792" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" style="height: 0.8rem;"><path d="M896 1664q-26 0-44-18l-624-602q-10-8-27.5-26T145 952.5 77 855 23.5 734 0 596q0-220 127-344t351-124q62 0 126.5 21.5t120 58T820 276t76 68q36-36 76-68t95.5-68.5 120-58T1314 128q224 0 351 124t127 344q0 221-229 450l-623 600q-18 18-44 18z" fill="#e25555"></path></svg> by Shubham Sah'''

st.markdown(footer, unsafe_allow_html=True)
