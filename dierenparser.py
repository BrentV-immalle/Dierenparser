from dataclasses import dataclass


@dataclass
class Dier:
    # def __init__(self): ik denk dat zowel str als "" kan.
    naam: str
    soort: ""
    aantalpoten: 0
    kleur: ""
    geluid: ""
    # def print(self):
    # print(
    # f'Het dier heet [{self.naam}], is van soort [{self.soort}], heeft [{self.aantalpoten}] poten, is [{self.kleur}] en maakt dit geluid: [{self.geluid}]!')


def parse_line(line):
    naam, soort, aantalpoten, kleur, geluid = line.split(' - ')
    d = Dier(naam, soort, int(aantalpoten), kleur, geluid)
    return d


def parse_text(str):
    dieren = []
    for line in str.splitlines():
        d = parse_line(line)
        dieren.append(d)
    return dieren


if __name__ == '__main__':
    dieren = []
    with open('dieren.txt', 'r') as f:
        dieren = parse_text(f.read())

    for dier in dieren:
        print(dier)
