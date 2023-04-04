# Vaatimusmäärittely

## Sovelluksen tarkoitus

Pong-peli, jota voi pelata yksin tietokonetta vastaan tai kaksinpelinä yhdellä tietokoneella.

## Käyttöliittymäluonnos

1. Aloitusnäkymä, jossa voi vaihtaa väriteemaa, aloittaa yksin- tai kaksinpelin ja katsoa yksinpelin ennätystulostaulua.
2. Pelaajien nimien määrittelynäkymä. Kun käyttäjä aloittaa yksinpelin aloitusnäkymästä, siirrytään ikkunaan, jossa kysytään pelaajan nimi. Kun käyttäjä aloittaa kaksinpelin, kysytään pelaajien nimet ja haluttu pituus pelille (esim 10 tai 20 pistettä). Tietojen syöttämisen jälkeen siirrytään automaattisesti näkymään 3 tai 4.
3. Yksinpelinäkymä, jossa vasenta mailaa ohjataan w-, a-, s- ja d- näppäimillä. Vastustajan mailaa ohjaa yksinkertainen tekoäly. 
4. Kaksinpelinäkymä, jossa vasenta mailaa ohjataan w-, a-, s- ja d- näppäimillä ja oikeaa mailaa nuolinäppäimillä.
5. Tulosnäkymä, jossa näkyy 3 korkeinta yksinpelitulosta pelaajien nimien kera. Tulosnäkymään pääsee alotusnäytöstä ja siihen siirrytään automaattisesti yksinpelin loputtua.

## Pelin toiminnallisuus

### Yksinpeli

- Pelin alussa pallo on keskellä ikkunaa. Se lähtee liikkumaan satunnaiseen suuntaan kun käyttäjä painaa ensimmäistä kertaa välilyöntinäppäintä.
- Ikkunan yläreunassa näkyy pelaajan nimi ja pisteet.
- Pelaaja saa pisteen aina, kun pallo osuu pelaajan omaan mailaan.
- Pallon liike nopeutuu tasaisesti.
- Peli päättyy, kun pallo osuu pelaajan mailan takana olevaan seinään.
- Pelin päätyttyä kierroksen pisteet ja pelaajan nimi tallennetaan tietokantaan.

### Kaksinpeli

- Pelin alussa pallo on keskellä ikkunaa. Se lähtee liikkumaan satunnaiseen suuntaan kun käyttäjä painaa ensimmäistä kertaa välilyöntinäppäintä.
- Ikkunan yläreunassa näkyvät pelaajien nimet ja pisteet.
- Pelaaja saa pisteen aina, kun pallo osuu toisen pelaajan mailaan takana olevaan seinään.
- Pallon liike nopeutuu tasaisesti.
- Peli päättyy, kun yhdellä pelaajista on ennen pelin aloitusta määritellyn pistemäärän verran pisteitä (esim 10 tai 20 pistettä)

## Jatkokehitysideoita

- Uudet pelitavat, kuten
  - Nelinpeli
  - Kaksinpeli netin välityksellä
  - Vaikeampi yksinpeli, jossa kimmokkeita tippuu ikkunan yläreunasta
- Kaksinpelitulostaulu, jossa näkyy pelaajien tulokset toisia pelaajia vastaan
- Muokattavuuden lisääminen
  - Pallon nopeuden määrittely
  - Pelikentän koon määrittely