# Quiz Application

This repository contains a Python application that implements a quiz game. The application uses a question bank and allows users to answer true or false questions. At the end of the quiz, the user's score is displayed.

## Application Description

The quiz application consists of the following classes:

### Question Class
File: `question.py`

This class represents a single question in the quiz. Each question has a text and an associated answer (true or false).

### QuizBrain Class
File: `quiz_brain.py`

This class manages the flow of the quiz game. It keeps track of the current question, the question list, and the user's score. The class provides methods to display the next question, check the user's answer, and determine if there are any more questions remaining.

### Data Module
File: `data.py`

This module contains the question data used in the quiz. It provides a list of dictionaries, where each dictionary represents a question and its correct answer.

### Main Script
File: `main.py`

This script creates an instance of the `QuizBrain` class and runs the quiz. It displays each question, takes the user's answer, and checks it against the correct answer. The final score is displayed at the end of the quiz.

Feel free to modify the question data in the `data.py` file to create your own quizzes.

## Dependencies

This application requires no external dependencies. It uses only the Python standard library.

## Disclaimer

This application is for educational purposes and demonstrates the implementation of a quiz game. Please use it responsibly and respect the license terms.

## Contributing

If you have any improvements or suggestions for this application, feel free to contribute by creating a pull request. Your contributions are greatly appreciated!
