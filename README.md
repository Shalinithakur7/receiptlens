# ReceiptLens AI - Smart Receipt Digitizer


ReceiptLens AI is a **Streamlit web app** that extracts **key information** from receipt images using the **Gemini API**.  
Instead of just raw OCR, it identifies:

<img width="1376" height="815" alt="image" src="https://github.com/user-attachments/assets/9c397895-1c43-439f-937b-3bbbcf909717" />

<img width="1430" height="858" alt="image" src="https://github.com/user-attachments/assets/cbdeddaf-0107-4c7d-90ce-5c21593beebb" />

<img width="937" height="826" alt="image" src="https://github.com/user-attachments/assets/6ccf63aa-1d85-47ea-810f-6971099469ff" />



- **Store name**
- **Date**
- **Items purchased**
- **Price per item**
- **Total amount and tax**
- **Categories** (Food, Travel, Shopping, etc.)

and displays everything in a **clean, structured format**.

---

## Features
- Upload receipt images (**JPG, PNG**)
- Extract **key details** (store, date, items, total, tax)
- **Categorize purchases** automatically
- Display results in a **structured table format**
- downloadable in form of img and csv file

---

## Tech Stack
- **Streamlit** (Frontend + UI)
- **Gemini API** (OCR + Information Extraction)
- **Pandas** (Structured results)
- **Python 3.11.5**

---

