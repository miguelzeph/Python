from selenium import webdriver


# Tem que colocar caminho do driver (neste caso Chrome)
chrome = webdriver.Chrome('./driver_Chrome79/chromedriver')

# Abrir a página do Python Club
chrome.get('http://pythonclub.com.br/')

# Seleciono todos os elementos que possuem a class post
posts = chrome.find_elements_by_class_name('post')

# Para cada post printar as informações
for post in posts:

    # O elemento `a` com a class `post-title`
    # contém todas as informações que queremos mostrar
    post_title = post.find_element_by_class_name('post-title')

    # `get_attribute` serve para extrair qualquer atributo do elemento
    post_link = post_title.get_attribute('href')

    # printar informações
    print(f"Titulo: {post_title.text}, Link: {post_link}")

# Fechar navegador
chrome.quit()