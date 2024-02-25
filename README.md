# Quiz Application with Kintone Integration

This is a Python quiz application that integrates with the Kintone platform for managing quiz questions. It allows users to add quiz questions via a menu, take quizzes with randomized questions, and track quiz results.

## Files

### `gui.py`

This file contains the main logic for the quiz application. It utilizes the Tkinter library to create a graphical user interface (GUI) for the application. The GUI allows users to navigate through different sections of the application, including adding questions, taking quizzes, and customizing quiz settings.

### `api.py`

This file contains functions for interacting with the Kintone API. It includes functions for posting data (questions) to Kintone, retrieving data (questions) from Kintone, and managing quiz questions.

## Functionality

- **Add Questions**: Users can add quiz questions by providing the question text, options, and correct answer via the GUI. The questions are then posted to the Kintone app using the `post_data` function from `api.py`.

- **Take Quizzes**: Users can take quizzes with randomized questions fetched from the Kintone app. The quiz questions are displayed in the GUI, and users can select their answers. The application tracks the number of correct and total guesses.

- **Customize Quizzes**: Users can customize quiz settings, such as allowing unlimited questions or guesses, randomizing answer options, and ensuring unique questions in each quiz session.

## Setup

1. Install the required Python packages


2. Run the `gui.py` file to start the application.

3. Ensure that you have valid API tokens and app IDs for accessing the Kintone app. Update the `quiz_api_token`, and `quiz_app_id` variables in `api.py` accordingly.

## Usage

1. Launch the application by running `gui.py`.

2. Navigate through the different sections of the GUI to add questions, take quizzes, or customize quiz settings.

3. Follow the on-screen instructions to interact with the application.

## Notes

- Ensure that you have a stable internet connection to access the Kintone API for retrieving and posting quiz questions.