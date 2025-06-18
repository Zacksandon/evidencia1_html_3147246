from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    telefono = Column(String(20))
    rol = Column(Enum("emprendedor", "administrador", "mentor", "inversor", name="rol_usuario"), default="emprendedor")
    ubicacion = Column(String(150))
    bio = Column(Text)
    habilidades = Column(Text)
    experiencia_años = Column(Integer, default=0)
    sitio_web = Column(String(200))
    linkedin = Column(String(200))
    foto_perfil = Column(String(300))
    verificado = Column(Boolean, default=False)
    activo = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_ultima_actividad = Column(DateTime, default=datetime.utcnow)

    proyectos = relationship("Proyecto", back_populates="usuario")
    reacciones = relationship("Reaccion", back_populates="usuario")
    comentarios = relationship("Comentario", back_populates="usuario")
    inscripciones = relationship("InscripcionEvento", back_populates="usuario")
    alianzas_participadas = relationship("ProyectoAlianza", back_populates="participante")
    mensajes_soporte = relationship("MensajeSoporte", back_populates="usuario")
    notificaciones = relationship("Notificacion", back_populates="usuario")
    seguimientos = relationship("Seguimiento", foreign_keys='Seguimiento.seguidor_id', back_populates="seguidor")
    seguidores = relationship("Seguimiento", foreign_keys='Seguimiento.seguido_id', back_populates="seguido")
