import streamlit as st
import joblib

from preprocessing import normalize_text


# Load trained artifacts

vectorizer = joblib.load(
    "artifacts/tfidf_vectorizer.joblib"
)

model = joblib.load(
    "artifacts/best_model.joblib"
)

label_encoder = joblib.load(
    "artifacts/label_encoder.joblib"
)


# Streamlit page configuration

st.set_page_config(
    page_title="E-Commerce Product Classifier",
    page_icon="🛒",
    layout="centered"
)


# Title

st.title("🛒 E-Commerce Product Category Classifier")

st.write(
    "Enter a product title or description and "
    "the machine learning model will predict its category."
)


# User input

text = st.text_area(
    "Product title / description",
    placeholder=(
        "Example: Samsung 55 inch 4K Smart LED TV "
        "with 128GB storage"
    ),
    height=150
)


# Prediction

if st.button("Predict Category", type="primary"):

    if not text.strip():

        st.warning(
            "Please enter a product title or description."
        )

    else:

        # 1. Preprocess input

        cleaned_text = normalize_text(
            text,
            keep_numbers=True
        )

        # 2. Convert text to TF-IDF features

        X = vectorizer.transform(
            [cleaned_text]
        )

        # 3. Predict encoded category

        prediction = model.predict(X)

        # 4. Convert encoded label to original name

        category = label_encoder.inverse_transform(
            prediction
        )[0]

        # 5. Display result

        st.success(
            f"Predicted Category: **{category}**"
        )