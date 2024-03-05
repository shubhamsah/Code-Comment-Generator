# Code Comment Generator

The Code Comment Generator is designed to generate informative and well-structured comments for code snippets. The primary goal is to enhance code readability, foster collaboration, and streamline the documentation process. It uses Gemini-pro as the model behind the scenes.

## Key Features

1. **Language Support:** The model supports a wide range of programming languages.
2. **Comment Types:** It can generate different comment types, such as single-line comments, multi-line comments, and docstrings.
3. **Context Awareness:** The model is context-aware, understanding the code's functionality to provide meaningful insights.
4. **Customization Options:** Users can customize template strings to align with project-specific coding standards.
5. **Edge Case Handling:** The model intelligently handles edge cases, including complex logic, nested structures, and diverse coding styles.
6. **Natural Language Fluency:** Generated comments are written in natural and fluent language.


## Example Usage

1. Input a code snippet.
2. The Code Comment Generator processes the input and produces a well-crafted comment.


## Usage

1. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
2. Set up your environment variables. Create a .env file and add your Google API key:
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```
3. Run the Streamlit app:
    ```
    streamlit run your_app_name.py
    ```

### Acknowledgments
The Code Comment Generator was developed by Shubham Sah.

Made with ❤️ by Shubham
