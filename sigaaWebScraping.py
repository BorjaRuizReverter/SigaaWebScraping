'''
Import the required packages
'''
import re
from tracemalloc import stop
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import maskpass
 
'''
The webdriver will need login creds to login"
'''
username = input ('Please type your login name: ')

'''
This is for echoing the password and mask it with asterisks(*)
'''
passwd = maskpass.askpass(prompt="Please type your password: ", mask="*")

'''
The webdrivers available depends on the OS. The script needs to know this to proceed accordingly. 
'''
import platform
os = platform.system()
print("It seems that you are on: ", os)
print("Sorry, but this script needs to know your OS to proceed accordingly.")

'''
The following lines tries to use different webdrivers
If it succeeds it will scrap the targeted website
'''
try:
    driver = webdriver.Firefox()
except:
    print("The webdrive from Firefox failed. We try another...")
else:
    print("The webdrive from Firefox succeed! So let it scrap...")

try:
    driver = webdriver.Chrome()
except:
    print("The webdrive from Chrome failed. We try another...")
else:
    print("The webdrive from Chrome succeed! So let it scrap...")

try:
    driver = webdriver.Ie()
except:
    print("The webdrive from InternetExplorer failed. We try another...")
else:
    print("The webdrive from InternetExplorer succeed! So let it scrap...")

try:
    driver = webdriver.Edge()
except:
    print("The webdrive from MicrosoftEdge failed. We try another...")
else:
    print("The webdrive from MicrosoftEdge succeed! So let it scrap...")

driver.get("https://sigaa.ufpb.br/sigaa/logon.jsf")
print(driver.title)

'''
This will make login at the targeted website. Please insert your login details here in order to continue
The method find_element_by_id is deprecated. We substitued for find_element
'''
username = driver.find_element(By.ID, "form:login")
username.clear()
username.send_keys(username)
password = driver.find_element(By.ID, "form:senha")
password.clear()
password.send_keys(passwd)

'''
This will make the webdriver navigate to the target group
'''
driver.find_element(By.ID, "form:entrar").click()
driver.find_element(By.ID, "form:portalDocente").click()

'''
This will make the webdriver choose the target group. For that, please insert the group details here
The method find_element_by_link_text is deprecated. We substitued for find_element(By.LINK_TEXT, "text")
'''
driver.find_element(By.LINK_TEXT, "DEPARTAMENTOCÓDIGO_DISCIPLINA - NOME_DISCIPLINA - T01").click()

'''
This will prepare the vcf file for writting
'''
nome_arquivo = r'contactos_sigaa.vcf'

'''
This will make the webdriver finally reach the target url
'''
driver.find_element(By.LINK_TEXT, "Participantes").click()

'''
The following lines grab, parse and format the data
'''
soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find_all(name = 'strong')
table2 = soup.find_all(name = 'em')

df1 = pd.DataFrame(columns = ['last_name'])
df2 = pd.DataFrame(columns = ['first_name'])
df3 = pd.DataFrame(columns = ['org'])
df4 = pd.DataFrame(columns = ['title'])
df5 = pd.DataFrame(columns = ['phone'])
df6 = pd.DataFrame(columns = ['email'])
df7 = pd.DataFrame(columns = ['website'])
df8 = pd.DataFrame(columns = ['street'])
df9 = pd.DataFrame(columns = ['city'])
df10 = pd.DataFrame(columns = ['p_code'])
df11 = pd.DataFrame(columns = ['country'])

names_table = table[6:len(table)]
i=0
while i<len(names_table):
    s = str(names_table[i])
    result = re.search('<strong>\n\t\t\t\t\t\t\t\t\t(.*)\n', s)
    #df2 = df2.append({'first_name': result.group(1).title()}, ignore_index=True) //Append will be deprecated, so we substituted for concat below
    df2 = pd.concat([df2, pd.DataFrame([{'first_name': result.group(1).title()}])], ignore_index = True)
    i = i + 1
    
email_table = table2[8:len(table2)]
i=3
while i<len(email_table):
    s = str(email_table[i])
    result = re.search('<em>(.*) </em>', s)
    #df6 = df6.append({'email': result.group(1)}, ignore_index=True) //Append will be deprecated, so we substituted for concat below
    df6 = pd.concat([df6, pd.DataFrame([{'email': result.group(1).lower()}])], ignore_index = True)
    i = i + 3

'''
All dataframes are concatenated into one
'''
df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11], axis = 1)

'''
Finally, the dataframe is stored in a csv file with the estructure of a vcf file 
'''
df.to_csv(nome_arquivo, index = None, header = True)
driver.close()
