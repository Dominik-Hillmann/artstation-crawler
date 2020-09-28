# artstation-crawler
A crawler retrieving pictures from a certain web page using their search terms.

## Usage
First, write the paths of the target directory for the pictures and the directory of the log file into `config.json`. Make sure to use `\\` if using Windows as path seperator. <br>
Example: you want to have 150 images of a cityscape at night, then your command will be
```bash
python artstation_crawler\artstation_crawler.py --search-terms cityscape night --number-pictures 150
```
or
```bash
python artstation_crawler\artstation_crawler.py -s cityscape night -n 150
```
for short.

## Parameters
* `search-terms` or `s`: The serach terms you would input to artstation.
* `number-pictures` or `n`: The maximum number of images you want to collect.
* `links-only` or `l`: This mode only looks for new URLs and saves them without downloading images.
* `pictures-only` or `p`: Gathers images from the given list of URLs that were collected earlier.

## Dependencies
Take a look at the `requirements.txt` if you want to create an environment with conda.
* Python 2.7
* Splinter brower
    * Take a look at https://splinter.readthedocs.io/en/latest/install.html
    * Using `geckodriver.exe` which has to be put into source directory of Python
* `bs4` library (BeautifulSoup)
* `Pillow` library
