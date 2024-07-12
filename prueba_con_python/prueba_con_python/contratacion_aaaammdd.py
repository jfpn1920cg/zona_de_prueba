#importa_la_libreria_intalados_que_se_utilizaron_para_realizar_el_codigo_son_los_siguientes:
#intalacion_para_la_libreria_(import_pandas_as_pd):_pip_install_pandas
#intalacion_para_la_libreria_(from sqlalchemy import create_engine):_pip_install_SQLAlchemy
#intalacion_para_base_de_datos:_pip install PyMySQL
#intalacion_para_base_de_datos:_pip_install_pandas_SQLAlchemy_PyMySQL)

#importa_la_libreria_pandas_para_trabajar_con_dataframes
import pandas as pd
#importa_create_engine_de_sqlalchemy_para_establecer_la_conexion_con_la_base_de_datos
from sqlalchemy import create_engine

#lee_el_archivo_excel_y_lo_carga_en_un_dataframe_de_pandas
file_path = 'contratacion_aaaammdd.xlsx'
df = pd.read_excel(file_path)

#_configura_pandas_para_que_muestre_todas_las_filas_y_columnas_del_dataframe
pd.set_option('display.max_rows', None)#muestra_todas_las_filas
pd.set_option('display.max_columns', None)#muestra_todas_las_columnas
pd.set_option('display.width', None)#ajusta el_ancho_de_la_salida_de_texto_para_que_se_muestre_correctamente
pd.set_option('display.max_colwidth', None)#muestra_el_contenido_completo_de_cada_columna
#imprime_el_contenido_del_dataframe_para_verificar_que_se_ha_leido_correctamente
print(df)

#configura_los_parametros_de_la_base_de_datos
DATABASE_TYPE = 'mysql'
DBAPI = 'pymysql'
ENDPOINT = 'localhost'
USER = 'root'         
PASSWORD = ''         
DATABASE = 'prueba_con_python'
connection_string = f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}/{DATABASE}"
engine = create_engine(connection_string)

#nombre_de_la_tabla_en_la_que_se_insertaran_los_datos
table_name = 'contratacion_aaaammdd'
#inserta_el_dataframe_en_la_base_de_datos_reemplazando_la_tabla_si_ya_existe
df.to_sql(table_name, engine, if_exists='replace', index=False)
print(f"Datos insertados en la tabla '{table_name}' de la base de datos '{DATABASE}'.")