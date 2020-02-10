# artstation-crawler
A crawler retrieving pictures from a certain web page using their search terms.

## Note
This a public version of a private project which is only supposed fill my GitHub page. For several reasons only the private version is functional.

## Usage
First, write the paths of the target directory for the pictures and the directory of the log file into `config.json`. Make sure to use `\\` if using Windows as path seperator. <br>
Example: you want to have 150 images of a cityscape at night, then your command will be
```sh
python main.py --search-terms cityscape night --number-pictures 150
```
or
```
python main.py -s cityscape night -n 150
```
for short.

## Parameters


## Dependencies
Take a look at the `requirements.txt` if you want to create an environment with conda.
* Python 2.7
* Splinter brower
    * Take a look at https://splinter.readthedocs.io/en/latest/install.html
    * Using `geckodriver.exe` which has to be put into source directory of Python
* `bs4` library (BeautifulSoup)
* `Pillow` library

## Pseudo code
```txt
Öffne Suchseite
lese 'zu besuchende URLs'
lese 'besuchte URLs' (beides zu Mengen)
wenn noch kein Ordner für die Suchbegriffe existiert, erstelle neuen Ordner

für die benötigte Zahl an Batches:
    benötigte Zahl sei Batchgröße

    Solange du noch nicht die benötigte Anzahl an noch nicht gesehenenen URLs hast:
        Scrolle nach unten
        Für alle neuen URLs
            Wenn neue URL nicht in 'gesehene URLs' ist
                füge URL zu 'zu besuchenden URLs' hinzu
                mache diese Liste persistent

    für jede gesammelte URL:
        Besuche in einem neuen Tab jede gesammelte URL
        Nimm Screenshot auf
        Schließe tab
        Nimm URL aus 'zu besuchenden URLs' raus
        füge die URL zu 'besuchten URLs' hinzu
        mache die Änderungen persistent

WICHTIG: Im Falle KeyboardInterrupt: mache beide Listen persistent

Brauchen: 
    ParameterParser zum allgemeinen verarbeiten des Kommandos
    BrowserWrapper, einerseits Suchseite offen, Screenshots in neuen Tabs, scrollen kann
    UrlManager, der die beiden Listen persistent macht und managed und weitergibt
    UrlExtractor, der 
```