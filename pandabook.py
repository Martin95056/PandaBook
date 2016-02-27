from panda import Panda
from social_network import SocialNetwork


def main():
    pandabook = SocialNetwork()
    martin = Panda("Martin", "martin@pandamail.com", "male")
    rado = Panda("Rado", "rado@pandamail.com", "male")
    lubo = Panda("Lubo", "lubo@pandamail.com", "male")
    dimitar = Panda("Dimitar", "dimitar@pandamail.com", "male")
    stanislav = Panda("Stanislav", "stanislav@pandamail.com", "male")
    denitsa = Panda("Denitsa", "denitsa@pandamail.com", "female")
    zornitsa = Panda("Zornitsa", "zornitsa@pandamail.com", "female")
    iva = Panda("Iva", "iva@pandamail.com", "female")
    dora = Panda("Dora", "dora@pandamail.com", "female")
    aneliya = Panda("Aneliya", "aneliya@pandamail.com", "female")

    pandabook.make_friends(martin, lubo)
    pandabook.make_friends(martin, rado)
    pandabook.make_friends(rado, denitsa)
    pandabook.make_friends(rado, dimitar)
    pandabook.make_friends(denitsa, zornitsa)
    pandabook.make_friends(denitsa, iva)
    pandabook.make_friends(denitsa, dora)
    pandabook.make_friends(lubo, dimitar)
    pandabook.make_friends(lubo, stanislav)
    pandabook.make_friends(stanislav, aneliya)

    pandabook.save()


if __name__ == '__main__':
    main()
