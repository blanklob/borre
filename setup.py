from setuptools import setup


def get_description():
    with open("README.md") as file:
        return file.read()


setup(
    name="bore",
    version="0.0.1",
    url="https://github.com/younessidbakkasse/bore",
    author=["Youness Id bakkasse", "David", "...", "..."],
    author_email=["Youness Id bakkasse", "David", "...", "..."],,
    description="A dice game made using Python",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.9, <4",
    install_requires=[
        "httpx >= 0.15.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    package_data={"bore": ["main.typed"]},
)
