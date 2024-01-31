import statsmodels.api as sm

# Data
y_values = [0, 4, 8, 9, 12, 25, 34, 85]  # Replace with your actual y values
x_values = [25, 34, 85, 10, 14, 8, 9, 12]  # Replace with your actual x values

# Adding a constant term to the independent variable
x_values = sm.add_constant(x_values)

# Creating the linear regression model
model = sm.OLS(y_values, x_values)

# Fitting the model
results = model.fit()

with open('summary.txt', 'w') as fh:
    fh.write(results.summary().as_text())

with open('summary.csv', 'w') as fh:
    fh.write(results.summary().as_csv())

# Printing the summary output
print(results.summary())