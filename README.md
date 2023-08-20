# SigaaWebScraping
This repository is aimed at scraping data from the "Sistema Integrado de Gestão de Atividades Acadêmicas (SIGAA)", which is the platform most public universities use in Brazil, with the purpose of generating a vcf file containing estructured data such as student's names and emails that can be directly imported to GoogleContacts.

This repository assumes that you have a registered access to the SIGAA platform as professor. Otherwise, it will not be useful.

## Installation
Make sure you are using the latest version of Python. Otherwise, download if from [here](https://www.python.org/downloads/)

After that install all the required packages:
```shell
pip install -r requirements.txt
```

You will also need a webdriver in order to the script manipulate the browser automaticly. Firefox, Internet Explorer, Safari, Opera, Chrome and Edge provide their own webdriver. For this you will need both the browser and the webdriver. Note that it depends on your OS!

In case you opt for Chrome, download the browser from [here](https://www.google.com/chrome/) and its webdriver (Chromedriver) from [here](https://googlechromelabs.github.io/chrome-for-testing/#stable).

In case you prefer Firefox, download the browser from [here](https://www.mozilla.org/en-US/firefox/new/) and its webdriver (Geckodriver) from [here](https://github.com/mozilla/geckodriver/releases). 

Once you have all that installed, you can clone this repository by open a terminal and typing:
```shell
git clone https://github.com/BorjaRuizReverter/SigaaWebScraping.git
```

Then move to repository folder cloned:
```shell
cd SigaaWebScraping
```
and open the python script and edit it, adding your login details and group details in the lines below
```python
username.send_keys("USUARIO")
password.send_keys("SENHA")
driver.find_element(By.LINK_TEXT, "DEPARTAMENTOCÓDIGO_DISCIPLINA - NOME_DISCIPLINA - TURMA").click()
```
Python files may not be executed by the Python interpreter if the path to these py files are not in the $PATH environment. So, add this directory to $PATH: 
```shell
export PATH=/home/WRITE_HERE_YOUR_USER_NAME/WRITE_HERE_THE_REST_OF_THE_PATH_UP_TO_SigaaWebScraping_DIRECTORY:$PATH
```
Finally, save the edition and run the python script!
```shell
./SigaaWebScraping.py
```
or 
```shell
python SigaaWebScraping.py
```
If it all works, your previously blank vcf file should now be filled with student's names and emails. This file has the suitable format to be imported from Google Contacts. 
