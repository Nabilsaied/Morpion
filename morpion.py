import random

class Morpion():
    def __init__(self):
        self.board = [["-", "-", "-"],
                      ["-", "-", "-"],
                      ["-", "-", "-"]
                      ]
        self.player1 = ""
        self.player2 = "IA"
        self.choice1 = ""
        self.choice2 = ""
        self.current_player = ""

    def afficher_menu(self):
        print('Bienvenue dans le Morpion')
        print("Menu:")
        print("1. Ajouter Ton Nom et ton choix")
        print("2. Jouer")
        print("3. Quitter")
        for row in self.board:
            print(' | '.join(row))
        print()

    def players(self):
        self.player1 = input("Tape ton nom dans le jeu : ")
        self.choice1 = input("Tu veux jouer avec 'X' ou avec 'O' ? : ").upper()
        if self.choice1 not in ["X", "O"]:
            print("Choix invalide. Saisissez 'X' ou 'O'.")
            return
        print(self.player1 + ", tu vas jouer avec ", self.choice1)
        self.choice2 = "O" if self.choice1 == "X" else "X"
        print("L'IA va jouer avec " + self.choice2)
        self.current_player = self.player1

    def change_player(self):
        if self.current_player == self.player1:
            self.current_player == self.player2
        else :
            self.current_player == self.player1

    def check_win(self, choice):
        win_conditions = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        return [choice, choice, choice] in win_conditions


    def jouer(self):
        game_over = False
        self.players()
        while not game_over:
            print(f"C'est le tour de {self.current_player}")
            if self.current_player == self.player1:
                valid_move = False
                while not valid_move:
                    try:
                        ligne = int(input("Choisis une ligne  (0, 1, 2): "))
                        col = int(input("Choisis une colonne (0, 1, 2): "))
                        if 0 <= ligne <= 2 and 0 <= col <= 2 and self.board[ligne][col] == "-":
                            self.board[ligne][col] = self.choice1
                            valid_move = True
                        else:
                            print("Cette case est déjà prise ou est hors des limites. Essayez de nouveau.")
                    except ValueError:
                        print("S'il vous plaît, entrez un nombre valide.")
            else:
                valid_move = False
                while not valid_move:
                    ligne, col = random.randint(0, 2), random.randint(0, 2)
                    if self.board[ligne][col] == "-":
                        self.board[ligne][col] = self.choice2
                        valid_move = True
                        print(f"L'IA a joué en ligne {ligne + 1}, colonne {col + 1}")

            for row in self.board:
                print(' | '.join(row))
            print()

            if self.check_win(self.choice1 if self.current_player == self.player1 else self.choice2):
                print(f"{self.current_player} a gagné!")
                game_over = True
            else:
                game_over = True
            self.change_player()

        print("Jeu terminé.")


def main():
    morpion_game = Morpion()
    while True:
        morpion_game.afficher_menu()
        choix = input("Choisissez une option (1, 2, 3) : ")
        if choix == '1':
            morpion_game.players()
        elif choix == '2':
            morpion_game.jouer()
            break
        elif choix == '3':
            print("Merci d'avoir joué. Au revoir!")
            break
        else:
            print("Choix non valide. Veuillez sélectionner une option valide.")


if __name__ == "__main__":
    main()
