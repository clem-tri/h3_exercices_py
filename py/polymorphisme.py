class Courrier:
    def __init__(self, poids, mode_expedition, address_exp, address_dest):
        self.poids = poids
        self.mode_expedition = mode_expedition
        self.address_exp = address_exp
        self.address_dest = address_dest

    def ToString(self):
        print("Adresse destination: %s \nAdresse expedition: %s\nPoids: %.2f grammes\nMode: %s " % (self.address_dest, self.address_exp, self.poids, self.mode_expedition))


class Lettre(Courrier):
    def __init__(self, poids, mode_expedition, address_exp, address_dest, format: str):
        Courrier.__init__(self, poids, mode_expedition, address_exp, address_dest)
        self.format = format

    def calculTimbre(self):

        tarif_base: float = 0

        if self.format == "A4":
            tarif_base = 2.5
        if self.format == "A3":
            tarif_base = 3.5

        montant = tarif_base * self.poids / 1000

        if self.mode_expedition == "Express":
            montant *= 2

        return montant

    def ToString(self):
        print("Lettre:\n")
        Courrier.ToString(self)
        print("Format:%s\nPrix du timbre:%.2f" % (self.format, self.calculTimbre()))


class Colis(Courrier):
    def __init__(self, poids, mode_expedition, address_exp, address_dest, volume: float):
        Courrier.__init__(self, poids, mode_expedition, address_exp, address_dest)
        self.volume = volume

    def calculTimbre(self):

        montant: float = 0.25 * self.volume * self.poids / 1000

        if self.mode_expedition == "Express":
            montant *= 2

        return montant

    def ToString(self):
        print("Colis:\n")
        Courrier.ToString(self)
        print("Volume: %.2f litres\nPrix du timbre:%.2f" % (self.volume, self.calculTimbre()))


L1=Lettre(80, "Normal", "Lille", "Paris", "A4")
L1.ToString()

C1 = Colis(3500, "Express", "Barcelone", "Marrakech", 2.25)
C1.ToString()

