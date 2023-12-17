# Quiz Game
This simple quiz game is designed to ask users a series of true or false questions. The game is divided into four files: data.py, main.py, question_model.py, and quiz_brain.py.

## Files
```bash
data.py
```
This file contains the data for the true or false questions used in the quiz. Each question is represented as a dictionary with attributes such as type, difficulty, category, question text, correct answer, and incorrect answers. You can generate your own data using APIs like the Open Trivia Database.

```bash
main.py
```
This is the main execution file. It imports the necessary modules, creates a list of Question objects from the data, initializes a QuizBrain, and runs the quiz loop until all questions are answered. Finally, it prints the user's final score.

```bash
question_model.py
```
Defines the Question class, which is used to represent each question in the quiz. Each Question object has attributes for the question text and the correct answer.

```bash
quiz_brain.py
```
Defines the QuizBrain class, which manages the quiz's logic. It keeps track of the user's score, question number, and the list of questions. The class includes methods for checking answers, displaying questions, and determining if there are more questions to ask.

## How to Run the Quiz
- Ensure you have Python installed on your machine.
-  Run the main.py file using a Python interpreter.
```bash
python main.py
```
- Answer each true or false question by typing "True" or "False" when prompted.
- After completing the quiz, the final score will be displayed.

## Generating Your Own Data
You can customize the quiz by generating your own data from sources like the Open Trivia Database. Modify the 'data.py' file to include your questions and answers, following the structure of the existing data.

*Feel free to customize the quiz questions or add more features to enhance the user experience. Enjoy the quiz!*