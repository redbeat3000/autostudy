# AutoStudy AI – AI-Powered Study Material Generator

AutoStudy AI is a Python-based tool that automatically generates study materials from a PDF or text input. It creates summaries and quiz questions, and exports them into a PDF. This project is perfect for students, educators, or anyone wanting to automate learning content creation.

---

## Features

- Extracts text from PDFs or manual input
- Generates concise summaries
- Creates simple quiz questions from the text
- Exports results to a neatly formatted PDF
- Fully written in Python and runs on Ubuntu
- Extendable to AI-powered summaries, flashcards, and audio guides

---

## Prerequisites

- Ubuntu or Linux-based OS
- Python 3
- Required Python packages:
  - `fpdf`
  - `PyPDF2` (optional for PDFs)
  - `pdfplumber` (recommended for PDFs)

---

## Installation

1. Update your system and install dependencies:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install fpdf PyPDF2 pdfplumber
