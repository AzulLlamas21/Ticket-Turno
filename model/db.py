from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/ticket'

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

def init_db():
    import model.package_model.Nivel  
    import model.package_model.Asunto
    import model.package_model.Municipio
    import model.package_model.Formulario
    import model.package_model.Usuario
    Base.metadata.create_all(bind=engine)

def get_bd():
    bd = SessionLocal()
    try:
        yield bd
    finally:
        bd.close()