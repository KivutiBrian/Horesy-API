from configurations.sqlalchemy_config import Base, get_db
from sqlalchemy.orm import Session

class Model(Base):

    @classmethod
    def fetch_all(cls, db: Session):
        """select all records"""
        return db.query(cls).all()


    def create(self, db:Session):
        """insert a new record"""
        db.add(self)
        db.commit()
        return self


    
        
        
        
