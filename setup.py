import setuptools

with open("Readme.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "TextSummarizer"
AUTHOR_USER_NAME = "anubhavtewari05"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "anubhavtewari05@gmail.com"



setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="Small package for NLP app",
    long_description = long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {"Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir = {"" : "src"},
    packages = setuptools.find_packages(where = "src")
)