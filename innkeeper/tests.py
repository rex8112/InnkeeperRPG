from django.contrib.auth.models import User
from django.test import TestCase

from .world import World
from .player import Player

class PlayerTest(TestCase):
    def test_creation(self):
        """
        Test that a player can be created.
        """
        user = User.objects.create_user('john', 'john@test.com', 'johnpassword')
        world = World('Test World', 1)
        player = Player(world, 1)
        player.user = user
        self.assertEqual(player.id, 1)
        self.assertEqual(player.name, 'New Player')
        self.assertEqual(player.settings, {})
        self.assertEqual(player.flags, [])
        self.assertEqual(player.characters, {})
        self.assertEqual(player.world, world)

        player.save()
        self.assertEqual(player.entry.id, 1)

    def test_load(self):
        """
        Test that a player can be loaded.
        """
        user = User.objects.create_user('john', 'john@test.com', 'johnpassword')
        world = World('Test World', 1)
        player = Player(world, 1)
        player.user = user
        player.save()

        player = Player.load(world, 1)
        self.assertEqual(player.id, 1)
        self.assertEqual(player.name, 'New Player')
        self.assertEqual(player.settings, {})
        self.assertEqual(player.flags, [])
        self.assertEqual(player.characters, {})
        self.assertEqual(player.world, world)