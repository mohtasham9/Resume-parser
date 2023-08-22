from setuptools import setup, find_packages

setup(
    name='GPTResParser',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pdfminer.six',
        'python-docx',
        'regex',
        'aiohttp',
        'freeGPT==1.2.4',
        'docx2txt==0.8'
    ]
)
