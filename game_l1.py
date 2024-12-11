import random  # Used to shuffle the words randomly in the game

def play_connections_game():
    # Define the words and their categories
    # Data is stored in a dictionary, where each key is a category, and the value is a list of words in that category.
    categories = {
        "Fruits": ["Apple", "Banana", "Cherry", "Orange"],
        "Countries": ["India", "Brazil", "France", "Japan"],
        "Colors": ["Red", "Blue", "Green", "Yellow"],
        "Animals": ["Lion", "Tiger", "Elephant", "Zebra"]
    }

    # Flatten the list of words into a single list and shuffle them
    # List comprehension is used here to create a single list from the dictionary values using outer loop and inner loop
    all_words = [word for group in categories.values() for word in group]
    random.shuffle(all_words)  # Shuffle the words randomly to make the game challenging

    # Print instructions for the player
    print("Welcome to the Connections Game!")
    print("Group the following words into their categories:")
    print(", ".join(all_words))  # Join all words into a single string separated by commas

    # Initialize game state
    remaining_categories = categories.copy()  # Copy the original dictionary to keep track of categories left to guess
    guessed_categories = []  # List to store correctly guessed categories

    while remaining_categories:  # Loop runs until the dictionary is empty
        print("\nEnter a group of 4 words separated by commas (e.g., Apple, Banana, Cherry, Orange):")
        guess = input("Your guess: ").strip().split(",")  # Take user input, split it into a list
        guess = [word.strip() for word in guess]  # Use list comprehension to remove extra spaces from each word

        # Check if the input has exactly 4 words
        if len(guess) != 4:
            print("Please enter exactly 4 words.")  # Validation: Ensure input has the correct format
            continue  # Skip to the next iteration of the loop

        # Check if the guessed group matches any remaining category
        found = False  # Boolean variable to track if the guess is correct
        for category, words in remaining_categories.items():  # Loop through the remaining categories
            if set(guess) == set(words):  # Use set comparison to check if the guessed words match a category
                print(f"Correct! You've grouped: {', '.join(guess)} as {category}.")
                guessed_categories.append(category)  # Add the category to the guessed list
                del remaining_categories[category]  # Remove the category from remaining categories
                found = True  # Mark as found
                break  # Exit the loop since the guess was correct

        if not found:  # If no match was found
            print("Incorrect grouping. Try again!")

    # When all categories are guessed, end the game
    print("\nCongratulations! You've correctly grouped all the words!")
    print(f"Your groups were: {', '.join(guessed_categories)}")

# Run the game
if __name__ == "__main__":
    play_connections_game()  # This ensures the game runs only when this file is executed directly
