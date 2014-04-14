from random import choice

def insult():
    return "Thou " + generate_insult() + "!"

def named_insult(name):
    return name + ", thou " + generate_insult() + "!"

def generate_insult():
    first_adjs = ["artless", "bawdy", "beslubbering", "bootless", "churlish"]
    second_adjs = ["base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained"]
    nouns = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig"]

    return choice(first_adjs) + " " + choice(second_adjs) + " " + choice(nouns)
