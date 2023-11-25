import random

class Move:
    def __init__(self, name, p_type, damage):
        """
        Initialize a Move object representing a Pokémon move (attack).

        Args:
            name (str): The name of the move.
            p_type (str): The type of the move (e.g., 'Water', 'Fire').
            damage (int): The base damage of the move.
        """
        ...
            
class Pokemon:
    def __init__(self, name, p_type, health, level, moves):
        """
        Initialize a Pokemon object.

        Args:
            name (str): The name of the Pokémon.
            p_type (str): The type of the Pokémon (e.g., 'Water', 'Fire').
            health (int): The health points of the Pokémon.
            level (int): The level of the Pokémon.
            moves (list): A list of Move objects available to the Pokémon.
        """
        ...
        
    def attack(self, enemy_pokemon):
        """
        Attack an enemy Pokémon.

        Args:
            enemy_pokemon (Pokemon): The Pokémon being attacked.
        """
        ...
        
    def receive_damage(self, damage):
        """
        Apply damage to the Pokémon and print its status.

        Args:
            damage (float): The amount of damage received.
        """
        ...
            
class Arena:
    def __init__(self, arena_name, pokemon1, pokemon2):
        """
        Initialize an Arena object where Pokémon battles take place.

        Args:
            arena_name (str): The name of the arena.
            pokemon1 (Pokemon): The first Pokémon in the battle.
            pokemon2 (Pokemon): The second Pokémon in the battle.
        """
        ...
        
    def fight(self):
        """
        Run a fight between two Pokémon.
        """
        ...
    
def main():
    
    # Create moves for fire:
    ember = Move("Ember", "Fire", 40)
    fiery_dance = Move("Fiery Dance", "Fire", 80)
    blaze_kick = Move("Blaze Kick", "Fire", 85)
    # Create moves for water:
    clamp = Move("Clamp", "Water", 35)
    dive = Move("Dive", "Water", 80)
    bubble_beam = Move("Bubble Beam", "Water", 65)
    
    # Create some Pokémon
    squirtle = Pokemon("Squirtle", "Water", 100, 5, [clamp, dive, bubble_beam])
    charmander = Pokemon("Charmander", "Fire", 90, 4, [ember, fiery_dance, blaze_kick])

    # create the arena
    kanto = Arena("Kanto Gyms", squirtle, charmander)
    kanto.fight()
    
if __name__ == "__main__":
    main()
