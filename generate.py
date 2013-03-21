from categories import *
from Scrapper import *

p = protein()
g = grain()
sp = spices()
sa = sauce()
#v = vegetable()
#fr = fruit()
#fl = flavor()

def findIngredient (str):
    temp = str.split(' ')
    for word in temp:
        for cat in category:
            for i in cat:
                if word == i[0]:
                    return [cat[0], word]
    return False

def generateRecipe (url, instruction):
    ingredients = scrap_recipe(url)
    newIngredients = []
    temp = []
    index = 0
    used = []
    for item in ingredients:
        info = findIngredient(item[1])
        temp.append(item[0])
        if info:
            if info[0] == 'protein':
                new = p.getSimilarIngredient(info[1], instruction, used)
            elif info[0] == 'grain':
                new = g.getSimilarIngredient(info[1], instruction, used)
            elif info[0] == 'spice':
                new = sp.getSimilarIngredient(info[1], instruction, used)
            elif info[0] == 'sauce':
                new = sa.getSimilarIngredient(info[1], instruction, used)
            else:
                new = info[1]
            '''    
            elif info[0] == 'vegetable':
                new = v.getSimilarIngredient(info[1], instruction, used)
            elif info[0] == 'fruit':
                new = fr.getSimilarIngredient(info[1], instruction, used)
            elif info[0] == 'flavor':
                new = fl.getSimilarIngredient(info[1], instruction, used)
            '''
            temp.append(new)
            used.append(new)
        else:
            temp.append(item[1])
        newIngredients.append(temp)
        temp = []
    print 'OLD'
    print ingredients
    print '\n'
    print 'NEW'
    print newIngredients
        
        
        
