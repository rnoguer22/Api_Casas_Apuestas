import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('UEFA_Predictions.csv')

# Guarda los datos en formato Markdown
markdown_table = df.to_markdown(index=False)

# Guarda el contenido en un archivo README.md
with open('README.md', 'w') as f:
    f.write(markdown_table)