from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from db import Base

class Seguimiento(Base):
    __tablename__ = "seguimientos"
    id = Column(Integer, primary_key=True)
    seguidor_id = Column(Integer, ForeignKey("usuarios.id"))
    seguido_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha_seguimiento = Column(DateTime, default=datetime.utcnow)

    seguidor = relationship("Usuario", foreign_keys=[seguidor_id], back_populates="seguimientos")
    seguido = relationship("Usuario", foreign_keys=[seguido_id], back_populates="seguidores")

