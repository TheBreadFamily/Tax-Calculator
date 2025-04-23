
import streamlit as st
from federal_tax_calculator import compute_tax

st.set_page_config(page_title="Federal Tax Calculator")

st.title("Federal Tax Calculator (2021–2023)")
st.markdown("Calculate your **estimated federal income tax** and **after-tax income** based on your filing status and tax year.")

year = st.selectbox("Select Tax Year", [2021, 2022, 2023])
status = st.selectbox("Select Filing Status", [
    "Single", 
    "Married Filing Jointly", 
    "Married Filing Separately", 
    "Head of Household"
])
income = st.number_input("Enter Taxable Income ($)", min_value=0, step=1000)

if st.button("Calculate"):
    tax, after = compute_tax(income, status, year)
    st.success(f"Estimated Federal Tax Owed: ${tax:,.2f}")
    st.info(f"After-Tax Income: ${after:,.2f}")
