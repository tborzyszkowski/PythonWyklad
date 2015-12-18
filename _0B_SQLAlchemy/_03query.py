# -*- coding: utf-8 -*-

from user_alch import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()

#
# przykłady prostych zapytań
#
print "-------- Id sorted ------------"
for instance in session.query(User).order_by(User.id):
    print instance.name, instance.fullname

print "-------- ORM instrumented ------------"
for name, fullname in session.query(User.name, User.fullname):
    print name, fullname

print "-------- named tuples ------------"
# patrz klasa KeyedTuple
for row in session.query(User, User.name).all():
    print row.User, row.name

#
# Zobacz opratory filtrowania:
# http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#common-filter-operators
#

#################################
# Zadanie
# Dla bazy wycen społki Lotos wykonaj zapytanie wypisujące wybrane kolumny
