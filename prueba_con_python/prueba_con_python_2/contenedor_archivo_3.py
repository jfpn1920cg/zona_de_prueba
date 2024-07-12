import pandas as pd
from sqlalchemy import create_engine
file_path = 'contenedor_archivo_3.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)
print("Nombres de las hojas en el archivo Excel:", list(all_sheets.keys()))
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
DATABASE_TYPE = 'mysql'
DBAPI = 'pymysql'
ENDPOINT = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'prueba_con_python_2'
connection_string = f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}/{DATABASE}"
engine = create_engine(connection_string)
def remove_duplicate_columns(df):
    df = df.loc[:, ~df.columns.duplicated()]
    return df
for sheet_name, df in all_sheets.items():
    df.columns = df.columns.str.strip()
    df = remove_duplicate_columns(df)
    print(f"\nContenido de la hoja: {sheet_name}")
    print(df)
    table_name = f'{sheet_name}'
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Datos insertados en la tabla '{table_name}' de la base de datos '{DATABASE}'.")
print("Todos los datos han sido insertados en la base de datos.")