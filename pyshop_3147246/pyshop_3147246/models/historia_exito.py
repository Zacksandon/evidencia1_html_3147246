from sqlalchemy import Column, Integer, String, Text, DateTime, DECIMAL, Boolean, ForeignKey
from datetime import datetime
from db import Base

class HistoriaExito(Base):
    __tablename__ = "historias_exito"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=False)
    logros_alcanzados = Column(Text)
    lecciones_aprendidas = Column(Text)
    consejos = Column(Text)
    imagen_url = Column(String(300))
    video_url = Column(Text)
    impacto_social = Column(Text)
    ingresos_generados = Column(DECIMAL(15, 2))
    empleos_creados = Column(Integer, default=0)
    destacada = Column(Boolean, default=False)
    fecha_publicacion = Column(DateTime, default=datetime.utcnow)
