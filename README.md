
# 🍔 Uber Eats Big Data Analytics Dashboard

A sleek and interactive **Streamlit dashboard** delivering insights from Uber Eats restaurant data. This project combines **Big Data tools** and **data visualization** to help users explore market trends, dish popularity, price ranges, and regional patterns.

---

## 🔍 Project Overview

This dashboard is built to analyze a large dataset of Uber Eats listings using backend tools like **Hive** and **Spark**, then present those insights through a user-friendly interface powered by **Streamlit** and **Plotly**.

Whether you're a data analyst, restaurant owner, or curious foodie — this tool helps uncover meaningful patterns in the food delivery space.

---

## 🛠️ Tech Stack

| Layer            | Technology                  |
|------------------|-----------------------------|
| **Frontend**     | Streamlit, Plotly           |
| **Backend**      | Apache Hive, Apache Spark   |
| **Data Handling**| Pandas, CSV files           |
| **Visualization**| Plotly charts, Streamlit UI |

---

## 📊 Key Features

- 🍽️ **Top Categories & Dishes**  
  Identify the most popular food categories and dishes.

- 💰 **Price vs Rating Analysis**  
  Explore how pricing varies across low-rated and high-rated restaurants.

- 🌍 **State-wise Restaurant Quality**  
  Visualize restaurant distribution and average ratings by U.S. state.

- 📈 **Dynamic Charts**  
  Interactive and responsive graphs powered by Plotly.

- 📂 **Expandable Data**  
  Designed to easily scale with larger datasets processed via Hive/Spark.

---

## 🚀 Getting Started

### 🔧 Prerequisites

Ensure you have Python installed (preferably 3.8+)

```bash
pip install -r requirements.txt
```

### ▶️ Launch the App

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser to explore the dashboard.

---

## 🧠 Insights Use Cases

- **Restaurant chains** can optimize pricing and menu strategies  
- **Consumers** can compare quality vs cost across states  
- **Analysts** can derive patterns from large-scale food delivery data  

---

## 📁 Folder Structure

```bash
uber-eats-streamlit-dashboard/
│
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── data/                   # Pre-processed CSVs or results
├── backend_queries/        # Hive/Spark scripts
├── assets/                 # Charts, images, logos
└── README.md               # Project documentation
```

---

## 🔮 Future Enhancements

- Integrate real-time data scraping  
- Add user filters (state, price range, rating)  
- Deploy using Docker or Streamlit Cloud  

---

## 👨‍💻 Developed By

**Aleem Wadhwaniya**  
[GitHub](https://github.com/Aliiim2711) • [LinkedIn](https://linkedin.com/in/aleemwadhwaniya)

---

## 📜 License

This project is licensed under the MIT License.
