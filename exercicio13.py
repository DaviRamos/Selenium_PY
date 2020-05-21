from selenium.webdriver import Firefox
from time import sleep

url = 'http://selenium.dunossauro.live/aula_06.html'

b = Firefox()

b.get(url)

#
# Usando o atributo Name [att*=valor]
# nome = b.find_element_by_css_selector('[name*= "ome"]')
# senha = b.find_element_by_css_selector('[name*= "nha"]')

# nome.send_keys('Davi')
# senha.send_keys('batata')

texto = b.find_elements_by_css_selector('form ~ br')

print(texto)