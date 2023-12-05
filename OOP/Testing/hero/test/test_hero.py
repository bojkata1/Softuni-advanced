import unittest
from project.hero import Hero


class HeroTests(unittest.TestCase):
    username = "TestUser"
    level = 2
    hp = 2
    dmg = 2

    def setUp(self):
        self.test_hero = Hero(self.username, self.level, self.hp, self.dmg)
        self.test_enemy = Hero("Enemy", 2, 1, 1)

    def test_init(self):
        self.assertEqual(self.username, self.test_hero.username)
        self.assertEqual(self.level, self.test_hero.level)
        self.assertEqual(self.hp, self.test_hero.health)
        self.assertEqual(self.dmg, self.test_hero.damage)

    def test_enemy_same_name(self):
        self.test_enemy.username = self.test_hero.username
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(self.test_enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_bellow_zero_health_raised(self):
        self.test_hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(self.test_enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_enemy_hero_bellow_zero_health_raised(self):
        self.test_enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(self.test_enemy)
        self.assertEqual(f"You cannot fight {self.test_enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_stats_change_hero_win(self):
        self.test_hero.health = 3
        self.assertEqual("You win", self.test_hero.battle(self.test_enemy))

        self.assertEqual(6, self.test_hero.health)
        self.assertEqual(7, self.test_hero.damage)
        self.assertEqual(3, self.test_hero.level)

        self.assertEqual(-3, self.test_enemy.health)

    def test_battle_stats_change_hero_lose(self):
        self.test_enemy.health = 100
        self.test_enemy.level = 10
        self.assertEqual("You lose", self.test_hero.battle(self.test_enemy))

        self.assertEqual(101, self.test_enemy.health)
        self.assertEqual(11, self.test_enemy.level)
        self.assertEqual(6, self.test_enemy.damage)

    def test_str(self):
        expected = f"Hero {self.test_hero.username}: {self.level} lvl\n" \
               f"Health: {self.test_hero.health}\n" \
               f"Damage: {self.test_hero.damage}\n"
        self.assertEqual(expected, str(self.test_hero))

    def test_draw(self):
        self.test_enemy.hp = 2
        self.test_enemy.damage = 2
        self.assertEqual("Draw", self.test_hero.battle(self.test_enemy))
