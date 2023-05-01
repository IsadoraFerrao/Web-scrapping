from requests_html import HTMLSession

sessao = HTMLSession() #iniciando a sessao
url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'
resposta = sessao.get(url) # pegando a resposta da url

links = resposta.html.find('#ad-list li a') # buscando informacoes no css atraves do ad-list, dentro da tag li e por fim na tag
for link in links:
	print(link.attrs['title']) #dicionário que contém todos os atributos HTML do elemento