import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "rouniyar.nandani@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="Nandani",
    author_email="rouniyar.nandani@gmail.com",
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/nandani537/End-to-End-Machine-Learning-Project-with-MLFLOW",
    project_urls={
        "Bug Tracker": f"https://github.com/nandani537/End-to-End-Machine-Learning-Project-with-MLFLOW/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)