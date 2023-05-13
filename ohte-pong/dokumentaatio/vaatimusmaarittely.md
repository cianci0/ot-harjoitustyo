# Vaatimusmäärittely

## Sovelluksen tarkoitus

Pong-peli, jota voi pelata yksin tietokonetta vastaan tai kaksinpelinä yhdellä tietokoneella.

## Käyttöliittymäluonnos

1. Aloitusnäkymä, jossa voi lukea pelin ohjeet, aloittaa yksin- tai kaksinpelin ja katsoa yksinpelin ennätystulostaulua. :heavy_check_mark:
2. Pelaajien nimien määrittelynäkymä. Kun käyttäjä aloittaa yksin- tai kaksinpelin aloitusnäkymästä, siirrytään ikkunaan jossa kysytään pelaajan tai pelaajien nimet. Tietojen syöttämisen jälkeen siirrytään näkymään 3 tai 4. :heavy_check_mark:
3. Yksinpelinäkymä, jossa vasenta mailaa ohjataan w- ja a-näppäimillä. Vastustajan mailaa ohjaa yksinkertainen tekoäly. :heavy_check_mark:
4. Kaksinpelinäkymä, jossa vasenta mailaa ohjataan w- ja a-näppäimillä ja oikeaa mailaa nuolinäppäimillä. :heavy_check_mark:
5. Tulosnäkymä, jossa näkyy 3 korkeinta yksinpelitulosta pelaajien nimien kera. :heavy_check_mark:

## Pelin toiminnallisuus

### Yksinpeli

- Pelin alussa pallo on keskellä ikkunaa. Se lähtee liikkumaan satunnaiseen suuntaan kun käyttäjä painaa ensimmäistä kertaa välilyöntinäppäintä. :heavy_check_mark:
- Ikkunan yläreunassa näkyy pelaajan  pisteet. :heavy_check_mark:
- Pelaaja saa pisteen aina, kun pallo osuu kumpaan tahansa mailaan. :heavy_check_mark:
- Peli päättyy, kun pallo osuu pelaajan mailan takana olevaan seinään. :heavy_check_mark:
- Pelin päätyttyä kierroksen pisteet ja pelaajan nimi tallennetaan tietokantaan. :heavy_check_mark:

### Kaksinpeli

- Pelin alussa pallo on keskellä ikkunaa. Se lähtee liikkumaan satunnaiseen suuntaan kun käyttäjä painaa ensimmäistä kertaa välilyöntinäppäintä. :heavy_check_mark:
- Ikkunan yläreunassa näkyvät pelaajien nimet ja pisteet. :heavy_check_mark:
- Pelaaja saa pisteen aina, kun pallo osuu toisen pelaajan mailaan takana olevaan seinään. :heavy_check_mark:
- Peli päättyy, kun yhdellä pelaajista on ennen pelin aloitusta määritellyn pistemäärän verran pisteitä (esim 5 tai 10 pistettä) :heavy_check_mark:

## Jatkokehitysideoita

- Uudet pelitavat, kuten
  - Nelinpeli
  - Kaksinpeli netin välityksellä
  - Vaikeampi yksinpeli, jossa kimmokkeita tippuu ikkunan yläreunasta
- Kaksinpelitulostaulu, jossa näkyy pelaajien tulokset toisia pelaajia vastaan
- Muokattavuuden lisääminen
  - Pallon nopeuden määrittely
  - Pelikentän koon määrittely
