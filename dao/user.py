from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        try:
            user = self.get_one(uid)
            self.session.delete(user)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, user_d):

        try:
            user = self.get_one(user_d.get("id"))
            user.username = user_d.get("username")
            user.password = user_d("password")
            user.role = user_d("role")

            self.session.add(user)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
