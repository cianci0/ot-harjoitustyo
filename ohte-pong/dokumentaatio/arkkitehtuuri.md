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

Jokainen näistä on toteutettu omana luokkanaan. Näkymistä yksi on aina kerrallaan näkyvänä. Näkymien näyttämisestä vastaa [UI](../src/ui/ui.py)-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta. Se ainoastaan kutsuu [TodoService](../src/services/todo_service.py)-luokan metodeja.

Kun sovelluksen todo-listan tilanne muuttuu, eli uusi käyttäjä kirjautuu, todoja merkitään tehdyksi tai niitä luodaan, kutsutaan sovelluksen metodia [initialize_todo_list](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/ui/todos_view.py#L70) joka renderöi todolistanäkymän uudelleen sovelluslogiikalta saamansa näytettävien todojen listan perusteella.
