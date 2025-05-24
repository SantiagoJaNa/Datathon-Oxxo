import csv
import pandas as pd

# Read CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

    import pandas as pd

df = pd.read_csv('')
df = df.drop_duplicates(keep='first')

df.to_csv('cleaned_file.csv', index=False)