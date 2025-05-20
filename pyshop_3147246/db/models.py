from .database import Base
from sqlalchemy import Column, Integer, String

#Crear la clase de modelo
class Categoria(Base):
    __tablename__='categorias'
    id = Column(Integer,
                primaryKey=True,
                )
    nombre = Column(String(50))