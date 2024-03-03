#   
# Coding in times of COVID-19.
# Hecho por Jonathan Friz B. jfriz[@]protonmail.com



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd
import random

driver = webdriver.Chrome('/Users/jonfen/Documents/Python test/chromedriver') 
print()
print("Activa casilla para que se descarge PDF y no sólo se abran en navegador")
#print('==>    chrome://settings/content/pdfDocuments?search=PDF   <==')
pdf_toggle = driver.get("chrome://settings/content/pdfDocuments?search=PDF")
time.sleep(4)

file = input("¿Cuál es el nombre de tu archivo excel, incluye extesión  si es xlsx o xls? ")

time.sleep(30)
df = pd.read_excel(file, engine = 'openpyxl')
lista_links = df['TITULO'].to_list()

for i in range(0, len(lista_links)):
    try:
        driver.get('https://scholar.google.com')
        title = driver.find_element_by_name("q")
        title.send_keys(lista_links[i])
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        html = driver.page_source
        time.sleep(3) 
        element = driver.find_element_by_xpath("/html/body/div/div[10]/div[2]/div[2]/div[2]/div/div[1]/div/div/a")
        time_sleep = random.uniform(3.0, 9.4)
        abrir = element.click()
        print(i+1, '^^^Yeah baby!^^^ - Encontrado en Google Scholar', lista_links[i])
    except:
            print(i+1, 'No encontrado en Google Scholar', lista_links[i])
            print("Intentaremos en Semantic Scholar")
            print()
            try:
                driver.get('https://www.semanticscholar.org')
                title = driver.find_element_by_name("q")
                title.send_keys(lista_links[i])
                driver.find_element_by_name("q").send_keys(Keys.ENTER)
                time_4 = random.uniform(3.0, 5.3)
                time.sleep(time_4) 
                element = driver.find_element_by_partial_link_text("View PDF")
                abrir = element.click()
                print(i+1, '^^^Yeah baby!^^^ - Encontrado en Semantic Scholar', lista_links[i])
            except:
                    print(i+1, "No encontrado en Semantic Scholar", lista_links[i])
                    print("Intentaremos en Research Gate")
                    print()
                    try:
                        driver.get('https://www.researchgate.net/search')
                        time_4 = random.uniform(1.8, 3.5)
                        time.sleep(time_4)
                        title = driver.find_element_by_name("q")
                        title.send_keys(lista_links[i])
                        driver.find_element_by_name("q").send_keys(Keys.ENTER)
                        html = driver.page_source
                        time.sleep(3) 
                        preview = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/a/div/div")
                        abrir_1 = preview.click()
                        time_1 = random.uniform(8.0, 12.3)
                        time.sleep(time_1)
                        element = driver.find_element_by_xpath("/html/body/div[1]/main/section/div[1]/div[1]/div/div[2]/div/div/div/div[2]/a/span")
                        abrir_2 = element.click()
                        time_2 = random.uniform(8.7, 12.4)
                        time.sleep(time_2)
                        element_2 = driver.find_element_by_xpath("/html/body/div[1]/main/section/section[1]/div/aside/div/div/div/div[2]/div/a[1]/span")
                        abrir_3 = element_2.click()
                        time.sleep(time_2)
                        print(i+1, '^^^Yeah baby!^^^ - Encontrado - en Research Gate', lista_links[i])
                    except: 
                            print(i+1, "No encontrado en Research Gate -", lista_links[i])
                            print("No encontrado del todo, :(")
                            print()
                            pass        

    time_sleep = random.uniform(7.0, 8.0)
    time.sleep(time_sleep)
    print("Espera", time_sleep, "segundos")



# ----------------------------------------------------------
# The nerd part
# ----------------------------------------------------------
print(colored("Never send a human to do a machine's job!", "red", attrs=["bold"]))

    
#   ╦┌─┐┌┐┌┌─┐┌┬┐┬ ┬┌─┐┌┐┌   ╔═╗┬─┐┬┌─┐  ╔╗  
#   ║│ ││││├─┤ │ ├─┤├─┤│││   ╠╣ ├┬┘│┌─┘  ╠╩╗ 
#  ╚╝└─┘┘└┘┴ ┴ ┴ ┴ ┴┴ ┴┘└┘   ╚  ┴└─┴└─┘  ╚═╝o