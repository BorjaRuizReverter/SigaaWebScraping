# SigaaWebScraping
This repository is aimed at scraping data from the "Sistema Integrado de Gestão de Atividades Acadêmicas (SIGAA)", which is the platform most public universities use in Brazil. The purpose is to generate a vcf file containing estructured data such as student's names and emails that can be directly imported to GoogleContacts.

This repository assumes that you have a registered access to the SIGAA platform as technician/professor. Otherwise, it will not be useful.

## Installation
1. Make sure you are using the latest version of Python. If you don't have it, you can download it from [here](https://www.python.org/downloads/).

2. Make sure you have GIT installed in your OS. If not, you can download it from [here](https://git-scm.com/downloads). Having GIT is not mandatory thought, since you can download this repository as a zipped folder.

3. Download the repository from [here](https://github.com/BorjaRuizReverter/SigaaWebScraping/archive/refs/heads/main.zip) and unzip it, or clone it:
```Shell
git clone https://github.com/BorjaRuizReverter/SigaaWebScraping.git
```

4. Then move to the repository folder created:
```Shell
cd SigaaWebScraping
```

5. If you are on a Linux OS, you will need Python development packages. So, install them via terminal. For that, type this if you are on a RedHat distro
```Shell
sudo dnf install python3-devel
```
or this if you are using a Debian distro:
```Shell
sudo apt install python3-dev
```
This is very important as to not suffering from fatal errors of this kind: `Python.h: No such file or directory` right on the next step, when installing some of the required packages (the maskpass package, specifically).

6. Once inside this folder, install all the required Python packages:
```Shell
pip install -r requirements.txt
```

## Usage
Finally, it is just running the python script. So, type this if you are on Linux:
```Shell
python3 SigaaWebScraping.py
```
or this if you are on Windows:
```Powershell
py.exe SigaaWebScraping.py
```

If everything proceed without issues, the script should have created a vcf file with student's names and emails. This file has the suitable format to be imported from Google Contacts.
