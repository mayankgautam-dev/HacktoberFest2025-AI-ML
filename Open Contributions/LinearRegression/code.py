import numpy as np
import matplotlib.pyplot as plt

# Dataset
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Mean
mean_x = np.mean(x)
mean_y = np.mean(y)

# Slope and Intercept
m = np.sum((x - mean_x)*(y - mean_y)) / np.sum((x - mean_x)**2)
b = mean_y - m*mean_x

# Predictions
y_pred = m*x + b

# Print results
print(f"Slope: {m:.2f}, Intercept: {b:.2f}")
print("Predicted y:", y_pred)

# Plot
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, y_pred, color='red', label='Best Fit Line')
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.title("Linear Regression Example")
plt.legend()
plt.show()
