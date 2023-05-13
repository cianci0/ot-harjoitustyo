# Ohjelman arkkitehtuuri

### Luokkakaavio
![Luokkakaavio](./kuvat/luokka.png)

Ohjelmassa on kokonaisuudessaan kahdeksan luokkaa, joista kaksinpelissä käytetään kuutta ja yksinpelissä seitsemää. 

Sekä yksin- että kaksinpelissä käytetään samaa <strong>Gameloop</strong>-luokkaa, jonka takia se on valitettavan monimutkainen ja vaikeasti testattava. <strong>Player</strong>-objektit ja <strong>Gameloop</strong>-luokka alustetaan pelityypistä riippuen src-hakemiston juuressa sijaitsevissa <strong>OnePlayer<strong>- ja <strong>TwoPlayer<strong> -luokissa, jonka jälkeen niissä kutsutaan Gameloop-luokan metodia <strong>loop()</strong>, joka aloittaa pelin. <strong>Gameloop</strong>-luokan alustusfunktiossa alustetaan pygame-ikkuna.

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
