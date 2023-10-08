from typing import List
from uuid import uuid4
from models import User,Gender,Role
db:List[User]=[
    User(
        id=uuid4(),
        first_name="Murad",
        last_name="Mammadzada",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name="Soap",
        last_name="Mactavish",
        gender=Gender.male,
        roles=[Role.student,Role.user]
    ),
]