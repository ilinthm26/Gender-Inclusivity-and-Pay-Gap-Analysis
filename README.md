# 📊 Gender Inclusivity and Pay Gap Analysis
## 📌 Project Overview

This project analyzes workforce data to evaluate gender representation, leadership inclusivity, and compensation equity within an organization.

The objective is to identify:

  Gender distribution across departments

  Representation in leadership roles

  Salary differences between genders

  Statistical significance of observed pay gaps

  Actionable insights for HR policy improvement

This project focuses on descriptive and diagnostic analytics using Python.

## 🎯 Business Problem

Organizations aim to promote gender inclusivity and ensure fair compensation practices. However, without structured data analysis, it is difficult to:

  Quantify representation gaps

  Measure pay equity

  Identify leadership imbalances

  Validate whether pay differences are statistically significant

This analysis provides a data-driven evaluation of gender inclusivity and compensation fairness.

## 📂 Dataset

This project uses the IBM HR Employee Attrition & Performance dataset from Kaggle.

Dataset features:

  1,470 employee records

  Demographics (Age, Gender, Department)

  Job roles and levels

  Monthly income

  Years at company

  Promotion indicators

## 🛠 Tech Stack

  Python

  pandas

  numpy

  matplotlib

  seaborn

  scipy (statistical testing)

  Streamlit (interactive dashboard)

## 📊 Key Analysis Areas
### 1️⃣ Gender Representation Analysis
Metrics:

  Overall gender distribution %

  Gender distribution by department

  Gender distribution by leadership level

  Leadership representation ratio

Engineered Features:

  Age_Band

  Tenure_Band

  Is_Leader (binary leadership flag)


### 2️⃣ Pay Gap Analysis
Average Salary by Gender

Median Salary by Gender

  Interpretation:

  Positive → Women earn less than men

  Negative → Women earn more than men

Department-Level Pay Gap

To control for role bias, salary comparison was also performed within each department.

### 3️⃣ Statistical Validation

To determine whether observed salary differences are significant:

Independent T-Test

  Hypothesis:

  H₀: No salary difference between genders

  H₁: Salary difference exists

  Decision Rule:

  p < 0.05 → Significant difference

  p ≥ 0.05 → No statistically significant difference

## 📈 Dashboard Features

The interactive Streamlit dashboard includes:

  Executive Summary

  Total Employees

  Female Workforce %

  Female Leadership %

  Overall Pay Gap %

  Gender Representation Page

  Gender distribution by department

  Leadership representation charts

  Tenure vs Gender breakdown

  Pay Equity Page

  Salary distribution (boxplots)

  Department-wise pay gap

  Tenure vs salary scatter plot

