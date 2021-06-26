from selenium import webdriver
from time import sleep
import os
import random
import sys
from colorama import Fore



driver = webdriver.Chrome()
driver.get('https://www.matematikfessor.dk/')
os.system("cls")
os.system("title Fessor Knepper by Scopes#9999")



g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW
re = Fore.RESET
l = Fore.LIGHTBLACK_EX


def banner():
    os.system("cls")
    print(f'''{b}
 _______                         _    _            _    
 |  ____|                       | |  | |          | |   
 | |__ ___  ___ ___  ___  _ __  | |__| | __ _  ___| | __
 |  __/ _ \/ __/ __|/ _ \| '__| |  __  |/ _` |/ __| |/ /
 | | |  __/\__ \__ \ (_) | |    | |  | | (_| | (__|   < 
 |_|  \___||___/___/\___/|_|    |_|  |_|\__,_|\___|_|\_\
                                                        
                                                        
                                                                                                      
     {re}
    ''')


def svar():
    print("Vi Fandt Svaret")
    sleep(1)
    os.system('cls')







def main():
    banner()
    Check = input("Er Du Logged Ind? (Ja) > ")
    if Check == "ja":
        os.system('cls')
        banner()
        check2 = input("Er du Inde i Opaven (ja) >")    
        if check2 == "ja":
            #dostuff
            UserCheck = input("Hvilket Regne Stykke: +, -, *")
            os.system("cls")
            regnestykke = int(input("Første Tal > "))
            regnestykke2 = int(input("Andet Tal > "))
            os.system("cls")
            resultat = regnestykke, UserCheck, regnestykke2
            driver.find_element_by_xpath('/html/body/div[2]/main/div/article/ul/li/div/div[1]/div[3]/div/p/input').send_keys(resultat)
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/main/div/article/ul/li/button').click()









if __name__ == '__main__':
    main()



