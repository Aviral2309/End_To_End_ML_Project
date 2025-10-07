from setuptools import find_packages, setup  ## it will automatically finds whatever packages used in the projects
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str)-> list[str]:
  '''
  this function will return the list of requirements
  '''
  requirements= []
  with open(file_path) as file_obj:
    requirements = file_obj.read().splitlines()  ## reading packags line by line 
    requirements = [req.replace("\n"," ") for req in requirements]  ## Removing \n from the last
    
    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
      
  return requirements

setup(  ## Meta Data Info for model
  name = 'ML_Project',
  version = '0.0.1',
  author='Aviral',
  author_email='aviralmittal0012@gmail.com',
  packages=find_packages(),
  install_requires= get_requirements('requirements.txt')
)