# Protótipo para a APS sobre Web Scraping com Python usando BeautifulSoup e requests
# O site da UNIP está sendo usado como alvo do projeto

from bs4 import BeautifulSoup
import requests

curso_desejado = input('Informe o curso desejado: ')
print('Resultados que incluem "{}":'.format(curso_desejado))

def procura_cursos():
    link_texto = requests.get('https://unip.br/cursos/index.aspx').text
    # faz a requisição da página de cursos do site da UNIP
    soup = BeautifulSoup(link_texto, 'lxml')
    # criando objeto 'soup' que recebe a página e o parser method 'lxml' a ser usado
    cursos = soup.find_all('div', class_='card h-100 shadow-sm')
    # aqui todos os cursos e suas informações são adicionados à 'cursos'
    aux = 0
    # variável auxiliar para verificar se o curso foi informado (provisório)
    for curso in cursos:
    # percorre curso por curso entre todos os cursos
        nome_curso = curso.find('h3', class_='card-title h6 mb-0').text
        if curso_desejado in nome_curso:
        # após verificar se o valor informado faz parte do nome de um curso, as informações são exibidas caso verdadeiro
            print('')
            print(' Curso:\n{}\n'.format(nome_curso))
            descricao = curso.find('small', class_='text-secondary').text.replace('  ', '')
            print(' Descrição:\n{}\n'.format(descricao))
            sobre = curso.a['href']
            # recebe apenas o link (apenas as partes finais link, na verdade) ao invés de todo o conteúdo da tag 'a'
            print(' Saiba mais sobre o curso:\nhttps://unip.br/cursos/{}'.format(sobre))
            print('')
            aux = 1
        
    if aux == 0:
        print('Curso não encontrado.')

procura_cursos()
# Outras funções (def) devem ser adicionadas conforme a necessidade ou demanda