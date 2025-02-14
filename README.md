# My Invoice OCR

This project is a simple OCR (Optical Character Recognition) app to extract text from invoice records using Google Gemini API and Streamlit for the UI.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/gemini_project.git
    cd gemini_project
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root directory and add your Google API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

5. **Install additional libraries:**

    ```sh
    pip install google-cloud-vision Pillow python-dotenv
    ```

## Usage

1. **Run the Streamlit app:**

    ```sh
    streamlit run app.py
    ```

2. **Upload an invoice image:**

    - Click on the "Upload an image" button and select an invoice image (jpg, png, jpeg).

3. **Enter your prompt:**

    - Type your question or prompt in the text input field.

4. **Get the response:**

    - Click on the "Press me" button to get the response from the Google Gemini API.

## Project Structure

```
gemini_project/
│
├── app.py              # Main application file
├── requirements.txt    # List of dependencies
├── .env                # Environment variables
└── README.md           # Project documentation
```

## Dependencies

- `streamlit`
- `google-cloud-vision`
- `python-dotenv`
- `Pillow`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
