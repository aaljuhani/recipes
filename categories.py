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
        ['lamb'],
        ['seitan'],
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
        ['rosemary'],
        ['ground ginger']],

     ['vegetable',
        ['bok choy'],
        ['okra'],
        ['lotus root'],
        ['edamame'],
  
        ['cabbage'], # in case you want to switch to bok choy (asian)
        ['red pepper'],
        ['green pepper'],
        ['spinach'],
        ['red bell pepper'],
        ['green bell pepper'],
        ['yam'],
        ['beans'],
        ['radish'],
        ['potato'],
        ['eggplant'],
        ['mushroom'],
     ],

    ['fruit',
        ['apple'],
        ['pomegranate'],
        ['raisins'],
        ['asian pear'],     
     ],

    ['sauce',
        ['curry sauce'],
        ['balsamic vinegar'],
        ['hoisin sauce'],
        ['soy sauce'],
        ['barbeque sauce'],
        ['ketchup'],
        ['tomato sauce']],
    ]

class protein:
    ingredients={'chicken':{'vegetarian':False,'color':'white','seafood':False,'fancy':False},
                 'beef':{'vegetarian':False,'color':'red','seafood':False,'fancy':False},
                 'pork':{'vegetarian':False,'color':'red','seafood':False,'fancy':False},
                 'tofu':{'vegetarian':True,'color':'white','seafood':False,'fancy':False},
                 'seitan':{'vegetarian':True,'color':'white','seafood':False,'fancy':False},
                 'tempeh':{'vegetarian':True,'color':'white','seafood':False,'fancy':False},
                 'lamb':{'vegetarian':False,'color':'red','seafood':False,'fancy':False},
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
    ingredients={'cumin seeds':{'cuisine':['indian', 'mexican'],'fancy':False},
                 'cumin':{'cuisine':['indian', 'mexican'],'fancy':False},
                 'turmeric':{'cuisine':['asian','indian'],'fancy':False},
                 'fennel seeds':{'cuisine':[],'fancy':False},
                 'fenugreek seeds':{'cuisine':['indian'],'fancy':False},
                 'curry':{'cuisine':['indian','asian'],'fancy':False},
                 'ginger':{'cuisine':['indian','asian'],'fancy':False},
                 

                 'chamomile':{'cuisine':['italian'],'fancy':False},
                 'lemon pepper':{'cuisine':['italian'],'fancy':False},
                 'oregano':{'cuisine':['italian'],'fancy':False},
                 'sun-dried tomatoes':{'cuisine':['italian'],'fancy':False},
                 'bay leaves':{'cuisine':['italian','american'],'fancy':False},
                 'basil leaves':{'cuisine':['italian'],'fancy':False},
                 'anise':{'cuisine':['italian'],'fancy':False},
                 'coriander':{'cuisine':['mexican','asian','indian'],'fancy':False},
                 'cloves':{'cuisine':['italian','indian','american'],'fancy':False},

                 'Cinnamon':{'cuisine':['asian','american'],'fancy':False},
                 'Thai Basil':{'cuisine':['asian'],'fancy':False},
                 'Kaffir Lime Leaves':{'cuisine':['asian'],'fancy':False},
                 'Nigella':{'cuisine':['asian'],'fancy':False},
                 'Turmeric':{'cuisine':['asian', 'indian'],'fancy':False},
                 'rosemary':{'cuisine':['italian', 'american'], 'fancy':False},
                  
                 
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
        

class vegetables:
    ingredients = {
        'onion':{'similarVeg':[], 'cuisine':[], 'fancy':False},
        'cabbage':{'similarVeg':['bok choy'], 'cuisine':[], 'fancy':False},
        'green onions':{'similarVeg':[], 'cuisine':[], 'fancy':False},
        'carrot':{'similarVeg':[], 'cuisine':[], 'fancy':False},
        'red pepper':{'similarVeg':['red bell pepper', 'okra'], 'cuisine':[], 'fancy':False},
        'green pepper':{'similarVeg':['green bell pepper', 'okra'], 'cuisine':[], 'fancy':False},
        'spinach':{'similarVeg':['bok choy'], 'cuisine':[], 'fancy':False},
        'red bell pepper':{'similarVeg':['red pepper', 'okra'], 'cuisine':[], 'fancy':False},
        'green bell pepper':{'similarVeg':['green pepper', 'okra'], 'cuisine':[], 'fancy':False},
        'yam':{'similarVeg':['lotus root', 'potato'], 'cuisine':[], 'fancy':False},
        'beans':{'similarVeg':['edamame'], 'cuisine':[], 'fancy':False},
        'radish':{'similarVeg':['lotus root'], 'cuisine':[], 'fancy':False},
        'potato':{'similarVeg':['yam', 'lotus root'], 'cuisine':[], 'fancy':False},
        'eggplant':{'similarVeg':['mushroom', 'okra', 'lotus root'], 'cuisine':[], 'fancy':False},
        'mushroom':{'similarVeg':['okra', 'eggplant', 'lotus root'], 'cuisine':[], 'fancy':False},
        
        'edamame': {'similarVeg':['beans'], 'cuisine':['asian'], 'fancy':False},
        'bok choy':{'similarVeg':['cabbage', 'spinach'], 'cuisine':['asian'], 'fancy':False},
        'okra':{'similarVeg':['red pepper', 'eggplant', 'mushroom', 'red bell pepper'], 'cuisine':['indian', 'american'], 'fancy':False},
        'lotus root':{'similarVeg':['potato', 'eggplant', 'radish', 'yam'], 'cuisine':['asian'], 'fancy':False},
        }

    def getSimilarIngredient(self,ingredient,instructions, used):
        count = 0
        if self.compatible(ingredient,ingredient,instructions, used):
            return ingredient
        replacement = random.choice(self.ingredients[ingredient]['similarVeg'])
        while not(replacement != ingredient and self.compatible(replacement,ingredient,instructions, used)):
            if count > 30:
               return ingredient
            count = count + 1;
            replacement = random.choice(self.ingredients[ingredient]['similarVeg'])
        return replacement
    
    def compatible(self, x, y, instructions, used):
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


class fruits:
    ingredients = {
        'apple':{'similar':['asian pear'], 'cuisine':['asian'], 'fancy':False},
        'pomegranate':{'similar':['raisins'], 'cuisine':['iranian', 'greek'], 'fancy':False},
        'raisins':{'similar':['pomegranate', 'asian pear'], 'cuisine':[], 'fancy':False},
        'asian pear':{'similar':['apple'], 'cuisine':['asian'], 'fancy':False},
        }

    def getSimilarIngredient(self,ingredient,instructions, used):
        count = 0
        if self.compatible(ingredient,ingredient,instructions, used):
            return ingredient
        replacement = random.choice(self.ingredients[ingredient]['similar'])
        while not(replacement != ingredient and self.compatible(replacement,ingredient,instructions, used)):
            if count > 30:
               return ingredient
            count = count + 1;
            replacement = random.choice(self.ingredients[ingredient]['similar'])
        return replacement
    
    def compatible(self, x, y, instructions, used):
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
                 'ketchup':{'cuisine':['american','italian'],'fancy':False},
                
                 'tomato sauce':{'cuisine':['italian','american'],'fancy':False}, #need to find a way to handle this
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
        

