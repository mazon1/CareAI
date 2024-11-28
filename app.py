import streamlit as st
import google.generativeai as genai
import os

# Set up the API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', st.secrets.get("GOOGLE_API_KEY"))
genai.configure(api_key=GOOGLE_API_KEY)


# Function to generate client notes from doctor summaries
def generate_notes(summary):
    try:
        # Use a pre-trained generative model (e.g., Gemini)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(summary)  # Pass the summary directly

        # Debug: Print the response structure
        # st.write(response) # Uncomment for debugging

        # Return the generated notes
        return response.text  # Use 'text' attribute instead of 'generated_text'
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
    summary = st.text_area("Enter Doctor Summary:", placeholder="e.g., Patient recovering from flu, prescribed rest and hydration.")

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


if __name__ == "__main__":
    main()
