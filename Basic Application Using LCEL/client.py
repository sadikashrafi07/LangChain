import requests
import streamlit as st

def get_groq_response(input_text):
    json_body = {
        "input": {
            "language": "French",
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }
    
    response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)
    
    # Extract the string output from the response JSON
    return response.json().get("output", "No output found")

## Streamlit app
st.title("LLM Application Using LCEL")
input_text = st.text_input("Enter the text you want to convert to French")

if input_text:
    output = get_groq_response(input_text)
    st.write(output)
