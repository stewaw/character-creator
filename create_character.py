import sys
import json

from random import randint


class Character:
    def __init__(
            self, name
    ):
        # Generate 6 ints between 3 and 18 inclusive.
        stats = [randint(3, 18) for _ in range(6)]
        self.Name = name
        self.Strength = stats[0]  # Each stat is taken in order from the list.
        self.Dexterity = stats[1]
        self.Constitution = stats[2]
        self.Intelligence = stats[3]
        self.Wisdom = stats[4]
        self.Charisma = stats[5]

    # Pretty printing for the name and stats when required.
    def __str__(self) -> str:
        return f'{self.Name}\nStrength: {self.Strength}\nDexterity: {self.Dexterity}\nConstitution: {self.Constitution}\nIntelligence: {self.Intelligence}\nWisdom: {self.Wisdom}\nCharisma: {self.Charisma}'

    # Output the name and stats as a dict for dumping to JSON.
    def to_json(self) -> dict:
        return {k: v for k, v in self.__dict__.items()}


if __name__ == '__main__':
    # Continue if args provided
    if len(sys.argv) > 1:
        char_name = sys.argv[1:]
        # Create character with name in Title Case.
        character = Character(' '.join(char_name).title())
        print(character)

        with open(f'{"_".join(char_name).lower()}.json', 'w') as out:
            json.dump(character.to_json(), out)
    # If no character name supplied in terminal, tell them
    else:
        print("Create a randomised character by entering their name after the .py")
