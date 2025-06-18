from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, DECIMAL, Boolean
from datetime import datetime
from db import Base

class Plantilla(Base):
    __tablename__ = "plantillas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=False)
    url = Column(Text)
    archivo_url = Column(String(300))
    categoria = Column(String(100), nullable=False)
    tipo_archivo = Column(Enum("pdf", "docx", "xlsx", "pptx", "html", "zip", name="tipo_archivo_plantilla"), default="pdf")
    tamaño_kb = Column(Integer)
    descargas = Column(Integer, default=0)
    calificacion = Column(DECIMAL(3, 2), default=0.00)
    gratuito = Column(Boolean, default=True)
    precio = Column(DECIMAL(10, 2))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
