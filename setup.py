from distutils.core import setup
import glob
import os

scripts = glob.glob(os.path.join('scripts', '*.py'))

# noinspection PyPackageRequirements
setup(

    name='IC443',

    version='0.1',

    packages=['ic443'],

    url='https://github.com/jackieblaum/IC443',

    license='BSD-3',

    author='Jackie Blaum',

    author_email='jackie.blaum@gmail.com',

    description='Slice FITS files into new separate FITS files',

    install_requires=['numpy',
                      'astropy',
                      #'reproject'
			],

    scripts=scripts,

)

