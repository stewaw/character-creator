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
        return (f'{self.Name}\n'
                f'Strength: {self.Strength}\n'
                f'Dexterity: {self.Dexterity}\n'
                f'Constitution: {self.Constitution}\n'
                f'Intelligence: {self.Intelligence}\n'
                f'Wisdom: {self.Wisdom}\n'
                f'Charisma: {self.Charisma}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        dude = Character(' '.join(sys.argv[1:]).title())
        print(dude)
    else:
        print("Create a randomised character by entering their name after the .py")
