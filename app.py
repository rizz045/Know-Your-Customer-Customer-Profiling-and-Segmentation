import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained segmentation model
try:
    with open("kmeans.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error("⚠️ Unable to load the segmentation model. Please ensure the 'segmentation.pkl' file is in the correct directory.")
    st.stop()

# Configure the Streamlit page
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

# App title and description
st.title("🎯 Customer Segmentation Dashboard")
st.markdown("""
Welcome! Use the sidebar to enter customer details, and our intelligent model will predict the customer segment they belong to.  
This tool helps you better understand and personalize your marketing strategies.
""")

# Sidebar input section
st.sidebar.header("📋 Enter Customer Information")

# Input fields
education = st.sidebar.selectbox("Education Level", ['Basic', 'Graduation', 'Master', 'PhD', '2n Cycle'])
marital_status = st.sidebar.selectbox("Marital Status", ['Single', 'Together', 'Married', 'Divorced', 'Widow'])
income = st.sidebar.number_input("Annual Income (in USD)", min_value=0, max_value=200000, value=50000, step=1000)
recency = st.sidebar.slider("Recency (days since last purchase)", 0, 100, 30)

mnt_wines = st.sidebar.slider("Amount Spent on Wine", 0, 1000, 50)
mnt_fruits = st.sidebar.slider("Amount Spent on Fruits", 0, 1000, 10)
mnt_meat = st.sidebar.slider("Amount Spent on Meat Products", 0, 1000, 30)
mnt_fish = st.sidebar.slider("Amount Spent on Fish Products", 0, 1000, 10)
mnt_sweets = st.sidebar.slider("Amount Spent on Sweet Products", 0, 1000, 5)
mnt_gold = st.sidebar.slider("Amount Spent on Gold Products", 0, 1000, 10)

num_deals = st.sidebar.slider("Number of Deal Purchases", 0, 15, 2)
num_web = st.sidebar.slider("Web Purchases", 0, 15, 3)
num_catalog = st.sidebar.slider("Catalog Purchases", 0, 15, 1)
num_store = st.sidebar.slider("Store Purchases", 0, 15, 2)
num_web_visits = st.sidebar.slider("Website Visits per Month", 0, 20, 5)

complain = st.sidebar.selectbox("Filed a Complaint?", [0, 1])
response = st.sidebar.selectbox("Responded to Last Campaign?", [0, 1])
age = st.sidebar.slider("Age", 18, 100, 35)
money_spent = st.sidebar.slider("Total Money Spent", 0, 10000, 500)
children = st.sidebar.slider("Number of Children", 0, 5, 1)
day_joined = st.sidebar.slider("Day of the Year Joined", 1, 365, 100)

# Create DataFrame for the input
input_data = pd.DataFrame({
    'Education': [education],
    'Marital_Status': [marital_status],
    'Income': [income],
    'Recency': [recency],
    'MntWines': [mnt_wines],
    'MntFruits': [mnt_fruits],
    'MntMeatProducts': [mnt_meat],
    'MntFishProducts': [mnt_fish],
    'MntSweetProducts': [mnt_sweets],
    'MntGoldProds': [mnt_gold],
    'NumDealsPurchases': [num_deals],
    'NumWebPurchases': [num_web],
    'NumCatalogPurchases': [num_catalog],
    'NumStorePurchases': [num_store],
    'NumWebVisitsMonth': [num_web_visits],
    'Complain': [complain],
    'Response': [response],
    'Age': [age],
    'Money_Spent': [money_spent],
    'Children': [children],
    'Day_Joined': [day_joined]
})

# Show input data for confirmation
with st.expander("🔍 Review Entered Customer Information"):
    st.write(input_data.T)

# Make prediction
if st.button("🔎 Predict Customer Segment"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🎉 The predicted customer segment is: **{prediction}**")
    except Exception as e:
        st.error("❌ Sorry, something went wrong during the prediction.")
        st.exception(e)
