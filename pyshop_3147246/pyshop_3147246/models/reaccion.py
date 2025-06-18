from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Reaccion(Base):
    __tablename__ = "reacciones"
    id = Column(Integer, primary_key=True)
    tipo = Column(Enum("me_gusta", "me_encanta", "me_interesa", "apoyo", "quiero_colaborar", name="tipo_reaccion"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"))
    fecha = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="reacciones")
    proyecto = relationship("Proyecto", back_populates="reacciones")
