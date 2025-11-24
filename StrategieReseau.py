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
        counter = 0
        nodes = {}
        arcs = []
        while True:
            print("Réseau actuel :")
            t.afficher()
            if counter == 0:
                entry = int(input("Entrez l'ID' de l'entrée : "))
                print(f"Entrée définie {entry})")
            else :
                cmd = input("Entrez une commande (1 : ajouter_noeud, 2 : ajouter_arc ou 3 : quitter) : ")
                if cmd == "1" or cmd == "ajouter_noeud":
                    n = int(input("Entrez l'ID du noeud : "))
                    x = int(input("Entrez la coordonnée x du noeud : "))
                    y = int(input("Entrez la coordonnée y du noeud : "))
                    nodes[n] = (x, y)
                    print(f"Noeud {n} ajouté en ({x}, {y})")
                elif cmd == "2" or cmd == "ajouter_arc":
                    n1 = int(input("Entrez l'ID du premier noeud : "))
                    n2 = int(input("Entrez l'ID du second noeud : "))
                    arcs.append((n1, n2))
                    print(f"Arc ajouté entre {n1} et {n2}")
                elif cmd == "3" or cmd == "quitter":
                    break
            counter += 1
        return entry, nodes, arcs


class StrategieReseauAuto(StrategieReseau):
    def configurer(
        self, t: Terrain
    ) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TODO
        return -1, {}, []
