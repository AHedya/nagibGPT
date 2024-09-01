import streamlit as st
import requests



url = 'http://backend:8000/generate_text/nagib_mahfouz'
#url = 'http://localhost:8000/generate_text/nagib_mahfouz'  ## remove comment incase of not using docker compose

# Function to handle API call
def call_api(sample, max_tokens , temp, top_k):
    sample = sample.strip()
    if len(sample) == 0 :
        raise ValueError('Sample cannot be empty')
    payload = {
        'sample':sample ,
        'max_tokens':max_tokens,
        'temp':temp,
        'top_k':top_k,
    }
    filter_payload = {k:v for k , v in payload.items() if v is not None and v !='' } #remove the filed if it's None 
    response = requests.post(url, json=filter_payload)
    return response

# Main Streamlit app
def main():
    st.title("API Caller")

    # Input fields
    sample = st.text_input("Enter sample to predict based on (Arabic)")
    show_more = st.checkbox("Show more options")

    if show_more:
        max_tokens = st.text_input("number of tokens to predict ")
        temp = st.text_input("model temperature")
        top_k = st.text_input("number of tokens to pool from ")
    else:
        max_tokens, temp, top_k = None, None, None

    if st.button("Submit"):
        # Make the API call
        try:
            with st.spinner("Calling API..."):

                response = call_api(sample , max_tokens, temp , top_k)
                st.subheader(response.json()['output'][0])

        except ValueError as e  :
            st.error(f"Value Error: {e}", '\mTry: مرحبا')
        except Exception as e:
            st.error(f"An error occurred while making the API call. {e}")      
            
    

if __name__ == "__main__":
    main()
