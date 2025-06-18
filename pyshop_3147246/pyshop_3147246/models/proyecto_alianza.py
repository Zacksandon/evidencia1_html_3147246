from sqlalchemy import Column, Integer, Text, DateTime, Enum, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class ProyectoAlianza(Base):
    __tablename__ = "proyecto_alianzas"
    id = Column(Integer, primary_key=True)
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"))
    participante_id = Column(Integer, ForeignKey("usuarios.id"))
    rol_alianza = Column(Enum("colaborador", "asesor", "inversor", "socio", name="rol_alianza"), default="colaborador")
    porcentaje_participacion = Column(DECIMAL(5, 2))
    descripcion_rol = Column(Text)
    fecha_propuesta = Column(DateTime, default=datetime.utcnow)
    fecha_respuesta = Column(DateTime)
    estado = Column(Enum("pendiente", "aceptada", "rechazada", "finalizada", name="estado_alianza"), default="pendiente")

    proyecto = relationship("Proyecto", back_populates="alianzas")
    participante = relationship("Usuario", back_populates="alianzas_participadas")