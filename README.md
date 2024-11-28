
# **CareNote AI**

CareNote AI is a web-based application designed to help healthcare professionals generate detailed client notes from concise doctor summaries using Google AI Studio's generative models. The app uses AI to simplify documentation, improve communication, and save time in clinical workflows.

---

## **Features**
- **AI-Powered Note Generation**: Converts short doctor summaries into detailed client notes.
- **Streamlined Workflow**: User-friendly interface for doctors to input summaries and get structured outputs.
- **Session History**: Maintains a chat-like interface for tracking input summaries and AI-generated notes.
- **Error Handling**: Provides clear feedback if any issues occur during note generation.

---

## **Technologies Used**
- **Python**: Core programming language.
- **Streamlit**: Framework for building the web app interface.
- **Google AI Studio**: For leveraging generative AI models (e.g., `gemini-pro`).
- **Google Generative AI SDK**: Python library for interacting with Google AI models.

---

## **Setup and Installation**

### **Prerequisites**
1. Python 3.7 or later.
2. A Google Cloud Platform (GCP) account with access to Vertex AI or Google AI Studio.
3. API key for Google AI Studio.

### **Installation Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/carenote-ai.git
   cd carenote-ai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.streamlit/secrets.toml` file and add your Google API key:
   ```toml
   [GOOGLE_API_KEY]
   GOOGLE_API_KEY = "your-google-api-key"
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser at `http://localhost:8501`.

---

## **Usage**
1. Enter a doctor summary in the provided text area (e.g., "Patient recovering from flu...").
2. Click the **Generate Notes** button.
3. View the AI-generated notes in the output section.
4. Review the session history to see past inputs and generated notes.

---

## **Example**
### **Input**:
```plaintext
Patient recovering from flu, prescribed rest and hydration.
```

### **Output**:
```plaintext
Diagnosis: Viral influenza.
Treatment Plan: Adequate hydration and complete rest for the next 5–7 days. Contact the clinic if symptoms worsen.
Follow-Up: Return for a check-up if symptoms persist.
```

---

## **Project Structure**
```
CareNoteAI/
├── app.py                 # Main Streamlit application
├── requirements.txt       # List of dependencies
├── .streamlit/
│   └── secrets.toml       # Securely stores API keys
└── README.md              # Project documentation
```

---

## **Future Improvements**
1. **Multilingual Support**: Add translation for notes in multiple languages (e.g., French for Canada).
2. **EHR Integration**: Export notes directly to Electronic Health Record (EHR) systems.
3. **Custom Templates**: Allow doctors to select or create custom note templates.
4. **Deployment**: Deploy the app on Streamlit Cloud for broader accessibility.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgments**
- **Google AI Studio**: For providing powerful generative AI models.
- **Streamlit**: For making web app development seamless and efficient.

