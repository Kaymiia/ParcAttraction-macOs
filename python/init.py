import sqlite3
import sys
import re

try:
    # Connexion à la base de données
    conn = sqlite3.connect("parc.db")
    cur = conn.cursor()

    # Exécution du fichier init.sql
    with open('sql_file/init.sql') as f:
        fichier = f.read()
        lines = fichier.split(";")
        for line in lines:
            line = line.strip()
            line = re.sub("\s+", " ", line)  # Remplacer les espaces multiples par un seul espace
            if line:  # S'assurer que la ligne n'est pas vide
                cur.execute(line)

    # Exécution du fichier create.sql
    with open('sql_file/create.sql') as f:
        fichier = f.read()
        lines = fichier.split(";")
        for line in lines:
            line = line.strip()
            line = re.sub("\s+", " ", line)  # Idem pour les espaces
            if line:  # S'assurer que la ligne n'est pas vide
                cur.execute(line)

    # Commit des changements et fermeture de la connexion
    conn.commit()
    conn.close()

except sqlite3.Error as e:
    print(f"Erreur lors de la connexion à la base de données: {e}")
    sys.exit(1)
