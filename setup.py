from setuptools import find_packages,setup
from typing import List

e_dot = '-e .'

def get_requriments(filepath:str)->List[str]:
    requirement = []

    with open(filepath) as file_obj:
        requirement = file_obj.readlines()
        requirement = [i.replace("\n","") for i in requirement]

        if e_dot in requirement:
            requirement.remove(e_dot)


setup(name='ML_project',
      version='0.0.1',
      description='ML Project',
      author='pratikesh howale',
      author_email='pratikeshhowale@gmail.com',
      packages=find_packages,
      install_requires=get_requriments('requirement.txt'))