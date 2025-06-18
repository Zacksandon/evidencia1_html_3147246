from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Proyecto(Base):
    __tablename__ = "proyectos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=False)
    problema_que_resuelve = Column(Text)
    solucion_propuesta = Column(Text)
    mercado_objetivo = Column(Text)
    modelo_negocio = Column(Text)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    etapa = Column(Enum("idea", "prototipo", "mvp", "lanzado", "escalando", name="etapa_proyecto"), default="idea")
    presupuesto_requerido = Column(DECIMAL(15, 2))
    presupuesto_recaudado = Column(DECIMAL(15, 2), default=0.00)
    imagen_principal = Column(String(300))
    video_pitch = Column(String(300))
    sitio_web = Column(String(200))
    repositorio_github = Column(String(200))
    estado = Column(Enum("activo", "pausado", "completado", "cancelado", name="estado_proyecto"), default="activo")
    visibilidad = Column(Enum("publico", "privado", "borrador", name="visibilidad_proyecto"), default="publico")
    fecha_publicacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="proyectos")
    categoria = relationship("Categoria", back_populates="proyectos")
    reacciones = relationship("Reaccion", back_populates="proyecto")
    comentarios = relationship("Comentario", back_populates="proyecto")
    alianzas = relationship("ProyectoAlianza", back_populates="proyecto")
