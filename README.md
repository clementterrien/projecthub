# projecthub

## Development

### Using a venv

    python -m venv venv

### Activate the venv

#### On MacOS/Linux
    source venv/bin/activate

### Install Dependencies
    pip install -r requirements.txt

### Use flake8

    pip install flake8

#### Use the flake8 file for preferences
1. Create a ./flake8 file

2. Insert your preferences like or use options in the flake8 cli.
~~~
[flake8]
max-line-length = 160
max-doc-length = 170
extend-exclude= venv/
~~~
*This is what I have in my .flake8 file. This file is gitignored.*
