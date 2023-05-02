# Ohjelman arkkitehtuuri

### Luokkakaavio
![Luokkakaavio](./kuvat/luokka.png)

Ohjelmassa on kokonaisuudessaan kuusi luokkaa, joista kaksinpelissä käytetään vain viittä (<strong>NPCPaddle</strong> jää pois). 

Sekä yksin- että kaksinpelissä käytetään samaa <strong>Gameloop</strong>-luokkaa, jonka takia se on valitettavan monimutkainen ja vaikeasti testattava. <strong>Player</strong>-objektit ja <strong>Gameloop</strong>-luokka alustetaan pelityypistä riippuen src-hakemiston juuressa sijaitsevissa oneplayer.py ja twoplayer.py -tiedostoissa, jonka jälkeen molemmissa tiedostoissa kutsutaan Gameloop-luokan metodia <strong>loop()</strong>, joka aloittaa pelin.

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
