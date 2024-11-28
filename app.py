import streamlit as st
import google.generativeai as genai
import os

# Set up the API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', st.secrets.get("GOOGLE_API_KEY"))
genai.configure(api_key=GOOGLE_API_KEY)


# Function to generate clinical notes
def generate_notes(summary):
    try:
        # Refined prompt to align with documentation standards
        prompt = f"""
        Create detailed clinical notes based on the following summary:
        - {summary}
        Include:
        1. Diagnosis
        2. Treatment Plan
        3. Medication Dosage and Instructions
        4. Follow-Up Recommendations
        Format the notes clearly for medical documentation.
        """

        # Use Google Generative AI model
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)

        # Extract response text
        notes = response.text

        # Post-process to ensure structure
        if "Diagnosis:" not in notes:
            notes = "Diagnosis: Not specified.\n" + notes
        if "Treatment Plan:" not in notes:
            notes += "\nTreatment Plan: Not specified."
        if "Follow-Up:" not in notes:
            notes += "\nFollow-Up: Not specified."

        return notes
    except Exception as e:
        st.error(f"Error generating notes: {e}")
        return "Sorry, I couldn't process your request."


# Streamlit app
def main():
    st.title("CareNote AI")
    st.markdown("Generate detailed client notes from doctor summaries using AI.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Input area for doctor summary
    summary = st.text_area(
        "Enter Doctor Summary:", 
        placeholder="e.g., Patient recovering from flu, prescribed Tylenol."
    )

    # Button to generate notes
    if st.button("Generate Notes"):
        if summary.strip():
            st.session_state.chat_history.append({"role": "doctor", "content": summary})
            notes = generate_notes(summary)
            st.session_state.chat_history.append({"role": "assistant", "content": notes})
        else:
            st.warning("Please enter a valid doctor summary.")

    # Display conversation history
    st.subheader("Generated Notes")
    for message in st.session_state.chat_history:
        st.write(f"**{message['role'].capitalize()}**: {message['content']}")

    st.markdown("---")
    st.markdown("**Disclaimer:** Ensure all AI-generated content is reviewed by a healthcare professional before use.")


if __name__ == "__main__":
    main()
