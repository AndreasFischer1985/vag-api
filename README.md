# VAG-API

[OpenAPI-Dokumentation](https://bundesapi.github.io/vag-api/) der API zu [start.vag](https://start.vag.de/desktop/) - dem Verkehrs-Aktiengesellschaft (VAG) Abfahrsmonitor mit Echtzeitprognose. Die API gibt Zugriff auf alle Haltestellen, Fahrten und Abfahrten im Gebiet des Verkehrsbund Großraum Nürnberg (VGN). Eine Schnittstellenbeschreibung durch die VAG findet sich auf [opendata.vag.de](https://opendata.vag.de) bzw. [hier](https://opendata.vag.de/dataset/api-echtzeitauskunft) unter [Creative CommonsAttribution 4.0 Int](https://creativecommons.org/licenses/by/4.0/) veröffentlicht. 

Eine Übersicht über den VGN Gesamtraum findet sich unter vgn.de:

<a href="https://www.vgn.de/media/schienennetz-gesamtraum-vgn.pdf">
<img src="https://github.com/AndreasFischer1985/vag-api/blob/main/VGN%20Schienennetz%20Gesamtraum.png" alt="VGN Schienennetz Gesamtraum" style="width:600px;"/>
</a>

## Informationen zu Haltestellen, Abfahrten & Fahrten

Informationen zu Haltestellen, aktuellen Abfahrten und Fahrten (vgl. Angebote wie https://www.vag.de/#abfahrt oder https://start.vag.de/desktop/).

### Beispiel
```bash
haltestellen=$(curl https://start.vag.de/dm/api/haltestellen.json/vgn)
abfahrtenNbg=$(curl https://start.vag.de/dm/api/abfahrten.json/vgn/510)
fahrtenBus=$(curl https://start.vag.de/dm/api/v1/fahrten.json/bus)
```


## Fahrplan-Informationen

Weitere Informationen zu Verbindungen zwischen zwei Haltestellen (vgl. Angebote wie https://www.vag.de/#fahrplan).

### Beispiel
```bash
haltestelle=$(curl https://efa-gateway.vag.de/api/v1/locations?name=Feucht)
verbindungen=$(curl https://apigateway.vag.de/efa/journeys?FromType=any&From=80000941&ToType=any&To=80021819&ChangeSpeed=normal&UseNearbyStops=false&RouteType=leasttime&MaxFootpath=10&Transportations=9462&TariffDetails=true&Departure=2022-07-08T07%3A39%3A00.000Z)
```
