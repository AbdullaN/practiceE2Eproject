import setuptools

with open("README.md", "r", encoding="utf-8") as f: #This helps display the info of your package in the pypi website if you want to publish it.
    long_description = f.read() 


__version__ = "0.0.0"

NAME = 'Kidney-Disease-Classification-Deep-Learning-Project'

REPO_NAME = '{NAME}'
AUTHOR_USER_NAME = "Abdulla"
SRC_REPO = "cnnClassifier" #This is your local package in your environment
AUTHOR_EMAIL = "Abdullahuni@outlook.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)