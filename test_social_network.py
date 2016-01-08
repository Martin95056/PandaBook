import unittest
from social_network import SocialNetwork
from panda import Panda


class TestSocialNetwork(unittest.TestCase):

	def test_social_network_add_panda(self):
		pandabook = SocialNetwork()
		ruja = Panda('Ruja', 'ruja@pandamail.com', 'female')
		pandabook.add_panda(ruja)

		self.assertEqual(pandabook._get_graph()[ruja], set())

	def test_social_network_has_panda(self):
		pandabook = SocialNetwork()
		ruja = Panda('Ruja', 'ruja@pandamail.com', 'female')
		martin = Panda('Martin', 'martin@pandamail.com', 'male')
		pandabook.add_panda(martin)

		self.assertTrue(pandabook.has_panda(martin))
		self.assertFalse(pandabook.has_panda(ruja))

	def test_social_network_make_friends(self):
		pandabook = SocialNetwork()
		ruja = Panda('Ruja', 'ruja@pandamail.com', 'female')
		martin = Panda('Martin', 'martin@pandamail.com', 'male')

		pandabook.make_friends(ruja, martin)
		self.assertEqual(pandabook._get_graph()[ruja], {martin})
		self.assertEqual(pandabook._get_graph()[martin], {ruja})


if __name__ == '__main__':
	unittest.main()
