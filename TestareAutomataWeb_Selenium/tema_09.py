# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
'''
Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication
tearDown()
Quit browser
'''

import unittest
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Login(unittest.TestCase):
    AUTHENTICATION_LINK=(By.LINK_TEXT,'Form Authentication')
    LOGIN_BUTTON=(By.XPATH,'//button[@class="radius"]')
    USER=(By.ID,'username')
    PASSWORD=(By.ID,'password')
    ERROR=(By.ID,'flash')
    SUCCES=(By.CLASS_NAME,'success')
    LOGOUT_BUTTON=(By.CLASS_NAME,'icon-signout')

    def setUp(self):
        # initializam chrome
        s = Service(ChromeDriverManager().install())  # Stocam serviciul de chrome
        self.chrome = webdriver.Chrome(service=s)  # definirea unei variabile care va stoca driverul de chrome
        # maximizam fereastra
        self.chrome.maximize_window()  # este o metoda folosita pentru maximizarea browserului
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.AUTHENTICATION_LINK).click()
        sleep(3)

    def tearDown(self):
        self.chrome.quit()

    '''
     ● Test 1
    - Verifică dacă noul url e corect
    '''
    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

    '''
    ● Test 2
    - Verifică dacă page title e corect
    '''
    def test_title(self):
        actual=self.chrome.title
        expected='The Internet'
        self.assertEqual(actual,expected,'Titlul e incorect')
    '''
    ● Test 3
    - Verifică textul de pe elementul xpath=//h2 e corect
    '''
    def test_element_corect(self):
        actual=self.chrome.find_element(By.XPATH,'//h2').text
        expected='Login Page'
        self.assertEqual(actual,expected,'Elementul nu corespunde')
    '''
    ● Test 4
    - Verifică dacă butonul de login este displayed
    '''
    def test_login_displayed(self):
        elem=self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(elem.is_displayed(),'Butonul Login nu e pe pagina')

    '''
    ● Test 5
    - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    '''
    def test_link_corect(self):
        actual=self.chrome.find_element(By.LINK_TEXT,'Elemental Selenium').get_attribute('href')
        expected='http://elementalselenium.com/'
        self.assertEqual(actual,expected,'Linkul href nu e corect')
    '''
    ● Test 6
    - Lasă goale user și pass
    - Click login
    - Verifică dacă eroarea e displayed
    '''
    def test_error(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        eroare=self.chrome.find_element(*self.ERROR)
        self.assertTrue(eroare.is_displayed(),'Nu apare eroarea de login')
    '''
    ● Test 7
    - Completează cu user și pass invalide
    - Click login
    - Verifică dacă mesajul de pe eroare e corect
    - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
    expected = 'Your username is invalid!'
    self.assertTrue(expected in actual, 'Error message text is
    incorrect')
    '''
    def test_mesaj_de_eroare_corect(self):
        self.chrome.find_element(*self.USER).send_keys('hi_darling')
        self.chrome.find_element(*self.PASSWORD).send_keys('1111')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    '''
    ● Test 8
    - Lasă goale user și pass
    - Click login
    - Apasă x la eroare
    - Verifică dacă eroarea a dispărut
    '''
    def test_dispare_eroarea(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(By.CLASS_NAME,'close').click()
        try:
            self.chrome.find_element(*self.ERROR)
        except NoSuchElementException:
            print('Eroarea a disparut, este bine')

    '''
    ● Test 9
    - Ia ca o listă toate //label
    - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
    Password)
    - Aici e ok să avem 2 asserturi
    '''
    def test_text_corect(self):
        lista_elemente=self.chrome.find_elements(By.XPATH,'//label')
        actual_1=lista_elemente[0].text
        expected_1='Username'
        actual_2=lista_elemente[1].text
        expected_2='Password'
        self.assertEqual(actual_1,expected_1,f'Eroare: actual:{actual_1}, expected:{expected_1}')
        self.assertEqual(actual_2,expected_2,f'Eroare: actual:{actual_2}, expected:{expected_2}')

    '''
    ● Test 10
    - Completează cu user și pass valide
    - Click login
    - Verifică ca noul url CONTINE /secure
    - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    - Verifică dacă elementul cu clasa=’flash succes’ este displayed
    - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
    '''
    def test_login(self):
        self.chrome.find_element(*self.USER).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        secure_url=self.chrome.current_url
        self.assertIn('/secure',secure_url,'Noul url nu contine /secure')
        WebDriverWait(self.chrome,5).until(EC.presence_of_element_located((By.CLASS_NAME,'success')))
        succes_element=self.chrome.find_element(*self.SUCCES)
        self.assertTrue(succes_element.is_displayed(),'Elementul nu este pe pagina')
        self.assertTrue('secure area!'in succes_element.text,'Textul de pe mesajul de succes nu este corect')

    '''
    ● Test 11
    - Completează cu user și pass valide
    - Click login
    - Click logout
    - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    '''
    def test_logout(self):
        self.chrome.find_element(*self.USER).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        actual=self.chrome.current_url
        expected='https://the-internet.herokuapp.com/login'
        self.assertEqual(actual,expected,'Nu ne-am intors pe pagina /login')

    # Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google

    '''
    ● Test 12 - brute force password hacking
    - Completează user tomsmith
    - Găsește elementul //h4
    - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
    potențială parolă.
    - Folosește o structură iterativă prin care să introduci rând pe rând
    parolele și să apeși pe login.
    - La final testul trebuie să îmi printeze fie
    ‘Nu am reușit să găsesc parola’
    ‘Parola secretă este [parola]’
    '''
    def test_brute_force_password_hacking(self):
        text=self.chrome.find_element(By.XPATH,'//h4').text
        lista_password=text.split()
        for i in range (len(lista_password)):
            self.chrome.find_element(*self.USER).send_keys('tomsmith')
            self.chrome.find_element(*self.PASSWORD).send_keys(lista_password[i])
            self.chrome.find_element(*self.LOGIN_BUTTON).click()
            url=self.chrome.current_url
            wanted_url='https://the-internet.herokuapp.com/secure'
            if url== wanted_url:
                print(f'Parola secretă este {lista_password[i]}')
                break
        url = self.chrome.current_url
        wanted_url = 'https://the-internet.herokuapp.com/secure'
        if url!=wanted_url:
            print('NU am reusit sa gasesc parola')



