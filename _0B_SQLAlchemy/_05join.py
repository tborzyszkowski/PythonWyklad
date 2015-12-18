# -*- coding: utf-8 -*-

from user_address_alch import *
from sqlalchemy.orm import sessionmaker, aliased


Session = sessionmaker(bind = engine)
session = Session()
#################################################

#
# primitywny join
#
for u, a in session.query(User, Address).\
                filter(User.id==Address.user_id).\
                filter(Address.email_address=='jack@google.com').\
                all():
    print(u)
    print(a)

#
# join wykorzystujący ForeignKey
#
print session.query(User).join(Address).\
        filter(Address.email_address=='jack@google.com').\
        all()

print "###############################################"
print session.query(User).join(Address, User.id==Address.user_id)    # explicit condition
print session.query(User).join(User.addresses)                       # specify relationship from left to right
print session.query(User).join(Address, User.addresses)              # same, with explicit target
print session.query(User).join('addresses')                          # same, using a string

print session.query(User).outerjoin(User.addresses)
print session.query(User, Address).select_from(Address).join(User)
print "###############################################"


#
# aliasy do powtarzających się tabel
#
adalias1 = aliased(Address)
adalias2 = aliased(Address)
for username, email1, email2 in \
        session.query(User.name, adalias1.email_address, adalias2.email_address).\
        join(adalias1, User.addresses).\
        join(adalias2, User.addresses).\
        filter(adalias1.email_address=='jack@google.com').\
        filter(adalias2.email_address=='j25@yahoo.com'):
     print(username, email1, email2)


#################################
# Zadanie
# Dla tabel z poprzenich zadań napisz zapytanie zliczające dla każdej
# dla każdej społki liczbę jej notowań w tabeli notowań.
