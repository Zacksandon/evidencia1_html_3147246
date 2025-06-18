from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, DECIMAL, Boolean
from datetime import datetime
from db import Base

class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=False)
    url = Column(Text)
    instructor = Column(String(100))
    duracion = Column(String(50))
    plataforma = Column(String(100))
    categoria = Column(String(100))
    nivel = Column(Enum("principiante", "intermedio", "avanzado", name="nivel_curso"), default="principiante")
    precio = Column(DECIMAL(10, 2), default=0.00)
    calificacion = Column(DECIMAL(3, 2), default=0.00)
    estudiantes_inscritos = Column(Integer, default=0)
    idioma = Column(String(50), default="Español")
    certificado = Column(Boolean, default=False)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
