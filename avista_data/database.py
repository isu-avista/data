from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = None
db = None

Base = declarative_base()
metadata = Base.metadata

import avista_data.user as usr

def init(uri):
    global db
    global engine
    global SessionLocal
    global metadata
    engine = create_engine(uri, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    metadata.create_all(bind=engine)
    db = SessionLocal()
    print(db)
    print(metadata)


def populate_initial_data():
    # if "Users" not in metadata.tables:
    global db
    metadata.create_all(bind=engine)

    if db is not None and db.query(usr.User).count() == 0:
        admin = usr.User()
        db.add(admin)
        usr.User.admin_account_details(admin)
        db.commit()


def clear_data():
    db.close()
    global metadata
    Base.metadata.drop_all(bind=engine)
