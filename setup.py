import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tales",
    version="0.0.4",
    author="elf",
    author_email="elflanded@gmail.com",
    description="A simple, and easy to use hypixel API wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elfq/tales",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)