# VAG-API

OpenAPI-Dokumentation der API zu [start.vag](https://start.vag.de/desktop/) - dem Verkehrs-Aktiengesellschaft (VAG) Abfahrsmonitor mit Echtzeitprognose.

## Beispiel

```bash
haltestellen=$(curl -m 60 https://start.vag.de/dm/api/haltestellen.json/vgn)
abfahrtenNbg=$(curl -m 60 https://start.vag.de/dm/api/abfahrten.json/vgn/510)
```
