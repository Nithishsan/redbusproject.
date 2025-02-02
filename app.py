import streamlit as st
import pandas as pd
import mysql.connector

# Function to Fetch Data from MySQL
def get_data():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="redbus"
    )
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM BusDetails")
    data = cursor.fetchall()
    cursor.close()
    db_connection.close()
    return pd.DataFrame(data) if data else pd.DataFrame()  # Return empty DataFrame if no data

# Load Data
bus_df = get_data()

# Ensure the DataFrame contains the expected columns
expected_columns = ["state", "route_name", "route_link", "bus_name", "bus_type", 
                    "departing_time", "duration", "reaching_time", "star_rating", "price", "seat_availability"]

for col in expected_columns:
    if col not in bus_df.columns:
        bus_df[col] = ""  # Add missing columns with default values

# Rename Columns to Match Code References
bus_df.rename(columns={"price": "Price", "star_rating": "Star Rating"}, inplace=True)

# Ensure "Price" is Numeric & Handle Missing Values
bus_df["Price"] = pd.to_numeric(bus_df["Price"], errors="coerce").fillna(0).astype(int)

# Streamlit UI
st.title(" Redbus Data Explorer")
st.sidebar.header(" Filter Options")

# Filter by State
states = bus_df["state"].unique().tolist()
selected_state = st.sidebar.selectbox("Select State:", ["All"] + states)
if selected_state != "All":
    bus_df = bus_df[bus_df["state"] == selected_state]

# Filter by Price Range
if not bus_df.empty:
    min_price, max_price = int(bus_df["Price"].min()), int(bus_df["Price"].max())
    min_price, max_price = (0, 10000) if min_price == max_price else (min_price, max_price)  # Prevent slider errors
    selected_min, selected_max = st.sidebar.slider("Select Price Range:", min_price, max_price, (min_price, max_price))
    bus_df = bus_df[(bus_df["Price"] >= selected_min) & (bus_df["Price"] <= selected_max)]

# Filter by Bus Type
bus_types = bus_df["bus_type"].dropna().unique().tolist()
selected_bus_type = st.sidebar.multiselect("Select Bus Type:", bus_types, default=bus_types)
bus_df = bus_df[bus_df["bus_type"].isin(selected_bus_type)]

# Filter by Star Rating
bus_df["Star Rating"] = pd.to_numeric(bus_df["Star Rating"], errors="coerce").fillna(0)
min_star, max_star = st.sidebar.slider("Select Star Rating:", 0.0, 5.0, (0.0, 5.0), 0.1)
bus_df = bus_df[(bus_df["Star Rating"] >= min_star) & (bus_df["Star Rating"] <= max_star)]

# Display Filtered Data
st.write(f"### Showing {len(bus_df)} Buses Matching Filters")
st.dataframe(bus_df)

# Download as CSV
st.download_button(" Download Data as CSV", bus_df.to_csv(index=False), "filtered_data.csv", "text/csv")
