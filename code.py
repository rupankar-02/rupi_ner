import streamlit as st
import spacy
from spacy import displacy
import newspaper

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Streamlit app title and description
st.title("Named Entity Recognizer")
st.info("This app analyzes paragraphs or news articles for named entities.")

# Radio button to select input type
input_type = st.radio("Select Input Type:", ("Paragraph", "URL"))

# Function to process and display entities from paragraph input
def process_paragraph(text):
    doc = nlp(text)
    ent_html = displacy.render(doc, style="ent")
    st.markdown(ent_html, unsafe_allow_html=True)

# Function to process and display entities from URL input
def process_url(url):
    article = newspaper.Article(url)
    try:
        article.download()
        article.parse()
        cleaned_text = article.text  # Use the parsed text directly
        doc = nlp(cleaned_text)
        ent_html = displacy.render(doc, style="ent")
        st.markdown(ent_html, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error: {e}. Please check if the URL is valid.")

# Render input components based on selection
if input_type == "Paragraph":
    text = st.text_area("Enter your paragraph here:")
    if st.button("Process"):
        if text:
            process_paragraph(text)
        else:
            st.warning("Please enter a paragraph.")

elif input_type == "URL":
    url = st.text_input("Enter the URL of the news article:")
    if st.button("Process"):
        if url:
            process_url(url)
        else:
            st.warning("Please enter a URL.")

# Slider for rating the app
rating = st.slider("Rate this app (out of 10):", 1, 10)
st.text(f"You rated this app: {rating}/10")

# Acknowledgment
st.info("Created by Rupankar Mitra for NLP Assignment.")
