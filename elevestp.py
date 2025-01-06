eleves=[]
notes=[]

def calculer_moyenne(notes) :
    return (sum(notes)/len(notes))

def afficher_repartitions(nom,notes) :
    eleve_r ="Étudiants ayant réussi : "
    eleve_e ="Étudiants en échec : "

    for i in range (len(notes)) :
        
        if (notes[i]>=10) :
            eleve_r+=nom[i]+","
        else :
            eleve_e+=nom[i]+","

    return eleve_r + "\n" + eleve_e
    

def meilleure_note (noms,notes) :
    meilleure_note=0
    for i in range (len(notes)) :
        if notes[i]>meilleure_note :
            meilleure_note = i
    
    p=f"L’étudiant ayant la meilleure note est {noms[meilleure_note]} avec {notes[meilleure_note]}"
    return p
        

    
    

ne=int(input("nb eleves ?"))
for i in range (ne) :
    e=str(input("nom :"))
    eleves.append(e)

    n=int(input(f"note de {e} :"))
    notes.append(n)
print("la moyenne : ",calculer_moyenne(notes))

print ("la répartiontion : " + afficher_repartitions(eleves,notes))

print(meilleure_note(eleves,notes))




