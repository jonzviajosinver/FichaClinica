class patient():
    ## Atributos
    name = ''  # nombre del paciente
    last_name = ''  # apellido del paciente
    run = ''  # rut del paciente
    sex = ''  # sexo del paciente
    day = '' # día de nacimiento
    month = '' # mes de nacimiento
    year = '' # año de nacimiento
    blood_type = ''  # grupo sanguineo del paciente
    allergy_to_any_medication = ''  # alergia a algún medicamento
    weight = 0  # peso del paciente
    height = 0  # estatura del paciente
    medicine_in_use = ''  # medicamentos en uso
    occupation = '' # ocupación
    marital_status = '' # estado civil
    who_does_he_live_with = '' # con quien vive
    address = '' # dirección
    phone_number = '' # numero de teléfono
    mail = '' # correo
    habits = '' # hábitos
    surgical_history = '' # historial quirurgico
    kinesiologist_treatment = '' # tratamiento kinesiologo
    kinesiological_observation = '' # observación kinesiologica
    vaccines = '' #vacunas
    

    def __init__(self,name,last_name,run,sex,day,month,year,blood_type,allergy_to_any_medication,weight,height,medicine_in_use,occupation,marital_status,who_does_he_live_with,address,phone_number,mail,habits,surgical_history,kinesiologist_treatment,kinesiological_observation,vaccines):
        self.name=name
        self.last_name=last_name
        self.run=run
        self.sex=sex
        self.day=day
        self.month=month
        self.year=year
        self.blood_type=blood_type
        self.allergy_to_any_medication=allergy_to_any_medication
        self.weight=weight
        self.height=height
        self.medicine_in_use=medicine_in_use
        self.occupation=occupation
        self.marital_status=marital_status
        self.who_does_he_live_with=who_does_he_live_with
        self.address=address
        self.phone_number=phone_number
        self.mail=mail
        self.habits=habits
        self.surgical_history=surgical_history
        self.kinesiologist_treatment=kinesiologist_treatment
        self.kinesiological_observation=kinesiological_observation
        self.vaccines=vaccines

    def print(self):
        print("Nombre del paciente")
        print(self.name)
        print("Apellido del paciente")
        print(self.last_name)
        print("Rut del paciente")
        print(self.run)
        print("Sexo del paciente")
        print(self.sex)
        print("Diá de atención del paciente")
        print(self.day)
        print("Mes de atención del paciente")
        print(self.month)
        print("Año de atención del paciente")
        print(self.year)
        print("Tipo de grupo sanguineo")
        print(self.blood_type)
        print("Alerguia a algun medicamento")
        print(self.allergy_to_any_medication)
        print("Peso del paciente")
        print(self.weight)
        print("Altura del paciente")
        print(self.height)
        print("Medicamentos en uso")
        print(self.medicine_in_use)
        print("Ocupación del paciente")
        print(self.occupation)
        print("Estado civil del paciente")
        print(self.marital_status)
        print("Con quien vive el paciente")
        print(self.who_does_he_live_with)
        print("Dirrección del paciente")
        print(self.address)
        print("Numero de telefono del paciente")
        print(self.phone_number)
        print("Correo del paciente")
        print(self.mail)
        print("Habitos del paciente")
        print(self.habits)
        print("Historial quirurgico del paciente")
        print(self.surgical_history)
        print("Tratamiento kineciologico del paciente")
        print(self.kinesiologist_treatment)
        print("Observación kineciologica del paciente")
        print(self.kinesiological_observation)
        print("Vacunas del paciente")
        print(self.vaccines)


print("Ficha Clinica")



print("Anote sus datos personales")



print("Ingrese su nombre")
name = (input())

print("Ingrese su apellido")
last_name = input()

print("Ingrese su rut")
run = input()

print("Ingrese su sexo")
sex = input().upper()

print("Ingrese su fecha de nacimiento")

print("día")
day=int (input())
if(day>-31):
    print("Ingrese el día")
        
    
print("mes")
month=int (input())
if(month>-12):
    print("Ingrese el mes")
        

print("año")
year=int (input())
if(year<-1900):
    print("Ingrese el año")
         

    

print("Ingrese su grupo sanguíneo")
blood_type = input()

print("Ingrese si posee alergia a algún medicamento")
allergy_to_any_medication = input()

print("Ingrese el peso del paciente")
weight = input()

print("Ingrese la estatura del paciente")
height = input()

print("Ingrese los medicamentos que usa el paciente")
medicine_in_use = input()

print("Ingrese su ocupacipon")
occupation = input()

print("Ingrese su estado civil")
marital_status = input()

print("Ingrese con quien vive")
who_does_he_live_with = input()

print("Ingrese su dirección")
address = input()

print("Ingrese su numero de teléfono")
phone_number = input()

print("Ingrese su correo")
mail = input()

print("Ingrese sus hábitos")
habits = input()

print("Ingrese sus antecedentes quirurgicos")
surgical_history = input()

print("Ingrese su tratamiento kinesiologo")
kinesiologist_treatment = input()

print("Ingrese su observación kinesiologa")
kinesiological_observation = input()

print("Ingrese sus vacunas")
vaccines = input()

patient=patient(name,last_name,run,sex,day,month,year,blood_type,allergy_to_any_medication,weight,height,medicine_in_use,occupation,marital_status,who_does_he_live_with,address,phone_number,mail,habits,surgical_history,kinesiologist_treatment,kinesiological_observation,vaccines)

patient.print()
