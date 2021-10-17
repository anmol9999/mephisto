menu = {

    'Veg manchurian':189,
    'frieed rice ':100,
    'momos':80

}

new_menu = {
    'chicken manchurian': 250,
    'chicken momos':160
}

print('before update ',menu)
menu.update(new_menu)
print('after update', menu)

update_menu = {
    'veg momos':100,
    'veg chowmein':120
}

menu.update(update_menu)
print('final menu',menu)