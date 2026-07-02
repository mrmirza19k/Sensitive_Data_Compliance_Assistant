# Sensitive Data Detection & Compliance Assistant

## AI Research Innovation Internship – Practical Assignment

### Developed By

**Tabrej Ansari**

---

# Project Overview

Sensitive Data Detection & Compliance Assistant is an AI-powered application developed to analyze documents containing sensitive or confidential information.

The application enables users to upload PDF, TXT, and CSV documents, automatically detects sensitive information using pattern matching techniques, classifies the document's security risk, generates an AI-powered compliance report, and allows users to interact with the uploaded document through natural language questions using Google's Gemini AI.

The objective is to assist organizations in identifying sensitive information and improving security and compliance awareness.

---

# Features

### Document Upload

Supports:

* PDF
* TXT
* CSV

---

### Sensitive Data Detection

The application detects:

* Aadhaar Numbers
* PAN Numbers
* Email Addresses
* Phone Numbers
* Credit Card Numbers
* Employee IDs
* API Keys
* Passwords
* Bank Account Numbers
* IFSC Codes
* Confidential Business Information

---

### Risk Classification

Documents are automatically classified as:

* Low Risk
* Medium Risk
* High Risk

The classification is based on a weighted scoring system considering the amount and type of sensitive information detected.

---

### AI Compliance Summary

Google Gemini Flash generates:

* Document Summary
* Sensitive Information Overview
* Compliance Observations
* Security Risks
* Recommended Remediation Steps
* Overall Risk Assessment

---

### Question Answering

Users can ask questions such as:

* What sensitive data exists in this document?
* How many email addresses are present?
* Summarize this document.
* What compliance risks are identified?

The responses are generated using Google Gemini based on the uploaded document.

---

# Technology Stack

## Frontend

* Streamlit

## Backend

* Python

## AI Model

* Google Gemini Flash
* Google AI Studio API

## Libraries

* PyPDF2
* Pandas
* Regex
* python-dotenv

---

# Architecture Overview

```text id="rvljlwm"
                 Upload Document
                        │
                        ▼
              Extract Document Text
                        │
                        ▼
          Sensitive Data Detection
                (Regex Engine)
                        │
                        ▼
           Risk Classification Engine
                        │
                        ▼
         Google Gemini Flash Analysis
             │                    │
             ▼                    ▼
     Compliance Summary     Question Answering
```

---

# AI / ML Approach Used

The application combines rule-based detection with Large Language Model capabilities.

### Rule-Based Detection

Sensitive information such as email addresses, PAN numbers, Aadhaar numbers, passwords, API keys, bank details, and phone numbers are detected using carefully designed Regular Expressions (Regex).

### Risk Scoring

Each sensitive information category is assigned a predefined weight.

The cumulative score determines the document's overall security risk:

* Low Risk
* Medium Risk
* High Risk

### AI-Powered Analysis

Google Gemini Flash analyzes the extracted document and generates:

* Compliance observations
* Security risks
* Document summary
* Recommended remediation steps
* Natural language responses to user questions

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/your-username/Sensitive_Data_Compliance_Assistant.git
```

---

## Navigate to Project

```bash
cd Sensitive_Data_Compliance_Assistant
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Run Application

```bash
streamlit run app.py
```

---

# Project Workflow

1. Upload a document.
2. Extract document text.
3. Detect sensitive information.
4. Calculate security risk.
5. Generate AI compliance summary.
6. Ask questions about the uploaded document.

---

# Challenges Faced

During development several challenges were encountered:

* Supporting multiple document formats.
* Designing reliable Regex patterns.
* Balancing detection accuracy.
* Integrating Google Gemini API.
* Managing API rate limits and temporary service unavailability.
* Organizing the project into modular and reusable components.

---

# Future Improvements

The application can be extended with:

* OCR support for scanned PDFs
* Automatic data masking
* Data redaction
* Multi-document analysis
* Vector database integration for very large documents
* User authentication
* Audit logging
* PDF report generation
* Docker support
* Cloud deployment
* GDPR, HIPAA, PCI-DSS and ISO 27001 compliance modules

---

# Evaluation Criteria Addressed

✔ Functionality

✔ AI Integration

✔ Problem Solving

✔ Modular Code Structure

✔ Security & Compliance Awareness

✔ User-Friendly Interface

✔ Documentation

---

# Repository Structure

```text
Sensitive_Data_Compliance_Assistant/

│── app.py
│── README.md
│── requirements.txt
│── .env
│
├── uploads/
│
├── utils/
│   ├── pdf_loader.py
│   ├── txt_loader.py
│   ├── csv_loader.py
│   ├── detector.py
│   ├── risk.py
│   ├── summarizer.py
│   ├── qa.py
│
└── assets/
```

---

# Deployment

The application can be deployed using:

* Streamlit Community Cloud
* Render
* Railway

---

# Demo Video

The demonstration video showcases:

* Project overview
* Uploading a document
* Sensitive data detection
* Risk classification
* AI-generated compliance summary
* Question answering
* Overall application workflow

---

# License

This project was developed solely for the AI Research Innovation Internship practical assignment at Proteccio Data.

Commercial use is not intended.
