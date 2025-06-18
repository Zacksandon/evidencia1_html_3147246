from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, DECIMAL, Boolean
from datetime import datetime
from db import Base

class Recurso(Base):
    __tablename__ = "recursos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=False)
    tipo = Column(Enum("guía", "herramienta", "curso", "plantilla", "ebook", "webinar", "podcast", name="tipo_recurso"), nullable=False)
    categoria = Column(String(100), nullable=False)
    enlace = Column(Text)
    archivo_url = Column(String(300))
    autor = Column(String(100))
    duracion_minutos = Column(Integer)
    nivel = Column(Enum("principiante", "intermedio", "avanzado", name="nivel_recurso"), default="principiante")
    calificacion = Column(DECIMAL(3, 2), default=0.00)
    numero_descargas = Column(Integer, default=0)
    gratuito = Column(Boolean, default=True)
    precio = Column(DECIMAL(10, 2))
    activo = Column(Boolean, default=True)
    fecha_publicacion = Column(DateTime, default=datetime.utcnow)
