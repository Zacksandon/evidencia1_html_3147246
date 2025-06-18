from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from db import Base

class MensajeSoporte(Base):
    __tablename__ = "mensajes_soporte"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    asunto = Column(String(200), nullable=False)
    mensaje = Column(Text, nullable=False)
    categoria_soporte = Column(Enum("tecnico", "cuenta", "proyecto", "evento", "general", name="categoria_soporte"), default="general")
    prioridad = Column(Enum("baja", "media", "alta", "urgente", name="prioridad_soporte"), default="media")
    estado = Column(Enum("abierto", "en_proceso", "resuelto", "cerrado", name="estado_soporte"), default="abierto")
    respuesta = Column(Text)
    admin_respuesta_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha = Column(DateTime, default=datetime.utcnow)
    fecha_respuesta = Column(DateTime)

    usuario = relationship("Usuario", back_populates="mensajes_soporte")
