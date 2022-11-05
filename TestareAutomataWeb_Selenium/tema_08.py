#Exerciții obligatorii - grad de dificultate: Usor spre Mediu
'''
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app

Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# initializam chrome
s = Service(ChromeDriverManager().install()) # Stocam serviciul de chrome
chrome = webdriver.Chrome(service=s) # definirea unei variabile care va stoca driverul de chrome
# maximizam fereastra
chrome.maximize_window() # este o metoda folosita pentru maximizarea browserului


# # SITE 1, NAME-5, ID-3, TAG_NAME-1, CLASS_NAME-1
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# chrome.find_element(By.ID,'ez-accept-all').click() # accepta cookies
#
# chrome.find_element(By.NAME,'firstname').send_keys('test')
# chrome.find_element(By.NAME,'lastname').send_keys('hungry')
#
# gen=chrome.find_elements(By.NAME,'sex')
# gen[1].click()
# years_of_experiance=chrome.find_elements(By.NAME,'exp')
# years_of_experiance[2].click()
#
# chrome.find_element(By.ID,'datepicker').send_keys('25/10/2022')
# profesie=chrome.find_elements(By.NAME,'profession')
# profesie[1].click()
# chrome.find_element(By.ID,'tool-2').click()
#
# lista_input=chrome.find_elements(By.TAG_NAME,'input')
# sleep(3)
# lista_input[11].clear()
# lista_input[11].send_keys('16/05/2019')
# sleep(3)
#
# continent=Select(chrome.find_element(By.CLASS_NAME,'input-xlarge'))
# continent.select_by_visible_text('Europe')
#
#
# sleep(5)
# chrome.quit()

# # SITE 2, CLASS_NAME-2, TAG_NAME-1, CSS_SELECTOR-3
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# elemente=chrome.find_elements(By.CLASS_NAME,'form-control')
# elemente[0].send_keys('adresa_test')
# elemente[1].send_keys('strada-test')
# varianta2=chrome.find_elements(By.TAG_NAME,'input')
# varianta2[2].send_keys('strada2-test')
# varianta2[3].send_keys('oras')
# sleep(3)
# chrome.find_element(By.CSS_SELECTOR,'input#administrative_area_level_1').send_keys('Tara,Stat') # dupa id
# chrome.find_element(By.CSS_SELECTOR,'input.form-control').clear() # dupa clasa
# sleep(3)
# chrome.find_element(By.CSS_SELECTOR,'input[placeholder="Enter address"]').send_keys('Test CSS_SELECTOR') #dupa atribut-valoare
# elemente[5].send_keys('codul postal')
# varianta2[6].send_keys('Tara')
# sleep(3)
# chrome.find_element(By.CLASS_NAME,'dismissButton').click()
# sleep(5)
# chrome.quit()

#
# # SITE 3, LINK_TEXT-2, PARTIAL_LINK_TEXT-2
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT,'Dropdown').click()
# drop=Select(chrome.find_element(By.ID,'dropdown'))
# drop.select_by_visible_text('Option 2')
# sleep(3)
# drop.select_by_value('1')
# sleep(4)
# chrome.get('https://the-internet.herokuapp.com/')
# sleep(3)
# chrome.find_element(By.PARTIAL_LINK_TEXT,'Red').click()
# sleep(3)
# chrome.find_element(By.LINK_TEXT,'here').click()
# sleep(3)
# chrome.find_element(By.PARTIAL_LINK_TEXT,'2').click()
# sleep(3)
#
# chrome.quit()


'''
- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.
'''

'''
Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.
'''

chrome.get('https://www.phptravels.net/')
chrome.find_element(By.XPATH,'//button[@id="ACCOUNT"]').click() # dupa atribut valoare
sign=chrome.find_element(By.XPATH,'//a[contains(text(),"Signup")]').click() #dupa partial text
chrome.find_element(By.XPATH,'(//input[@class="form-control"])[1]').send_keys('heyBeautiful') #xPath ca lista, am luat un singur element
#din copil in parinte, la un frate si la copilul lui
chrome.find_element(By.XPATH,'(//input[@class="form-control"])[1]//parent::div//parent::div/following-sibling::div/div/input').send_keys('Smile')
chrome.find_element(By.XPATH,'//*[@placeholder="Phone"]').send_keys('12345') #xPath incomplet
chrome.find_element(By.XPATH, '//input[@placeholder="Password"] | //input[@name="email"]').send_keys('hihi@gmail.com') # va interactiona cu primul element gasit
lista_elemente=chrome.find_elements(By.XPATH,'//input[@class="form-control"]') # folosirea unei liste
lista_elemente[4].send_keys('pass')
sleep(5)
chrome.quit()

'''
Exerciții extra - Opțional
https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sh
eet/
'''

# chrome.find_element(By.XPATH,'//*[@id="select2-account_type-container"]').click()
# chrome.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Customer')