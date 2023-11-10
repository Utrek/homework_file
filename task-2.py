def do_cook_book (file):
    file = open(file,'r',encoding='utf-8')
    ingredient_dict = {}
    ingredients = []
    key_list = ['ingredient_name', 'quantity', 'measure']
    dishes_ingredients = []
    quantity_ingredients = []
    cook_book = {}
    cook_ingredients=[]
    cook_book_dishes=[]
    while True:
        line = file.readline()
        if "|" not in line and len(line) > 2:
            key = line.strip()
            cook_book_dishes.append(key)
        elif "|" in line:
            ingredients.append( line.strip().split('|'))   
        elif "|" not in line and len(line.strip()) == 1: 
            quantity_ingredients.append(int(line.strip()) ) 
        elif not line:
            break
    for ingredient in ingredients:
        ingredient_dict = dict(zip(key_list, ingredient))
        dishes_ingredients.append(ingredient_dict)   
    count1 = 0
    count2 = quantity_ingredients[0]
    cook_ingredients.append(dishes_ingredients[0:quantity_ingredients[0]])
    for n in range(1,len(quantity_ingredients)): 
        count1 = count2 
        count2 += quantity_ingredients[n]
        cook_ingredients.append(dishes_ingredients[count1:count2])
    for i in range(0,4):
        for j in range(0,4):
            if i == j:
                cook_book[cook_book_dishes[i]] = cook_ingredients[j]
    return cook_book

cook_book = do_cook_book ('recipes.txt')

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list_by_dishes:
                shop_list_by_dishes[ingredient['ingredient_name']] = {'measure':ingredient['measure'],'quantity':int(ingredient['quantity'])*person_count}
            elif ingredient['ingredient_name']  in shop_list_by_dishes:
                quantity_double_ingredient = shop_list_by_dishes[ingredient['ingredient_name']]['quantity']
                shop_list_by_dishes[ingredient['ingredient_name']] = {'measure':ingredient['measure'],'quantity':int(ingredient['quantity'])*person_count+quantity_double_ingredient}
    for key,value in shop_list_by_dishes.items(): 
        print(key, ':', value)


get_shop_list_by_dishes(['Фахитос', 'Омлет','Запеченный картофель','Утка по-пекински'], 1)


     


    
     



  
     
     


    


        

    


    
       
              

 
        
            


  



            
        







