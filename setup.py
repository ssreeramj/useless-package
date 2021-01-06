import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="useless_ssreeramj",
    version="0.0.1",
    author="Sreeram Jagannath S",
    author_email="ssreeramj@gmail.com",
    description="Pretty much a useless package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ssreeramj/useless-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)