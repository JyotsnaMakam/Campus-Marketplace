# 🛍️ Campus Service Marketplace

A full-stack web application built with **Streamlit** and **Python** that allows students to list, sort, and book campus services. This project demonstrates data handling, session management, and cloud deployment.

## 🚀 Live Demo
Check out the live app here: [https://campus-marketplace-ahxbmzpmghjvca5czrbt3c.streamlit.app/]

## ✨ Key Features
* **Kaggle-Integrated Authentication**: User data is managed through a processed Kaggle dataset.
* **Real-time Dashboard**: Users can track their remaining balance and cart status on the home page.
* **Service Marketplace**: Browse services with dynamic "Add to Cart" functionality and price sorting.
* **Multi-page Navigation**: Seamless transitions between Registration, Marketplace, Bookings, and Payments.
* **Responsive UI**: A clean, modern interface designed for both desktop and mobile use.

## 🛠️ Tech Stack
* **Frontend**: Streamlit
* **Backend**: Python
* **Data Handling**: Pandas
* **Version Control**: Git & GitHub
* **Deployment**: Streamlit Community Cloud

## 📂 Project Structure
```text
Campus-Marketplace/
├── pages/ # Sub-pages for the application
│ ├── 1_Registration.py # User login & data cleaning
│ ├── 2_Marketplace.py # Service listings
│ ├── 3_My_Bookings.py # Shopping cart summary
│ └── 4_Payments.py # Payment processing logic
├── main.py # Application entry point & Dashboard
├── database.py # Data handling functions
├── users.csv # Local user database
├── requirements.txt # Deployment dependencies
└── README.md # Project documentation