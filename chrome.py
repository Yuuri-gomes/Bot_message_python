import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def new_chat(contato): 
    new_chat = driver.find_element_by_xpath('//div[@class="gQzdc"]')
    new_chat.click()

    # Enter the name of chat
    novo_contato = driver.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
    novo_contato.send_keys(contato)

    time.sleep(1)

    try:
        # Select for the title having user name
        usuario = driver.find_element_by_xpath(f'//span[@title="{contato}"]')
        usuario.click()
    except NoSuchElementException:
        print(f'Usuário: {contato}, não econtrado na lista de contato')


if __name__ == '__main__':

    # Register the drive
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.get('https://web.whatsapp.com/')

    time.sleep(15)

    lista_de_contatos = ['']

    for contato in lista_de_contatos:

        try:
            usuario = driver.find_element_by_xpath(f'//span[@title="{contato}"]')
            usuario.click()
        except NoSuchElementException as se:
            new_chat(contato)

        campo_de_texto = driver.find_element_by_xpath('//div[@class="_1Plpp"]')
        campo_de_texto.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

        campo_de_texto = driver.find_element_by_xpath('//button[@class="_35EW6"]')
        campo_de_texto.click()
