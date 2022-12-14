from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'feather',
    version = '0.0.2',
    author = 'Feather CLI',
    author_email = 'me@feathererp.com',
    license = 'MIT',
    description = 'Feather erp manage cli',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/dogansalman/feather-cli',
    py_modules = ['feather', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        feather=feather:cli
    '''
)