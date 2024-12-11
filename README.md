# Connections Game

A fun and interactive word association game built using **Streamlit** and **AWS S3**, inspired by popular NYT connections game.

---

## Key Features

### Level 1: **Fetch Categories from AWS S3**
- Categories and words are stored in a JSON file in an S3 bucket.
- The app dynamically fetches and parses this data at runtime, ensuring flexibility and scalability.

### Level 2: **Dynamic Word Grid and Game Logic**
- Randomly selects 4 categories from the fetched data and displays a shuffled grid of words.
- Interactive buttons allow players to select words, with real-time feedback:
  - **Selected words** are highlighted in blue.
  - **Correct matches** turn green.
- Players receive instant messages for correct or incorrect guesses.

### Level 3: **Victory Condition and Replay**
- Balloons and success messages celebrate the completion of all categories.
- Includes a reset button to replay with a new randomized set of categories.

---

## How It Works
1. **Fetch Data**:
   - Connects to an AWS S3 bucket to fetch the categories and words stored in a JSON file.
   - Validates that enough categories are available for the game.

2. **Initialize the Game**:
   - Randomly selects 4 categories and shuffles their words into a 4x4 grid.
   - Keeps track of guessed categories, correct words, and remaining options.

3. **Interactive Gameplay**:
   - Players select words by clicking buttons on a styled grid.
   - Correct matches are automatically identified and celebrated.
   - Players win when all categories are discovered.

---

## Technologies Used
- **Streamlit**: Powers the web app with a responsive and interactive user interface.
- **AWS S3**: Stores the game data, enabling dynamic content updates.
- **Python**: Handles game logic, word selection, and user interaction.

---

## How to Run

### Prerequisites
- Python 3.8+
- AWS credentials with access to the S3 bucket containing the game data.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/connections-game.git
   cd connections-game
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. Access the game in your browser at `http://localhost:8501`.

---

## Game Data Format
The JSON file in S3 should follow this structure:
```json
{
  "categories": {
    "Fruits": ["Apple", "Banana", "Cherry", "Mango"],
    "Animals": ["Dog", "Cat", "Elephant", "Lion"],
    "Colors": ["Red", "Blue", "Green", "Yellow"],
    "Countries": ["India", "USA", "France", "Germany"]
  }
}
```

---

## Future Enhancements
- Add timers for more challenging gameplay.
- Implement multiplayer support.
- Allow custom categories to be uploaded by users.
- Introduce scoring and leaderboard functionality.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements
- Thanks to the Streamlit and AWS communities for their amazing tools and resources.
