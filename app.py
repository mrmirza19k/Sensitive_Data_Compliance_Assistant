import streamlit as st
import os

from utils.pdf_loader import extract_pdf_text
from utils.txt_loader import extract_txt_text
from utils.csv_loader import extract_csv_text
from utils.detector import detect_sensitive_data
from utils.risk import calculate_risk
from utils.summarizer import generate_summary
from utils.qa import ask_question


st.set_page_config(
    page_title="Sensitive Data Detection & Compliance Assistant",
    page_icon="🔒",
    layout="wide",
)
UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

st.title("🔒 Sensitive Data Detection & Compliance Assistant")
st.markdown(
    "Upload a document to detect sensitive information, classify risk, "
    "generate an AI compliance summary, and ask questions about the document."
)

st.divider()

with st.sidebar:
    st.header("Project Information")

    st.info(
        """
        **Supported Files**
        - PDF
        - TXT
        - CSV

        **Features**
        - Sensitive Data Detection
        - Risk Classification
        - AI Summary
        - Question Answering
        """
    )

    st.subheader("📄 Upload Document")

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["pdf", "txt", "csv"]
)

if uploaded_file is not None:

    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    file_extension = uploaded_file.name.split(".")[-1].lower()

    document_text = ""

    if file_extension == "pdf":
        document_text = extract_pdf_text(file_path)

    elif file_extension == "txt":
        document_text = extract_txt_text(file_path)

    elif file_extension == "csv":
        document_text = extract_csv_text(file_path)

    sensitive_data = detect_sensitive_data(document_text)
    risk = calculate_risk(sensitive_data)
    
    with st.spinner("Generating AI Compliance Summary..."):
        ai_summary = generate_summary(document_text)

st.divider()

st.subheader("📋 Document Information")

doc_col1, doc_col2, doc_col3 = st.columns(3)

with doc_col1:
    if uploaded_file:
        st.metric("File Name", uploaded_file.name)
    else:
        st.metric("File Name", "-")

with doc_col2:
    if uploaded_file:
        st.metric("File Type", uploaded_file.type)
    else:
        st.metric("File Type", "-")

with doc_col3:
    if uploaded_file:
        size = round(uploaded_file.size / 1024, 2)
        st.metric("File Size", f"{size} KB")
    else:
        st.metric("File Size", "-")

if uploaded_file:

    st.success("Document Ready for Analysis")

    st.write("Saved Location:")

    st.code(file_path)


st.divider()

st.subheader("🔍 Sensitive Data Detection")

col1, col2 = st.columns(2)

if uploaded_file:

    with col1:
        st.info(f"📧 Emails: {len(sensitive_data['Emails'])}")
        st.info(f"📱 Phone Numbers: {len(sensitive_data['Phone Numbers'])}")
        st.info(f"🪪 PAN Numbers: {len(sensitive_data['PAN Numbers'])}")
        st.info(f"🆔 Aadhaar Numbers: {len(sensitive_data['Aadhaar Numbers'])}")
        st.info(f"🏦 Bank Accounts: {len(sensitive_data['Bank Account'])}")

    with col2:
        st.info(f"💳 Credit Cards: {len(sensitive_data['Credit Card Numbers'])}")
        st.info(f"🔑 API Keys: {len(sensitive_data['API Keys'])}")
        st.info(f"🔒 Passwords: {len(sensitive_data['Passwords'])}")
        st.info(f"👨‍💼 Employee IDs: {len(sensitive_data['Employee IDs'])}")
        st.info(f"🏢 IFSC Codes: {len(sensitive_data['IFSC Code'])}")

else:

    with col1:
        st.info("📧 Emails: 0")
        st.info("📱 Phone Numbers: 0")
        st.info("🪪 PAN Numbers: 0")
        st.info("🆔 Aadhaar Numbers: 0")
        st.info("🏦 Bank Accounts: 0")

    with col2:
        st.info("💳 Credit Cards: 0")
        st.info("🔑 API Keys: 0")
        st.info("🔒 Passwords: 0")
        st.info("👨‍💼 Employee IDs: 0")
        st.info("🏢 IFSC Codes: 0")

if uploaded_file:

    st.subheader("📋 Detected Sensitive Data")

    for category, values in sensitive_data.items():

        if values:

            with st.expander(f"{category} ({len(values)})"):

                for value in values:
                    st.write(f"• {value}")

st.divider()

st.subheader("⚠ Risk Classification")

if uploaded_file:

    if risk["level"] == "Low":
        st.success(f"🟢 Low Risk (Score: {risk['score']})")

    elif risk["level"] == "Medium":
        st.warning(f"🟠 Medium Risk (Score: {risk['score']})")

    else:
        st.error(f"🔴 High Risk (Score: {risk['score']})")

else:
    st.info("Upload a document to analyze risk.")

if uploaded_file:

    st.subheader("📌 Risk Factors")

    if risk["reasons"]:

        for reason in risk["reasons"]:
            st.write(f"• {reason}")

    else:
        st.success("No sensitive information detected.")

st.divider()

st.subheader("🤖 AI Compliance Summary")

if uploaded_file:

    st.markdown(ai_summary)

else:

    st.info("Upload a document to generate an AI compliance summary.")


st.divider()

st.subheader("💬 Ask Questions About the Document")

if uploaded_file:

    question = st.text_input(
        "Ask anything about this document"
    )

    if st.button("Ask AI"):

        if question:

            with st.spinner("Thinking..."):

                answer = ask_question(document_text, question)

            st.success(answer)

else:

    st.info("Upload a document first.")

if uploaded_file is not None:

    st.divider()

    st.subheader("📄 Extracted Text")

    st.text_area(
        "Document Content",
        value=document_text,
        height=350
    )