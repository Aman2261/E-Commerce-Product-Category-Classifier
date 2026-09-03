# E-Commerce Product Category Classifier

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

An NLP-based machine learning system that automatically predicts the category of an e-commerce product from its title or description.

The project was built to explore the complete machine learning workflow — from raw product text and preprocessing to model comparison, evaluation, and preparing the final model for deployment.

---

## Problem Statement

Large e-commerce platforms deal with thousands of product listings every day. Manually assigning each listing to the correct category can be slow, inconsistent, and difficult to scale.

This project aims to automate that process.

Given a product title or description such as:

> **"Samsung 55 inch 4K Smart LED TV"**

the system predicts the most likely product category:

> **Electronics**

The model was trained to classify products into four categories:

-  Books
-  Clothing & Accessories
-  Electronics
-  Household

---

## Project Goals

The main goals of the project were to:

- Build an end-to-end text classification pipeline.
- Understand how preprocessing affects NLP models.
- Convert product descriptions into numerical features using TF-IDF.
- Compare different machine learning algorithms.
- Use cross-validation for model selection.
- Evaluate the final model on unseen data.
- Investigate whether preserving product specifications such as `4K`, `128GB`, and `15W` improves classification.
- Prepare the trained model for real-world deployment.

---

## Dataset

The project uses an e-commerce product classification dataset containing **50,425 product listings**.

| Category | Number of Products |
|----------|-------------------:|
| Household | 19,313 |
| Books | 11,820 |
| Electronics | 10,621 |
| Clothing & Accessories | 8,671 |
| **Total** | **50,425** |

Each record contains:

- `Category` — target class
- `Text` — product title/description

The dataset contains four relatively distinct product categories, making it suitable for supervised text classification.

---

## Machine Learning Pipeline

The overall workflow is:

```text
Raw Product Listings
        ↓
Text Cleaning & Normalization
        ↓
Train / Test Split
        ↓
TF-IDF Feature Extraction
        ↓
Model Comparison
        ↓
3-Fold Stratified Cross-Validation
        ↓
Select Best Model
        ↓
Final Evaluation on Test Set
        ↓
Model & Vectorizer Serialization
```
# Dashboard Link : https://e-commerce-category-classifier.streamlit.app/
