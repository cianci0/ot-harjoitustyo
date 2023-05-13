# Ohjelman arkkitehtuuri

### Luokkakaavio
![Luokkakaavio](./kuvat/luokka.png)

Ohjelmassa on kokonaisuudessaan kahdeksan luokkaa. Luokka <strong>Ui</strong> vastaa käyttöliittymän toteutuksesta, luokat <strong>OnePlayer</strong> ja <strong>TwoPlayer</strong> pelin alustuksesta ja loput pelilogiikasta. 

Sekä yksin- että kaksinpelissä käytetään samaa <strong>Gameloop</strong>-luokkaa, jonka takia se on valitettavan monimutkainen. <strong>Player</strong>-objektit ja <strong>Gameloop</strong>-luokka alustetaan pelityypistä riippuen src-hakemiston juuressa sijaitsevissa <strong>OnePlayer</strong>- ja <strong>TwoPlayer</strong> -luokissa, jonka jälkeen niissä kutsutaan Gameloop-luokan metodia <strong>loop()</strong>, joka aloittaa pelin. Gameloop-luokka saa yhedksi attribuutikseen <strong>Clock</strong>-olion, joka toimii pitkälti kuten pygame-kirjaston kello.

### Pakkauskaavio
![Pakkauskaavio](./kuvat/pakkaus.png)

Tällä hetkellä ohjelman käyttöliittymä on kokonaan src-hakemiston juuressa sijaitsevassa index.py -tiedostossa, mutta tarkoituksenani on jakaa se järkeviin osiin uuteen ui-hakemistoon, josta tulee objects-hakemiston rinnakkaishakemisto.

### Käyttöliittymä

Käyttöliittymä sisältää viisi eri näkymää:

- Päävalikko, josta pääsee
  - yksinpelinäkymään
  - kaksinpelinäkymään
  - tulostaulunäkymään
 
  ja
  - ohjenäkymään

Näistä viidestä näkymästä tulostaulu on vielä toteuttamatta. Kaikki näkymät on toteutettu samassa tiedostossa yhdessä tkinter-ikkunassa, jossa nappia painettaessa ja toiseen näkymään siirryttäessä poistetaan tarvittavat widgetit ja luodaan uudet tilalle.

### Sekvenssikaavio
![Sekvenssikaavio](./kuvat/sekvenssikaavio1.jpg)

### Pelilogiikan sekvenssikaavio
![Sekvenssikaavio](./kuvat/sekvenssikaavio2.jpg)
