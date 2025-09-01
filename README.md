ReceiptLens AI - Smart Receipt Digitizer

ReceiptLens AI is a Streamlit web app that extracts key information from receipt images using the Gemini API. Instead of just raw OCR, it identifies important details like store name, date, total amount, tax, and items, and even categorizes the purchases.

Features

Upload receipt images (JPG, PNG)

Extract key details from receipts:
Store name
Date
Items purchased
Price per item
Total amount and tax

Categorize purchases (Food, Travel, Shopping, etc.)

Display results in a clean, structured format

Tech Stack

Streamlit (Frontend + UI)
Gemini API (OCR + Information Extraction)
Pandas (for structured results)
Python 3.11.5

Installation

Clone the repository

git clone https://github.com/yourusername/receipt-lens-ai.git
cd receipt-lens-ai


Create and activate a virtual environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Add your Gemini API key

Create a .env file in the root folder

Add this line:

GEMINI_API_KEY=your_api_key_here


Run the app

streamlit run app.py

Future Enhancements

Export results as CSV, Excel, or JSON

Batch upload for multiple receipts

Expense summary and monthly reports

User login with personal receipt history

Integration with Google Sheets or Notion

Demo

Live App: [Insert Streamlit Cloud Link Here]

GitHub Repo: [Insert Repository Link Here]