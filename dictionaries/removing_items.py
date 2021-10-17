hotel_menu = {
'Veg manchurian': 189, 
'frieed rice ': 100, 
'momos': 80, 
'chicken manchurian': 250, 
'chicken momos': 160, 
'veg momos': 100,
'veg chowmein': 120,
'costly food item': 999
}

# remove
if 'costly food item' in hotel_menu:  

    rmv_value = hotel_menu.pop('costly food item')
    print(rmv_value)
    print(hotel_menu)


rnd_value = hotel_menu.popitem()
print(rnd_value)
print(hotel_menu)

hotel_menu.clear()
print(hotel_menu)