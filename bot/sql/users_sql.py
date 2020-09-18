""" users Table """

from sqlalchemy import (
    Column,
    String,
    Integer
)
from . import (
    SESSION,
    BASE
)


class Users(BASE):
    """ Table to store the received messages """
    __tablename__ = "users"
    chat_id = Column(Integer, primary_key=True)
    f_name = Column(String(256))
    usname = Column(String(256))

    def __init__(self, chat_id, f_name, usname):
        self.chat_id = int(chat_id)  # ensure string
        self.f_name = f_name
        self.usname = usname

    def __repr__(self):
        return "<User(chat_id={}, f_name={}, usname={})>".format(self.chat_id, self.f_name, self.usname)


Users.__table__.create(checkfirst=True)


def add_user_to_db(chat_id, f_name, usname):
    """ add the message to the table """
    __user = Users(int(chat_id), f_name, usname)
    SESSION.add(__user)
    SESSION.commit()
    SESSION.close()

def check_user_in_db(chat_id):
    r = SESSION.query(Users).filter_by(chat_id=chat_id).first()
    if r == []:
        pp = False
    else:
        pp = True
