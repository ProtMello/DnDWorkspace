#!/usr/bin/env python

from dataclasses import dataclass
from dataclasses_json import dataclass_json
import json


@dataclass
class Stat:
    charisma: int
    constitution: int
    dexterity: int
    intellect: int
    strength: int
    wisdom: int


@dataclass
class Health:
    base: int
    current: int
    temp: int


@dataclass_json
@dataclass
class DNDCharacter:
    name: str
    race: str
    class_name: str
    armor_class: int
    proficiencies: list
    skills: list
    stats: Stat
    health: Health


you = DNDCharacter(
    "HARK",
    "Half-Orc",
    "Monk",
    13,
    ["Common", "Short Swords", "Daggers", "Orcish", "Tuba"],
    ["Unarmored Strike", "Flurry of Blows", "Dash", "High Jump"],
    Stat(12, 16, 16, 12, 10, 14),
    Health(11, 10, 5),
)

x = open("foo.json", "w")
print(you.name)

you.race = "Guman"
you.skills.append("Iron Fist")
you.stats.strength = 12

you = you.to_dict()
json.dump(you, x, indent=4)
