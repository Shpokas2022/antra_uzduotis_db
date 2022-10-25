from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///db/asmens_kortele.db')
Base = declarative_base()

class Supply_action(Base):
    __tablename__ = "supply_action"
    id = Column(Integer, primary_key=True)
    status_id = Column("status_id", Integer, ForeignKey("status.id"))
    person_id = Column("person_id", Integer, ForeignKey("person.id"))
    helmet_id = Column("hekmet_id", Integer, ForeignKey("clothing.id"))
    jacket_id = Column("jacket_id", Integer, ForeignKey("clothing.id"))
    pants_id = Column("pants_id", Integer, ForeignKey("clothing.id"))
    shoes_id = Column("shoes_id", Integer, ForeignKey("clothing.id"))
    
    person = relationship("Person", back_populates="supply_action")
    # person = relationship("Person", foreign_keys=[person_id])
    clothing = relationship("Clothing", back_populates="supply_action")
    status = relationship("Status", back_populates="supply_actions")


    def __repr__(self):
        return f"({self.id})"

class Clothing(Base):
    __tablename__ = "clothing"
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)
    size = Column("Dydis", String)
    type_id = Column("type_id", Integer, ForeignKey("clothing_type.id"))
    clothing_types = relationship("Clothing_type", back_populates="clothing")
    supply_actions = relationship("Supply_action", back_populates="clothing")

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.size})"

class Clothing_type(Base):
    __tablename__ = "clothing_type"
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)
    clothing = relationship("Clothing", back_populates="clothing_types")
    
    def __repr__(self):
        return f"({self.id}, {self.name})"

class Status (Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)
    supply_actions = relationship("Supply_action", back_populates="status")

    def __repr__(self):
        return f"({self.id}, {self.name})"

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    f_name = Column("Vardas", String)
    s_name = Column("Pavarde", String)
    personal_id = Column("Asmens_kodas", Integer)
    phone = Column("Telefonas", String)
    e_mail = Column("El.paštas", String)

    supply_action = relationship("Supply_action", back_populates="person")

    def __repr__(self):
        return f"({self.id}, {self.f_name}, {self.s_name}, {self.personal_id}, {self.phone}, {self.e_mail})"

if __name__ == "__main__":
    Base.metadata.create_all(engine)