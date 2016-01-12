import unittest
from social_network import SocialNetwork
from panda import Panda


class TestSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.pandabook = SocialNetwork()
        self.ruja = Panda('Ruja', 'ruja@pandamail.com', 'female')
        self.martin = Panda('Martin', 'martin@pandamail.com', 'male')

    def test_social_network_add_panda(self):
        self.pandabook.add_panda(self.ruja)

        self.assertEqual(self.pandabook._get_graph()[self.ruja], set())

    def test_social_network_has_panda(self):
        self.pandabook.add_panda(self.martin)

        self.assertTrue(self.pandabook.has_panda(self.martin))
        self.assertFalse(self.pandabook.has_panda(self.ruja))

    def test_social_network_make_friends(self):
        self.pandabook.make_friends(self.ruja, self.martin)

        self.assertEqual(self.pandabook._get_graph()[self.ruja], {self.martin})
        self.assertEqual(self.pandabook._get_graph()[self.martin], {self.ruja})

    def test_social_netowrk_connection_level(self):
        random = Panda("Random", "random@pandamail.com", "male")
        random1 = Panda("Random1", "random1@pandamail.com", "male")
        random2 = Panda("Random2", "random2@pandamail.com", "female")
        random3 = Panda("Random3", "random3@pandamail.com", "female")

        self.pandabook.make_friends(self.ruja, self.martin)
        self.pandabook.make_friends(self.ruja, random)
        self.pandabook.make_friends(self.martin, random1)
        self.pandabook.make_friends(self.martin, random2)
        self.pandabook.make_friends(random, random3)
        
        self.assertEqual(self.pandabook.connection_level(self.ruja, random3), 2)

        random_gay = Panda("RandomGay", "randomgay@pandamail.com", "female")
        self.pandabook.add_panda(random_gay)

        self.assertEqual(self.pandabook.connection_level(self.ruja, random_gay), -1)

    def test_social_network_are_connected(self):
        gosho = Panda("Gosho", "gosho@pandamail.com", "male")
        krasi = Panda("Krasi", "krasi@pandamail.com", "female")

        self.pandabook.make_friends(self.ruja, self.martin)
        self.pandabook.make_friends(self.martin, gosho)

        self.assertTrue(self.pandabook.are_connected(self.ruja, gosho))

        self.assertFalse(self.pandabook.are_connected(self.ruja, krasi))

    def test_social_network_how_many_gender_in_network(self):
        random = Panda("Random", "random@pandamail.com", "male")
        random1 = Panda("Random1", "random1@pandamail.com", "male")
        random2 = Panda("Random2", "random2@pandamail.com", "female")
        random3 = Panda("Random3", "random3@pandamail.com", "female")

        self.pandabook.make_friends(self.ruja, self.martin)
        self.pandabook.make_friends(self.ruja, random)
        self.pandabook.make_friends(self.martin, random1)
        self.pandabook.make_friends(self.martin, random2)
        self.pandabook.make_friends(random, random3)

        self.assertEqual(self.pandabook.how_many_gender_in_network(1, self.ruja, "male"), 2)
        self.assertEqual(self.pandabook.how_many_gender_in_network(1, self.ruja, "female"), 1)
        self.assertEqual(self.pandabook.how_many_gender_in_network(2, self.ruja, "male"), 3)


if __name__ == '__main__':
    unittest.main()
