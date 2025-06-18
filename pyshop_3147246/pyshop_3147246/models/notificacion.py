from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Enum, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from db import Base

class Notificacion(Base):
    __tablename__ = "notificaciones"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    titulo = Column(String(200), nullable=False)
    mensaje = Column(Text, nullable=False)
    tipo = Column(Enum("proyecto", "evento", "comentario", "reaccion", "alianza", "sistema", name="tipo_notificacion"), nullable=False)
    leida = Column(Boolean, default=False)
    url_relacionada = Column(String(300))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="notificaciones")
