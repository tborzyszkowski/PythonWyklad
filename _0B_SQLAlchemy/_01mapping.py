# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine

if __name__ == '__main__':
    print "Wersja biblioteki:", sqlalchemy.__version__

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///baza.db', echo=False)

if __name__ == '__main__':
    print "#"
    print "# Model deklaratywny"
    print "#"

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)


if __name__ == '__main__':
    #print dir(User)
    print User.__table__.__repr__
    print User.__table__

Base.metadata.create_all(engine)

#
# Sprawdź używając SQLite Managera co powstało w bazie
#
if __name__ == '__main__':
    print "---- Tworzenie instancji ----------"

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
if __name__ == '__main__':
    print ed_user.id, ed_user.name, ed_user.fullname, ed_user.password

#
# Dlaczego 'id' jest puste ???
#
