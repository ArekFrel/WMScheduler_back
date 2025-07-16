from Planner.confidential import *
import pyodbc
from sqlalchemy import create_engine
"""
**********************************
*                                *
*       Database information     *
*                                *
**********************************
"""

SERVER = SERVER_conf
DATABASE = DATABASE_conf
DRIVER = DRIVER_conf
DRIVER_AL = DRIVER_conf_sql_alch

CONN = pyodbc.connect(
    "Driver="+DRIVER+";"
    "Server="+SERVER+";"
    "Database="+DATABASE+";"
    "UID="+LGIN+";"
    "PWD="+PSW+";"
)
sql_al_conn_string = f"mssql+pyodbc://{LGIN}:{PSW}@{SERVER}/{DATABASE}?driver={DRIVER_AL}"
ENGINE = create_engine(sql_al_conn_string)
CONN.timeout = 20
CURSOR = CONN.cursor()