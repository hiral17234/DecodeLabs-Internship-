# DecodeLabs AI Internship – Project 1

## Rule-Based AI Chatbot using Python

---

## 📌 Overview

This project demonstrates the development of a Rule-Based Artificial Intelligence Chatbot using Python. The chatbot interacts with users through predefined responses and simulates basic conversational behavior using decision-making logic.

The project focuses on understanding the fundamental principles of Artificial Intelligence systems, including input processing, control flow, dictionaries, loops, and rule-based response generation.

This chatbot was developed as part of the DecodeLabs Artificial Intelligence Internship Program.

---

## 🎯 Objectives

* Understand the fundamentals of Rule-Based AI Systems
* Implement a conversational chatbot using Python
* Learn input processing and sanitization techniques
* Apply dictionaries for efficient response lookup
* Use loops and conditional statements for interaction control
* Understand the Input-Process-Output (IPO) model

---

## 🛠️ Technologies Used

* Python 3.14
* Visual Studio Code (VS Code)
* Git
* GitHub

---

## 🧠 AI Concepts Implemented

### 1. Rule-Based Artificial Intelligence

The chatbot responds using predefined rules rather than machine learning models.

### 2. Input Processing

User inputs are cleaned using:

* `lower()`
* `strip()`

to ensure consistent processing.

### 3. Dictionary-Based Response Mapping

Responses are stored in Python dictionaries for faster and more efficient lookup.

### 4. Infinite Loop Interaction

The chatbot continuously interacts with the user until an exit command is provided.

### 5. Exit Control Logic

The chatbot terminates when the user enters:

```text
bye
```

using the `break` statement.

---

## ⚙️ Project Workflow

```text
User Input
     ↓
Input Sanitization
     ↓
Dictionary Lookup
     ↓
Response Generation
     ↓
Display Output
     ↓
Repeat Until Exit
```

---

## 💬 Supported Commands

| User Input        | Bot Response                |
| ----------------- | --------------------------- |
| hello             | Greeting Response           |
| hi                | Greeting Response           |
| hey               | Greeting Response           |
| how are you       | Well-being Response         |
| what is your name | Bot Introduction            |
| who created you   | Creator Information         |
| good morning      | Morning Greeting            |
| good evening      | Evening Greeting            |
| thanks            | Gratitude Response          |
| thank you         | Gratitude Response          |
| help              | Displays Available Commands |
| bye               | Exit Chatbot                |

---

## 📂 Repository Structure

```text
DecodeLabs-Project1/
│
├── Project I - Chatbot.py
├── README.md
├── screenshot.png
│
└── Output/
    └── chatbot_execution.png
```

---

## 📷 Project Output

The chatbot was tested successfully using multiple user inputs and responses.

### Sample Interaction

```text
You: hello
Oreo: Hello! Nice to meet you.

You: how are you
Oreo: I am doing great. Thanks for asking!

You: bye
Oreo: Goodbye! Have a nice day.

Chatbot closed successfully.
```

### Screenshot

![Chatbot Output](screenshot.png)

---

## 🚀 Key Learning Outcomes

* Understanding Rule-Based AI Architecture
* Working with Python Dictionaries
* Using While Loops and Conditional Statements
* Handling User Input Efficiently
* Building Interactive Console Applications
* Applying Fundamental AI Concepts

---

## 🔮 Future Improvements

* Natural Language Processing (NLP)
* Multiple Conversation Flows
* Voice-Based Interaction
* GUI-Based Chatbot Interface
* Integration with Machine Learning Models
* Context-Aware Responses

---

## 👩‍💻 Author

**Hiral Goyal**

Artificial Intelligence Intern
DecodeLabs Internship Program – 2026

---

## ⭐ Acknowledgements

This project was completed as part of the DecodeLabs Artificial Intelligence Internship Program. The objective of this assignment was to build a foundational understanding of conversational AI systems through the implementation of a Rule-Based Chatbot using Python.
