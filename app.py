import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Uber Eats Analytics", layout="wide")
st.title("🍽️ Uber Eats Analytics Dashboard")
st.markdown("Welcome! This dashboard presents insights about restaurant categories, pricing, and customer preferences using Uber Eats data.")

# Utility: Load Data with Error Handling
def load_csv(path, label):
    try:
        df = pd.read_csv(path)
        st.success(f"{label} loaded successfully ✅")
        return df
    except Exception as e:
        st.error(f"❌ Error loading {label}: {e}")
        return pd.DataFrame()

# Load Datasets
top_categories = load_csv("data/top_categories.csv", "Top Categories")
high_rated_by_price = load_csv("data/high_rated_by_price.csv", "High Rated by Price Range")
popular_dishes = load_csv("data/popular_dishes.csv", "Popular Dishes")
low_rated_by_cat_price = load_csv("data/low_rated_by_category_price.csv", "Low Rated Categories by Price")
avg_rated_categories = load_csv("data/highest_avg_rated_categories.csv", "Top Avg Rated Categories")
statewise_high_rated = load_csv("data/high_rated_by_state.csv", "High Rated Restaurants by State")

# Section 1: Top Categories
if not top_categories.empty:
    st.header("1️⃣ Most Common Restaurant Categories")
    fig1 = px.bar(top_categories, x='category', y='total_restaurants', title="Top 10 Categories")
    st.plotly_chart(fig1, use_container_width=True)

# Section 2: Price Range Preferences of High Rated Restaurants
if not high_rated_by_price.empty:
    st.header("2️⃣ Rating Distribution by Price Category")
    fig2 = px.pie(high_rated_by_price, names='price_category', values='count', title="High Rated Restaurants by Price Category")
    st.plotly_chart(fig2, use_container_width=True)

# Section 3: Popular Dishes
if not popular_dishes.empty:
    st.header("3️⃣ Most Popular Dishes (Highly Rated Restaurants)")
    fig3 = px.bar(popular_dishes.head(10), x='dish_name', y='popularity', title="Top 10 Popular Dishes")
    st.plotly_chart(fig3, use_container_width=True)

# Section 4: Low Rated Patterns
if not low_rated_by_cat_price.empty:
    st.header("4️⃣ Low Rated Categories & Price Range")
    fig4 = px.bar(low_rated_by_cat_price, x='category', y='low_rated_count', color='price_range',
                  title="Low Ratings by Category and Price", barmode='group')
    st.plotly_chart(fig4, use_container_width=True)

# Section 5: Top Avg Rated Categories (Min 50 Restaurants)
if not avg_rated_categories.empty:
    st.header("5️⃣ Highest Average Rated Categories (≥ 50 Restaurants)")
    st.dataframe(avg_rated_categories)

# Section 6: State-wise High Rated Restaurant Count
if not statewise_high_rated.empty:
    st.header("6️⃣ States with Most High Rated Restaurants")
    fig6 = px.choropleth(statewise_high_rated, locations='state', locationmode='USA-states',
                         color='count', scope='usa',
                         title="High Rated Restaurants by US State",
                         color_continuous_scale="Viridis")
    st.plotly_chart(fig6, use_container_width=True)

# Footer
st.markdown("---")
st.caption("Developed by Aleem Wadhwaniya | Data sourced from Uber Eats USA dataset")
