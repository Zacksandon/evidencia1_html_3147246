from sqlalchemy import Column, Integer, Text, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class InscripcionEvento(Base):
    __tablename__ = "inscripciones_evento"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    evento_id = Column(Integer, ForeignKey("eventos.id"))
    estado_inscripcion = Column(Enum("inscrito", "confirmado", "asistio", "no_asistio", "cancelado", name="estado_inscripcion"), default="inscrito")
    fecha_inscripcion = Column(DateTime, default=datetime.utcnow)
    notas = Column(Text)

    usuario = relationship("Usuario", back_populates="inscripciones")
    evento = relationship("Evento", back_populates="inscripciones")
