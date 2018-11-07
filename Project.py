Food_court_dictionaries={'Food_court_9':{'zi char':('Food stall 1',3.00), 'ma la xiang guo': ('Food stall 2',9.50),'bibimbap':('Food stall 4', 5.00), 'shang hai bun':('Food stall 3', 1.50)}, \
	'Foodgle_food_court':{'chicken rice':('Food stall 2', 3.00), 'phad thai':('Food stall 1', 3.50),'nasi ayam panggang':('Food stall 3', 4.00), \
                     	'bak kut teh': ('Food stall 4', 4.50),'hokkein mee':('Food stall 5', 3.50), 'crispy chicken':('Food stall 6', 3.00)}, \
	'Northhill_food_court':{'zi char':('Food stall 1', 5.00), 'fisball noodle': ('Food stall 2', 2.80),'baked rice':('Food stall 4', 4.00), 'mixed rice':('Food stall 3', 4.00), \
                     	'prawn paste chicken':('Food stall 3', 9,90),}, \
	'Pioneer_food_court':{'tom yum soup':('Food Stall 1', 6.00), 'yong tau foo':('food stall 2', 4.00)}, \
	'Quad_cafe':{'fried beef kway teow':('Food stall 4', 5.00), 'laksa':('Food stall 3', 3.00),'korean ramen': ('Food stall 5', 3.50), 'watercress soup':('Food stall 2', 4.00)}, \
	'Food_court_13':{'tonkatsu ramen':('Food stall 5', 6.80), 'Tonkatsu Original Curry rice':('Food stall 5', 5.00),'cha shu donburi bowl':('Food stall 5', 5.00), \
               	'black pepper chicken':('Food stall 2', 6.00)}, \
	'Food_court_2':{'bbq pork chop':('Food stall 1', 4.00), 'beef ball soup':('Food stall 3', 3.00),'ayam penyant':('Food stall 2', 4.50), 'xiao long bao':('Food stall 4', 4.30),\
              	'lemon chicken rice':('Food stall 5', 3.00), 'yong tau foo':('Food stall 6', 4.00), 'ice cream waffles':('Food stall 7', 2.50), 'ice cream': ('Food stall 7', 1.00)},\
	
	'Northspine_food_court':{'bak chor mee':('Food stall 2', 2.20), 'nasi padang':('Food stall 1', 4.00), 'mini wok':('Food stall 1', 4.00), 'ma la xiang guo':('Food stall 4', 10.00),\
                      	'bibimbamp':('Food stall 5', 4.50), 'veitnanese beef Noodle':('Food stall 6', 4.80),'chicken chop':('Food stall 7', 4.00), 'pig organ soup':('Food stall 3', 4.00),\
                      	'mixed rice':('Food stall 8', 4.00)}, \
	'Food_court_1':{'baked rice':('Food stall 1', 5.00),'sambal spaghetti':('Food stall 2',4.60),'Garlic Fried Rice':('Food stall 2', 2.00), \
              	'grilled chicken with satay sauce':('Food stall 2', 5.80)}, \
	'Food_court_11':{'ice cream waffles':('Food stall 11', 2.00),'ma la xiang guo': ('Food stall 4', 10.00)}, \
	'Food_court_14':{'ban mian':('Food stall 1', 3.00), 'taiwanese chicken chop rice':('Food stall 2', 5.00),'bee hoon kway':('Food stall 1', 2.80), 'chicken chop': ('Food stall 4', 7.90),\
               	'nasi lemak': ('Food stall 3', 3.50), 'dry ramen': ('Food stall 1', 2.80), 'nasi penyet':('Food stall 5', 4.50),'baked rice':( 'Food stall 4', 4.20)}, \
	'Food_court_16':{'tonkatsu ramen':('Food stall 2', 6.00), 'black tonkatsu udon':('Food stall 2', 6.00),'curry rice':('Food stall 2', 5.00), \
               	'chicken rice':('Food stall 1',3.00),'chile burger': ('Food stall 3', 5.00)}, \
	'Koufu':{'ke kou mian':('Food stall 3', 3.50), 'hotplate chicken fuyong':('Food stall 2', 4.30),'salmon rice bowl': ('Food stall 1', 4.00), \
       	'fishball noodle': ('Food stall 3', 3.00)}, \
	'NIE_canteen':{'bak chor mee':('Food stall 1', 2.50), 'fish ball noodle':('Food stall 1', 2.50),'prawn noodle':('Food stall 2', 2.50), 'ba chor mee':('Food stall 2', 2.50), \
            	'chicken rice':('Food stall 6', 2.50)}, \
	}

#Check the user  rich or poor
def check_money():
    dict_1={}
    money=-1
    while money<0:
        try:
            money=float(input("How much money do you have?"))
            if money<0:
                print("Your money can't have a negative value")
        except ValueError:
            print("you get an ValueError,please input a number!")
        except:
            print("you get an error,please input a number!")
    while True:
        for food_court, info_on_food in Food_court_dictionaries.items():
            for type_of_food,food_stall_and_price in info_on_food.items():
                if  food_stall_and_price[1]<money:
                    dict_1[food_court]={type_of_food:food_stall_and_price}
        if len(dict_1)==0:
            money=float(input("Sorry,but your money is not enough,please input another amount: "))
            continue
        else:
            print(dict_1)
            break
check_money()


            


    

                
