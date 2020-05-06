from selenium.webdriver import Firefox
from time import sleep

url = 'https://selenium.dunossauro.live/aula_04_a.html'

navegador = Firefox()

navegador.get(url)

lista_n_ordenada = navegador.find_element_by_tag_name('ul')  # 1

lis = lista_n_ordenada.find_elements_by_tag_name('li')  # 2

lis[0].find_element_by_tag_name('a').text  # 3

navegador.quit()