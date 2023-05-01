from requests_html import HTMLSession

sessao = HTMLSession() #iniciando a sessao
url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'
resposta = sessao.get(url) # pegando a resposta da url
links = resposta.html.find('#ad-list li a') # buscando informacoes no css atraves do ad-list, dentro da tag li e por fim na tag
anuncios = [] # armazenar os dados extraídos de cada página

for link in links:
    url_iphone = link.attrs['href'] #pegando o dominio de cada anúncio
    resposta_iphone = sessao.get(url_iphone) #fazendo a requisição das informações do link para o servidor
    titulo = resposta_iphone.html.find('h1', first=True).text #
    preco = resposta_iphone.html.find('h2', first=True).text
    anuncios.append({
        'url': url_iphone,
        'titulo': titulo,
        'preco': preco
    })
print(anuncios)