# VAG-API

OpenAPI-Dokumentation der API zu [start.vag](https://start.vag.de/desktop/) - dem Verkehrs-Aktiengesellschaft (VAG) Abfahrsmonitor mit Echtzeitprognose.


## Abfahrt

https://www.vag.de/#abfahrt


### Beispiel
```bash
haltestellen=$(curl -m 60 https://start.vag.de/dm/api/haltestellen.json/vgn)
abfahrtenNbg=$(curl -m 60 https://start.vag.de/dm/api/abfahrten.json/vgn/510)
```


## Fahrplan (WIP)

https://www.vag.de/#fahrplan

### Beispiel
```bash
haltestelle=$(curl -m 60 https://efa-gateway.vag.de/api/v1/locations?name=Feucht)
verbindungen=$(curl -m 60 https://apigateway.vag.de/efa/journeys?FromType=any&From=80000941&ToType=any&To=80021819&ChangeSpeed=normal&UseNearbyStops=false&RouteType=leasttime&MaxFootpath=10&Transportations=9462&TariffDetails=true&Departure=2022-07-08T07%3A39%3A00.000Z)
```
