from IPython.display import display
from io import StringIO
import pandas as pd

def separator(message=None, n=40):
  if message != None:
    print(message)
  print('='*n)

def basicEDA(df, emoji='📊'):
    separator(f'{emoji} >> Exploratory Data Analysis Report')
    separator(f'{emoji} >> Missing Values and Percentage')

    null_values = df.isnull().sum()
    percent_null = (null_values / len(df)) * 100

    null_summary = pd.concat([null_values, percent_null], axis=1, keys=['Missing Values', 'Percentage (%)'])

    display(null_summary.style.set_table_styles([
        {'selector': 'thead th', 'props': [('background-color', '#6c757d'), ('color', 'white')]},
        {'selector': 'tbody td', 'props': [('border', '1px solid #ddd'), ('text-align', 'right')]}
    ]).format({'Percentage (%)': '{:.2f}%'}))

    separator()

    separator(f'{emoji} >> Data Summary')
    print(df.info())
    separator()

    buffer = StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    print(info_str)
    separator()

    separator(f"{emoji} >> Statistical Analysis")
    display(df.describe(include='all').style.set_table_styles([
        {'selector': 'thead th', 'props': [('background-color', '#17a2b8'), ('color', 'white')]},
        {'selector': 'tbody td', 'props': [('border', '1px solid #ddd'), ('text-align', 'right')]}
    ]))