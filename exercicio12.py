from selenium.webdriver import Firefox
from time import sleep

url = 'http://selenium.dunossauro.live/aula_06_a.html'

b = Firefox()

b.get(url)

# Usando o atributo [attr=valor]

#nome = b.find_element_by_css_selector('[type = "text"]')
#senha = b.find_element_by_css_selector('[type = "password"]')
#btn = b.find_element_by_css_selector('[type = "submit"]')

# Usando o atributo Name [attr=valor]
#nome = b.find_element_by_css_selector('[name = "nome"]')
#senha = b.find_element_by_css_selector('[name = "senha"]')
#btn = b.find_element_by_css_selector('[name = "l0c0"]')

# Usando o atributo Name [att*=valor]
nome = b.find_element_by_css_selector('[name*= "ome"]')
senha = b.find_element_by_css_selector('[name*= "nha"]')
btn = b.find_element_by_css_selector('[name*= "l0"]')

nome.send_keys('Davi')
senha.send_keys('batata')
btn.click()

#b.find_element_by_css_selector('input').send_keys('Davi')