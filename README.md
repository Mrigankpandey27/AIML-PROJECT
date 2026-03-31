# 🚦 Traffic Congestion Detector

A lightweight **Machine Learning** application built with Python to predict road traffic levels. This project uses a **Decision Tree Classifier** to analyze environmental factors and provide real-time travel suggestions.

---

### 📖 Project Overview
The **Traffic Congestion Detector** is designed to demonstrate the basics of supervised learning. By processing variables like time, weather, and road type, the model forecasts whether traffic will be **Low**, **Medium**, or **High**, helping users plan their commutes more efficiently.

### ✨ Key Features
* **🧠 Brain by scikit-learn**: Utilizes the `DecisionTreeClassifier` to identify patterns from historical data.
* **📊 Data Processing**: Uses `pandas` to map categorical text (e.g., "rainy", "weekend") into numerical values for model training.
* **🛠️ Robust Logic**: Features a student-friendly command-line interface (CLI) with `try/except` blocks to handle user input errors gracefully.
* **📝 Custom Dataset**: Includes 14 handmade scenarios covering weekday rush hours, foggy mornings, and clear weekend drives.

### ⚙️ Project Components
* **Data Module**: A built-in dictionary containing features like `hour`, `day`, `weather`, and `road`.
* **Preprocessing Engine**: A workflow that converts human-readable labels into machine-ready integers.
* **Inference Engine**: The trained model that calculates predictions using the `.predict()` method.
* **CLI Interface**: An interactive loop that collects user data and displays traffic alerts and "Quick Tips."

### 🚀 Setup & Installation
1.  **Install Dependencies**:
    ```bash
    pip install pandas scikit-learn
    ```
2.  **Run the Script**:
    ```bash
    python traffic_project.py
    ```

### 🛠️ How to Use
1.  Enter the **Hour** (0-23).
2.  Specify the **Day Type** (Weekday/Weekend).
3.  Select the **Weather** (Clear/Rainy/Foggy).
4.  Choose the **Road Type** (City/Highway).
5.  Receive an instant traffic prediction and a helpful travel suggestion!

---
*Developed as a functional introduction to Machine Learning and Data Science.*
