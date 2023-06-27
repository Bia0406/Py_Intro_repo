class Angajat:
    def __int__(self, nume, prenume, functie, salariu, vechime):
        self.nume = nume
        self.prenume = prenume
        self.functie = functie
        self.salariu = salariu
        self.vechime = vechime

    def date_angajat(self):
        print(f'Angajat : {self.nume}{self.prenume}')
        print(f'Functia : {self.functie}')
        print(f'Salariu : {self.salariu}')
        print(f'Vechime : {self.vechime}')
        print('----------------------------------------')

    def salariu_angajat(self, salariu):
        if salariu <= 3000:
            print('Muncitor necalificat')
        elif salariu >= 3000:
            print('Muncitor cu calificare')
        else:
            print('Nu am putut identifica')

    def marire_salariu(self, suma, vechime):
        if vechime <= 5:
            self.salariu += 300
            print(f'Salariu dvs s-a majorat cu {suma}')
            print(f'Salariul este {self.salariu}')
        elif vechime >= 5:
            self.salariu += 500
            print(f'Salariul dvs s-a majorat cu {suma}')
            print(f'Salariul este {self.salariu}')
        else:
            print(f'Nu am putut identifica')


