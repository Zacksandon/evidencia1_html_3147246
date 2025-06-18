from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime)
    modalidad = Column(Enum("virtual", "presencial", "hibrido", name="modalidad_evento"))
    ubicacion_fisica = Column(String(200))
    enlace = Column(String(300))
    capacidad_maxima = Column(Integer)
    precio = Column(DECIMAL(10, 2), default=0.00)
    organizador_id = Column(Integer, ForeignKey("usuarios.id"))
    imagen_evento = Column(String(300))
    estado = Column(Enum("programado", "en_curso", "finalizado", "cancelado", name="estado_evento"), default="programado")
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    inscripciones = relationship("InscripcionEvento", back_populates="evento")
