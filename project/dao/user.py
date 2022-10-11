from sqlalchemy.orm.scoping import scoped_session

from project.dao.models import User


class UserDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk):
        return self._db_session.query(User).filter(User.id == pk).one_or_none()

    def get_by_email(self, email):
        return self._db_session.query(User).filter(User.email == email).one_or_none()

    def get_all(self):
        return self._db_session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent


    def update(self, user_d):
        user = self.get_by_id(user_d.get('id'))
        if user:
            if user_d.get('password'):
                user.password = user_d.get('password')
            if user_d.get('email'):
                user.email = user_d.get('email')
            if user_d.get('name'):
                user.name = user_d.get('name')
            if user_d.get('surname'):
                user.surname = user_d.get('surname')
            if user_d.get('favorite_genre'):
                user.favorite_genre = user_d.get('favorite_genre')

        self._db_session.add(user)
        self._db_session.commit()


