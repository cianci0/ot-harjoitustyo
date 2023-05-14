# Käyttöohje

Lataa projektin viimeisin [release](https://github.com/cianci0/ot-harjoitustyo/releases)

## Ohjelman käynnistäminen

Siirry hakemistoon <em>ohte-pong</em>

Asenna riippuvuudet komennolla

```bash
poetry install
```

Luo tarvittavat tietokannat komennolla

```bash
poetry run invoke build
```
Huom! Ohjelma ei toimi eikä sitä voi testata ennen kuin tietokannat on luotu

ja käynnistä ohjelma komennolla

```
poetry run invoke start
```

Voit suorittaa testit ja tarkastella testikattavuutta komennolla

```
poetry run invoke coverage-report
```

ja tarkastella lint-virheitä komennolla

```
poetry run invoke lint
```
