# -*- coding: utf-8 -*-
from random import choice, randint

goods = [
    [10, 3],
    [2, 6],
    [5, 5],
    [7, 8],
    [6, 1],
    [1, 1],
    [3, 10],
    [8, 5],
    [7, 6],
    [4, 7]]

MAX_WEIGHT = 10


def random_chromosome():
    return [randint(0, 1) for i in range(10)]


def calc_fitness(chromo):
    fit = 0
    weight = 0
    for value in goods:
        w, f = value
        key = goods.index(value)
        weight += chromo[key] * w
        fit += chromo[key] * f
    if weight >= MAX_WEIGHT:
        return 0
    else:
        return fit


def mate(chromo1, chromo2):
    point = randint(0, 9)
    return chromo1[:point] + chromo2[point:]


def mutate(chromo):
    for i in range(2):
        chromo[randint(0, 9)] = randint(0, 1)
    return chromo


def alphas(arrs):
    decorated = [(calc_fitness(chromo), chromo) for chromo in arrs]
    decorated.sort(reverse=True)
    return [chromo[1] for chromo in decorated][:10]


if __name__ == '__main__':
    NUM_OFFSPRING = 250
    SEEDS = [random_chromosome() for i in range(NUM_OFFSPRING)]
    top10 = alphas(SEEDS)
    top = top10[0]
    i = 0
    top_prev = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    top_p_p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while top[:-1] != top_prev[:-1] and top[:-1] != top_p_p:
        top_p_p = top_prev
        top_prev = top10[0]
        offspring = []
        for j in range(NUM_OFFSPRING):
            offspring.append(mate(choice(top10), choice(top10)))

        top10 = alphas(offspring)
        top = top10[0]
        i += 1
    sum_weight = 0
    sum_fit = 0
    for val in goods:
        w, f = val
        key = goods.index(val)
        if top_prev[key] > 0:
            weight = top_prev[key] * w
            fit = top_prev[key] * f
            print "%d:\tweight %d price %d" % (key, weight, fit)
            sum_weight += weight
            sum_fit += fit
    print "#Sum:\nweight %d price %d" % (sum_weight, sum_fit)
