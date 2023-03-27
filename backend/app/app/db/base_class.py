from sqlalchemy.ext.declarative import declared_attr, as_declarative
from typing import Any

@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate tablename automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

