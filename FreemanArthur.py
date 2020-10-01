#TP1 Arthur Freeman Algrithme. 
#Implémentation d'algorithme Greedy pour maximaliser
#l'espace occupé sur un disque de capacité space, en prenant
#des fichiers fi de poids si. 

def save_files_space(files, space):
    weight = 0  #On initialise la taille et le tableau des objets à prendre.
    to_take = [] 
    #On trie en sens inverse selon la taille. 
    files.sort(key=lambda x : x[1], reverse=True) #Plus grande taille à la plus petite..

    #Pour chaque fichier,  
    for i in range(0, len(files)):
        #Si l'ajout de ce fichier ne dépasse pas la taille disponible.
        if weight + files[i][1] < space: 
            weight += files[i][1] #On incrémente l'espace pris.
            to_take.append(files[i]) #On le prends 
    return to_take #Une fois qu'on ne peux plus prendre de fichiers, on renvoie le tableau final.

#Même algorithme, expcepté que l'on maximalise le nombre de fichiers.
def save_files_number(files, space):
    weight = 0
    to_take = []
    #En triant du plus petit au plus grand, on prends d'abord
    files.sort(key=lambda x : x[1]) #les fichiers les plus petits.

    for i in range(0, len(files)): #On les prends jusqu'à ce qu'on ne puisse plus.
        if weight + files[i][1] < space:
            weight += files[i][1]
            to_take.append(files[i])
    return to_take

#Set de fichiers pour tester.
files = [("f1",2.61),("f2",8.2),("f3",5.97),("f4",1.5)]
print(save_files_space(files, 10)) #c'est bien les résultats attendus.
print(save_files_number(files, 10))