from fastapi import HTTPException
from sqlalchemy.orm import Session
import uuid
# model
from models.role import Role
# schema 
from schema import role

class RoleService:
    
    @classmethod
    def get_roles(cls,db:Session):
        """return a list of all roles"""
        return db.query(Role).all()

    @classmethod
    def get_role(cls,role_public_id:str,db:Session):
        """return a role that matches the roleId provided"""
        # check if role exists and raise an exception if none exists
        role: role_schema.Role = db.query(Role).filter(Role.public_id == role_public_id).first()
        if not role:
            raise HTTPException(detail=f"Could not find role that matches id {role_public_id}", status_code=404)
        return role

    @classmethod
    def create_new_role(cls,roleData:role.RolePost, db:Session):
        """create a new role"""
        # check if role name provided exists
        role: role.Role = db.query(Role).filter(Role.name == roleData.name).first()
        if role:
            raise HTTPException(detail=f"{roleData.name} role already exists", status_code=400)
        # add the record to the database
        record = Role(
            pid = str(uuid.uuid4()),
            name = roleData.name.title(),
            description = roleData.description
        )
        # insert record and commit to the database
        db.add(record)
        db.commit()
        db.refresh(record)
        # return the created role
        return record

    @classmethod
    def update_role_details(cls,role_public_id: str, roleData: role.RolePut, db: Session):
        """update role details"""
        role: role.Role = db.query(Role).filter(Role.public_id == role_public_id).first()
        if not role:
            raise HTTPException(detail=f"Could not find role that matches id {role_public_id}", status_code=404)

        role.name = roleData.name
        role.description = roleData.description
        # update the changes
        db.commit()
        db.refresh(role)
        # return the updated role
        return role