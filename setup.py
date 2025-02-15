from setuptools import setup, find_packages

setup(
    name="conversify",
    version="0.1.0",
    author="Deepak",
    author_email="lambda@example.com",
    description="A package for structuring, formatting, and beautifying chat conversations.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/prdeepakbabu/conversify",
    packages=find_packages(),
    install_requires=[
        "pytest>=6.0",
        "requests>=2.25.1",
        "logging",  # Logging support
        "json",  # JSON processing
        "unittest"  # Unit testing support
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "conversify=conversify.conversify:main",
        ],
    },
)
