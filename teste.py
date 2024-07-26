from gologin import GoLogin
# from anticaptchaofficial.geetestproxyless import *

import requests,json,re,threading,time,random

from playwright.sync_api import sync_playwright, TimeoutError, expect

token_id = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NmExZTgxY2IzZjdkMmJkMzRiNWJkMmMiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NmExZTg0ZGUwZDQ4Y2RkMjJjMzAyOTgifQ.ybf44IvNKB7bsYWBVSQaSBpVHmt_PkDeR9NqpwjwILY"
# LISTA DE PROXIES - Host e Port
lista_proxies = []
lista_host = []
lista_port = []

lista_disc = []
with open(r"C:\Users\Arthur\Downloads\Automação\Contas discord\Confirmado sms\50 disc sms.txt","r") as arquivo:
    lista_limpa = []
    for linha in arquivo:
        if linha.strip():
            parte = linha.split(':')
            lista_limpa.append(parte[9])
    # for line in arquivo:
    #     lista_disc.append(line.strip())
lista_disc = [s.strip() for s in lista_limpa]

lista_disc2= []
with open(r"C:\Users\Arthur\Downloads\Automação\Contas discord\100 discord com meus gmails.txt","r") as arquivo:
    for line in arquivo:
        lista_disc2.append(line.strip())


lista_ids = []
with open(r"C:\Users\Arthur\Downloads\Automação\perfis\gologin.txt","r") as arquivo:
    for line in arquivo:
        lista_ids.append(line.strip())


lista_cookies = []
with open(r"C:\Users\Arthur\Downloads\Automação\Webshare 100 proxies - Copia.txt","r") as arquivo:
    for line in arquivo:
        lista_proxies.append(line.strip())

for linha in lista_proxies:
    parte=linha.split(':')
    lista_host.append(parte[0])
    lista_port.append(parte[1])
# twitter cookie
lista_tt = []
with open(r"C:\Users\Arthur\Downloads\Automação\Contas twitter\100 tt, spellborn, 2 leva e  on-3 txt.txt","r") as arquivo:
    for line in arquivo:
        lista_tt.append(line.strip())
#Twitter cookie 1
auth_tokens = []
with open(r"C:\Users\Arthur\Downloads\Automação\Contas twitter\12-07-2024-100contas.txt", 'r') as arquivo:
    for linha in arquivo:
        token = re.search(r'auth: (.+)', linha)
        if token:
            auth_tokens.append(token.group(1))

#Twitter cookie 2
auth_tokens_colchete = []
with open(r'C:\Users\Arthur\Downloads\Automação\Contas twitter\100 twitters 2 leva.txt', 'r', encoding='utf-8') as arquivo:
    # Iterar sobre cada linha do arquivo

    for linha in arquivo:
        # Usar expressão regular para encontrar conteúdo dentro de colchetes
        # Isso irá procurar por padrões que se pareçam com [algum_texto]
        resultados = re.findall(r'\[(.*?)\]', linha)

        # Checar se encontrou algum resultado
        if resultados:
            # Iterar sobre todos os resultados encontrados na linha
            for conteudo in resultados:
                auth_tokens_colchete.append(conteudo)

#Twitter via mail
with open(r"C:\Users\Arthur\Downloads\Automação\Contas twitter\100 twitters 2 leva.txt", 'r') as arquivo:
    for linha in arquivo:
        token = re.search(r'auth: (.+)', linha)
        if token:
            auth_tokens.append(token.group(1))

#Google key
gkeys = []
with open(r"C:\Users\Arthur\Downloads\Automação\contas gmail\Temporarias\100 gkeys.txt", 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        token = re.search(r'Key: (.+)', linha)
        if token:
            gkeys.append(token.group(1))

#Seeds
seeds = []
with open(r"C:\Users\Arthur\Downloads\Automação\Perfis\gologin1-100 (wallets 250-349).txt", 'r') as arquivo:
    for linha in arquivo:
        token = re.search(r'Seed: (.+)', linha)
        if token:
            seeds.append(token.group(1))
###########
# CRIAR PERFIS
#Usa lista de proxies para colocar 1 em cada perfil
def criar_perfis():
    gl = GoLogin({
        "token": token_id
    })

    #NUMERO DE PERFIS A CRIAR
    for i in range(100):
        #


        profile_id = gl.create({
            "name": f'perfil{i}',
            "os": 'win',
            "navigator": {
                "language": 'en-US',
                "userAgent": 'random',
                "resolution": '1920x1080',
                "platform": 'win',
            },
            'proxy': {
                'mode': 'http',  # Specify 'none' if not using proxy
                #'autoProxyRegion': 'us',
                 "host": lista_host[i],
                 "port": lista_port[i],
                 "username": "fnnjvqml",
                 "password": "xo45dczckbbo",
            },
            "webRTC": {
                "mode": "alerted",
                "enabled": True,
            },
            "storage": {
                "local": False,
                # Local Storage is special browser caches that websites may use for user tracking in a way similar to cookies.
                # Having them enabled is generally advised but may increase browser profile loading times.

                "extensions": True,
                # Extension storage is a special cotainer where a browser stores extensions and their parameter.
                # Enable it if you need to install extensions from a browser interface.

                "bookmarks": True,  # This option enables saving bookmarks in a browser interface.

                "history": False,  # Warning! Enabling this option may increase the amount of data required
                # to open/save a browser profile significantly.
                # In the interests of security, you may wish to disable this feature,
                # but it may make using GoLogin less convenient.

                "passwords": False,  # This option will save passwords stored in browsers.
                # It is used for pre-filling login forms on websites.
                # All passwords are securely encrypted alongside all your data.

                "session": False,  # This option will save browser session. It is used to save last open tabs.

                "indexedDb": False
                # IndexedDB is special browser caches that websites may use for user tracking in a way similar to cookies.
                # Having them enabled is generally advised but may increase browser profile loading times.
            }
        });

        print('profile id=', profile_id);

        #COLOCANDO ID NO BLOCO DE NOTAS
        with open(r'C:\Users\Arthur\Downloads\Automação\Perfis\gologin.txt','a') as ids:
            ids.write(profile_id  + '\n')

# COLOCAR COOKIES
# Recebe lista de perfis e lista de tokens para colocar nos perfis
def cookies_perfis():
    for i in range(100):
        url = f"https://api.gologin.com/browser/{lista_ids[i]}/cookies"

        payload = json.dumps([
            {
                "domain": ".twitter.com",
                "hostOnly": False,
                "httpOnly": False,
                "name": "auth_token",
                "path": "/",
                "sameSite": "no_restriction",
                "secure": True,
                "session": True,
                "storeId": "0",
                "value": lista_tt[i],
                "id": 1
            }
        ])
        headers = {
          'Authorization': f'Bearer {token_id}',
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

email= []
with open(r"C:\Users\Arthur\Downloads\Automação\Contas twitter\100 twitters 2 leva.txt", 'r') as arquivo:
    for linha in arquivo:
        token = re.search(r'login: @(.+)', linha)
        if token:
            email.append(token.group(1))

senha= []
with open(r"C:\Users\Arthur\Downloads\Automação\Contas twitter\100 twitters 2 leva.txt", 'r') as arquivo:
    for linha in arquivo:
        if 'password:' in linha and 'email_password:' not in linha:
            token = re.search(r'password: (.+)', linha)
            if token:
                senha.append(token.group(1))

codigo_2fa= []
with open(r"C:\Users\Arthur\Downloads\Automação\Contas twitter\100 twitters 2 leva.txt", 'r') as arquivo:
    for linha in arquivo:
        token = re.search(r'2fa: (.+)', linha)
        if token:
            codigo_2fa.append(token.group(1))

def twitter_via_mail(page,context,i):
    context.add_init_script("window.localStorage.setItem('disable-save-password', 'true');")
    #Logar

    Carregar  = False
    while Carregar ==False:
        try:
            page.goto('https://x.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJteCI6IjIifQ%3D%3D%22%7D')
            page.wait_for_selector('//input[@autocomplete="username"]').fill(email[i])
            Carregar = True
        except TimeoutError:
            continue
    #email

    page.click("//span[normalize-space()='Next']")
    #senha
    page.wait_for_selector('//input[@autocomplete="current-password"]').fill(senha[i])
    page.click("//span[normalize-space()='Log in']")
    #2fa
    nova_pagina = context.new_page()
    nova_pagina.goto("https://" + codigo_2fa[i])

    validado = False
    while validado == False:
        try:

            code = nova_pagina.wait_for_selector('//div[@id="verifyCode"]').inner_text()
            page.wait_for_selector('//input[@data-testid="ocfEnterTextTextInput"]').fill(code)
            page.wait_for_timeout(500)
            page.click("//span[normalize-space()='Next']")
            #Pegar e salvar token
            page.wait_for_url('https://x.com/home',timeout=10000)
            validado= True
        except TimeoutError:
            nova_pagina.wait_for_timeout(5000)
            continue
    cookies =context.cookies('https://www.x.com/home')

    for cookie in cookies:
        if cookie['name'] == 'auth_token':
            valor_auth_token = cookie['value']

            break  # Sai do loop após encontrar
    #connect_from_discord_token(page,context,i)
    with open(r"D:\Users\Arthur\Downloads\Automação\Contas twitter\100 tokens twitters 2 leva 16-07.txt", "a") as arquivo:
        arquivo.write(f'{valor_auth_token}\n')


#Abrir e testar
def extrair_seed(nome_arquivo):
    auth_tokens = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            token = re.search(r'Seed:(.+)', linha)
            if token:
                auth_tokens.append(token.group(1).strip())
    return auth_tokens
def connect_from_seedphrase(page,context, nome_perfil,seed):
    # Rabby
    carregar = False
    while not carregar:
        try:
            page.goto("chrome-extension://apabdpkogoomjbommgehhpgolmlmgapf/popup.html")
            page.wait_for_load_state("load")
            page.click("//span[normalize-space()='Next']", timeout=3000)
            carregar = True
        except Exception as e:
            page.reload()

    # get started
    page.wait_for_selector('//span[normalize-space()="Get Started"]').click()
    #import seed
    page.wait_for_selector('//div[normalize-space()="Import Seed Phrase"]').click()
    # senha
    page.fill('#password', 'Arthur12')
    # confirm
    page.fill('#confirmPassword', 'Arthur12')
    # next
    page.wait_for_selector('//button[@type="submit"]')
    page.click('//button[@type="submit"]')
    try:
        nova_pagina = context.wait_for_event("page")
    except TimeoutError:
        print(f'Timeout error, perfil {nome_perfil}')
        # nova_pagina= page.new_page()
        # nova_pagina.goto('chrome-extension://acmacodkjbdgmoleebolmdjonilkdbch/index.html#/import/mnemonics')
    nova_pagina.wait_for_load_state("load")
    nova_pagina.wait_for_timeout(2000)
    nova_pagina.wait_for_selector('//input[@type="password"]')
    nova_pagina.fill('//input[@type="password"]',seed)
    # Next
    nova_pagina.wait_for_timeout(2000)
    nova_pagina.wait_for_selector('//button[@type="submit"]').click()
    # Add adress
    nova_pagina.click('//button[@role="switch"]')
    nova_pagina.wait_for_selector('button[aria-checked="true"]')
    nova_pagina.wait_for_timeout(2000)
    nova_pagina.screenshot(path=fr'C:\Users\Arthur\Downloads\Automação\screenshots\comprovação\Rabby\{nome_perfil}.png')

def connect_from_discord_token(page,context,i):
    page.goto('chrome-extension://gihdkpfhgihmaefjlhiknfldbnedekdg/popup/index.html')
    page.wait_for_load_state()
    page.fill('//input[@id="token"]', lista_disc[i])
    page.wait_for_selector('//button[@id="submit"]').click()
    nova_pagina = context.wait_for_event("page")
    nova_pagina.wait_for_timeout(3000)
def rabby_new(page, context,nome_perfil):
    # Rabby
    carregar = False
    while not carregar:
        try:
            page.goto("chrome-extension://apabdpkogoomjbommgehhpgolmlmgapf/popup.html")
            page.wait_for_load_state("load")
            page.click("//span[normalize-space()='Next']", timeout=3000)
            carregar = True
        except Exception as e:
            page.reload()

    # get started
    page.click('//span[normalize-space()="Get Started"]')
    # nova carteira
    page.click('//div[normalize-space()="Create New Seed Phrase"]')
    # senha
    page.fill('#password', 'Arthur12')
    # confirm
    page.fill('#confirmPassword', 'Arthur12')
    # next
    page.click('//span[normalize-space()="Next"]')
    # mudar aba
    nova_pagina = context.wait_for_event("page")
    # show seedphrase
    nova_pagina.click('//span[normalize-space()="Show Seed Phrase"]')
    # copiar seedphrase
    nova_pagina.click('//*[@id="root"]/div/div/div/div[2]/div[3]')
    # salvar seed numa variavel
    nova_pagina.wait_for_timeout(random.uniform(0.1, 1))
    seed = pyperclip.paste()
    # Continuar
    nova_pagina.click("//*[@id='root']/div/div/div/div[3]/button")
    # mudar aba
    nova_pagina = context.wait_for_event("page")
    # Add adress
    nova_pagina.click('//button[@role="switch"]')
    nova_pagina.wait_for_selector('button[aria-checked="true"]')
    # salvar endereço numa variavel
    nova_pagina.click("css=.copy-icon")
    endereço = pyperclip.paste()
    # salva seed e endereço
    with open(r"C:\Users\Arthur\Downloads\Automação\Perfis\2 leva\wallets 250-349.txt", "a") as arquivo:
        arquivo.write(f'Nome: {nome_perfil}\nSeed: {seed}\nEndereço: {endereço}\n\n')
def rabby_recover(page, context,i):
    # Rabby
    carregar = False
    while not carregar:
        try:
            page.goto("chrome-extension://dlbkfhkahegonboadgmicaeefhalfmol/popup.html#/welcome")
            page.wait_for_load_state("load")
            page.click("//span[normalize-space()='Next']", timeout=3000)
            carregar = True
        except Exception as e:
            page.reload()

    # get started
    page.click('//span[normalize-space()="Get Started"]')
    # nova carteira
    page.click('//div[normalize-space()="Import Seed Phrase"]')
    # senha
    page.fill('#password', 'Arthur12')
    # confirm
    page.fill('#confirmPassword', 'Arthur12')
    # next
    page.click('//span[normalize-space()="Next"]')
    #colocar seed

    new = context.wait_for_event("page")
    new.fill('(//input[@type="password"])[1]',seeds[i])
    new.wait_for_timeout(1000)
    # next
    new.wait_for_selector('//button[@type="submit"]').click()
    #finalizar
    new.click('//button[@role="switch"]')
    new.wait_for_selector('button[aria-checked="true"]')
    new.wait_for_timeout(1000)


def seraph(page,context):
    #Pegar email
    nova_pagina = context.new_page()
    carregar = False
    while carregar == False:
        try:
            nova_pagina.goto('https://mail.tm/')
            carregar = True
        except TimeoutError:
            continue

    email_correto = False
    while email_correto == False:
        email_seraph = nova_pagina.wait_for_selector('//input[@value]').get_attribute('value')
        if email_seraph != ("..."):
            email_correto = True
    #Logar
    page.goto('https://rush.seraph.game/')
    page.click('//span[normalize-space()="Login/Register"]')
    page.wait_for_selector('//input[@placeholder="Please enter email address"]').fill(email_seraph)
    page.click('//span[@class="el-checkbox__inner"]')
    page.click('//button[@class="el-button el-button--primary button"]')
    #Pegar codigo

    #nova_pagina.wait_for_timeout(5000)
    #nova_pagina.reload()
    nova_pagina.click('//div[@class="truncate text-sm font-medium leading-5 text-indigo-600 dark:text-indigo-400"]')
    # nova_pagina.pause()
    iframe =nova_pagina.frame_locator('//iframe[@srcdoc]')
    code_email =iframe.locator('//div[@style="font-size: 28px;font-weight: 600;line-height: 40px;margin-bottom: 20px;"]').inner_text()
    page.wait_for_selector('//input[@type="text"]').fill(code_email)
    page.click('//button[@class="el-button el-button--primary button"]')
    # page.wait_for_selector('//span[normalize-space()="Drag the slider to complete the puzzle"]')
    # url = page.url
    #page.wait_for_selector('//div[normalize-space()="Verification Sucessfull"]',timeout=200000)

    #captcha
    page.wait_for_selector('//div[@class="custom-toast visible toast_b_bg"]',timeout=100000)

    #missoes
    page.wait_for_timeout(500)
    page.hover('//div[@class="control-item item_1"]')
    page.click('//span[normalize-space()="Start the Journey"]')

    #conectar tt
    page.click('//div[@style="top: 250px; left: 0px;"]')
    page.click('//button[@class="ant-btn css-1s7eslg ant-btn-default footer-button"]')
    new_page = context.wait_for_event("page")
    new_page.click('//span[normalize-space()="Authorize app"]')
    new_page.click('//span[normalize-space()="Complete Authorization"]')
    new_page.click('//span[normalize-space()="Go to Quest"]')
    new_page.wait_for_selector('//button[@class="ant-btn css-1s7eslg ant-btn-default footer-button-receive"]').click()

    #missoes
    new_page.click('//div[@style="top: 100px; left: 0px;"]')
    new_page.click('//span[normalize-space()="Go to Quest"]')
    new_page.click('//span[@class="ant-modal-close-x"]')

    new_page.click('//div[@style="top: 250px; left: 120px;"]')
    new_page.wait_for_selector('//button[@class="ant-btn css-1s7eslg ant-btn-default footer-button-receive"]').click()

    new_page.click('//div[@style="top: 250px; left: 240px;"]')
    new_page.wait_for_selector('//button[@class="ant-btn css-1s7eslg ant-btn-default footer-button-receive"]').click()

    new_page.click('//div[@style="top: 100px; left: 0px;"]')
    new_page.wait_for_selector('//button[@class="ant-btn css-1s7eslg ant-btn-default footer-button-receive"]').click()

    #abrir baus
    new_page.wait_for_selector('//div[normalize-space()="Go to Open Chest"]').click()

    points = new_page.wait_for_selector('//span[@class="item-point"]').inner_text()
    while int(points) >= 500:
        new_page.wait_for_selector('(//span[normalize-space()="Open chest"])[1]').click()
        new_page.wait_for_selector('//button[@class="ant-btn css-1s7eslg ant-btn-default submit"]').click()
        new_page.wait_for_selector('//span[normalize-space()="Accept"]').click()
        points = new_page.wait_for_selector('//span[@class="item-point"]').inner_text()
        print (int(points))
    new_page.goto('https://rush.seraph.game/mint')
    penas = new_page.wait_for_selector('(//div[@class="num"])[1]').inner_text()
    print(penas)







    # # #captcha
    # solver = geetestProxyless()
    # solver.set_verbose(1)
    # solver.set_key("YOUR_API_KEY_HERE")
    # solver.set_website_url(url)
    # solver.set_gt_key("captchaId value")
    # solver.set_version(4)

def seraph_mint(page,context):
    #Pegar email
    nova_pagina = context.new_page()
    carregar = False
    while carregar == False:
        try:
            nova_pagina.goto('https://mail.tm/')
            carregar = True
        except TimeoutError:
            continue

    email_correto = False
    while email_correto == False:
        email_seraph = nova_pagina.wait_for_selector('//input[@value]').get_attribute('value')
        if email_seraph != ("..."):
            email_correto = True
    #Logar
    page.goto('https://rush.seraph.game/')
    page.click('//span[normalize-space()="Login/Register"]')
    page.wait_for_selector('//input[@placeholder="Please enter email address"]').fill(email_seraph)
    page.click('//span[@class="el-checkbox__inner"]')
    page.click('//button[@class="el-button el-button--primary button"]')
    #Pegar codigo

    #nova_pagina.wait_for_timeout(5000)
    #nova_pagina.reload()
    nova_pagina.click('//div[@class="truncate text-sm font-medium leading-5 text-indigo-600 dark:text-indigo-400"]')
    # nova_pagina.pause()
    iframe =nova_pagina.frame_locator('//iframe[@srcdoc]')
    code_email =iframe.locator('//div[@style="font-size: 28px;font-weight: 600;line-height: 40px;margin-bottom: 20px;"]').inner_text()
    page.wait_for_selector('//input[@type="text"]').fill(code_email)
    page.click('//button[@class="el-button el-button--primary button"]')
    # page.wait_for_selector('//span[normalize-space()="Drag the slider to complete the puzzle"]')
    # url = page.url
    #page.wait_for_selector('//div[normalize-space()="Verification Sucessfull"]',timeout=200000)

    #captcha
    page.wait_for_selector('//div[@class="custom-toast visible toast_b_bg"]',timeout=100000)

    #missoes
    page.wait_for_timeout(500)
    page.hover('//div[@class="control-item item_1"]')
    page.click('//span[normalize-space()="Start the Journey"]')

    #conectar tt
    page.click('//div[@style="top: 250px; left: 0px;"]')
    page.click('//button[@class="ant-btn css-1s7eslg ant-btn-default footer-button"]')
    new_page = context.wait_for_event("page")
    new_page.click('//span[normalize-space()="Authorize app"]')
    new_page.click('//span[normalize-space()="Complete Authorization"]')
    new_page.click('//span[normalize-space()="Go to Quest"]')
    new_page.wait_for_selector('//button[@class="ant-btn css-1s7eslg ant-btn-default footer-button-receive"]').click()

    #missoes
    new_page.click('//div[@style="top: 100px; left: 0px;"]')
    new_page.click('//span[normalize-space()="Go to Quest"]')
    new_page.click('//span[@class="ant-modal-close-x"]')

    new_page.click('//div[@style="top: 250px; left: 120px;"]')
    new_page.wait_for_selector('//button[@class="ant-btn css-1s7eslg ant-btn-default footer-button-receive"]').click()

    new_page.click('//div[@style="top: 250px; left: 240px;"]')
    new_page.wait_for_selector('//button[@class="ant-btn css-1s7eslg ant-btn-default footer-button-receive"]').click()

    new_page.click('//div[@style="top: 100px; left: 0px;"]')
    new_page.wait_for_selector('//button[@class="ant-btn css-1s7eslg ant-btn-default footer-button-receive"]').click()

    #abrir baus
    new_page.wait_for_selector('//div[normalize-space()="Go to Open Chest"]').click()

    points = new_page.wait_for_selector('//span[@class="item-point"]').inner_text()
    while int(points) >= 500:
        new_page.wait_for_selector('(//span[normalize-space()="Open chest"])[1]').click()
        new_page.wait_for_selector('//button[@class="ant-btn css-1s7eslg ant-btn-default submit"]').click()
        new_page.wait_for_selector('//span[normalize-space()="Accept"]').click()
        points = new_page.wait_for_selector('//span[@class="item-point"]').inner_text()
        print (int(points))
    new_page.goto('https://rush.seraph.game/mint')
    penas = new_page.wait_for_selector('(//div[@class="num"])[1]').inner_text()
    print(penas)







    # # #captcha
    # solver = geetestProxyless()
    # solver.set_verbose(1)
    # solver.set_key("YOUR_API_KEY_HERE")
    # solver.set_website_url(url)
    # solver.set_gt_key("captchaId value")
    # solver.set_version(4)
def spellborn(page,context,i):
    page.goto('https://www.spellborne.gg/invite/ujjqap9gw5')
    new_page = context.new_page()
    new_page.goto('https://api999.com/google/')
    new_page.wait_for_selector('//input[@name="key_value"]').fill(gkeys[i])
    new_page.wait_for_selector('//input[@name="getMail"]').click()
    # #email
    # email=  new_page.wait_for_selector('(//td)[2]').inner_text()
    # #senha
    # senha= new_page.wait_for_selector('(//td)[3]').inner_text()
    #email
    email=  new_page.wait_for_selector('//input[@id="gmail"]').inner_text()
    print(email)
    #senha
    senha= new_page.wait_for_selector('//input[@id="password"]').inner_text()
    #ir para o spell


    page.wait_for_selector('//div[@class="sc-ewNCnA cgdAEZ"]').click()

    #conectar
    nova_pagina = context.wait_for_event("page")
    nova_pagina.wait_for_selector('//input[@type="email"]').fill(email)
    nova_pagina.click("//span[normalize-space()='Next']")
    nova_pagina.wait_for_selector('//input[@type="password"]').fill(senha)
    nova_pagina.click("//span[normalize-space()='Next']")

    nova_pagina.click('//input[@id="confirm"]')
    nova_pagina.click("//a[normalize-space()='Lakukan ini nanti']")
    nova_pagina.click("//div[normalize-space()='Konfirmasi']")

    #spell
    page.click('//div[@class="sc-bXCLgj cWXxZS"]')
    page.click("//div[normalize-space()='Continue']")
    page.click("//div[normalize-space()='Confirm Selection']")

    #historia inicial
    dialogo_meio = False

    while dialogo_meio == False:
        try:
            page.click("//div[normalize-space()='But how do I do that ?!']")
        except:
            #skipar texto
            page.click('//div[@class="sc-jQmLoh jDVBsG"]')
            page.wait_for_timeout(200)
    #lutar contra bellatrix
    page.click('(//div[@class="sc-jQmLoh jDVBsG"])[1]')
    page.click("//div[normalize-space()='Fight']")
    page.click("//div[normalize-space()='Smack']")

    #pegar kit medico
    page.click('//div[@class="sc-gsFSjX sc-hzhKNl bgBwoT bXYYKo"]')
    page.click("//div[normalize-space()='Use']")
    page.click("//div[normalize-space()='Woodot']")

    #captcha
    page.click('//div[@aria-label="showCaptcha"]')
    page.click("//div[normalize-space()='Verify']")







lista_alfabeto =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","t","s","u","v","w","x","y","z","b",]


def blocklords(page,context,i):
    page.goto('https://community.blocklords.com/ref/UD7MTJG6')
    nova_pagina = context.new_page()
    nova_pagina.goto('https://mail.tm/')
    # # Pegar email
    # nova_pagina = context.new_page()
    # carregar = False
    # while carregar == False:
    #     try:
    #         nova_pagina.goto('https://mail.tm/')
    #         carregar = True
    #     except TimeoutError:
    #         continue
    #
    # email_correto = False
    # while email_correto == False:
    #     email_seraph = nova_pagina.wait_for_selector('//input[@value]').get_attribute('value')
    #     if email_seraph != ("..."):
    #         email_correto = True
    #
    # #BLOCLORD EMAIL VERIFY
    # carregar = False
    # while carregar == False:
    #     try:
    #         page.goto('https://community.blocklords.com/ref/UD7MTJG6')
    #         carregar = True
    #     except TimeoutError:
    #         continue
    #
    # page.wait_for_selector('//input[@type="email"]').fill(email_seraph)
    # page.wait_for_selector('//button[@aria-disabled="false"]').click()

    # #Talvez esperar confirmação do email saindo
    # page.wait_for_selector("//div[normalize-space()='Thank you!']")
    #
    # #Login blocklords
    # #reload
    # nova_pagina.click('//a[@class="router-link-active router-link-exact-active group mt-1 flex items-center rounded-md px-2 py-2 text-sm font-medium leading-5 text-gray-600 transition hover:bg-gray-50 dark:text-gray-300 hover:text-gray-900 dark:focus:bg-gray-800 dark:hover:bg-gray-800 dark:focus:text-white dark:hover:text-white dark:focus:outline-none"]')
    #
    #
    # nova_pagina.click('//a[@class="truncate text-sm font-medium leading-5 text-indigo-600 dark:text-indigo-400"]')
    #
    # iframe = nova_pagina.frame_locator('//iframe[@srcdoc]')
    # code_email = iframe.locator( "//a[normalize-space()='Secure Login']").click()
    #
    # #Check dps de ir email
    # carregar = False
    # while carregar == False:
    #     try:
    #         page.wait_for_selector('//input[@type="checkbox"]').click()
    #         carregar = True
    #     except TimeoutError:
    #         #page.reload()
    #         continue
    # page.wait_for_selector('//button[@aria-disabled="false"]').click()
    # #botar username
    # tamanho = random.randint(7, 10)  # Tamanho aleatório da palavra (entre 7 e 10 caracteres)
    # palavra = ''.join(random.choice(lista_alfabeto) for _ in range(tamanho))
    # carregar = False
    # while carregar == False:
    #     try:
    #         page.wait_for_selector('//input[@placeholder="Username"]').fill(palavra)
    #         carregar = True
    #     except TimeoutError:
    #         # page.reload()
    #         continue
    # page.wait_for_selector('//button[@aria-disabled="false"]').click()



    # page.wait_for_selector('//input[@type="text"]').fill(code_email)
    # page.click('//button[@class="el-button el-button--primary button"]')

# Recebe lista de ids para abrir e codigo para automatizar açgp
def abrir_perfis_automatizados():
    for i in range(100):
        gl = GoLogin({
            "token": token_id,
            "profile_id": lista_ids[i],
            "port": i +5000
            })
        debugger_address = gl.start()


        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp("http://"+debugger_address)
            context = browser.contexts[0]

            page = context.pages[0]
            #twitter_via_mail(page, context,i)
            #semaforo.release()
            # page.goto('x.com')
            # connect_from_discord_token(page, context, i)
            #spellborn(page, context, i)
            #rabby_recover(page, context,i)


            blocklords(page,context,i)

            #semaforo.release()
            #page.close()

        #gl.stop()
def abrir_perfis_automatizados_seraph():
    for i in range(1):
        gl = GoLogin({
            "token": token_id,
            "profile_id": lista_ids[i],
            "port": i +200
            })
        debugger_address = gl.start()


        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp("http://"+debugger_address)
            context = browser.contexts[0]

            page = context.pages[0]
            #twitter_via_mail(page, context,i)
            #semaforo.release()
            #seraph(page,context)



            #page.close()

        #gl.stop()



#EXECUTAR FUNÇÕES

#criar_perfis()
#cookies_perfis()
#abrir_perfis()

#abrir_perfis_automatizados()
#abrir_perfis_automatizados_seraph()
#ronins new,recover,start
#rabby new,recover,start

#varias listar q eu n tenho



# threads = []
# limite_perfis = 3
# semaforo = threading.Semaphore(limite_perfis)
# for i in range (100):
#     semaforo.acquire()
#     thread = threading.Thread(target=criar_perfis(), args=())
#     threads.append(thread)
#     thread.start()
#     time.sleep(3)
#
# # Aguarda todas as threads completarem
# for thread in threads:
#     thread.join()

#testar para cirar discord
# Pega um item do Local Storage
# item_key = 'seu_item'  # Substitua pela chave do item que você deseja acessar
# local_storage_value = page.evaluate(f"localStorage.getItem('{item_key}')")
