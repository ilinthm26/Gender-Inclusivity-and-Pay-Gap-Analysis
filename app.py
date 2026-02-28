
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="HR Analytics Dashboard",layout="wide")


@st.cache_data
def load_data():
    return pd.read_csv("data/processed_hr_data.csv")
df=load_data()

st.title("Gender Inclusivity and Pay Gap")
st.write("This project analyzes workforce data to evaluate gender representation, leadership inclusivity, and compensation equity within an organization.")

# Global sidebar filters

st.sidebar.header("🔎 Filters")

# Department

department=st.sidebar.multiselect(
    "Select Department",
    options=sorted(df['Department'].unique()),
    default=sorted(df['Department'].unique())
)

#Leadership Level
leadership_role=st.sidebar.radio(
    "Select Leadership Level",
    options=['All']+sorted(df['leadership_level'].unique())
)
# Apply filters for dynamic job role list
temp_df=df[df['Department'].isin(department)]

if leadership_role!='All':
    temp_df=temp_df[
        temp_df['leadership_level']==leadership_role
    ]

# job role
job_role=st.sidebar.selectbox(
    "Select Job Role",
    options=['All']+sorted(temp_df['JobRole'].unique())
)

# Apply job role filter
if job_role!='All':
    temp_df=temp_df[
        temp_df['JobRole']==job_role
    ]

st.sidebar.markdown("---")
st.sidebar.success("Filter Applied")

# Stop if empty

if len(temp_df)==0:
    st.warning("Oops! No data available in the selected filter!")
    st.stop()
# ===================================
# Tabs

tab1,tab2,tab3=st.tabs(
    ["📊 Executive Summary", "👩 Gender Analysis", "💰 Pay Gap Analysis"]
)

# =======================
# TAB 1 — Executive Summary
# =======================

with tab1:
    st.subheader("📊 Executive Summary")
    col1,col2,col3,col4=st.columns(4)

    total_length=len(temp_df)

    female_pct=(temp_df['Gender']=='Female').mean()*100
    male_pct=(temp_df['Gender']=='Male').mean()*100
    leaders=temp_df[temp_df['IsLeader']==1]

    female_pct_leaders= (
        (leaders['Gender']=='Female').mean()*100
        if len(leaders)>0 else 0
    )

    # paygap
    avg_sal=temp_df.groupby('Gender')['MonthlyIncome'].mean()
    female_avg=avg_sal.get('Female',0)
    male_avg=avg_sal.get('Male',0)
    pay_gap=((male_avg-female_avg)/male_avg*100) if male_avg!=0 else 0
    overall_attrition=(temp_df['Attrition']=='Yes').mean()*100
    attrition_rate_Female=((temp_df['Attrition']=='Yes')&( temp_df['Gender']=='Female')).mean()*100

    attrition_rate_Male=((temp_df['Attrition']=='Yes')&( temp_df['Gender']=='Male')).mean()*100

    gender_dist=(temp_df['Gender'].value_counts(normalize=True))
    diversity_index=1-sum(gender_dist**2)
    # promotion gap(leadership pipeline gap)
    female_leadership_ratio=(
        len(temp_df[(temp_df['Gender'] == 'Female') & (temp_df['IsLeader'] == 1)])/
        len(temp_df[temp_df['Gender'] == 'Female'])
        if len(temp_df[temp_df['Gender']=='Female'])>0 else 0
    )



    # Median Pay Gap
    median_sal= temp_df.groupby('Gender')['MonthlyIncome'].median()
    median_gap=(
    (median_sal.get('Male',0)-median_sal.get('Female',0))
        /median_sal.get('Male',1)*100
    )



    col1.metric("Total Employees:",total_length)
    col2.metric("Female Workforce Percentage:",f"{female_pct:.2f}%")
    col3.metric("Male Workforce Percentage:",f"{male_pct:.2f}%")
    col4.metric("Female Leadership Percentage:",f"{female_pct_leaders:.2f}%")

    col5, col6, col7, col8 = st.columns(4)
    col9,col10,col11,col12=st.columns([1,1,1,1])


    col5.metric("Pay Gap:",f"{pay_gap:.2f}%")
    col6.metric("Attrition Rate:",round(overall_attrition,2))
    col7.metric("Attrition Rate - Female:",round(attrition_rate_Female,2))
    col8.metric("Attrition Rate - Male:",round(attrition_rate_Male,2))
    col9.metric("Diversity Index:",f'{diversity_index:.2f}')
    col10.metric("Females Who Became Leaders:",f'{female_leadership_ratio*100:.2f}%')
    col11.metric("Median Pay Gap:",f"{median_gap:.2f}%")

    st.download_button(
        label="📥 Download Filtered Data",
        data=temp_df.to_csv(index=False),
        file_name="filtered_csv",
        mime='text/csv'
    )
# =======================
# TAB 2 — Gender Analysis
# =======================

with tab2:
    st.subheader("👩 Gender Inclusivity Analysis")

    row1_col1,row1_col2,row1_col3=st.columns([1,1,1])
    row2_col1,row2_col2,row2_col3=st.columns([1,1,1])

    overall_distribution = (
            (df['Gender']
            .value_counts(normalize=True)*100)
            .round(2)
            .rename('Percentage')
            .reset_index()

    )
    overall_distribution.columns=['Gender',"Count"]
    row1_col1.write('Overall Gender Distribution')
    row1_col1.dataframe(overall_distribution)

    fig1=px.pie(
        overall_distribution,
        values='Count',
        names='Gender',
        hole=0.5,
        color='Gender',
        color_discrete_sequence=["#FF4B4B", "#1F77B4"]
    )
    fig1.update_layout(template="simple_white")
    row2_col1.plotly_chart(fig1,width='stretch')

    # dept_count= temp_df['Department'].value_counts().reset_index()

    dept_count=(
        pd.crosstab(
            temp_df['Department'],
            temp_df['Gender']
        )
    )
    plot_df_1 = (
        dept_count
        .reset_index()
        .melt(id_vars="Department",
              var_name="Gender",
              value_name="Count")
    )
    row1_col2.write('Department Vs Gender Distribution')
    row1_col2.dataframe(dept_count)
    fig2=px.bar(plot_df_1,
                x='Gender',
                y='Count',
                color='Department',
                barmode='group',
                text_auto=".1f",
                color_discrete_sequence=["#FF4B4B",'#17BECF', "#1F77B4"]
                )

    fig2.update_layout(
        xaxis_showgrid=False,
        yaxis_showgrid=False
    )
    row2_col2.plotly_chart(fig2,use_container_width=True)

    is_leader_count =(pd.crosstab(
        temp_df['IsLeader'],
        temp_df['Gender'],
        normalize="index"
    )*100
    ).round(2)
    is_leader_count.index = is_leader_count.index.map({
        0: "Non-Leader",
        1: "Leader"
    })
    plot_df = (
        is_leader_count
        .reset_index()
        .melt(id_vars="IsLeader",
              var_name="Gender",
              value_name="Percentage")
    )


    # is_leader_count.columns=['Count']
    row1_col3.write("IsLeader Vs Gender")
    row1_col3.dataframe(is_leader_count)

    fig3=px.bar(
        plot_df,
        x="IsLeader",
        y='Percentage',
        color='Gender',
        barmode='group',
        text_auto=".1f",
        color_discrete_sequence=["#FF4B4B", "#1F77B4"]
    )
    fig3.update_layout(
        xaxis_showgrid=False,
        yaxis_showgrid=False
    )
    row2_col3.plotly_chart(fig3)

#----------------------------
#Tab 3: Pay Gap Analysis
#----------------------------
with tab3:
    st.subheader("💰 Pay Gap Analysis")
    row1_col1,row1_col2,row1_col3=st.columns([1,1,1])
    row2_col1,row2_col2,row2_col3=st.columns([1,1,1])
    salary_gender=(
        temp_df
        .groupby('Gender')['MonthlyIncome']
        .agg(['mean','median'])
    )
    row1_col1.write("Overall Distribution of Salary over Gender")
    row1_col1.dataframe(salary_gender)
    # overall salary distribution over gender

    fig_salary=px.box(
        temp_df,
        x='Gender',
        y='MonthlyIncome',
        color='Gender',
        color_discrete_sequence=["#1F77B4", "#FF4B4B"]
    )

    # Adjust layout for more spacing
    fig_salary.update_layout(
        boxmode='group',
        width=700,
        height=500,
        yaxis_title="Monthly Income",
        xaxis_title="Gender",
        title="Salary Distribution by Gender (Outliers Highlighted)",
        xaxis_showgrid=False,
        yaxis_showgrid=False
    )

    row2_col1.plotly_chart(fig_salary)
    row2_col1.write("(Hover to see more details.)")

# Department level pay gap

    dept_pay_gap=(temp_df
        .groupby(['Department','Gender'])['MonthlyIncome']
        .mean()
        .unstack()
                  )

    dept_pay_gap['PayGap%']=(
    (dept_pay_gap['Male']-dept_pay_gap['Female'])/dept_pay_gap['Male']*100
    ).round(2)
    row1_col2.write("Department Wise Salary Distribution")
    row1_col2.dataframe(dept_pay_gap)
    # Reset index if your DataFrame index is Department
    dept_pay_gap = dept_pay_gap.reset_index()

    fig_dept_sal=px.bar(
        dept_pay_gap,
        x='PayGap%',
        y='Department',
        orientation='h',
        color='PayGap%',
        barmode='group',
        text_auto=".2f",
        color_continuous_scale=['#1F77B4', '#FF4B4B'],
    )
    fig_dept_sal.update_layout(
        boxmode='group',
        width=700,
        height=500,
        yaxis_title="Department",
        xaxis_title="Pay Gap%",
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        title="Pay Gap by Departments"
    )
    row2_col2.plotly_chart(fig_dept_sal)
    row2_col2.write("(Negative values means it favours female workforce.)")

# Pay gap by leadership level


    pay_gap_leadership_level = (temp_df
                    .groupby(['leadership_level', 'Gender'])['MonthlyIncome']
                    .mean()
                    .unstack()
                    )

    pay_gap_leadership_level['PayGap%'] = (
            (pay_gap_leadership_level['Male'] - pay_gap_leadership_level['Female']) / pay_gap_leadership_level['Male'] * 100
    ).round(2)
    row1_col3.write("Department Wise Salary Distribution")
    row1_col3.dataframe(pay_gap_leadership_level)

    # Reset index if your DataFrame index is Department
    pay_gap_leadership_level = pay_gap_leadership_level.reset_index()

    fig_leadership_level = px.bar(
        pay_gap_leadership_level,
        x='leadership_level',
        y='PayGap%',
        color='PayGap%',
        barmode='group',
        text_auto=".2f",
        color_continuous_scale=['#1F77B4', '#FF4B4B'],
    )
    fig_leadership_level.update_layout(
        boxmode='group',
        width=700,
        height=500,
        yaxis_title="Pay Gap%",
        xaxis_title="leadership_level",
        title="Pay Gap by Leadership Level",
        xaxis_showgrid=False,
        yaxis_showgrid=False
    )
    row2_col3.plotly_chart(fig_leadership_level)



