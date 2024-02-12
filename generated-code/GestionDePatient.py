class Patient:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def afficher_informations(self):
        print(f"Nom: {self.nom} {self.prenom}")
        print(f"Age: {self.age}")
        print("---")


class Secretaire:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def planifier_rdv(self, patient, date):
        print(f"RDV planifié pour {patient.nom} {patient.prenom} le {date}.")


class Medecin:
    def __init__(self, nom, prenom, specialite):
        self.nom = nom
        self.prenom = prenom
        self.specialite = specialite

    def consulter_patient(self, patient):
        print(f"{self.specialite} - Consultation de {patient.nom} {patient.prenom}.")


class CabinetMedical:
    def __init__(self):
        self.patients = []
        self.secretaires = []
        self.medecins = []

    def ajouter_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.nom} {patient.prenom} ajouté avec succès.")

    def ajouter_secretaire(self, secretaire):
        self.secretaires.append(secretaire)
        print(f"Secrétaire {secretaire.nom} {secretaire.prenom} ajoutée avec succès.")

    def ajouter_medecin(self, medecin):
        self.medecins.append(medecin)
        print(f"Médecin {medecin.nom} {medecin.prenom} ajouté avec succès.")

    def planifier_rdv(self, patient, date):
        if not self.secretaires:
            print("Aucune secrétaire disponible pour planifier le RDV.")
        else:
            secretaire = self.secretaires[0]
            secretaire.planifier_rdv(patient, date)

    def consulter_patient(self, patient):
        if not self.medecins:
            print("Aucun médecin disponible pour la consultation.")
        else:
            medecin = self.medecins[0]
            medecin.consulter_patient(patient)

cabinet = CabinetMedical()

patient1 = Patient("Dupont", "Jean", 30)
cabinet.ajouter_patient(patient1)

secretaire1 = Secretaire("Martin", "Alice")
cabinet.ajouter_secretaire(secretaire1)

medecin1 = Medecin("Dr. Smith", "John", "Cardiologie")
cabinet.ajouter_medecin(medecin1)

cabinet.planifier_rdv(patient1, "2024-02-10")
cabinet.consulter_patient(patient1)
