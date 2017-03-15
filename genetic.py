# -*- coding: utf-8 -*-

from random import randint,random
from operator import add


def birey(length,min, max):
    return [randint(min,max) for x in xrange(length)]

def populasyon(bireySayisi,length,min,max):
    return [birey(length,min,max) for x in xrange(bireySayisi)]


def fitness(birey, hedef):
    topl = reduce(add,birey,0)
    return abs(hedef-topl)

def grade(pop, hedef):
    summed = reduce(add, (fitness(x, hedef)for x in pop),0)
    return summed / (len(pop)*1.0)


## güçlü olmayan bireyler evrim geçirterek güçlü bireyler elde etmeliyiz
## daha sonra mutasyona uğratmalıyız - mutasyon yerel maksimum değerinde
## sıkışmaması için

def evolve(pop, hedef, retain=0.2, random_select=0.05, mutate=0.01):
    graded = [(fitness(x,hedef),x) for x in pop]
    graded = [ x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]
    for birey in graded[retain_length:]:
        if random_select > random():
            parents.append(birey)

    for birey in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(birey)-1)
            birey[pos_to_mutate] = randint(min(birey), max(birey))
    parents_length = len(parents)
    istenilen_length = len(pop) - parents_length
    cocuklar = []
    while len(cocuklar) < istenilen_length:
        erkek = randint(0, parents_length-1)
        disi = randint(0, parents_length-1)
        if erkek != disi:
            erkek = parents[erkek]
            disi = parents[disi]
            yarim = len(erkek) / 2
            cocuk = erkek[:yarim] + disi[yarim:]
            cocuklar.append(cocuk)
    parents.extend(cocuklar)
    return parents
