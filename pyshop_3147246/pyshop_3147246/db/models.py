from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# Tabla: Usuarios
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


# Tabla: Categorías
class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(Text)
    icono = Column(String(100))
    color = Column(String(7), default="#007bff")
    activa = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    proyectos = relationship("Proyecto", back_populates="categoria")


# Tabla: Proyectos
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


# Tabla: Reacciones
class Reaccion(Base):
    __tablename__ = "reacciones"
    id = Column(Integer, primary_key=True)
    tipo = Column(Enum("me_gusta", "me_encanta", "me_interesa", "apoyo", "quiero_colaborar", name="tipo_reaccion"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"))
    fecha = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="reacciones")
    proyecto = relationship("Proyecto", back_populates="reacciones")


# Tabla: Comentarios
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


# Tabla: Eventos
class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime)
    modalidad = Column(Enum("virtual", "presencial", "hibrido", name="modalidad_evento"))
    ubicacion_fisica = Column(String(200))
    enlace = Column(String(300))
    capacidad_maxima = Column(Integer)
    precio = Column(DECIMAL(10, 2), default=0.00)
    organizador_id = Column(Integer, ForeignKey("usuarios.id"))
    imagen_evento = Column(String(300))
    estado = Column(Enum("programado", "en_curso", "finalizado", "cancelado", name="estado_evento"), default="programado")
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    inscripciones = relationship("InscripcionEvento", back_populates="evento")


# Tabla: Inscripciones a eventos
class InscripcionEvento(Base):
    __tablename__ = "inscripciones_evento"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    evento_id = Column(Integer, ForeignKey("eventos.id"))
    estado_inscripcion = Column(Enum("inscrito", "confirmado", "asistio", "no_asistio", "cancelado", name="estado_inscripcion"), default="inscrito")
    fecha_inscripcion = Column(DateTime, default=datetime.utcnow)
    notas = Column(Text)

    usuario = relationship("Usuario", back_populates="inscripciones")
    evento = relationship("Evento", back_populates="inscripciones")


# Tabla: Alianzas de proyectos
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


# Tabla: Recursos educativos
class Recurso(Base):
    __tablename__ = "recursos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=False)
    tipo = Column(Enum("guía", "herramienta", "curso", "plantilla", "ebook", "webinar", "podcast", name="tipo_recurso"), nullable=False)
    categoria = Column(String(100), nullable=False)
    enlace = Column(Text)
    archivo_url = Column(String(300))
    autor = Column(String(100))
    duracion_minutos = Column(Integer)
    nivel = Column(Enum("principiante", "intermedio", "avanzado", name="nivel_recurso"), default="principiante")
    calificacion = Column(DECIMAL(3, 2), default=0.00)
    numero_descargas = Column(Integer, default=0)
    gratuito = Column(Boolean, default=True)
    precio = Column(DECIMAL(10, 2))
    activo = Column(Boolean, default=True)
    fecha_publicacion = Column(DateTime, default=datetime.utcnow)


# Tabla: Cursos
class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=False)
    url = Column(Text)
    instructor = Column(String(100))
    duracion = Column(String(50))
    plataforma = Column(String(100))
    categoria = Column(String(100))
    nivel = Column(Enum("principiante", "intermedio", "avanzado", name="nivel_curso"), default="principiante")
    precio = Column(DECIMAL(10, 2), default=0.00)
    calificacion = Column(DECIMAL(3, 2), default=0.00)
    estudiantes_inscritos = Column(Integer, default=0)
    idioma = Column(String(50), default="Español")
    certificado = Column(Boolean, default=False)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)


# Tabla: Plantillas
class Plantilla(Base):
    __tablename__ = "plantillas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=False)
    url = Column(Text)
    archivo_url = Column(String(300))
    categoria = Column(String(100), nullable=False)
    tipo_archivo = Column(Enum("pdf", "docx", "xlsx", "pptx", "html", "zip", name="tipo_archivo_plantilla"), default="pdf")
    tamaño_kb = Column(Integer)
    descargas = Column(Integer, default=0)
    calificacion = Column(DECIMAL(3, 2), default=0.00)
    gratuito = Column(Boolean, default=True)
    precio = Column(DECIMAL(10, 2))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)


# Tabla: Historias de éxito
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


# Tabla: Mensajes de soporte
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


# Tabla: Notificaciones
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


# Tabla: Seguimientos entre usuarios
class Seguimiento(Base):
    __tablename__ = "seguimientos"
    id = Column(Integer, primary_key=True)
    seguidor_id = Column(Integer, ForeignKey("usuarios.id"))
    seguido_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha_seguimiento = Column(DateTime, default=datetime.utcnow)

    seguidor = relationship("Usuario", foreign_keys=[seguidor_id], back_populates="seguimientos")
    seguido = relationship("Usuario", foreign_keys=[seguido_id], back_populates="seguidores")
