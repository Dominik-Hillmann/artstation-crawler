# artstation-crawler
A crawler retrieving pictures from artstation given their tags.

## Usage

## Dependencies
* Python 2.7
* `selenium`
    * Downloaded via, the `geckodriver.exe` has to be put into source directory of Python
* `splinter` library
* `bs4` library

## Pseudo code
```txt
# Öffne Suchseite
# lese 'zu besuchende URLs'
# lese 'besuchte URLs' (beides zu Mengen)

# für die benötigte Zahl an Batches:
    # benötigte Zahl sei Batchgröße

    # Solange du noch nicht die benötigte Anzahl an noch nicht gesehenenen URLs hast:
        # Scrolle nach unten
        # Für alle neuen URLs
            # Wenn neue URL nicht in 'gesehene URLs' ist
                # füge URL zu 'zu besuchenden URLs' hinzu
                # mache diese Liste persistent

    # für jede gesammelte URL:
        # Besuche in einem neuen Tab jede gesammelte URL
        # Nimm Screenshot auf
        # Schließe tab
        # Nimm URL aus 'zu besuchenden URLs' raus
        # füge die URL zu 'besuchten URLs' hinzu
        # mache die Änderungen persistent

# WICHTIG: Im Falle KeyboardInterrupt: mache beide Listen persistent

# Brauchen: 
    # ParameterParser zum allgemeinen verarbeiten des Kommandos
    # BrowserWrapper, einerseits Suchseite offen, Screenshots in neuen Tabs, scrollen kann
    # UrlManager, der die beiden Listen persistent macht und managed und weitergibt
    # UrlExtractor, der 
```