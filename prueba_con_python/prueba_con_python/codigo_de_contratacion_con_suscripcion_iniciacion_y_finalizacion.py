import pandas as pd
from sqlalchemy import create_engine
file_path = 'codigo_de_contratacion_con_suscripcion_iniciacion_y_finalizacion.xlsx'
df = pd.read_excel(file_path)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print(df)
DATABASE_TYPE = 'mysql'
DBAPI = 'pymysql'
ENDPOINT = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'prueba_con_python'
connection_string = f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}/{DATABASE}"
engine = create_engine(connection_string)
table_name = 'codigo_de_contratacion_con_suscripcion_iniciacion_y_finalizacion'
df.to_sql(table_name, engine, if_exists='replace', index=False)
print(f"Datos insertados en la tabla '{table_name}' de la base de datos '{DATABASE}'.")