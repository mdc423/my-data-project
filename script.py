import csv

# Your Logic
data = [['id', 'value'], [1, 100], [2, 200]]

#Your "Build Test" (The Output
with open('output_matrix.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
print("Matrix generated successfully.")