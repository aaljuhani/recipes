from categories import *
from Scrapper import *

#generateRecipe('http://allrecipes.com/Recipe/Juggernauts-Meatloaf/Detail.aspx','asian')

p = protein()
g = grain()
sp = spices()
sa = sauce()
v = vegetables()
fr = fruits()
#fl = flavor()

def findIngredient (str):
    str = str.replace('finely', '')
    str = str.replace('chopped', '')
    str = str.replace('diced', '')
    str = str.replace('dried','')
    for cat in category:
        for i in cat:
            if str.replace(' ','') == i[0].replace(' ',''):
                return [cat[0], i[0]]
    temp = str.split(' ')
    for word in temp:
        for cat in category:
            for i in cat:
                if word == i[0]:
                    return [cat[0], word]
    return False
'''
def findIngredient (str):
    str = str.replace('finely', '')
    str = str.replace('chopped', '')
    str = str.replace('diced', '')
    str = str.replace('dried','')
    for cat in category:
        for i in cat:
            if str.replace(' ','') == i[0].replace(' ',''):
                return [cat[0], i[0]]
    temp = str.split(' ')
    for word in temp:
        for cat in category:
            for i in cat:
                if word == i[0]:
                    return [cat[0], word]
    return False
'''

def generateRecipe (url, instruction):
    recipe = scrap_recipe(url)
    ingredients = recipe[0]
    translation = []
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
                translation.append([' meat ', new + ' '])
                
                if item[1].find('ground') != -1:
                    translation.append([item[1].replace('ground ', ''), new])
                    new = 'ground ' + new
                
            elif info[0] == 'grain':
                new = g.getSimilarIngredient(info[1], instruction, used)
            elif info[0] == 'spice':
                new = sp.getSimilarIngredient(info[1], instruction, used)
            elif info[0] == 'sauce':
                new = sa.getSimilarIngredient(info[1], instruction, used)
            elif info[0] == 'fruit':
                new = fr.getSimilarIngredient(info[1], instruction, used)
            elif info[0] == 'vegetable':
                new = v.getSimilarIngredient(info[1], instruction, used)
            else:
                new = info[1]
                

            
            '''
            elif info[0] == 'flavor':
                new = fl.getSimilarIngredient(info[1], instruction, used)
            '''
            if instruction == 'vegetarian':
                new = new.replace('egg', 'egg substitute')
            translation.append([item[1].replace('dried ', ''), new])
            temp.append(new)
            used.append(new)
        else:
            if instruction == 'vegetarian':
                temp.append(item[1].replace('egg', 'egg substitute'))
                translation.append([item[1], item[1].replace('egg', 'egg substitute')])
            else:
                temp.append(item[1])
        newIngredients.append(temp)
        temp = []
    directions = recipe[1]
    newdir = []
    temp = ''
    for step in directions:
        temp = step
        for item in translation:
            temp = temp.replace(item[0], ' ' + item[1])
        newdir.append(temp)
    
    print ('\n'),
    print ('NEW INGREDIENTS'),
    print ('\n'),
    for item in newIngredients:
        print ('\n'),
        print (item[0]),
        print (','),
        print (item[1]),
    print ('\n')
    print ('NEW DIRECTIONS')
    c = 1
    for item in newdir:
        print ('\n')
        print (c),
        print ('.'),
        print (item),
        c = c + 1



            
    
        
        
        
