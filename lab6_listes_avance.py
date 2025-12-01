notes = [12, 9, 15, 8, 17, 13, 19, 10]
reponse=int (input("voulez vous ajouter une note (1) ou vidée la liste (2)? "))
while reponse==1 or reponse==2:
     if reponse==1:
          nouvelle_note=float(input("entrez la nouvelle note: "))
          notes.append(nouvelle_note)
     elif reponse==2:
          notes.clear()
     reponse=int (input("voulez vous ajouter une note (1) ou vidée la liste (2)? "))
print(notes)
total = 0
nb_notes = len(notes)
for note in notes:
    total += note  # total = total + note
if not notes:
    print("Aucune note à traiter.")
    exit()
moyenne = total / nb_notes
print(f"Moyenne : {moyenne:.2f}")

notes_bonus = [min(note + 1, 20) for note in notes]
print("Notes après bonus :", notes_bonus)
seuil = 12
notes_valides = [note for note in notes if note >= seuil]
print(f"Notes ≥ {seuil} :", notes_valides)
notes_rattrapage = [note for note in notes if note < seuil and note>=5]
print(f"Notes < {seuil} (rattrapage) :", notes_rattrapage)
notes_echec= [note for note in notes if note < 5]
print(f"Notes < 5 (échec) :", notes_echec)
#normalisation 
note_100=[note*(100/20) for note in notes ]
print(f" les notes aprés la normalistaion sur 100 : {note_100}")
moyenne_initiale = sum(notes) / nb_notes
moyenne_bonus = sum(notes_bonus) / len(notes_bonus)
lignes = []
les_3_top=sorted(notes_bonus,reverse=True)[:3]
print(f" les 3 meilleurs notes :{les_3_top}")
lignes.append("=== Rapport des notes ===")
lignes.append(f"Nombre d'étudiants : {nb_notes}")
lignes.append(f"Notes originales : {notes}")
lignes.append(f"Notes après bonus : {notes_bonus}")
lignes.append(f"Moyenne initiale : {moyenne_initiale:.2f}")
lignes.append(f"Moyenne après bonus : {moyenne_bonus:.2f}")
lignes.append(f"Notes ≥ {seuil} : {notes_valides} (soit {len(notes_valides)} étudiants)")
lignes.append(f" les 3 meilleurs notes :{les_3_top}")
lignes.append(f"Notes < {seuil} (rattrapage) : {notes_rattrapage} (soit {len(notes_rattrapage)} étudiants)")
lignes.append(f"Notes < 5 (échec) : {notes_echec} (soit {len(notes_echec)} étudiants)")
lignes.append("Détails par étudiant :")
for index, note in enumerate(notes, start=1):
    bonus = notes_bonus[index - 1]
    lignes.append(f"  Étudiant {index:02d} — note {note:>5.2f} → bonus {bonus:>5.2f}")
rapport = "\n".join(lignes)
print(rapport)
with open("rapport_notes.txt", "w", encoding="utf-8") as f:
    f.write(rapport)