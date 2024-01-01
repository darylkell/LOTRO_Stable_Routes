## LOTRO Stable routes
Finds paths from A to B for Lord of the Rings Online, considering only the usage of stables.

```
usage: lotro_stable_routing.py [-h] [source] [destination] [number]

Provide a source, destination, and desired number of results (number)

positional arguments:
  source       Stable to leave from
  destination  Stable to arrive at
  number       Number of results to return

options:
  -h, --help   show this help message and exit
```

### Example:
```
python .\lotro_stable_routing.py                                                                                   ─╯

From: esteldin
To: ost rimmon
Number of results: 5

85 paths found:

1)  (5 hops) esteldin -> west bree -> south bree -> minas tirith -> ost rimmon
2)  (5 hops) esteldin -> west bree -> south bree -> aldburg -> ost rimmon
3)  (5 hops) esteldin -> rivendell stables -> south bree -> minas tirith -> ost rimmon
4)  (5 hops) esteldin -> rivendell stables -> south bree -> aldburg -> ost rimmon
5)  (5 hops) esteldin -> rivendell stables -> zidir-nesad -> minas tirith -> ost rimmon
```
