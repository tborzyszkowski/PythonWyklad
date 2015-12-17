# -*- coding: utf-8 -*-

from _01mapping import *
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind = engine)
session = Session()
print "\nSession class:\n", Session
#print "\nsession object:\n",dir(session)

# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
session.add(ed_user)
print "ed_user.id:", ed_user.id

session.add_all([
        User(name='wendy', fullname='Wendy Williams', password='foobar'),
        User(name='mary', fullname='Mary Contrary', password='xxg527'),
        User(name='fred', fullname='Fred Flinstone', password='blah')])
ed_user.password = 'f8s7ccs'

print "session.dirty: ", session.dirty
print "session.new:", session.new
print "before commit: ed_user.id: ", ed_user.id
#session.commit()
print "after  commit: ed_user.id: ", ed_user.id

#
# proste zapytanie
#

our_user = session.query(User).filter_by(name='ed').first()
print our_user, ed_user is our_user

#
# Rolling Back
#
print "--------- Rolling Back -----------"
print ed_user
ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
session.add(fake_user)
qr = session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
print "Before rollback:", qr

session.rollback()
print "After rollback:", ed_user.name, fake_user in session

qr = session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()
print "Query result:", qr


#
# Zobacz stany obiektwow w sesji (Transient, Pending, Persistent, Detached):
#    http://docs.sqlalchemy.org/en/rel_1_0/orm/session_state_management.html#session-object-states
#
