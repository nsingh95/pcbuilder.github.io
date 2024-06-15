import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Step 1: Load the data files
sales_df = pd.read_csv('sales.csv')
transaction_df = pd.read_csv('transaction.csv')
date_df = pd.read_csv('date.csv')

# Step 2: Data Preprocessing
# Merge data files using the common date column
merged_df = pd.merge(sales_df, date_df, on='date')
merged_df = pd.merge(merged_df, transaction_df, on=['date', 'sell_id', 'sell_category'])

# Handle missing values
merged_df = merged_df.dropna()

# Convert data types if necessary
merged_df['date'] = pd.to_datetime(merged_df['date'])

# Step 3: Exploratory Data Analysis (EDA)
# Descriptive statistics
print(merged_df.describe())

# Distribution plots
sns.histplot(merged_df['price'])
plt.title('Price Distribution')
plt.show()

sns.boxplot(x=merged_df['price'])
plt.title('Price Boxplot')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(merged_df.corr(), annot=True)
plt.title('Correlation Heatmap')
plt.show()

# Scatter plot of price vs. sales
sns.scatterplot(x='price', y='sales', data=merged_df)
plt.title('Price vs Sales')
plt.show()

# Time series analysis
merged_df.set_index('date', inplace=True)
merged_df['sales'].plot()
plt.title('Sales Over Time')
plt.show()
merged_df.reset_index(inplace=True)

# Step 4: Feature Engineering
# Create new features
merged_df['revenue'] = merged_df['price'] * merged_df['sales']

# (Optional) Log transformation for skewed data
merged_df['log_price'] = np.log(merged_df['price'])
merged_df['log_sales'] = np.log(merged_df['sales'])

print(merged_df.head())

# Step 5: Model Building
# Split the data into training and testing sets
X = merged_df[['price']]
y = merged_df['sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model performance
print('R-squared:', r2_score(y_test, y_pred))
print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))

# Plot residuals
plt.scatter(y_test, y_test - y_pred)
plt.hlines(y=0, xmin=min(y_test), xmax=max(y_test), colors='r')
plt.title('Residuals Plot')
plt.show()

# Step 6: Price Optimization
# Calculate price elasticity of demand
merged_df['price_elasticity'] = (merged_df['sales'] / merged_df['price'])

# Predict sales at different price points
prices = np.linspace(min(merged_df['price']), max(merged_df['price']), 100)
predicted_sales = model.predict(prices.reshape(-1, 1))

# Calculate revenue at different price points
revenue = prices * predicted_sales

# Find the price that maximizes revenue
optimal_price = prices[np.argmax(revenue)]
print('Optimal Price:', optimal_price)

# Plot revenue vs. price
plt.plot(prices, revenue)
plt.axvline(x=optimal_price, color='r', linestyle='--')
plt
