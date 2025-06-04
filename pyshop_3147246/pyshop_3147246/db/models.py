from .database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

# Tabla: Usuarios
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    correo = Column(String(100), unique=True)
    password = Column(String(100))
    rol = Column(Enum("emprendedor", "administrador", name="rol_usuario"))
    ubicacion = Column(String(100))
    bio = Column(Text)
    habilidades = Column(Text)
    fecha_registro = Column(DateTime, default=datetime.utcnow)

    proyectos = relationship("Proyecto", back_populates="usuario")
    reacciones = relationship("Reaccion", back_populates="usuario")
    comentarios = relationship("Comentario", back_populates="usuario")
    inscripciones = relationship("InscripcionEvento", back_populates="usuario")

# Tabla: Proyectos
class Proyecto(Base):
    __tablename__ = "proyectos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(150))
    descripcion = Column(Text)
    categoria = Column(String(50))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha_publicacion = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="proyectos")
    reacciones = relationship("Reaccion", back_populates="proyecto")
    comentarios = relationship("Comentario", back_populates="proyecto")

# Tabla: Reacciones
class Reaccion(Base):
    __tablename__ = "reacciones"
    id = Column(Integer, primary_key=True)
    tipo = Column(Enum("me_gusta", "me_encanta", "me_interesa", "apoyo", name="tipo_reaccion"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"))
    fecha = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="reacciones")
    proyecto = relationship("Proyecto", back_populates="reacciones")

# Tabla: Comentarios
class Comentario(Base):
    __tablename__ = "comentarios"
    id = Column(Integer, primary_key=True)
    texto = Column(Text)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"))
    fecha = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="comentarios")
    proyecto = relationship("Proyecto", back_populates="comentarios")

# Tabla: Eventos
class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    descripcion = Column(Text)
    fecha = Column(DateTime)
    modalidad = Column(Enum("virtual", "presencial", name="modalidad_evento"))
    enlace = Column(String(200))

    inscripciones = relationship("InscripcionEvento", back_populates="evento")

# Tabla: Inscripción a eventos
class InscripcionEvento(Base):
    __tablename__ = "inscripciones_evento"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    evento_id = Column(Integer, ForeignKey("eventos.id"))
    fecha_inscripcion = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="inscripciones")
    evento = relationship("Evento", back_populates="inscripciones")
