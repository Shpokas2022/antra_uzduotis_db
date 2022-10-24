from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///db/asmens_kortele.db')
Base = declarative_base()

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    f_name = Column("Vardas", String)
    s_name = Column("Pavarde", String)
    personal_id = Column("Asmens_kodas", Integer)
    phone = Column("Telefonas", String)
    e_mail = Column("El.paštas", String)
    accounts = relationship("Account", back_populates="person")
    relatives = relationship("Relative", back_populates="person")
    clothings = relationship("Clothing", back_populates="person")

    def __repr__(self):
        return f"({self.id}, {self.f_name}, {self.s_name}, {self.personal_id}, {self.phone}, {self.e_mail})"

class Relative(Base):
    __tablename__ = "relative"
    id = Column(Integer, primary_key=True)
    f_name = Column("Vardas", String)
    s_name = Column("Pavarde", String)
    relative_kind = Column("Giminystės ryšys", String)
    phone = Column("Telefonas", String)
    e_mail = Column("El.paštas", String)
    real_id = Column("real_id", Integer, ForeignKey("person.id"))
    person = relationship("Person", back_populates="relatives")

    def __repr__(self):
        return f"({self.id}, {self.f_name}, {self.s_name}, {self.relative_kind}, {self.phone}, {self.e_mail})"

class Clothing(Base):
    id = Column(Integer, primary_key=True)
    jacket = Column("Striuke", String)
    pants = Column("Kelnes", String)
    shoes = Column("batai", String)
    person_id = Column("person_id", Integer, ForeignKey("person.id"))
    person = relationship("Person", back_populates="clothings")

    def __repr__(self):
        return f"({self.id}, {self.jacket}, {self.pants}, {self.shoes})"

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    iban = Column("Saskaita", String)
    name = Column("Pavadinimas", String)
    # ForeignKey veda į lentelės pavadinimą
    person_id = Column("person_id", Integer, ForeignKey("person.id"))
    bank_id = Column("bank_id", Integer, ForeignKey('bank.id')) 
# Relationship veda į objekto pavadinimą
    person = relationship("Person", back_populates="accounts")
    bank = relationship("Bank", back_populates="accounts")
    
    def __repr__(self):
        return f"({self.id}, {self.iban}, {self.name})"


class Bank(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True)
    bank_name = Column("Pavadinimas", String)
    address = Column("Adresas", String)
    banko_code = Column("Kodas", String, nullable=True)
    swift = Column("SWIFT", String, nullable=True)
    accounts = relationship("Account", back_populates="bank")

    def __repr__(self):
        return f"({self.id}, {self.bank_name}, {self.banko_code}, {self.swift}, {self.address})"

if __name__ == "__main__":
    Base.metadata.create_all(engine)