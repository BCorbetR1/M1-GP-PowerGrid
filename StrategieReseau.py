from Terrain import Terrain, Case


class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        return -1, {}, []

# implémentation de la fonction qui gère la configuration manuelle d'un réseau à partir d'un terrain. L'utilisateur doit avoir l'occasion 
# d'entrer les informations de la nouvelle configuration. Vous pouvez, par exemple, implémenter une fonction qui, dans une boucle, affiche
# le réseau et le terrain puis demande à l'utilisateur d'ajouter un noeud à un endroit du terrain. L'utilisateur devrait alors spécifier 
# quels liaisons seront générées entre ce nouveau noeud et les noeuds voisins existants
class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TOVERIFY
        counter = 0
        while True:
            t.afficher()
            if counter == 0:
                entree = int(input("Entrez la coordonnée x de l'entrée : "))
                print(f"Entrée définie {entree})")
            else :
                cmd = input("Entrez une commande (ajouter_noeud, ajouter_arc ou quitter) : ")
                if cmd == "ajouter_noeud":
                    n = int(input("Entrez l'ID du noeud : "))
                    x = int(input("Entrez la coordonnée x du noeud : "))
                    y = int(input("Entrez la coordonnée y du noeud : "))
                    self.ajouter_noeud(n, (x, y))
                    print(f"Noeud {n} ajouté en ({x}, {y})")
                elif cmd == "ajouter_arc":
                    n1 = int(input("Entrez l'ID du premier noeud : "))
                    n2 = int(input("Entrez l'ID du second noeud : "))
                    self.ajouter_arc(n1, n2)
                    print(f"Arc ajouté entre {n1} et {n2}")
                elif cmd == "quitter":
                    break
            counter += 1
        return self.entree, self.noeuds, self.arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TODO
        return -1, {}, []
