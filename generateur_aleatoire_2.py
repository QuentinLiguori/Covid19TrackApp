import random
import string


# Generation Aléatoire d'Adresse MAC, de Date, de Position (Latitude, Longitude) et de Ville
# Exemple d'Adresse MAC:    08:78:08:F8:13:15
# Exemple de Date:          Wed May 26 16:05:32 GMT+02:00 2021
# Exemple de Position:      Latitude : 49.035945999999996
#                           Longitude : 2.0155355999999998
# Exemple de Ville:         Vauréal


# Liste des villes pouvant être utilisées pour la génération aléatoire
city = ['Paris', 'Cergy', 'Pontoise', 'Conflans-Sainte-Honorine', "Conflans Fin d'Oise", 'Vaureal', "Maisons-Laffitte", "Mantes La Jolie", "Herblay",
        "Cormeille en Parisi", "Argenteuil", "Neuville sur Oise", "Poissy", "Saint-Germaien-en-Laye", "Sartrouville", "Nanterre", "Chatou", "Toulouse", "Marseille",
        "Nice", "Tours", "Rouen", "Orleans", "Cherbourg", "Strasbourg", "Brest", "Barneville Carteret", "Fort-Mahon", "Font-Romeu", "Super-Besse", "Montgeron",
        "Nogent-sur-Seine", "Boulogne-Billancourt", "Guyancourt", "Carrieres-sous-Poissy", "Meylan", "Chatillon", "Lyon", "Annecy", "Biarritz", "Montpellier",
        "La Rochelle", "Saint-Malo", "Bordeaux", "Maurecourt", "Andresy", "Triel-sur-Seine", "Buzancais" ,"Mesnil-le-Roi"," Chamonix-Mont-Blanc","Argentiere",
        "Amiens","Fontaine-les-Grès","Nantes","Limoges","Geneve","Saint-Etienne","Grenoble","Aix-en-Provence"]

print("Il y a "+str(len((city)))+" villes de connues")

# Les jours de la semaine pour la Date
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Les mois de l'année
# month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

# La liste des lettre à parcourir pour le 4ème élément de l'adresse MAC
lettre = ["A", "B", "C", "D", "E", "F"]


# Avec ces éléments, on prépare des Requêtes SQL (INSERT), au vu de remplir une BDD
# Exemple de Requete: INSERT INTO cas (ID) VALUES (valeur généré)

# Les Bases de Données
# cas(
#   ID  VARCHAR(50)     PRIMARY KEY
# )

# Requete de création:
# CREATE TABLE cas (
# 	ID VARCHAR(50) PRIMARY KEY
# );

# data(
#   ID  INTEGER     NOT NULL    AUTO_INCREMENT  PRIMARY KEY,
#   date    VARCHAR(60),
#   ville   VARCHAR(50)
# )

# Requête de Création:
# CREATE TABLE data (
# 	ID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
# 	date VARCHAR(60),
# 	ville VARCHAR(50)
# );


# Ouverture du fichier de données
data = open("covid.txt", "a")

# Ouverture du fichier des Requêtes
requetes = open("requetes.txt","a")

# 1ère ligne du fichier
data.write("City; Time; Position; Adress\n")

nbId = 1000

# Generation de nbId id
for i in range(nbId):

    # Choix de la ville
    ville = random.choice(city)
    # print("City: "+ville)

    # Ajout de la ville dans le fichier
    data.write(str(ville)+"; ")

    # Pour la Date
    Date = ''
    # Exemple de Date:          Wed May 26 16:05:32 GMT+02:00 2021

    Date += str(random.choice(day))+" "
    # print("Date: "+Date)

    Date += str(random.choice(month))+" "
    # print("Date: "+Date)

    # Le numéro du jours
    # print(random.randint(1,31))
    Date += str(random.randint(1,31))
    # print("Date: "+Date)

    # L'heure
    heure = ''
    h =' '
    h +=str(random.randint(00,23))
    # print("h= "+h)

    heure += str(h)+':'
    # print("Heure: "+heure)

    m =''
    m +=str(random.randint(00,59))
    # print("m= "+m)

    heure += str(m)+':'
    # print("Heure: "+heure)

    s =''
    s +=str(random.randint(00,59))
    # print("s= "+s)

    heure += str(s)
    # print("Heure: "+heure)

    Date += " "+str(heure)
    # print("Date: "+Date)

    Date += ' GMT+02:00'
    # print("Date: "+Date)

    Date += " 2021"
    # print("Date: "+Date)

    # Ajout de la Date dans le fichier
    data.write(Date+"; ")

    # Ajout de la Date et de la Ville dans la Table de données data
    # requetes.write("INSERT INTO data VALUES ("+str(Date)+")\n")

    requetes.write("INSERT INTO data (date, ville) VALUES ('"+str(Date)+"', '"+str(ville)+"')\n")


    # Pour la Position
    # Exemple de Position:      Latitude : 49.035945999999996
    #                           Longitude : 2.0155355999999998

    Position = ''

    # Ajout de la Latitude
    Position += "Latitude: "+str(random.uniform(0,90))
    # Ajout de la Longitude
    Position += ", Longitude: "+str(random.uniform(0,90))

    # print("Position:\n"+Position)

    # Ajout de la Position dans le fichier
    data.write(Position+"; ")


    # Pour l'Adresse MAC
    # print("Lettre à utiliser: "+str(lettre))
    adresse = ''

    for j in range(6):
        if j == 3:
            # On met une Lettre à la place d'un chiffre
            # print("i:"+str(i))
            n = random.choice(lettre)
            # print("Lettre:"+n)
            adresse += str(n)

            # print("Adresse: "+adresse)

            n = random.randint(0, 9)
            # print("n: "+str(n))
        else:
            n = random.randint(0, 9)
            # print("n: "+str(n))
            adresse += str(n)

            # print("Adresse: "+adresse)

            n = random.randint(0, 9)
            # print("n: "+str(n))
        if j < 5:
            adresse += str(n) + ':'
        else:
            adresse += str(n)
    # print("Adresse Mac: "+adresse)

    # Ajout de l'adresse dans le fichier de données
    data.write(str(adresse)+"\n\n")

    # Ajout de l'adresse dans la table cas
    requetes.write("INSERT INTO cas VALUES ('"+str(adresse)+"')\n\n")

data.close()
requetes.close()