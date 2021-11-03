from typing import List
from itertools import permutations

def chances_from_population(population: List[int], draw=1, remove=True):
    total_population = sum(population)

    if draw == 1:
        return (feno/total_population for feno in population)
    else:
        new_populations = [population.copy() for _ in range(len(population))]
        if remove:
            for i in range(len(population)):
                if population[i] > 1:
                    new_populations[i][i] -= 1

        return [[feno/total_population, list(chances_from_population(new_pop, draw - 1, remove))] for feno, new_pop in zip(population, new_populations)]


def parse_chances(chances: list, draw=1, ordered=False):

    result = dict()

    # Generate options
    options = list(permutations(range(0, 3), draw))
    print(options)
    for option in options:
        option_chances = []
        depth = 0
        modif_option = list(option)
        modif_chance = chances[modif_option[0]]
        while depth < draw:
            option_chances.append(modif_chance[0])
            modif_option = modif_option[1]
            if type(modif_option) != list:
                modif_option = [modif_option]
            modif_chance = modif_chance[1][modif_option[0]]
            if type(modif_chance) != list:
                modif_chance = [modif_chance]
            depth += 1

        result[option] = option_chances

    print(result)




def sum_tuple(tuples, normalised=True):
    result = [sum(_) for _ in zip(*tuples)]
    if normalised:
        return [_/sum(result) for _ in result]
    return result


def equal_population(population: tuple) -> bool:
    return all(population[0] == x for x in population)


def obtain_offspring_chance(population: List[int], target: str, inheritance=(0.5, 0.5)) -> float:
    """
    :param population: (domi AA, hetero Aa, recessive aa)
    :param target: what type are you targeting (index of population) ("A*", "aa", "AA" etc)
    :param inheritance: chance of inheriting dominant, recessive allele

    :return: chance of obtaining target type from population
    """
    # population = (domi, hetero, recessive)
    # mating of various types
    # chance of getting a (domi, hetero, recessive) when mating with a (A, B)

    inheritance_table = {
        (0, 0): (1, 0, 0),
        (0, 1): (inheritance[0], inheritance[1], 0),
        (0, 2): (0, 1, 0),
        (1, 1): (inheritance[0] ** 2, 1 - (inheritance[0] ** 2 + inheritance[1] ** 2), inheritance[1] ** 2),
        (1, 2): (0, inheritance[0], inheritance[1]),
        (2, 2): (0, 0, 1)
    }
    print(inheritance_table)
    random_inheritence = sum_tuple(inheritance_table.values())

    if equal_population(population):
        match (target[0], target[1]):
            case ["A", "A"]:
                return random_inheritence[0]
            case ["A", "a"]:
                return random_inheritence[1]
            case ["a", "a"]:
                return  random_inheritence[2]
            case ["A", "a"] | ["a", "A"]:
                return 0
            case ["A", _] | [_, "A"]:
                return 1
            case ["a", _] | [_, "a"]:
                return 2
            case _:
                raise Exception("Incorrect target")
    else:
        return 0


pop = [2, 2, 2] # domi, hetero, recessive
parents = 2
print(obtain_offspring_chance(pop, "A*"))
print(chances := chances_from_population(pop, parents))
parse_chances(chances, parents)