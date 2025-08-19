import pdfplumber
from fpdf import FPDF


# -----------------------------
# Function to extract text from PDF
# -----------------------------
def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# -----------------------------
# Function to generate a summary (basic)
# -----------------------------
def summarize_text(text, max_sentences=5):
    sentences = text.split('.')
    summary = '. '.join(sentences[:max_sentences]) + '.'
    return summary

# -----------------------------
# Function to generate quiz questions (simple)
# -----------------------------
def generate_quiz(text, num_questions=3):
    sentences = text.split('.')
    questions = []
    for i in range(min(num_questions, len(sentences))):
        question = sentences[i].strip()
        if question:
            questions.append(f"Q{i+1}: {question}?")
    return questions

# -----------------------------
# Function to export to PDF
# -----------------------------
def export_pdf(summary, questions, output_path="study_material.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "AutoStudy AI – Study Material", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Summary:", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, summary)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Quiz Questions:", ln=True)
    pdf.set_font("Arial", '', 12)
    for q in questions:
        pdf.multi_cell(0, 10, q)
    pdf.output(output_path)
    print(f"\nPDF exported to {output_path}")

# -----------------------------
# Main Program
# -----------------------------
def main():
    choice = input("Enter PDF path (or leave blank to type text manually): ").strip()
    if choice:
        text = extract_text(choice)
    else:
        print("Enter your text (end with a blank line):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        text = " ".join(lines)

    summary = summarize_text(text)
    quiz = generate_quiz(text)

    print("\n--- Summary ---")
    print(summary)
    print("\n--- Quiz Questions ---")
    for q in quiz:
        print(q)

    export_pdf(summary, quiz)

if __name__ == "__main__":
    main()
