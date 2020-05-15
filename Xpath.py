from parsel import Selector
import pprint

with open("receita.html") as f:
    content = f.read()

response = Selector(text=content)

# print(response.get())

# print(response.xpath("/"))

# print(response.xpath("/html"))

# print(response.xpath("/html/head"))

# print(response.xpath("/html/head").getall())

# print(response.xpath("/html/head/title").getall())

# print(response.xpath("//h1").getall())

# Qualquer texto sem filhos
#print(response.xpath("//h1/text()").getall())

# Qualquer texto mesmo no filho
#print(response.xpath("//h1//text()").getall())

# print(response.xpath("//ul[2]").getall())

# print(response.xpath("//ul[2]/li[3]").getall())

# texto vazio
# print(response.xpath("//ul[2]/li[3]/text()").getall())

# ['3', ' ', 'ovos']
# print(response.xpath("//ul[2]/li[3]//text()").getall())

# ['3', ' ', 'ovos']
# print(response.xpath("//ul[2]/li[3]/span/text()").getall())

#pp = pprint.PrettyPrinter(indent=8)

# ['<li>Junte meia xÃ\xadcara (chÃ¡) de Ã¡gua quente e mexa com uma colher.</li>']
#pp.pprint(response.xpath("//ol[1]/li[2]").getall())

# ['ingredients', 'instructions']
# print(response.xpath("//h1/@data-section").getall())

# print(response.xpath("//a"))

# [<Selector xpath='//a/@href' data='https://rennerocha.github.io/xpath/'>]
# print(response.xpath("//a/@href"))

# ['https://rennerocha.github.io/xpath/']
# print(response.xpath("//a/@href").getall())

# ['<h1 data-section="ingredients">Ingredientes</h1>', '<h1 data-section="instructions">InstruÃ§Ãµes</h1>']
# print(response.xpath("//h1[@data-section]").getall())

# ['<tr>\n                <th>Quantidade</th>\n                <th>Ingrediente</th>\n            </tr>']
# print(response.xpath("//tr[th]").getall())

# Negando o contains
# print(response.xpath("//tr[not(th)]").getall())

# ['<li>Cubra com papel-alumÃ\xadnio e leve ao forno mÃ©dio (180Â°C), em banho-maria, por cerca de 1 hora e 30 minutos.</li>']
# print(response.xpath("//li[contains(text(), 'forno')]").getall())

# o ponto pega qualqer coisa referente ao elemento neste caos o LI
# ['<li><span class="qtde" data-qtde="1">1</span> <span>caixa de leite de condensado</span></li>', '<li><span class="qtde" data-qtde="2">2</span> <span>medidas de leite</span></li>']
# print(response.xpath("//li[contains(., 'leite')]").getall())

#print(response.xpath("//span[@data-qtde=2]").getall())

#print(response.xpath("//span[@data-qtde!=2]").getall())

#print(response.xpath("//span[@data-qtde>1]").getall())

#print(response.xpath("//span[@data-qtde<2]").getall())

#print(response.xpath("//ol/li").getall())

# print(response.xpath("(//ol/li)[2]"))

### Ver Parent Sibling e anchestror