# SigaaWebScraping
This repository is aimed at scraping data from the "Sistema Integrado de Gestão de Atividades Acadêmicas (SIGAA)", which is the platform most public universities use in Brazil, with the purpose of generating a vcf file containing estructured data such as student's names and emails that can be directly imported to GoogleContacts.

## Pre-Installation
Make sure you are using the latest version of Python. Otherwise, download if from [here](https://www.python.org/downloads/)

Selenium and bs4 packages are both required for webScraping. So, installed them by typing in the terminal:
```shell
pip install bs4 selenium
```

Also, the RegEx Module is need in order to work with Regular Expressions.
```shell
pip install re
```
Finally, install pandas for parsing the data:
```shell
pip install pandas
```
