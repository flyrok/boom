"""

See:
https://github.com/flyrok/boom_pa
"""

from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).resolve().parent

# Get the long description from the README file
readme=here / 'README.md'
with open(readme, encoding='utf-8') as f:
    long_description = f.read()

PROJECT_NAME="boom_pa"
exec(open(here / PROJECT_NAME / "version.py").read())

VERSION=__version__
DESCRIPTION="Compute peak overpressure in Pa using BOOM"
URL="https://github.com/flyrok/boom_pa"
AUTHOR="A Ferris"
EMAIL="aferris@flyrok.org"
CLASSIFIERS=['Development Status :: 3 - Alpha',
    'Intended Audience :: Seismic Researchers',
    'Topic :: Obspy/FDSN :: Helper Scripts',
    'License :: OSI Approved :: GPL-3 License',
     'Programming Language :: Python :: 3']
KEYWORDS="BOOM overpressure"     

INSTALL_REQUIRES = [
    'numpy>=1.6.1',
    ]

setup(
    name=PROJECT_NAME,  # Required
    version=VERSION,  # Required
    description=DESCRIPTION,  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url=URL,  # Optional
    author=AUTHOR,  # Optional
    author_email=EMAIL,  # Optional
    classifiers=CLASSIFIERS ,
    keywords=KEYWORDS,  # Optional
    python_requires='>=3.6',
    include_package_data=True,
    packages=['boom_pa'],
    entry_points={  # Optional
        'console_scripts': [
            'boom_pa=boom_pa.boom_pa:main',
        ],
    },
    install_requires=INSTALL_REQUIRES,
    extras_require={},
    package_data={  
    },
    project_urls={  # Optional
        'Source': URL,
    },
)

