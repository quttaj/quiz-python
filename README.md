# Python Quiz

A desktop trivia game for one or two players, built with Python and Tkinter. The application loads 10 questions from Open Trivia DB, randomises the answer choices and tracks scores throughout the game.

Created by **Ivanna Poltavets** as a learning and portfolio project.

**[Try the browser adaptation](https://viktorina-iva.poltavets200530.chatgpt.site/)** · **[Explore the Python source](original-python/)**

The browser adaptation was created with ChatGPT assistance and has an updated interface. This repository contains the original Python desktop application; the browser version is a separate implementation.

## Features

- Single-player mode and local two-player mode on the same computer.
- Starting-team selection and alternating turns in two-player mode.
- Questions retrieved from the Open Trivia DB API.
- Randomised answer choices and decoded HTML entities in question text.
- Feedback after each submitted answer, including the correct answer when needed.
- Final percentage scores for the player or both teams.
- Basic text-file export of session results, with limitations noted below.

## Technologies

| Technology | Purpose |
| --- | --- |
| Python | Application and game logic |
| Tkinter | Desktop windows, answer selection and result dialogs |
| Requests | HTTP requests to the question API |
| Open Trivia DB | Trivia question data |
| `random` and `html` | Answer shuffling and HTML entity decoding |

## Run locally

You need **Python 3**, **Tkinter**, an internet connection and a desktop environment. The only third-party Python package imported by the application is `requests`.

### 1. Download the project

Download and extract the repository ZIP, or clone it:

```bash
git clone https://github.com/quttaj/quiz-python.git
cd quiz-python
```

If you downloaded the ZIP, open a terminal in the extracted repository folder instead.

### 2. Install the dependency

```bash
python -m pip install requests
```

Tkinter must also be available in your Python installation. You can check it with:

```bash
python -m tkinter
```

This should open a small test window. If Tkinter is missing, install the Tcl/Tk support provided by your Python installer or operating system; it is not installed with `pip install tkinter`.

### 3. Start the quiz

```bash
cd original-python
python main_both.py
```

Use `python3` in place of `python` if that is the Python 3 command on your system.

Questions are fetched before the mode-selection window opens, so startup requires a working connection to Open Trivia DB. If the request fails or the API returns no questions, check the terminal message, wait briefly and try again.

## How to play

1. Choose **One Player** or **Two Players**.
2. In two-player mode, choose the team that should start.
3. Select an answer and click **Next** to submit it and advance.
4. Continue through the questions to see the final score.
5. Use **Quit** to close the quiz early.

The application writes `quiz_results.txt` to the current working directory when the quiz window closes. Running it from `original-python` as shown above keeps the results in that folder. Each export replaces the previous file.

## Project structure

```text
quiz-python/
├── README.md
└── original-python/
    ├── main_both.py        # Entry point and question-bank preparation
    ├── question_model.py   # Question text, correct answer and choices
    ├── quiz_data.py        # API request and response validation
    ├── quiz_brain_both.py  # Turn management, scoring and results export
    ├── quiz_ui_both.py     # Tkinter settings and quiz windows
    └── quiz_results.txt    # Results output
```

## Implementation highlights

The project separates question data, game logic and the graphical interface into individual modules. It demonstrates API integration, JSON processing, class-based organisation, event-driven GUI programming and local multiplayer state management.

## Current limitations

- The interface has four answer controls, while the API request does not restrict questions to the multiple-choice type. True/false questions can therefore leave unused or stale answer controls visible.
- The results export does not yet retain each submitted answer. Its per-question answer and correctness fields are incomplete; the in-game score is calculated separately.
- Questions are loaded online at startup; there is no offline question set or in-app retry flow.

## Possible next improvements

- Match the number of answer controls to the question type.
- Store answer history and complete the detailed results export.
- Add in-app handling for network failures and missing answer selections.
- Add automated tests for scoring and turn changes.

## Author

**Ivanna Poltavets**  
[GitHub](https://github.com/quttaj) · [Email](mailto:iv.poltavetss@gmail.com)

Question data is provided by [Open Trivia DB](https://opentdb.com/).
