# Task 1: Rule-Based AI Chatbot 🤖

## Goal
Create a simple rule-based chatbot that responds to predefined user inputs using basic decision-making logic.

## Description
This project implements a rule-based chatbot that interacts with users through a continuous conversation loop. The bot recognizes greetings, answers predefined questions from a knowledge base, and exits gracefully on command.

## Key Features
- Handles greetings (hi, hello, hey)
- Responds to predefined questions using a dictionary-based knowledge base
- Supports multiple exit commands (exit, bye, quit)
- Runs in a continuous loop until the user chooses to exit
- Handles empty input and unrecognized queries gracefully

## Key Skills Used
- Control flow (if-elif-else)
- Decision-making logic
- Dictionaries for knowledge storage
- Basic AI / rule-based system concepts

## How It Works
1. The bot greets the user when the program starts
2. The program enters a `while True` loop, continuously asking for input
3. User input is checked against:
   - Exit commands → ends the program
   - Greetings → friendly response
   - Knowledge base keys → returns matching answer
   - Anything else → fallback message
4. The loop continues until the user types an exit command
