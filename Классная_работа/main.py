from data import db_session
from flask import Flask
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = "21"
    user.position = "captain"
    user.speciality = "research enginee"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    app.run()


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Karim"
    user.name = "Islyamov"
    user.age = "12"
    user.position = "Programmist"
    user.speciality = "Bezdelnik"
    user.address = "Kirpichka_231"
    user.email = "BigKarim@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    app.run()


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Matvei"
    user.name = "Molenov"
    user.age = "16"
    user.position = "MCtraher"
    user.speciality = "SYSAdmin"
    user.address = "pppp_1"
    user.email = "qwerty123123@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    app.run()

if __name__ == '__main__':
    main()