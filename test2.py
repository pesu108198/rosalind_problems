import matplotlib.pyplot as plt

# Your data
x_values = [ 1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16]
y_values = [19.5, 24.0, 20.0, 24.0, 20.0, 25.0, 20.0, 25.0, 20.0, 25.0, 20.0, 25.0, 22.0, 26.0, 24.0, 26.4]

plt.figure(figsize=(10, 6))

# ---------------------------------------------------------
# CHANGE 3: Decrease width
# Use 'width=0.4' (or any number less than 0.8) inside plt.bar
# ---------------------------------------------------------
plt.bar(x_values, y_values, width=0.4, color='skyblue', edgecolor='black')

# ---------------------------------------------------------
# CHANGE 1: Force every number on X-axis to appear
# passing 'x_values' ensures every single bar gets a label
# ---------------------------------------------------------
plt.xticks(x_values)

# ---------------------------------------------------------
# CHANGE 2: Start Y-axis from 15
# ---------------------------------------------------------
plt.ylim(bottom=15) 

plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Customized Bar Chart')

plt.show()