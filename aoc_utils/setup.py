from setuptools import setup, find_packages

setup(
    name="aoc_utils",  # Replace with your module's name
    version="0.1.0",   # Replace with your version
    author="Rishabh Sood",  # Replace with your name
    long_description_content_type="text/markdown",
    packages=find_packages(),  # Automatically finds and includes packages in your directory
    install_requires=[
        "requests",
        "beautifulsoup4",
        "markdownify"
    ],  # Dependencies required for your module
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',  # Minimum Python version required
)