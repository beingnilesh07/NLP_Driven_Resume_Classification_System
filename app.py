import streamlit as st
import pickle
import re
import math
from io import BytesIO
import docx2txt
import pdfplumber
import tempfile
import win32com.client
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

#  Page Setup
st.set_page_config(page_title="Resume Classifier", page_icon="📄")

st.title("📄 Resume Classifier")
st.write("Upload a resume and the model will predict its job category.")
st.divider()

#Category Mapping
INT_TO_CATEGORY = {
    0: "Peoplesoft_resumes",
    1: "React_JS_Developer",
    2: "SQL_Developer",
    3: "workday_resumes"}

CATEGORY_EMOJI = {
    "Peoplesoft_resumes": "🏢",
    "React_JS_Developer": "⚛️",
    "SQL_Developer": "🗄️",
    "workday_resumes": "☁️"}

#Model Loading
@st.cache_resource
def load_artifacts():
    with open("C:\\Users\\bilad\\ExcelR\\Project\\Resume_Classification\\Models\\svm_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("C:\\Users\\bilad\\ExcelR\\Project\\Resume_Classification\\Models\\tfidf.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

try:
    model, vectorizer = load_artifacts()
    st.success("✅ Model loaded successfully!")

except FileNotFoundError:
    st.error("Model files not found. Please check the Models folder.")
    st.stop()


# Text Extraction
def extract_text(uploaded_file):
    file_bytes = uploaded_file.read()
    filename = uploaded_file.name.lower()
    try:

        # DOCX
        if filename.endswith(".docx"):
            return docx2txt.process(BytesIO(file_bytes))

        # PDF
        elif filename.endswith(".pdf"):
            text = ""

            with pdfplumber.open(BytesIO(file_bytes)) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""

            return text
        # .DOC 
        elif filename.endswith(".doc"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".doc") as tmp:
                tmp.write(file_bytes)
                temp_path = tmp.name

            word = win32com.client.Dispatch("Word.Application")
            word.Visible = False

            doc = word.Documents.Open(temp_path)
            text = doc.Content.Text
            doc.Close(False)
            word.Quit()
            return text
        else:
            st.error("Unsupported file type")
            return None
    except Exception as e:
        st.error(f"Error extracting text: {e}")
        return None
    


# Text Cleaning 
def clean_text(text):
    text=str(text)
    text=text.lower()
    text=text.replace('{html}', "")
    cleanr=re.compile('<.*?>')
    cleantext=re.sub(cleanr, '', text)
    rem_url=re.sub(r'hhtp\S+','', cleantext)
    rem_num=re.sub('[0-9]+', '',rem_url)
    tokenizer=RegexpTokenizer(r'\w+')
    tokens=tokenizer.tokenize(rem_num)
    filtered_words=[w for w in tokens if len(w) > 2 if not w in stopwords.words('english')]
    return " ".join(filtered_words)

# Upload Files
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "doc"])

if uploaded_file:
    st.write(
        f"**File:** {uploaded_file.name} | **Size:** {uploaded_file.size // 1024} KB"   )
    with st.spinner("Extracting text..."):
        raw_text = extract_text(uploaded_file)
    if raw_text and raw_text.strip():
        with st.expander("📋 Preview Extracted Text"):
            st.text(raw_text[:2000])
        st.divider()
        if st.button("🔍 Classify Resume", use_container_width=True):
            with st.spinner("Classifying..."):
                cleaned_text = clean_text(raw_text)
                vectorized = vectorizer.transform([cleaned_text])
                prediction = model.predict(vectorized)[0]

                # Convert Number to Category
                if isinstance(prediction, (int, float)) or "int" in str(type(prediction)):
                    category = INT_TO_CATEGORY.get(int(prediction), "Unknown")
                else:
                    category = str(prediction)

                # Confidence Score       
                confidence = None
                if hasattr(model, "predict_proba"):
                    probs = model.predict_proba(vectorized)[0]
                    confidence = round(max(probs) * 100, 2)
                elif hasattr(model, "decision_function"):
                    score = model.decision_function(vectorized)[0]

                    if hasattr(score, "__len__"):
                        score = max(score)
                    confidence = round(1 / (1 + math.exp(-abs(score))) * 100, 2 )

            # Result
            emoji = CATEGORY_EMOJI.get(category, "📄")
            label = category.replace("_", " ")
            st.success(f"{emoji} Predicted Category: **{label}**")

            if confidence:
                st.metric(
                    label="Confidence Score",
                    value=f"{confidence}%")
                st.progress(confidence / 100)
    else:
        st.warning("No text extracted from the resume.")