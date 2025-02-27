from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "seaborn",
        "matplotlib",
        "quarto",
    ],
    python_requires=">=3.9",
)