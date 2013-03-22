import random
'''
Create these classes with internal data structures
protein: --> Done
    type of meat (red/white)
    vegetarian (y/n)
    seafood (y/n)
    fancy (y/n)

grain: --> Done
    healthy (y/n)
    cuisine (country)
    fancy (y/n)
    
spice: --> Done
    cuisine (country)
    fancy (y/n)
    
vegetable:
    each vegetable has a list of similar vegetables
    cuisine

fruit:
    each vegetable has a list of similar vegetables
    cuisine
    
flavor:
    cuisine
    fancy

sauce:  --> Done
    cuisine
    fancy
'''
    
category =[
    ['protein' ,
        ['chicken'],
        ['beef'],
        ['pork'],
        ['turkey'],
        ['tofu'],
        ['tempeh']],

    ['grain' ,
        ['Brown Rice'],
        ['Oats'],
        ['Popcorn'],
        ['Oatmeal'],
        ['Whole Wheat Pasta'],
        ['Wild Rice'],
        ['Bulgur'],
        ['Cornbread'],
        ['Couscous'],
        ['Crackers'],
        ['Noodles'],
        ['Spaghetti'],
        ['Macaroni'],
        ['White Bread'],
        ['White Rice']],

    ['spice',
        ['cumin seeds'],
        ['cumin'],
        ['turmeric'],
        ['coriander seeds'],
        ['fennel seeds'],
        ['fenugreek seeds'],
        ['curry'],
        ['ginger'],
        ['chamomile'],
        ['lemon pepper'],
        ['oregano'],
        ['sun-dried tomatoes'],
        ['bay leaves'],
        ['basil leaves'],
        ['anise'],
        ['coriander'],
        ['cloves'],
        ['cinnamon'],
        ['thai basil'],
        ['kaffir lime leaves'],
        ['nigella'],
        ['turmeric'],
        ['saffron'],
        ['salt'],
        ['sugar'],
        ['pepper'],
        ['ground garlic']
        ['ground ginger']],

    ['vegetable',
        ['onion'],
        ['grean onions'],
        ['carrot'],
        ['red bell pepper'],
        ['peas']],

    ['fruit',
        ['apple'],
        ['pinapple']],
    ['sauce',
        ['curry sauce'],
        ['balsamic vinegar'],
        ['hoisin sauce'],
        ['soy sauce'],
        ['barbeque sauce'],
        ['tomato sauce']],
    ]

class protein:
    ingredients={'chicken':{'vegetarian':False,'color':'white','seafood':False,'fancy':False},
                 'beef':{'vegetarian':False,'color':'red','seafood':False,'fancy':False},
                 'pork':{'vegetarian':False,'color':'red','seafood':False,'fancy':False},
                 'tofu':{'vegetarian':True,'color':'white','seafood':False,'fancy':False},
                 'seitan':{'vegetarian':True,'color':'white','seafood':False,'fancy':False},
                 'salmon':{'vegetarian':False,'color':'white','seafood':True,'fancy':False},}
    #instructions is a list of steps involving the ingredient
    def getSimilarIngredient(self,ingredient,instructions, used):
        if self.compatible(ingredient,ingredient,instructions, used):
            return ingredient
        replacement = random.choice(list(self.ingredients.keys()))
        while not(replacement != ingredient and self.compatible(replacement,ingredient,instructions, used)):
            replacement = random.choice(list(self.ingredients.keys()))
        return replacement
    
    def compatible(self,x,y,instructions, used):
        if x in used:
            return False
        if instructions == 'vegetarian':
            return self.ingredients[x]['vegetarian']
        elif instructions == 'seafood':
            return self.ingredients[x]['seafood']
        elif instructions == 'fancy':
            return self.ingredients[x]['fancy']
        else:
            return True               
            
        #do something to check if new ingredient is compatible with the instructions as well    
        return self.ingredients[x]['vegetarian'] == self.ingredients[y]['vegetarian']
        


class grain:
    ingredients={'brown rice':{'healthy':True,'cuisine':'Asia','fancy':False},
                 'oats':{'healthy':True,'cuisine':'England','fancy':False},
                 'popcorn':{'healthy':True,'cuisine':'America','fancy':False},
                 'oatmeal':{'healthy':True,'cuisine':'England','fancy':False},
                 'whole wheat pasta':{'healthy':True,'cuisine':'Italy','fancy':False},
                 'wild Rice':{'healthy':True,'cuisine':'India','fancy':False},
                 'bulgur':{'healthy':True,'cuisine':'Africa','fancy':False},

                 'cornbread':{'healthy':False,'cuisine':'America','fancy':False},
                 'couscous':{'healthy':False,'cuisine':'Africa','fancy':False},
                 'crackers':{'healthy':False,'cuisine':'America','fancy':False},
                 'noodles':{'healthy':False,'cuisine':'Asia','fancy':False},
                 'spaghetti':{'healthy':False,'cuisine':'Italy','fancy':False},
                 'macaroni':{'healthy':False,'cuisine':'Italy','fancy':False},
                 'white bread':{'healthy':False,'cuisine':'Greek','fancy':False},
                 'white rice':{'healthy':False,'cuisine':'America','fancy':False},}

    #instructions is a list of steps involving the ingredient
    def getSimilarIngredient(self,ingredient,instructions, used):
        if self.compatible(ingredient,ingredient,instructions, used):
            return ingredient
        replacement = random.choice(list(self.ingredients.keys()))
        while not(replacement != ingredient and self.compatible(replacement,ingredient,instructions, used)):
            replacement = random.choice(list(self.ingredients.keys()))
        return replacement
    
    def compatible(self,x,y,instructions, used):
        #do something to check if new ingredient is compatible with the instructions as well
        if x in used:
            return False
        if instructions == 'healthy':
            return self.ingredients[x]['healthy']
        elif instructions == 'fancy':
            return self.ingredients[x]['fancy']
        elif instructions == 'asian':
            return self.ingredients[x]['cuisine'] == 'Asia'
        elif instructions == 'italian':
            return self.ingredients[x]['cuisine'] == 'Italy'
        elif instructions == 'greek':
            return self.ingredients[x]['cuisine'] == 'Greek'
        elif instructions == 'american':
            return self.ingredients[x]['cuisine'] == 'America'
        elif instructions == 'indian':
            return self.ingredients[x]['cuisine'] == 'India'
        elif instructions == 'english':
            return self.ingredients[x]['cuisine'] == 'England'
        else:
            return True   
        return self.ingredients[x]['healthy'] == self.ingredients[y]['healthy']
        



class spices:
    ingredients={'cumin seeds':{'cuisine':'India','fancy':False},
                 'cumin':{'cuisine':'India','fancy':False},
                 'turmeric':{'cuisine':'India','fancy':False},
                 'soriander seeds':{'cuisine':'India','fancy':False},
                 'fennel seeds':{'cuisine':'India','fancy':False},
                 'fenugreek seeds':{'cuisine':'India','fancy':False},
                 'curry':{'cuisine':'India','fancy':False},
                 'ginger':{'cuisine':'India','fancy':False},
                 

                 'chamomile':{'cuisine':'Italy','fancy':False},
                 'lemon pepper':{'cuisine':'Italy','fancy':False},
                 'oregano':{'cuisine':'Italy','fancy':False},
                 'sun-dried tomatoes':{'cuisine':'Italy','fancy':False},
                 'bay leaves':{'cuisine':'Italy','fancy':False},
                 'basil leaves':{'cuisine':'Italy','fancy':False},
                 'anise':{'cuisine':'Italy','fancy':False},
                 'coriander':{'cuisine':'Italy','fancy':False},
                 'cloves':{'cuisine':'Italy','fancy':False},

                 'Cinnamon':{'cuisine':'Asia','fancy':False},
                 'Thai Basil':{'cuisine':'Asia','fancy':False},
                 'Kaffir Lime Leaves':{'cuisine':'Asia','fancy':False},
                 'Nigella':{'cuisine':'Asia','fancy':False},
                 'Turmeric':{'cuisine':'Asia','fancy':False},
                  
                 
                'Saffron':{'cuisine':'Iran','fancy':False}, #doesnt originate from iran, but aside form that it bringsup a point that an ingredient can be common in multiple cuisines 
                 

                
                 'salt':{'cuisine':'worldwide','fancy':False},
                 'sugar':{'cuisine':'worldwide','fancy':False},
                 'pepper':{'cuisine':'worldwide','fancy':False},}

    #instructions is a list of steps involving the ingredient
    def getSimilarIngredient(self,ingredient,instructions, used):
       count = 0
       if self.compatible(ingredient,ingredient,instructions, used):
           return ingredient
       replacement = random.choice(list(self.ingredients.keys()))
       while not(replacement != ingredient and self.compatible(replacement,ingredient,instructions, used)):
           if count > 30:
               return ingredient
           count = count + 1;
           replacement = random.choice(list(self.ingredients.keys()))
       return replacement
    
    def compatible(self,x,y,instructions, used):
        #do something to check if new ingredient is compatible with the instructions as well
        if x in used:
            return False
        if instructions == 'fancy':
            return self.ingredients[x]['fancy']
        elif instructions == 'asian':
            return self.ingredients[x]['cuisine'] == 'Asia'
        elif instructions == 'italian':
            return self.ingredients[x]['cuisine'] == 'Italy'
        elif instructions == 'greek':
            return self.ingredients[x]['cuisine'] == 'Greek'
        elif instructions == 'american':
            return self.ingredients[x]['cuisine'] == 'America'
        elif instructions == 'indian':
            return self.ingredients[x]['cuisine'] == 'India'
        elif instructions == 'english':
            return self.ingredients[x]['cuisine'] == 'England'
        elif instructions == 'iranian':
            return self.ingredients[x]['cuisine'] == 'Iran'
        else:
            return True   
        return self.ingredients[x]['cuisine'] == self.ingredients[y]['cuisine']
        


class sauce:
    ingredients={'curry sauce':{'cuisine':'India','fancy':False},
                

                 'balsamic vinegar':{'cuisine':'Italy','fancy':False},
                 

                 'hoisin sauce':{'cuisine':'Asia','fancy':False},
                 'soy sauce':{'cuisine':'Asia','fancy':False},
                 
                'barbeque sauce':{'cuisine':'America','fancy':False},
                
                 'tomato sauce':{'cuisine':'worldwide','fancy':False}, #need to find a way to handle this
                }

    #instructions is a list of steps involving the ingredient
    def getSimilarIngredient(self,ingredient,instructions, used):
        if self.compatible(ingredient,ingredient,instructions, used):
            return ingredient
        replacement = random.choice(list(self.ingredients.keys()))
        while not(replacement != ingredient and self.compatible(replacement,ingredient,instructions, used)):
            replacement = random.choice(list(self.ingredients.keys()))
        return replacement
    
    def compatible(self,x,y,instructions, used):
        #do something to check if new ingredient is compatible with the instructions as well
        if x in used:
            return False
        if instructions == 'fancy':
            return self.ingredients[x]['fancy']
        elif instructions == 'asian':
            return self.ingredients[x]['cuisine'] == 'Asia'
        elif instructions == 'italian':
            return self.ingredients[x]['cuisine'] == 'Italy'
        elif instructions == 'greek':
            return self.ingredients[x]['cuisine'] == 'Greek'
        elif instructions == 'american':
            return self.ingredients[x]['cuisine'] == 'America'
        elif instructions == 'indian':
            return self.ingredients[x]['cuisine'] == 'India'
        elif instructions == 'english':
            return self.ingredients[x]['cuisine'] == 'England'
        elif instructions == 'iranian':
            return self.ingredients[x]['cuisine'] == 'Iran'
        else:
            return True 
        return self.ingredients[x]['cuisine'] == self.ingredients[y]['cuisine']
        

