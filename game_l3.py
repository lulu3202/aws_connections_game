import streamlit as st
import boto3
import json
import random
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve environment variables
bucket_name = os.getenv("AWS_BUCKET_NAME")
file_name = os.getenv("AWS_FILE_NAME")
access_key = os.getenv("AWS_ACCESS_KEY")
secret_key = os.getenv("AWS_SECRET_KEY")

def fetch_categories_from_s3(bucket_name, file_name):
    """
    Fetch categories from an S3 bucket.
    """
    try:
        # Initialize the S3 client using credentials from environment variables
        s3 = boto3.client(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )
        
        # Fetch the file content from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        file_content = response['Body'].read().decode('utf-8')
        
        # Parse the JSON content
        data = json.loads(file_content)
        return data.get("categories", {})
    except Exception as e:
        print(f"Error fetching categories from S3: {e}")
        return {}

def initialize_game():
    # Fetch categories from S3
    all_categories = fetch_categories_from_s3(bucket_name, file_name)

    if not all_categories:
        return {}, []

    # Check if there are at least 4 categories to sample
    if len(all_categories) < 4:
        st.error(f"Not enough categories available. Found {len(all_categories)} categories, but 4 are required.")
        return {}, []

    # Randomly select 4 categories
    selected_categories = dict(random.sample(list(all_categories.items()), 4))

    # Flatten the list of words into a single list and shuffle them
    all_words = [word for group in selected_categories.values() for word in group]
    random.shuffle(all_words)

    return selected_categories, all_words

# Initialize session state
if "categories" not in st.session_state:
    st.session_state.categories, st.session_state.all_words = initialize_game()
    st.session_state.remaining_categories = st.session_state.categories.copy()
    st.session_state.guessed_categories = []
    st.session_state.selected_words = []  # Track selected words
    st.session_state.correct_words = []   # Track correctly guessed words
    st.session_state.message = ""  # Track success/error message

# If categories could not be fetched, exit early
if not st.session_state.categories:
    st.stop()

# CSS for the grid
st.markdown("""
    <style>
    .word-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-bottom: 20px;
    }
    .word-button {
        width: 100%;
        padding: 20px 10px;
        text-align: center;
        border: 2px solid #e0e0e0;
        background-color: #ffffff;
        cursor: pointer;
    }
    .word-button.selected {
        background-color: #b3d9ff;
        border-color: #0066cc;
    }
    .word-button.correct {
        background-color: #90EE90;
        border-color: #008000;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Connections Game")
st.write("Select four words that belong together!")

# Create 4x4 grid of buttons using HTML
cols = st.columns(4)
for i, word in enumerate(st.session_state.all_words):
    col_index = i % 4
    with cols[col_index]:
        # Determine button state (selected, correct, or normal)
        button_state = ""
        if word in st.session_state.correct_words:
            button_state = "correct"
        elif word in st.session_state.selected_words:
            button_state = "selected"
            
        # Create button with appropriate styling
        if st.button(
            word,
            key=f"button_{i}",
            disabled=word in st.session_state.correct_words,
            type="secondary" if button_state == "selected" else "primary"
        ):
            if word in st.session_state.selected_words:
                st.session_state.selected_words.remove(word)
            elif len(st.session_state.selected_words) < 4:
                st.session_state.selected_words.append(word)

# Show selected words
st.write("Selected words:", ", ".join(st.session_state.selected_words))

# Display message if any
if st.session_state.message:
    st.write(st.session_state.message)

# Submit button
if st.button("Submit Selection", disabled=len(st.session_state.selected_words) != 4):
    # Check if selection is correct
    found = False
    for category, words in st.session_state.remaining_categories.items():
        if set(st.session_state.selected_words) == set(words):
            st.session_state.message = f"Correct! You've found the {category} category!"
            st.session_state.correct_words.extend(st.session_state.selected_words)
            st.session_state.guessed_categories.append(category)
            del st.session_state.remaining_categories[category]
            found = True
            break
    
    if not found:
        st.session_state.message = "That's not a correct group. Try again!"
    
    # Clear selection
    st.session_state.selected_words = []
    st.rerun()

# Check for win condition
if not st.session_state.remaining_categories:
    st.balloons()
    st.success("Congratulations! You've found all the categories!")
    st.write(f"Categories found: {', '.join(st.session_state.guessed_categories)}")

# Add a reset button
if st.button("Reset Game"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
