from setuptools import setup

setup(name='TVcrawler',
    version='0.1',
    description="""
    TV Show Crawler | Download Torrent Of Your Show's Latest Episode \n\n
    - tvcrawler "SHOW_TITLE"
    """,
    url='http://github.com/dorukgezici/TVcrawler',
    author='Doruk Gezici',
    author_email='dorukgezici@gmail.com',
    license='MIT',
    packages=['TVcrawler'],
    install_requires=['requests'],
    scripts=['bin/TVcrawler'],
    zip_safe=False)
