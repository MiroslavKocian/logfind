try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'My Project',
    'author': 'Miroslav Kocian',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'mirkocian@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'name': 'logfind',
    #'scripts': ['bin/logfind'],
    'entry_points' : {
        'console_scripts': [
            'logfind=logfind.logfind:run'
        ]
    }
}

setup(**config)