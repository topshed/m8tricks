__project__ = 'm8tricks'
__version__ = '0.71'
__keywords__ = ['raspberrypi', 'sensehat']
__author__ = "Richard Hayler"
__author_email__ = ''
__url__ = ''

__requires__ = ['guizero']

__classifiers__ = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Programming Language :: Python :: 3',
]

__entry_points__ = {'console_scripts' : ['m8tricks = m8tricks.m8tricks:main']}
