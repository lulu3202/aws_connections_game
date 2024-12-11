# Minimalist Connections Game

A fun and interactive word association game built using **Streamlit** and **AWS S3**, inspired by popular NYT connections game. 
Live Game: https://awsconnectionsgame.streamlit.app/
---
## Technologies Used
- Python: Handles game logic, word selection, and user interaction.
- Boto3: Used to access AWS S3 and store the game data, enabling dynamic content updates.
- Streamlit: Powers the web app with a responsive and interactive user interface.
---
## Key Files
### Level 1: game_l1.py - A (very) simple Python script that gets the job done 
### Level 2: python game_l2.py - A smarter Python script (with S3 integration)
### Level 3: game_l3.py - An interactive Streamlit interface to enhance user experience
### Level 4: app.py - Cloud deployment 
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
## Deployment and Secrets Management

level 2 - Deploy Locally:
- Keep sensitive keys (e.g., IAM access) safe using .env files for local use and .gitignore to exclude them from GitHub.

level 3 - Deploy Streamlit Locally: 
- Store sensitive info in a .streamlit/secrets.toml file for local testing.
- Use st.secrets to access variables in Streamlit.

level 4 - Deploy to Streamlit Cloud:
- Push the code to your GitHub repo.
- Update the secrets in the Streamlit Cloud console via the st.secrets method.

---
## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

