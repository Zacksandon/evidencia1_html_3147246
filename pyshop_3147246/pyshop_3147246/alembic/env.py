from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

import os
import sys

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar conexión y metadata desde tu archivo de base de datos
from db import MARIADB_URL, engine, Base

# Importar todos los modelos (gracias al __init__.py en models/)
import models

# Obtener la configuración de Alembic
config = context.config
config.set_main_option("sqlalchemy.url", MARIADB_URL)

# Configuración de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata de todos los modelos (necesario para autogenerar migraciones)
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Ejecutar migraciones en modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecutar migraciones en modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# Decide si correr offline u online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
