import random

words = [
    ["me", ["noun"]],
    ["you", ["noun"]],
    ["GORGAR", ["noun"]],
    ["hurt", ["imperative", "transitive", "participle"]],
    ["got", ["transitive"]],
    ["speaks", ["intransitive"]],
    ["beat", ["imperative", "transitive"]]
]

patterns = [
    ["identity", "noun noun"],
    ["transitive", "noun transitive noun"],
    ["transitive", "noun transitive noun"],
    ["transitive", "noun transitive noun"],
    ["participle", "noun participle"],
    #["intransitive", "noun intransitive"],
    ["intransitive", "GORGAR speaks"],
    ["imperative", "imperative noun"]
]
    
def build_categories(words):
    
    categories = {}
    for word in words:
        for type in word[1]:
            if not type in categories:
                categories[type] = []
            categories[type].append(word[0])
    
    return categories
 
categories = build_categories(words)
 
def make_phrase(categories, patterns):
    
    phrase = ""
    pattern = random.choice(patterns)
    
    for word in pattern[1].split(" "):
        if word in categories:
            phrase += random.choice(categories[word]) + " "
        else:
            phrase += word + " "

    return phrase[0:-1]

def speak(categories, patterns):
    
    divisor = 2
    speech = ""
    while True:
    
        if speech != "":
            speech += ". "
        speech += make_phrase(categories, patterns)
        if random.uniform(0, 1) > (1.0 / divisor):
            return speech
        else:
            divisor *= 2
    
    
print speak(categories, patterns)