import request.request as req

# Ajouter une critique liée à une attraction
def add_critique(data):
    cur, conn = req.get_db_connection()
    try:
        query = """
        INSERT INTO critique (nom, prenom, crit, note, attraction_id)
        VALUES (?, ?, ?, ?, ?);
        """
        cur.execute(query, (
            data.get('nom', 'Anonyme'),
            data.get('prenom', 'Anonyme'),
            data['crit'],
            data['note'],
            data['attraction_id']
        ))
        conn.commit()
        return cur.lastrowid
    except Exception as e:
        print("Erreur lors de l'ajout de la critique :", e)
        return False
    finally:
        cur.close()
        conn.close()

# Récupérer toutes les critiques pour une attraction spécifique
def get_critiques_by_attraction(attraction_id):
    cur, conn = req.get_db_connection()
    try:
        cur.execute("SELECT * FROM critique WHERE attraction_id = ?;", (attraction_id,))
        return cur.fetchall()
    except Exception as e:
        print("Erreur lors de la récupération des critiques :", e)
        return []
    finally:
        cur.close()
        conn.close()

# Supprimer une critique par ID
def delete_critique(critique_id):
    cur, conn = req.get_db_connection()
    try:
        cur.execute("DELETE FROM critique WHERE critique_id = ?;", (critique_id,))
        conn.commit()
        return cur.rowcount > 0
    except Exception as e:
        print("Erreur lors de la suppression de la critique :", e)
        return False
    finally:
        cur.close()
        conn.close()
