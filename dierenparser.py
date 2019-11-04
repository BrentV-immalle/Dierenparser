class Dier:

    def __init__(self):
        self.naam = ""
        self.soort = ""
        self.aantalPoten = 0
        self.kleur = ""
        self.geluid = ""

    def print(self):
        print(
            f'Het dier heet [{self.naam}], is van soort [{self.soort}], heeft [{self.aantalpoten}] poten, is [{self.kleur}] en maakt dit geluid: [{self.geluid}]!')


def parse_line(line):
    naam, soort, aantalpoten, kleur, geluid = line.split(' - ')
    d = Dier()
    d.naam = naam
    d.soort = soort
    d.aantalpoten = int(aantalpoten)
    d.kleur = kleur
    d.geluid = geluid
    print(f'Parsed: [{naam}] [{soort}] [{aantalpoten}] [{kleur}] [{geluid}]')
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
        dier.print()

if __name__ == '__main__':
    import doctest
    doctest.testfile("parse_line.txt")
