## boom_pa ##


### Purpose/Scope ###
Compute peak over pressure using the BOOM model


## Install ##

Clone source package  
`git clone http://github.com/flyrok/boom_pa`

Install with pip after download  
`pip install .`

Install in editable mode  
`pip install -e .`

Or install directly from github  
`pip install git+https://github.com/flyrok/boom_pa#egg=boom_pa`

Or just puth the executable on your PATH and call directly  
`./boom_pa.py`


## Python Dependencies ##

python>=3.6 (script uses f-strings)  
numpy=>1.6.1


## Usage/Examples ##

To see help:  
`boom_pa --help`    

To see version:  
`boom_pa --version`    

To compute pressure for 1kt at 1000m:  
`boom_pa -w 1 -d 1000`


