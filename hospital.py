class Patient(object):
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.bed_number = 'none'

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def admit(self, patient):
        if len(self.patients) < self.capacity:      #if there is space in hospital
            patient.bed_number = len(self.patients)+1  #assign bed number
            self.patients.append(patient)           #admit patient
            print "Patient admitted"
        else:
            print "Hospital is full, could not admit patient"
        return self
    def discharge(self, patient):
        for person in self.patients:
            if person == patient:
                person.bed_number = 'none'
                self.patients.remove(person)
        return self
    def showPatients(self):
        for person in self.patients:
            print person.name, person.bed_number

p1 = Patient("Julee", ["authority", "amoxicillin"])
p2 = Patient("Hiet", ["foolishness", "peaches"])
p3 = Patient("Shine", ["pollen", "dust mites"])
p4 = Patient("Sword", ["structure"])

h1 = Hospital("Teedersea", 3)

h1.admit(p1).admit(p2).admit(p3).admit(p4).showPatients()
print '*'
h1.discharge(p2).showPatients()
