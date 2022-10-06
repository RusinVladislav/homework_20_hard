from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_d):
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, gid):
        try:
            genre = self.get_one(gid)
            self.session.delete(genre)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, genre_d):

        try:
            genre = self.get_one(genre_d.get("id"))
            genre.name = genre_d.get("name")

            self.session.add(genre)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
