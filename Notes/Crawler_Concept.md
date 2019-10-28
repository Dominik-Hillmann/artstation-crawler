# Konzept für den artsation-Crawler

## Schnittstellen
* artstation hat keine eigene API, weswegen `beautifulsoup` genutzt werden wird
    * ein einfache zu benutzende Bibliothek für Python, um Zugriff auf DOM-Elemente in Python zu haben

## Crawling
* Website über einfache GET-Anfragen
* URL des Hauptbildes einfach über das `src`-Attribut erhältlich
    * führt zu Website, die nur Bild enthält
* weitere Elemente werden über die Tags gefunden über:
    * alle neuen Bilder müssen bestimmte, im Voraus festgelegte Tags beinhalten
    * weitercrawlen über vorgeschlagende Bilder eines Künstlers, die ebenfalls Tags enthalten
    * und über Leute, die kommentieren, die ebenfalls Tags enthalten
    * erste Anfrage muss irgendwie über Suchfunktion erstellt werden
* alle Pfade werden nach Suchalgorithmus in Baumstruktur abgearbeitet
* terminiert bei bestimmter Anzahl gefundener Bilder oder wenn sich der Baum erschöpft hat und keine weiteren Bilder gefunden werden, die die gesuchten Tags enthalten
* Erstellung eines Logs, damit schnell abgefragt werden kann, ob ein Bild bereits heruntergeladen worden ist


## Ressourcen
* Dokumentation `beautifulsoup`: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* Bild herunterladen: https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
* normale Website, Beispiel: https://www.artstation.com/artwork/oO8GRB
* Website nur mit Bild, Beispiel: https://cdna.artstation.com/p/assets/images/images/018/254/710/large/ranulf-busby-doku-fs-01.jpg?1558717505


