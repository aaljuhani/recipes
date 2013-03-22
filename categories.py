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
        ['ground garlic'],
        ['ground ginger']],

     ['vegetable',
        ['bok choy'],
        ['okra'],
        ['lotus root'],
        ['edamame'],
  
        ['cabbage'], # in case you want to switch to bok choy (asian)
        ['pepper'],
        ['spinach'],
        ['red bell pepper'],
        ['yam'],
        ['beans'],
        ['radish'],
        ['potato'],
        ['eggplant'],
        ['mushroom'],
     ],


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
    ingredients={'brown rice':{'healthy':True,'cuisine':['asian'],'fancy':False},
                 'oats':{'healthy':True,'cuisine':['english'],'fancy':False},
                 'popcorn':{'healthy':True,'cuisine':['america'],'fancy':False},
                 'oatmeal':{'healthy':True,'cuisine':['english'],'fancy':False},
                 'whole wheat pasta':{'healthy':True,'cuisine':['italian'],'fancy':False},
                 'wild Rice':{'healthy':True,'cuisine':['indian'],'fancy':False},
                 'bulgur':{'healthy':True,'cuisine':['african'],'fancy':False},

                 'cornbread':{'healthy':False,'cuisine':['american'],'fancy':False},
                 'couscous':{'healthy':False,'cuisine':['african'],'fancy':False},
                 'crackers':{'healthy':False,'cuisine':['american'],'fancy':False},
                 'noodles':{'healthy':False,'cuisine':['asian'],'fancy':False},
                 'spaghetti':{'healthy':False,'cuisine':['italian'],'fancy':False},
                 'macaroni':{'healthy':False,'cuisine':['italian'],'fancy':False},
                 'white bread':{'healthy':False,'cuisine':['greek'],'fancy':False},
                 'white rice':{'healthy':False,'cuisine':['american'],'fancy':False},}

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
        elif instructions in self.ingredients[x]['cuisine']:
            return True
        else:
            return False   
        return self.ingredients[x]['healthy'] == self.ingredients[y]['healthy']
        



class spices:
    ingredients={'cumin seeds':{'cuisine':['indian'],'fancy':False},
                 'cumin':{'cuisine':['indian'],'fancy':False},
                 'turmeric':{'cuisine':['indian'],'fancy':False},
                 'soriander seeds':{'cuisine':['indian'],'fancy':False},
                 'fennel seeds':{'cuisine':['indian'],'fancy':False},
                 'fenugreek seeds':{'cuisine':['indian'],'fancy':False},
                 'curry':{'cuisine':['indian'],'fancy':False},
                 'ginger':{'cuisine':['indian'],'fancy':False},
                 

                 'chamomile':{'cuisine':['italian'],'fancy':False},
                 'lemon pepper':{'cuisine':['italian'],'fancy':False},
                 'oregano':{'cuisine':['italian'],'fancy':False},
                 'sun-dried tomatoes':{'cuisine':['italian'],'fancy':False},
                 'bay leaves':{'cuisine':['italian'],'fancy':False},
                 'basil leaves':{'cuisine':['italian'],'fancy':False},
                 'anise':{'cuisine':['italian'],'fancy':False},
                 'coriander':{'cuisine':['italian'],'fancy':False},
                 'cloves':{'cuisine':['italian'],'fancy':False},

                 'Cinnamon':{'cuisine':['asian'],'fancy':False},
                 'Thai Basil':{'cuisine':['asian'],'fancy':False},
                 'Kaffir Lime Leaves':{'cuisine':['asian'],'fancy':False},
                 'Nigella':{'cuisine':['asian'],'fancy':False},
                 'Turmeric':{'cuisine':['asian'],'fancy':False},
                  
                 
                'Saffron':{'cuisine':['iranian'],'fancy':False}, #doesnt originate from iran, but aside form that it bringsup a point that an ingredient can be common in multiple cuisines 
                 }

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
        elif instructions in self.ingredients[x]['cuisine']:
            return True
        else:
            return False   
        return self.ingredients[x]['cuisine'] == self.ingredients[y]['cuisine']
        


class sauce:
    ingredients={'curry sauce':{'cuisine':['indian'],'fancy':False},
                

                 'balsamic vinegar':{'cuisine':['italian'],'fancy':False},
                 

                 'hoisin sauce':{'cuisine':['asian'],'fancy':False},
                 'soy sauce':{'cuisine':['asian'],'fancy':False},
                 
                'barbeque sauce':{'cuisine':['american'],'fancy':False},
                
                 'tomato sauce':{'cuisine':['italian','american'],'fancy':False}, #need to find a way to handle this
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
        elif instructions in self.ingredients[x]['cuisine']:
            return True
        else:
            return False 
        return self.ingredients[x]['cuisine'] == self.ingredients[y]['cuisine']
        

