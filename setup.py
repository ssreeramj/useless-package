import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mup',
    version="0.0.1",
    author="Sreeram Jagannath S",
    author_email="ssreeramj@gmail.com",
    description="This is the Most Useless Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ssreeramj/useless-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)