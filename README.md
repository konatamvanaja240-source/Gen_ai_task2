# Gen_ai_task2
Career Advisor Chatbot

## Overview
The Career Advisor Chatbot is a Generative AI-powered application built using Python, Streamlit, and Google Gemini AI. The chatbot provides career guidance, skill recommendations, learning roadmaps, certification suggestions, and interview preparation tips through a conversational interface.

## Features
Career path recommendations
Skill development guidance
Learning roadmaps
Certification suggestions
Interview preparation assistance
Interactive chat interface
Conversation history management
## Technologies Used
Python
Streamlit
Google Gemini 2.5 Flash
Python-dotenv

## Project Structure
Career-Advisor-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
## Create a Virtual Environment
python -m venv venv

## Activate the Environment

Windows:

venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

## Install Dependencies
pip install -r requirements.txt
Configure Environment Variables

## Create a .env file and add your Gemini API key:
GEMINI_API_KEY="AQ.Ab8RN6IIFpbImbbRoFecr0dy4i7MF7V3KCaUIzJ-W9eh4ra0NQ"

## Run the Application
streamlit run app.py

## How It Works
The user enters a career-related question.
Streamlit captures the input.
The application loads the Gemini API key from the .env file.
A system prompt defines the chatbot as an expert Career Advisor.
The system prompt, chat history, and user query are combined into a prompt.
The prompt is sent to Gemini 2.5 Flash.
Gemini generates a career-related response.
The response is displayed in the Streamlit interface.
Chat history is maintained using Streamlit Session State.


