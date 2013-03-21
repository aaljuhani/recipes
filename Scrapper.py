import urllib2
import re
from bs4 import BeautifulSoup


def scrap_recipe (url):
    #page to scrap
    recipe_URL = url
    p = re.compile('<p>.*</', re.I|re.M|re.S)

    #page content 
    page = urllib2.urlopen(recipe_URL).read()

    soup = BeautifulSoup(page)

    # geting the Title of the recipe
    title = BeautifulSoup(soup.findAll('h1', attrs={'id' : 'itemTitle'}).__str__()).__str__()
    recipe_title = title[title.find('>')+1:title.find('<',title.find('>')+1,len(title))]
    print "TITLE"
    print recipe_title
    print "\n"


    ingredient_div = BeautifulSoup(soup.findAll('div', attrs={'id' : 'zoneIngredients'}).__str__())
    ingredient_spans = BeautifulSoup(ingredient_div.findAll('span').__str__())
    ingredient_list = BeautifulSoup(ingredient_spans.findAll(lambda tag: len(tag.attrs) == 2).__str__()).__str__()


    # get the clear ingredients without the html code
    openB = 0
    closeB = 0
    cleanIngredient = ''
    while (openB < len(ingredient_list)):
        openB = ingredient_list.find('<',openB+1,len(ingredient_list))
        cleanIngredient = cleanIngredient+ingredient_list[closeB+1:openB]
        if (openB == -1):
               break
        closeB = ingredient_list.find('>',openB+1,len(ingredient_list))

    Ingredient = cleanIngredient[cleanIngredient.find(',',cleanIngredient.find(',',cleanIngredient.find(',')+1)+1)+2:len(ingredient_list)] 

    print "INGREDIENT"
    print Ingredient
    print "\n"


    # get description
    description_spans = BeautifulSoup(soup.findAll('span', attrs={'class' : 'plaincharacterwrap break'}).__str__()).__str__()

    # get the clear ingredients without the html code
    openB = 0
    closeB = 0
    cleanDescription = ''
    while (openB < len(description_spans)):
        openB = description_spans.find('<',openB+1,len(description_spans))
        cleanDescription = cleanDescription+description_spans[closeB+1:openB]
        if (openB == -1):
               break
        closeB = description_spans.find('>',openB+1,len(description_spans))


    print "DESCRIPTION"
    print cleanDescription
    print "\n"

    Ingredient = Ingredient.split(',')    

    Ingredients = []
    temp = []
    for word in Ingredient:
        if re.match(r'[\D-]*$', word):
            temp.append(word)
            Ingredients.append(temp)
            temp = []
        else:
            temp.append(word)

    for pair in Ingredients:
        if len(pair) < 2:
            Ingredients.remove(pair)
            
    '''
    Ingredients = []
    lastInt = 0
    currEntry = ""
    temp = ""
    for word in Ingredient:
        currEntry = currEntry + " " + word
        if (lastInt == 0):
            try:
                int(word)
                lastInt = 1
                if currEntry != "":
                    Ingredients.append(currEntry)
                currEntry = ""
            except:
                continue
            
        if (lastInt == 1):
            currEntry = currEntry + " " + word
            Ingredients.append(currEntry)
            currEntry = ""
            lastInt = 0
            
            
'''      
    print Ingredients
    print "\n"








