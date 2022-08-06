from setuptools import setup,find_packages
from typing import List 

def get_requirements_list()->List[str]:
    " This function will return the list of requirement mention in requirements.txt file "
    with open(REQUIREMENT_FILE_NAME) as requiremet_file:
        return  requiremet_file.readlines().remove("-e .")


#Declaring varibles for setup functions 
PROJECT_NAME = "housing-predictor"

VERSION = "0.0.2"

AUTHOR = "FAZLULLAH BOKHARI"

DESCRIPTION = "This is a first version of housing-predictor" 

PACKAGES = find_packages()

REQUIREMENT_FILE_NAME = "requirements.txt"

setup(
    name = PROJECT_NAME,
    version = VERSION, 
    author = AUTHOR, 
    description = DESCRIPTION, 
    packages=PACKAGES,
    install_requires = get_requirements_list()
) 
