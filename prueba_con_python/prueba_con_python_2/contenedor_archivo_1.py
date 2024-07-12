#para_realizar_este_codigo_se_a_instalado_las_siguientes_libreiras:
#se_utlizo_el_codigo_(import_pandas_as_pd)_instalamos:_pip_install_pandas
#se_utlizo_el_codigo_(from_sqlalchemy_import_create_engine)_instalamos:
#se_instalo_para_realiza_el_codigo:_pip_install --upgrade_numpy
#se_instalo_para_realiza_el_codigo:_pip_install --upgrade_pytz
#se_instalo_para_realiza_el_codigo:_pip_install_--upgrade_python-dateutil
#se_instalo_para_realiza_el_codigo:_pip_install_--upgrade_openpyxl

#importa_la_biblioteca_pandas_para_trabajar_con_datos_en_estructuras_de_dataframe.
import pandas as pd  
#importa_create_engine_de_sqlalchemy_para_manejar_la_conexion_a_la_base_de_datos.
from sqlalchemy import create_engine  

#define_la_ruta_del_archivo_excel_que_se_va_a_leer.
file_path = 'contenedor_archivo_1.xlsx'

#lee_todas_las_hojas_del_archivo_excel_y_las_almacena_en_un_diccionario.
#la_clave_del_diccionario_sera_el_nombre_de_la_hoja_y_el_valor_sera_un_dataframe_con_los_datos_de_esa_hoja.
all_sheets = pd.read_excel(file_path, sheet_name=None)
print("Nombres de las hojas en el archivo Excel:", list(all_sheets.keys()))

#configura_pandas_para_mostrar_todos_los_datos_sin_truncarlos.
pd.set_option('display.max_rows', None)#muestra_todas_las_filas.
pd.set_option('display.max_columns', None)#muestra_todas_las_columnas.
pd.set_option('display.width', None)#ajusta_el_ancho_de_visualizacion.
pd.set_option('display.max_colwidth', None)#ajusta_el_ancho_maximo_de_cada_columna.

#define_los_parametros_de_conexion_a_la_base_de_datos.
DATABASE_TYPE = 'mysql'
DBAPI = 'pymysql'
ENDPOINT = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'prueba_con_python_2'
connection_string = f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}/{DATABASE}"

#crea_el_motor_de_conexion_a_la_base_de_datos_usando_sqlalchemy.
engine = create_engine(connection_string)

#itera_sobre_cada_hoja_en_el_archivo_excel.
for sheet_name, df in all_sheets.items():
    print(f"Contenido de la hoja: {sheet_name}")
    print(df)

    #define_el_nombre_de_la_tabla_en_la_base_de_datos_como_el_nombre_de_la_hoja.
    table_name = f'{sheet_name}'
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Datos insertados en la tabla '{table_name}' de la base de datos '{DATABASE}'.")
print("Todos los datos han sido insertados en la base de datos.")