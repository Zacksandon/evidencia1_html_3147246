from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL básica
MARIADB_URL = "mysql+pymysql://root:@localhost:3315/py_shop"

# Crear el motor con parámetros específicos
engine = create_engine(
    MARIADB_URL, 
    echo=True,
    connect_args={
        "auth_plugin_map": {
            "mysql_native_password": "mysql_native_password"
        }
    }
)

# Crear una sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()