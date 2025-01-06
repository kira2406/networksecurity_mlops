'''
Used by python setuptools to define the configuration of project such as metadata, dependencies
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    req_list:list[str] = []
    try:
        # Open requirements.txt file
        with open('requirements.txt', 'r') as file:
            # read lines from file
            lines = file.readlines()

            for line in lines:
                req = line.strip()
                # ignore empty lines and -e .
                if req and req != "-e .":
                    req_list.append(req)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return req_list

setup(
    name="NetworkSecurityMLOps",
    version="0.0.1",
    author="Kushwanth Parameshwaraiah",
    author_email="kush.p030.24@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)
