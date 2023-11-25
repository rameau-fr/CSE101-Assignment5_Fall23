import unittest
import random
from Homework_5 import Move, Pokemon, Arena  # Replace 'your_module' with the actual name of your Python file

class TestPokemonBattle(unittest.TestCase):

    def setUp(self):
        random.seed(0)  # Set a fixed seed for reproducibility of tests
        # Create test moves
        self.fire_move = Move("Fire Move", "Fire", 50)
        self.water_move = Move("Water Move", "Water", 30)
        # Create test Pokemons
        self.charmander = Pokemon("Charmander", "Fire", 100, 5, [self.fire_move])
        self.squirtle = Pokemon("Squirtle", "Water", 120, 4, [self.water_move])

    def test_move_initialization(self):
        # Testing Move class initialization
        self.assertEqual(self.fire_move.name, "Fire Move")
        self.assertEqual(self.fire_move.p_type, "Fire")
        self.assertEqual(self.fire_move.damage, 50)

    def test_pokemon_initialization(self):
        # Testing Pokemon class initialization
        self.assertEqual(self.charmander.name, "Charmander")
        self.assertEqual(self.charmander.p_type, "Fire")
        self.assertEqual(self.charmander.health, 100)
        self.assertEqual(self.charmander.level, 5)
        self.assertEqual(self.charmander.moves[0].name, "Fire Move")

    def test_pokemon_receive_damage(self):
        # Testing damage reception
        initial_health = self.squirtle.health
        damage = 20
        self.squirtle.receive_damage(damage)
        self.assertEqual(self.squirtle.health, initial_health - damage)

    # More tests can be added here to cover other methods and logic

if __name__ == '__main__':
    unittest.main()
