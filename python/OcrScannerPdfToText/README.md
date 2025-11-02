# Description
this project is not done, theoreticaly it works, but not that good :D 

# Install 
To use this scipt, you need to install the following
## `tesseract` 
You will find a full documentation for installing [here (tesseract-ocr.github.io)](https://tesseract-ocr.github.io/tessdoc/Installation.html)

## `poppler`
[Github](https://github.com/innodatalabs/poppler)
- On Windows you can download the release from GitHub
- On Mac you can install it through brew `brew install poppler`


# Run
create a virtuall invironment, install requierements and run the application.

## Windows
```CLI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
## MacOS
```CLI
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

# Usage
```cli
usage: scan.py [-h] [-l LANGUAGE] [-o OUTPUT] [-d DPI] [--pages START END] pdf_path
```
## Example
```cli
python3 scan.py -l de -o ./text.txt -d 300 --pages 1 3 file.pdf
```
