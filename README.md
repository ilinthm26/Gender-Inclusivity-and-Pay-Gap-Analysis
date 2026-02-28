# 📊 IBM Gender Inclusivity & Pay Gap Analysis
## 📌 Project Overview

This project analyzes workforce data to evaluate gender representation, leadership inclusivity, compensation equity, and statistical validation of pay differences within an organization.

The goal is to determine:

Are women equally represented in the workforce?

Are women equally represented in leadership?

Is there a measurable gender pay gap?

Are observed salary differences statistically significant?

The analysis combines:

Exploratory Data Analysis (EDA)

KPI-driven insights

Department-level analysis

Statistical hypothesis testing

Effect size evaluation

Interactive Streamlit dashboard

## 📁 Dataset

Original Data Source: [IBM HR Analytics Dataset] (https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

Processed file: processed_hr_data, processed_hr_data_eda.csv

Key variables used:

Gender

MonthlyIncome

Department

IsLeader

leadership_level

Attrition

JobRole

## 🔍 Exploratory Data Analysis (EDA)

The notebook performs:

Workforce gender distribution

Department-wise gender representation

Leadership representation analysis

Salary distribution (mean & median)

Department-level pay gap

Leadership-level pay gap

Attrition by gender


## 📊 Key Performance Indicators (KPIs)
1️⃣ Workforce Representation

Female Workforce %

Male Workforce %

Gender Diversity Index

2️⃣ Leadership Inclusivity

Female Leadership %

Male Leadership %


3️⃣ Pay Gap Metrics

Mean Pay Gap

Median Pay Gap

Department-Level Pay Gap

Leadership-Level Pay Gap

Pay Gap Formula Used:

(Male Average Salary − Female Average Salary) / Male Average Salary × 100

Interpretation:

Positive → Gap favors males

Negative → Gap favors females

Near zero → Pay equity

4️⃣ Attrition Analysis

Overall Attrition Rate

Female Attrition Rate

Male Attrition Rate

## 🧪 Statistical Validation

To determine whether observed salary differences are statistically significant, an Independent Two-Sample Welch’s T-Test was performed.

Hypothesis

H₀: No salary difference between genders

H₁: Salary difference exists

Decision Rule

p < 0.05 → Reject H₀ (Significant difference)

p ≥ 0.05 → Fail to reject H₀ (Not significant)

📈 Statistical Results

T-Statistic: -1.2223

P-Value: 0.2218

Cohen’s d (Effect Size): -0.065

Interpretation

p-value > 0.05 → No statistically significant salary difference

Cohen’s d ≈ 0 → Practically negligible difference

Negative sign → Female mean salary slightly higher

### Final Statistical Conclusion

The analysis does not provide evidence of a statistically or practically significant gender-based salary disparity in the dataset.

## 📊 Effect Size (Cohen’s d)

Effect size measures practical significance:

Value	Interpretation
0.2	Small effect
0.5	Medium effect
0.8	Large effect

Observed: -0.065 → Negligible effect

This indicates near salary parity.

📈 Interactive Dashboard (Streamlit)

# The project includes a fully interactive Streamlit dashboard featuring:

## 🔎 Global Filters

Department

Leadership Level

Job Role

 ## 📊 Tabs

Executive Summary

Gender Inclusivity Analysis

Pay Gap Analysis


📉 Visualizations

Pie charts

Grouped bar charts

Box plots

Department pay gap bars

Leadership pay gap analysis


## 🛠 Technologies Used

Python

Pandas

NumPy

SciPy

Plotly

Streamlit

Jupyter Notebook / Google Colab

## 🎯 Business Insights

Based on the analysis:

Workforce gender distribution is balanced.

Leadership representation can be monitored using pipeline metrics.

No statistically significant pay gap detected.

Effect size confirms minimal practical difference.

Compensation appears equitable across genders in the analyzed dataset.

## 📌 Future Improvements

Adjusted pay gap using regression (control for department & leadership level)

Logistic regression for promotion bias

Time-based trend analysis

Inclusion of additional diversity dimensions

Confidence intervals for salary estimates

## 👩‍💻 Author

Ilin Thomas
## ⭐ Why This Project Matters

Gender pay equity and leadership inclusivity are critical components of organizational fairness and diversity strategy.

This project demonstrates:

Data cleaning & EDA

KPI design

Statistical hypothesis testing

Effect size interpretation

Interactive dashboard development

Business insight communication
