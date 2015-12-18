# -*- coding: utf-8 -*-

from user_alch import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Session = sessionmaker(bind = engine)
session = Session()
#################################################


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

User.addresses = relationship(
    "Address", order_by=Address.id, back_populates="user")

Base.metadata.create_all(engine)

#
# Dodawanie adresow
#

jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
print "jack.addresses:        ", jack.addresses

jack.addresses = [
        Address(email_address='jack@google.com'),
        Address(email_address='j25@yahoo.com')]
print "jack.addresses[1]:     ", jack.addresses[1]
print "jack.addresses[1].user:", jack.addresses[1].user

#
# zapisz
#
#session.add(jack)
#session.commit()

#
# Zapytania
#
jack = session.query(User).filter_by(name='jack').one()
print "jack:", jack
print "jack.addresses", jack.addresses

#################################
# Zadanie
# Zaprojektuj tabelę opisującą daną społkę giełdową.
# Powiąż tę tabelę z tabelą kursow akcji z poprzednich zadań.
