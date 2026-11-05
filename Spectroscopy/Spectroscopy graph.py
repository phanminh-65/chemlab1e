
import numpy as np
import matplotlib.pyplot as plt

# Experimental data
concentration = np.array([0.817, 1.634, 2.450, 3.267, 4.084, 6.126])
absorbance = np.array([0.060, 0.122, 0.185, 0.248, 0.311, 0.458])

# Calculate linear regression
slope, intercept = np.polyfit(concentration, absorbance, 1)

# Calculate predicted absorbance
predicted = slope * concentration + intercept

# Calculate R-squared
ss_res = np.sum((absorbance - predicted) ** 2)
ss_tot = np.sum((absorbance - np.mean(absorbance)) ** 2)
r_squared = 1 - (ss_res / ss_tot)

# Generate best-fit line
x_line = np.linspace(0, 7, 100)
y_line = slope * x_line + intercept

# Create plot
plt.figure(figsize=(8, 6))

# Plot experimental data
plt.scatter(concentration, absorbance,
            label="Experimental Data")

# Plot linear regression
plt.plot(x_line, y_line,
         label="Linear Regression")

# Add equation and R-squared to graph
equation = (
    f"y = {slope:.5f}x + {intercept:.5f}\n"
    f"R² = {r_squared:.5f}"
)

plt.text(0.05, 0.95, equation,
         transform=plt.gca().transAxes,
         verticalalignment='top',
         bbox=dict(facecolor='white', alpha=0.8))

# Graph title and axis labels
plt.title("Calcium Calibration Curve")
plt.xlabel("Ca²⁺ Concentration (ppm)")
plt.ylabel("Absorbance")

plt.xlim(0, 7)
plt.ylim(0, 0.55)

plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# Display graph
plt.show()

# Print regression results
print(f"Best-fit equation: y = {slope:.5f}x + {intercept:.5f}")
print(f"R-squared: {r_squared:.5f}")
