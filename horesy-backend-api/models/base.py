from configurations.sqlalchemy_config import Base
from sqlalchemy.orm import Session

class Model:

    @classmethod
    def fetch_all(cls, db: Session):
        """select all records"""
        return db.query(cls).all()


    def create(self, db:Session):
        """insert a new record"""
        db.add(self)
        db.commit()
        return self


    
        
        
        
