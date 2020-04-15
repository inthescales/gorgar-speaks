import random

words = [
    ["me", ["noun"]],
    ["you", ["noun"]],
    ["GORGAR", ["noun", "proper"]],
    ["hurt", ["imperative", "transitive", "participle"]],
    ["got", ["transitive"]],
    ["speaks", ["intransitive"]],
    ["beat", ["imperative", "transitive"]]
]

patterns = [
    ["identity", "noun noun", ["no_dupe"]],
    ["transitive", "noun transitive noun", []],
    ["transitive", "noun transitive noun", []],
    ["transitive", "noun transitive noun", []],
    ["participle", "noun participle", []],
    ["intransitive", "proper intransitive", []],
    ["imperative", "imperative noun", []]
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
    disqualified = []
    
    for word in pattern[1].split(" "):
        chosen = ""
        if word in categories:
            chosen = random.choice(list(set(categories[word]) - set(disqualified)))
        else:
            chosen += word
            
        if "no_dupe" in pattern[2]:
            disqualified.append(chosen)
            
        phrase += chosen + " "

    return phrase[0:-1]    
    
def speak_from(categories, patterns):
    
    divisor = 2
    speech = ""
    while True:
    
        if speech != "":
            speech += " "
            
        speech += make_phrase(categories, patterns).upper() + "."
        if random.uniform(0, 1) > (1.0 / divisor):
            return speech
        else:
            divisor *= 2

def speak():
    global words, patterns
    categories = build_categories(words)
    return speak_from(categories, patterns)
