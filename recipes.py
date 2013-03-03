import categories

#def parseIngredient:

#def substitute:


def classifyIngredient (item):
    for cat in categories.category:
        for ingredient in cat:
            if (item == ingredient[0]):
                print cat[0]
                print ingredient[0]
                print ingredient
                break

            
