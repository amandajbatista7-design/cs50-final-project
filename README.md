# LEARN WITH FUN
#### Video Demo:  <https://www.youtube.com/watch?v=VaJ4Vnb3DQw>
#### Description:

## Project Description

My project is a webpage designed to help children, ages 3 to 7 years old, practice and learn to recognize the letters of the alphabet and identify colors and shapes through two interactive games.

- **Alphabet Game**:
  - The user listens to an audio that says a letter.
  - The user selects the correct letter from three options.
  - The options are displayed in colorful images, that are buttons.
  - The game includes 26 questions, one for each letter of the alphabet

- **Matching Game**:
  - A question is presented for the user, asking for a shape in a specific color.
  - The user selects a shape from three options.
  - Features a 'Read Aloud' button to read the question for young children who cannot yet read.
  - The game presents 10 questions in a random order each time it runs.
  - The database contains a total of 132 questions.
Since these games are designed for kids, in both games, the user needs to choose an answer until they get it right. The goal is to learn, not to score points. To make it clear whether they selected the correct or incorrect option:
  - The selected image will turn red if incorrect.
  - The selected image will turn green if correct.
  - When the correct answer is selected, a "Next" button will appear, leading the user to the next question.

## Static Files

- **Images**:
  - .png images for the alphabet game options (created using Canva).
  - 132 images of 12 different shapes in 11 different colors for the shapes and colors Matching game (created using Canva).
  - Background image used in all project pages (created using Canva).
  - All images were compressed using TinyPNG.

- **Audio**:
  - .m4a audio files recorded with my voice, saying the 26 letters of the alphabet.

- **Styles**:
  - `styles.css` file for the project's styling.

## styles.css:

- **Fonts**:
  - Imported from Google APIs for readability and attractiveness for the target audience.

- **Background**:
  - Styled with the help of Copilot.

- **Navigation Bar**:
  - Styled with attractive colors.
  - Resizable for medium and smaller screens.

- **Home Page Buttons**:
  - .game-link style for buttons that navigate to the games (created with the guidance of Copilot).

- **Answer Feedback**:
  - .correct-answer and .incorrect-answer styles to change the color of images when selected, turning them green or red.

- **Layout**:
  - Definitions for the positions of buttons and answers on the screen.

## Templates

- **layout.html**:
  - Contains the project's layout.
  - Includes a navigation bar that allows the user to navigate to the homepage, the alphabet game, and the matching game.
  - Changes the color of the words when the cursor hovers over them.

- **index.html**:
  - Serves as the homepage.
  - Includes a welcome message and a brief explanation of the games.
  - Contains buttons to navigate to the games (created with the help of Copilot).

- **letters.html**:
  - Contains the alphabet game.
  - Runs in JavaScript and presents all 26 questions in a random order.
  - Includes functions to show the question, handle incorrect and correct answers (providing feedback by saying ‘Correct!’ or ‘Incorrect!’), and disable buttons.
  - When the answer is correct, it disables the buttons and shows the ‘Next’ button.

- **end_letters.html**:
  - Appears when the user finishes the alphabet game.
  - Shows the end message.
  - Includes two buttons (in JavaScript): one to try the game again and one to go back to the homepage.

- **shapes_colors.html**:
  - Contains the Matching game.
  - Includes a function and button to read the questions aloud (created with guidance from Copilot and CS50 Duck).
  - Functions to show the questions, handle correct and incorrect answers, and disable buttons, similar to the Alphabet game.

- **end_shapes.html**:
  - Appears when the user finishes the Matching game.
  - Displays the end message.
  - Includes buttons to let the user try the game again or go back to the homepage.

## Python Files

- **app.py**:
  - Runs the program using Python.
  - Includes routes for all the HTML pages.
  - Contains functions for the Matching game.
  - Connects with `sqlite3` to get data from the database in `shapes.db`.
  - Includes functions to get the questions and answers.
  - The answer options are all images.
  - Includes a function to submit the answers.

- **insert_data.py**:
  - The fastest way to load the database (`shapes.db`) as suggested by Copilot.
  - Includes all the questions and answers for the Shapes and Colors game.

## Database

- **shapes.db**:
  - SQL database containing tables with the questions and answers for the Shapes and Colors game.

## License

- The license chosen for this webpage is the MIT License, detailed in `LICENSE.txt`.

