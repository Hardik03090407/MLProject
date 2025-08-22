from setuptools import find_packages,setup
from typing import List

HYPON_e_Dot="-e ."
def get_requirements(file_path:str)->List[str]:
    'this will open the list in requirements'
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPON_e_Dot in requirements:
            requirements.remove(HYPON_e_Dot)
    return requirements

setup(
name="ML Project",
version='0.0.1',
author="Hardik",
author_email="hardikrawat79@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt"),
)
   
