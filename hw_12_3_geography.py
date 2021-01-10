# 1. make a dictionary of cities and EU countries

import json
import random

drzava_grad = {
    "Austrija": "Beč",
    "Belgija": "Bruxelles",
    "Bugarska": "Sofija",
    "Cipar": "Nikozija",
    "Češka": "Prag",
    "Danska": "Kopenhagen",
    "Estonija": "Tallinn",
    "Finska": "Helsinki",
    "Francuska": "Pariz",
    "Grčka": "Atena",
    "Hrvatska": "Zagreb",
    "Irska": "Dublin",
    "Italija": "Rim",
    "Latvija": "Riga",
    "Litva": "Vilnius",
    "Luksemburg": "Luxembourg",
    "Mađarska": "Budimpešta",
    "Malta": "Valletta",
    "Nizozemska": "Amsterdam",
    "Njemačka": "Berlin",
    "Poljska": "Varšava",
    "Portugal": "Lisabon",
    "Rumunjska": "Bukurešt",
    "Slovačka": "Bratislava",
    "Slovenija": "Ljubljana",
    "Španjolska": "Madrid",
    "Švedska": "Stockholm",
    }

def ponovi_igru():
    ponovi = input("Igrati ponovo? ")
    if ponovi.casefold() == "da":
        print("U redu, igrajmo ponovo! ")
        pokreni_igru()
    else:
        print("U redu, do viđenja!")

def pokreni_igru():
    x = random.choice(list(drzava_grad))
    pogodi = input("Koji je glavni grad države " + x + "? ")
    for drzava, grad in drzava_grad.items():
        if drzava == x:
            if grad.casefold() == pogodi:
                print("Bravo, točan odgovor!")
                ponovi_igru()
            else:
                print("Netočno, odgovor je bio: " + grad + ". Više sreće drugi put.")
                ponovi_igru()




ime = input("Tvoje ime: ")

print("Bok " + ime.upper() + ". Cilj ove igre je pogoditi glavni grad  države. Krenimo!")

pokreni_igru()