import boto3
import json
import random
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def fetch_categories_from_s3(bucket_name, file_name):
    """
    Fetch categories from an S3 bucket.

    Args:
        bucket_name (str): Name of the S3 bucket.
        file_name (str): Name of the file in the S3 bucket.

    Returns:
        dict: Dictionary of categories loaded from the S3 file.
    """
    try:
        # Initialize the S3 client
        s3 = boto3.client("s3")

        # Fetch the file content from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        file_content = response['Body'].read().decode('utf-8')

        # Parse the JSON content
        data = json.loads(file_content)
        return data.get("categories", {})
    except Exception as e:
        print(f"Error fetching categories from S3: {e}")
        return {}

def play_connections_game():
    # Load bucket name and file name from environment variables
    bucket_name = os.getenv("AWS_BUCKET_NAME")
    file_name = os.getenv("AWS_FILE_NAME")

    if not bucket_name or not file_name:
        print("Missing AWS_BUCKET_NAME or AWS_FILE_NAME environment variables. Exiting the game.")
        return

    # Load categories from the S3 bucket
    all_categories = fetch_categories_from_s3(bucket_name, file_name)

    if not all_categories:
        print("Failed to load categories from S3. Exiting the game.")
        return

    # Check if there are at least 4 categories to sample
    if len(all_categories) < 4:
        print(f"Not enough categories available. Found {len(all_categories)} categories, but 4 are required.")
        return

    # Randomly select 4 categories
    selected_categories = dict(random.sample(list(all_categories.items()), 4))

    # Flatten the list of words into a single list and shuffle them
    all_words = [word for group in selected_categories.values() for word in group]
    random.shuffle(all_words)

    # Print instructions for the player
    print("Welcome to the Connections Game!")
    print("Group the following words into their categories:")
    print(", ".join(all_words))

    # Initialize game state
    remaining_categories = selected_categories.copy()
    guessed_categories = []

    while remaining_categories:
        print("\nEnter a group of 4 words separated by commas (e.g., Apple, Banana, Cherry, Orange):")
        guess = input("Your guess: ").strip().split(",")
        guess = [word.strip() for word in guess]

        if len(guess) != 4:
            print("Please enter exactly 4 words.")
            continue

        found = False
        for category, words in remaining_categories.items():
            if set(guess) == set(words):
                print(f"Correct! You've grouped: {', '.join(guess)} as {category}.")
                guessed_categories.append(category)
                del remaining_categories[category]
                found = True
                break

        if not found:
            print("Incorrect grouping. Try again!")

    print("\nCongratulations! You've correctly grouped all the words!")
    print(f"Your groups were: {', '.join(guessed_categories)}")

# Run the game
if __name__ == "__main__":
    play_connections_game()
