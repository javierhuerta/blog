from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'postgres://hqzywnlmociqux:'
    '864343d9c0c4884e4026c78be4819d1e8b789f3ed16f460bdf258d93ccb3d5b1@'
    'ec2-54-225-70-53.compute-1.amazonaws.com:5432/d76ur6jvtbdjt0',
    convert_unicode=True
)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import application.models
    Base.metadata.create_all(bind=engine)