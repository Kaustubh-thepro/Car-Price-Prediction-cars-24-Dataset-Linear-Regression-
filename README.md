# Car-Price-Prediction-cars-24-Dataset-Linear-Regression-
Live Link - https://cars24-prediction.streamlit.app/

# 🚗 Cars24 Price Prediction

This project predicts **used car prices** based on features such as car name, year, location, fuel type, drive type, distance driven, and ownership details.  
The dataset was sourced from **Cars24 combined data**, cleaned, and analyzed before training a **Linear Regression model**.

---

## 📌 Project Workflow

### 1. **Data Preparation**
- Loaded dataset `cars_24_combined.csv`
- Cleaned and preprocessed the data:
  - Removed missing values (`Year`, `Location`)
  - Converted `Year` to integer
  - Handled categorical columns (`Car Name`, `Location`, `Fuel`, `Drive`, `Type`, `Owner`)

### 2. **Exploratory Data Analysis (EDA)**
- Plotted relationships between:
  - `Year` vs `Price`
  - `Distance` vs `Price`
  - `Owner` vs `Price`
  - Boxplots for categorical features (`Fuel`, `Drive`, `Type`, `Owner`)
- Identified outliers in price distribution

### 3. **Outlier Removal**
- Applied **IQR-based filtering** within groups:
  - Fuel type
  - Drive type
  - Car type
  - Owner

### 4. **Model Building**
- Features (`X`): All columns except `Price`
- Target (`y`): `Price`
- Preprocessing:
  - One-hot encoded categorical features
- Model: **Linear Regression**
- Pipeline created for seamless transformation + model training

### 5. **Model Evaluation**
- Metrics used:
  - **R² Score**
  - **Mean Absolute Error (MAE)**
  - **Root Mean Squared Error (RMSE)**
- Example Results:
  - `MAE`: ~ (value depends on dataset)
  - `RMSE`: ~ (value depends on dataset)

### 6. **Model Deployment**
- Final trained model saved as:
  ```
  LinearRegressionModelv2.pkl
  ```

---

## 🛠️ Tech Stack
- **Python** 🐍
- **Pandas**, **NumPy** – Data manipulation
- **Matplotlib**, **Seaborn** – Visualization
- **Scikit-learn** – Preprocessing & ML model
- **Pickle** – Model saving

---

## 📂 Project Structure
```
├── Cars 24 Prediction.ipynb     # Jupyter Notebook with full code
├── cars_24_combined.csv         # Dataset (not included here)
├── LinearRegressionModelv2.pkl  # Saved trained model
└── README.md                    # Project documentation
```

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/cars24-price-prediction.git
   cd cars24-price-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the notebook or script to train the model:
   ```bash
   jupyter notebook "Cars 24 Prediction.ipynb"
   ```

4. Use the saved model (`LinearRegressionModelv2.pkl`) for predictions:
   ```python
   import pickle

   model = pickle.load(open('LinearRegressionModelv2.pkl', 'rb'))
   prediction = model.predict([your_input_features])
   print(prediction)
   ```

---

## 📊 Example Visualization
- Year vs Price trend
- Distance vs Price regression
- Fuel/Drive/Type vs Price distributions

*(visuals available in the notebook)*

---

## ✨ Future Improvements
- Try advanced regression models: **Random Forest, XGBoost, Gradient Boosting**
- Hyperparameter tuning for better accuracy
- Feature engineering (e.g., car age instead of year)
- Deploy as a **Streamlit / Flask web app**

---

## 👨‍💻 Author
**Your Name**  
🔗 [LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/)

---
