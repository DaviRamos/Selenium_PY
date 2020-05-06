from selenium.webdriver import Firefox
from time import sleep

url = 'https://selenium.dunossauro.live/exercicio_02.html'

navegador = Firefox()

navegador.get(url)

sleep(2)

a = navegador.find_element_by_tag_name('a')

resultado = 'Você ganhou'
msg= ''

while resultado not in msg:
    a.click()
    msg = navegador.find_elements_by_tag_name('p')[-1].text
    print(msg)
    
navegador.quit()