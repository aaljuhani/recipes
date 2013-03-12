import random
'''
Create these classes with internal data structures
protein:
    type of meat (red/white)
    vegetarian (y/n)
    seafood (y/n)
    fancy (y/n)

grain:
    healthy (y/n)
    cuisine (country)
    fancy (y/n)
    
spice:
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

sauce:
    cuisine
    fancy
'''
    
category =[
    ['protein' ,
     ['chicken' , 'whitemeat'],
     ['beaf' , 'redmeat'],
     ['pork' , 'redmeat'],
     ['turkey' , 'whitemeat'],
     ['tofu' , 'veg'],
     ['tempeh' , 'veg']],

    ['grain' ,
     ['rice', 'h'],
     ['brown rice', 'healthy'],
     ['basmati rice' , 'indian']],

    ['spice',
     ['salt'],
     ['pepper'],
     ['cumin' , 'indian'],
     ['cloves' , 'indian'],
     ['cardamon' , 'indian'],
     ['cinnamon']],

    ['vegetable',
     ['onion'],
     ['grean onions'],
     ['carrot'],
     ['red bell pepper'],
     ['peas']],

    ['fruit',
     ['apple'],
     ['pinapple']
     ],

    ['flavor',
     ['garlic'],
     ['ginger']]

    ]

class protein:
    ingredients={'chicken':{'vegetarian':False,'color':'white','seafood':False,'fancy':False},
                 'beef':{'vegetarian':False,'color':'red','seafood':False,'fancy':False},
                 'pork':{'vegetarian':False,'color':'red','seafood':False,'fancy':False},
                 'tofu':{'vegetarian':True,'color':'white','seafood':False,'fancy':False},
                 'seitan':{'vegetarian':True,'color':'white','seafood':False,'fancy':False},
                 'salmon':{'vegetarian':False,'color':'white','seafood':True,'fancy':False},}
    #instructions is a list of steps involving the ingredient
    def getSimilarIngredient(self,ingredient,instructions):
        replacement = random.choice(list(self.ingredients.keys()))
        while not(replacement != ingredient and self.compatible(replacement,ingredient,instructions)):
            replacement = random.choice(list(self.ingredients.keys()))
        return replacement
    
    def compatible(self,x,y,instructions):
        #do something to check if new ingredient is compatible with the instructions as well    
        return self.ingredients[x]['vegetarian'] == self.ingredients[y]['vegetarian']
        
