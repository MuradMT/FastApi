from enum import Enum
from typing import Optional,List
from uuid import UUID, uuid4
from pydantic import BaseModel
# private attributes - __some __ indicates the attribute access modifier
class Gender(str,Enum): # python have multiple inheritance at the same time
    male="male"
    female="female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student="student"
class User(BaseModel): # python inheritance syntax
    id:Optional[UUID]=uuid4() #id is attribute(we say it property)
    #optional means you can give it or not and type will be uuid(or we say guid)
    #x:str-this is type annotation in python
    first_name:str
    last_name: str
    middle_name: Optional[str]
    gender:Gender
    roles:List[Role]