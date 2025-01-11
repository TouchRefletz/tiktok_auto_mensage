import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

################################################################

# Código abaixo para abrir o navegador com a sua conta do TikTok

################################################################


chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe" # Troque caso o caminho do seu navegador for outro

options = webdriver.ChromeOptions() # Habilita a opção de inicializar o Chrome com scripts com opções personalizadas
options.binary_location = chrome_path # Adiciona o caminho do Chrome citado anteriormente nas opções de inicialização do script
options.add_argument("--profile-directory=Default") # Por padrão, é aberto o perfil padrão do navegador. Troque caso seja necessário para "--profile-directory=Profile 1", por exemplo

options.add_argument("user-data-dir=C:/Users/<USUARIO>/AppData/Local/Google/Chrome/User Data") #Seleciona as informações do perfis dos usuários existentes no seu navegador. Troque <USUARIO> pelo o nome do seu usuário na pasta "C:\Users"

chromedriver_path = "chromedriver.exe" # Seleciona o driver atual instalado do Chrome para rodar o script. O driver instalado para o chrome é recomendado para as versões mais atuais do programa. Caso não funcione, baixe um novo driver em "https://sites.google.com/chromium.org/driver/downloads" e troque o arquivo .exe dessa pasta

service = Service(chromedriver_path) # Inclui o driver do chrome baixado na inicialização do Chrome com o script

driver = webdriver.Chrome(service=service, options=options)  # Inicia o chrome com as configurações citadas anteriormente no código


###############################################################

# Código abaixo para mandar mensagens automaticamente no TikTok

###############################################################


time.sleep(5) # Delay para evitar problemas no código por conta do carregamento. Ajuste caso o delay seja pequeno

driver.get("https://www.tiktok.com/messages") # Abre as mensagens do seu TikTok

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-1mez8np-PInfoNickname"))) # Delay para evitar problemas no código por conta do carregamento. Ajuste caso o delay seja pequeno

nicknames = driver.find_element(By.CLASS_NAME, "css-1mez8np-PInfoNickname") # Seleciona todos os usernames que existem na sua aba de conversas

nicknames_to_keep = ["<USUARIO1>", "<USUARIO2>", "<USUARIO3>"] # Nessa lista estão os nomes na qual você deseja enviar as mensagens. Troque <USUARIO1>, <USUARIO2>, e <USUARIO3> para os nomes dos usuários desejados

filtered_nicknames = [element for element in nicknames if any(name in element.get_attribute("innerHTML") for name in nicknames_to_keep)] # Filtra os nomes que você citou acima com base em todos os nomes selecionados anteriormente em "nicknames"

# ALERTA: Caso algum problema ocorra entre as linhas 44 e 46 do código, provavelmente será pelo nome de usuário não estar correto/não existir. Por favor cheque duas vezes antes de rodar o código definitivamente

for element in filtered_nicknames: # Roda um código em cada usuário selecionado anteriormente
    main_div = element.find_element(By.XPATH, "../../..")  # Encontra a div clicável do usuário
    main_div.click() # Seleciona essa div clicando

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.public-DraftEditor-content[contenteditable="true"]'))) # Delay para evitar problemas no código por conta do carregamento. Ajuste caso o delay seja pequeno
    
    input_element = driver.find_element(By.CSS_SELECTOR, '.public-DraftEditor-content[contenteditable="true"]') # Localiza o campo de texto pra mandar a mensagem

    input_element.send_keys("<MENSAGEM>" + Keys.RETURN) # Envia a mensagem digitando uma mensagem e clicando em "Enter" logo em seguida. Caso queira modificar a mensagem que será enviada, modifique <MENSAGEM>, entre as aspas

    time.sleep(3) # Delay para evitar problemas no código por conta do carregamento. Ajuste caso o delay seja pequeno

driver.close() # Fecha o navegador automaticamente