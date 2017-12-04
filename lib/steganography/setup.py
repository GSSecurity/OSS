import os

from setuptools import setup

from lib.steganography import __version__

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name='SteganographyApp',
    version=__version__,
    description="Digital image SteganographyApp of encrypted text",
    long_description=long_description,
    author='haminiku',
    author_email='haminiku1129@gmail.com',
    url='https://github.com/subc/SteganographyApp',
    packages=['SteganographyApp'],
    package_dir={'SteganographyApp': 'SteganographyApp'},
    include_package_data=True,
    install_requires=["pillow", 'django'],
    license='MIT License',
    zip_safe=False,
    keywords=["Implementation Hide Text In Image with encryption", "stegano", "SteganographyApp",
              "Digital image SteganographyApp of encrypted text"],
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points={
        'console_scripts': [
         'SteganographyApp = SteganographyApp.SteganographyApp:main',
        ],
    },
)
