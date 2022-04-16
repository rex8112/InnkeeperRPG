from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase

from .player import Player
from .world import World


class PlayerTest(TestCase):
    def test_creation(self):
        """
        Test that a player can be created.
        """
        user = User.objects.create_user('john', 'john@test.com', 'johnpassword')
        world = settings.world
        player = Player(world, user)
        self.assertEqual(player.user, user)
        self.assertEqual(player.name, 'New Player')
        self.assertEqual(player.settings, {})
        self.assertEqual(player.flags, [])
        self.assertEqual(player.characters, {})
        self.assertEqual(player.world, world)

        player.save()
        self.assertEqual(player.user.id, user.id)

    def test_load(self):
        """
        Test that a player can be loaded.
        """
        user = User.objects.create_user('john', 'john@test.com', 'johnpassword')
        world = settings.world
        player = Player(world, user)
        player.save()

        player = Player.load(world, user)
        self.assertEqual(player.user, user)
        self.assertEqual(player.name, 'New Player')
        self.assertEqual(player.settings, {})
        self.assertEqual(player.flags, [])
        self.assertEqual(player.characters, {})
        self.assertEqual(player.world, world)
