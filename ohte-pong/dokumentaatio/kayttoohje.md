# Käyttöohje

Lataa projektin viimeisin [release](https://github.com/cianci0/ot-harjoitustyo/releases)

## Ohjelman käynnistäminen

Siirry hakemistoon ohte-pong

Asenna riippuvuudet komennolla

```bash
poetry install
```

Luo tarvittavat tietokannat komennolla

```bash
poetry run invoke build
```

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
