import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Read data from Excel file
excel_file_path = r"./Pohalim_H.xlsx"
df = pd.read_excel(excel_file_path)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the overlapping areas
plt.fill_between(
    df.index,
    df["gate_low"],
    df["gate_height"],
    color="blue",
    alpha=0.3,
    label="Gate Range",
)

# Plot the execution gates as points
plt.scatter(
    df.index, df["execution_gate"], color="black", marker="o", label="Execution Gate"
)

# Color the points based on buy/sell
colors = {"buy": "green", "sell": "red"}
for i, row in df.iterrows():
    plt.scatter(i, row["execution_gate"], color=colors[row["buy_sell"]], marker="o")

# Add labels and legend
plt.xlabel("Data Points")
plt.ylabel("Gate Value")
plt.title("Gate Heights, Lows, and Execution Points")
plt.legend()

# Add regression line
regression_x = np.array(df.index).reshape(-1, 1)
regression_y = df["execution_gate"]
# regression_y = df["end_d"]
regressor = LinearRegression()
regressor.fit(regression_x, regression_y)
regression_line = regressor.predict(regression_x)
plt.plot(
    df.index, regression_line, color="purple", linestyle="--", label="Regression Line"
)

# Display the regression line formula
slope = regressor.coef_[0]
y_intercept = regressor.intercept_
formula = f"Regression Line: y = {slope:.2f}x + {y_intercept:.2f}"
plt.annotate(formula, (0.25, 0.9), xycoords="axes fraction", fontsize=12)

# Show the plot
plt.tight_layout()
plt.legend()
plt.show()
