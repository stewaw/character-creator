import sys
import json

from random import randint


class Character:
    def __init__(
            self, name
    ):
        stats = [randint(3, 18) for _ in range(6)]
        self.Name = name
        self.Strength = stats[0]
        self.Dexterity = stats[1]
        self.Constitution = stats[2]
        self.Intelligence = stats[3]
        self.Wisdom = stats[4]
        self.Charisma = stats[5]

    def __str__(self) -> str:
        return f'{self.Name}\nStrength: {self.Strength}\nDexterity: {self.Dexterity}\nConstitution: {self.Constitution}\nIntelligence: {self.Intelligence}\nWisdom: {self.Wisdom}\nCharisma: {self.Charisma}'

    def to_json(self) -> dict:
        return {k: v for k, v in self.__dict__.items()}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        char_name = sys.argv[1:]
        character = Character(' '.join(char_name).title())
        print(character)

        with open(f'{"_".join(char_name).lower()}.json', 'w') as out:
            json.dump(character.to_json(), out)

    else:
        print("Create a randomised character by entering their name after the .py")
