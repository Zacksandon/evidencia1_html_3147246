from sqlalchemy import Column, Integer, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Comentario(Base):
    __tablename__ = "comentarios"
    id = Column(Integer, primary_key=True)
    texto = Column(Text, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"))
    comentario_padre_id = Column(Integer, ForeignKey("comentarios.id"), nullable=True)
    activo = Column(Boolean, default=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="comentarios")
    proyecto = relationship("Proyecto", back_populates="comentarios")
