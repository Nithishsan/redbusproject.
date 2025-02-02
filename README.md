##REDBUS

## Project Overview  
This project automates the process of scraping bus details from the RedBus website, storing them in a MySQL database, and displaying them through an interactive web interface built with Streamlit.  

---

## Features  

### **Web Scraper**  
- **Collects bus route details** (route names and links).  
- **Extracts key bus information**, including:  
  - State  
  - Route Name  
  - Bus Name  
  - Bus Type  
  - Departing Time  
  - Duration  
  - Reaching Time  
  - Star Rating  
  - Price  
  - Seat Availability  
- **Stores the extracted data** in a MySQL database.  
- **Exports the data** into a CSV file for further analysis.  

---

## Requirements  

### **Software & Libraries**  
- **Python** (Version 3.7+)  
- **Required Python Libraries:**  
  - `streamlit`  
  - `mysql-connector-python`  
  - `pandas`  

---

## Streamlit Web App  

### **Functionalities**  
- **Displays bus details** in a structured table format.  
- **Provides filtering options** to refine search results based on:  
  - **State Selection** – View available bus routes by state.  
  - **Route Selection** – Filter buses based on a selected state and route.  
  - **Bus Type** – Choose between AC, Non-AC, Seater, or Sleeper buses.  
  - **Departing Time** – Filter buses within specified time ranges (e.g., *06:01 to 12:00*).  
  - **Price Range** – Filter buses by ticket prices.  
  - **Star Rating** – View buses based on their customer ratings.  

---

## How It Works  

### **Database Querying**  
The Streamlit application connects to the **MySQL database** (`redbus`), retrieves bus data from the `BusDetails` table, and presents it in the frontend interface.  

### **Dynamic Filtering**  
Users can apply multiple filters via the **sidebar**, and the app instantly updates the displayed results. Filtering is handled in real-time by executing conditions on the retrieved database data.
