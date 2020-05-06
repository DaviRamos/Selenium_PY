from selenium.webdriver import Firefox
from time import sleep

url = 'https://selenium.dunossauro.live/exercicio_01.html'

navegador = Firefox()

navegador.get(url)

sleep(2)

ps = navegador.find_elements_by_tag_name('p')
h1 = navegador.find_element_by_tag_name('h1').text

lista_de_dicionarios = {}

for p in ps:
        lista_de_dicionarios.update(
            {p.get_attribute('atributo'): p.text}
        )
{h1: lista_de_dicionarios}

navegador.quit()