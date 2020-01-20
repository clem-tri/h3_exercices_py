class DateNaissance:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def ToString(self):
        return "%02d/%02d/%d" %(self.jour, self.mois, self.annee)


class Personne:
    def __init__(self, nom, prenom, date_naissance: DateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    def Afficher(self):
        print("Nom: %s \nPrénom: %s \nDate de naissance: %s" % (self.nom, self.prenom, self.date_naissance.ToString()))


class Employe(Personne):

    def __init__(self, nom, prenom, date_naissance, salaire):
        Personne.__init__(self, nom, prenom, date_naissance)
        self.salaire = salaire

    def Afficher(self):
        print("Nom:%s \nPrénom: %s \nDate de naissance: %s\nSalaire: %s" % (self.nom, self.prenom, self.date_naissance.ToString(), self.salaire))


class Chef(Employe):
    def __init__(self, nom, prenom, date_naissance, salaire, service):
        Employe.__init__(self, nom, prenom, date_naissance, salaire)
        self.service = service

    def Afficher(self):
        print("Nom:%s \nPrénom: %s \nDate de naissance: %s\nSalaire: %s\nService : %s" % (self.nom, self.prenom, self.date_naissance.ToString(), self.salaire, self.service))


P = Personne("Ilyass", "Math", DateNaissance(1, 7, 1982))
P.Afficher()

E=Employe("Ilyass", "Math", DateNaissance(1, 7, 1985),7865.548)
E.Afficher()

Ch=Chef("Ilyass", "Math", DateNaissance(1,7,1988),7865.548,"Ressource humaine")
Ch.Afficher()