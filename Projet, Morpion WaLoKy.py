# Initialiser la grille 
grid = [[" " for _ in range(3)] for _ in range(3)]




# Fonction pour afficher la grille
def show_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

# Fonction pour vérifier si une case est vide
def empty_box(grid, box):
    return grid[box // 3][box% 3] == " "

# Fonction pour jouer le jeu
def play():
    player = "X"
    for ride in range(9):  # Maximum 9 tours pour une partie de morpion
        show_grid(grid)
        box = int(input(f"player {player}, choisis une case (0-8) : "))
        
        # Vérifie si la case est valide
        while not (0 <= box < 9) or not empty_box(grid, box):
            box = int(input("Case invalide ou déjà prise. Choisis une autre case (0-8) : "))
        
        # Place le coup sur la grille
        grid[box // 3][box % 3] = player
        
        # Vérifie la condition de victoire
        if check_victory(grid, player):
            show_grid(grid)
            print(f"the player {player} won!")
            return
    
        # Alterne le player
        player = "O" if player == "X" else "X"
    
    show_grid(grid)
    print("it's a draw!")

# Fonction pour vérifier la victoire
def check_victory(grid, player):
    for row in grid:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([grid[row][col] == player for row in range(3)]):
            return True
    if all([grid[i][i] == player for i in range(3)]) or \
       all([grid[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Démarrer le jeu
play()
