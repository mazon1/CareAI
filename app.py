import streamlit as st
import requests

# Streamlit UI
st.title("CareNote AI")
st.markdown("Generate detailed client notes from doctor summaries using AI.")

# Input field for doctor summary
summary = st.text_area("Enter Doctor Summary:", placeholder="e.g., Patient recovering from flu...")

# Button to generate notes
if st.button("Generate Notes"):
    if summary.strip():
        # Simulate API call to Gemini Nano AI
        with st.spinner("Generating notes..."):
            generated_notes = generate_notes(summary)
        st.text_area("Generated Notes:", value=generated_notes, height=200, placeholder="Your detailed notes will appear here.")
    else:
        st.warning("Please enter a doctor summary.")

# Simulated function to generate notes
def generate_notes(summary):
    try:
        # Replace with the actual API endpoint and your API key
        api_url = "https://api.geminiai.example.com/generate"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_API_KEY"
        }
        response = requests.post(api_url, json={"summary": summary}, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("notes", "No notes returned from API.")
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"An error occurred: {e}"
