# Namespace packages - are like package-like  directories
# 1. May contain modules.
# 2. May contain nested regular packages.
# 3. May contain nested namespace packages.
# 4. But cannot contain __init__.py

def respond(language):
    match language:
        case "Java" | "Javascript":
            return "Hmm coffee"
        case "Python":
            return "I'm not scared of snakes"
        case "Rust":
            return "Don't drink too much water"
        case _:
            return "HeHe"
print(respond('Python'))  

symbols = {
    "F": "\u2192",
    "B": "\u2190",
    "L": "\u2191",
    "R": "\u2193",
    "pick": "\u2925",
}
print(symbols)

def op(command):
    match command:
        case ['move', *directions]:
            return tuple(symbols[direction] for direction in directions) 
        case 'pick':
            return symbols['pick']
        case _:
            raise ValueError(f'{command} does not compute!')
        
from itertools import zip_longest
l1 = [1,2,3]
l2 = [10,20,30,40]
list(zip_longest(l1,l2, fillvalue='hehe')) 
zip(l1,l2, strict=True)  