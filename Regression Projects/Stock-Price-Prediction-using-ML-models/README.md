
# Stock Price Prediction 📈

## Overview

This project predicts the future stock price of **Tesla, Inc. (TSLA)** using historical data from the past **10 years**. The goal is to help investors and enthusiasts forecast stock trends and make informed decisions.

Multiple machine learning and deep learning models have been used to find the best prediction approach, including **Random Forest**, **Linear Regression**, **LSTM**, and **GRU**. The **LSTM model** gave the most accurate results.

---

## Features

* Fetches and analyzes **Tesla stock historical data** (past 10 years)
* Preprocesses and cleans data for modeling
* Visualizes stock trends, patterns, and predictions
* Predicts Tesla stock price for the **next 1 year**
* Compares performance of **Random Forest, Linear Regression, LSTM, and GRU models**
* Evaluates models using **RMSE** and **R² metrics**

---

## Tech Stack

* **Language:** Python
* **Libraries:**

  * `pandas` – data manipulation
  * `numpy` – numerical computations
  * `matplotlib` & `seaborn` – data visualization
  * `scikit-learn` – Random Forest & Linear Regression
  * `tensorflow` / `keras` – LSTM & GRU models
  * `yfinance` – fetching historical stock data
* **IDE:** Jupyter Notebook / VS Code

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/tesla-stock-prediction.git
cd tesla-stock-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python stock_prediction.py
```

or open the Jupyter notebook `Tesla_Stock_Prediction.ipynb` to run step-by-step analysis.

---

## How It Works

1. **Data Collection:** Fetches **Tesla stock prices** for the past 10 years using `yfinance`.
2. **Data Preprocessing:** Cleans missing values, scales data, and prepares features for models.
3. **Model Training:** Trains multiple models:

   * **Linear Regression** – simple and interpretable
   * **Random Forest** – handles non-linear trends
   * **LSTM & GRU** – deep learning models capturing long-term dependencies
4. **Prediction:** Generates **stock price predictions for the next 1 year**.
5. **Evaluation:** Compares models using **RMSE** and **R²**, with **LSTM achieving the best results**.

---

## Example

```
Stock: Tesla (TSLA)  
Prediction Horizon: 1 year  
Best Model: LSTM  
RMSE: 18.23  
R² Score: 0.92
```

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---

## Contact

**Janavi Singh**

---
