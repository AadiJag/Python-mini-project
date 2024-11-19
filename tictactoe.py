import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 15
CIRCLE_RADIUS = CELL_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = CELL_SIZE // 4
LINE_COLOR = (28, 170, 156)
CIRCLE_COLOR = (242, 85, 96)
CROSS_COLOR = (28, 170, 156)
BACKGROUND_COLOR = (28, 28, 28)

# Fonts
font = pygame.font.Font(None, 100)
small_font = pygame.font.Font(None, 50)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Game board
board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Game variables
current_player = "X"
game_over = False
winner_message = ""

# Draw grid lines
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)

# Draw X and O
def draw_marks():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            mark = board[row][col]
            if mark == "X":
                draw_X(row, col)
            elif mark == "O":
                draw_O(row, col)

# Draw X mark
def draw_X(row, col):
    x_center = col * CELL_SIZE + CELL_SIZE // 2
    y_center = row * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.line(screen, CROSS_COLOR, (x_center - SPACE, y_center - SPACE), (x_center + SPACE, y_center + SPACE), CROSS_WIDTH)
    pygame.draw.line(screen, CROSS_COLOR, (x_center - SPACE, y_center + SPACE), (x_center + SPACE, y_center - SPACE), CROSS_WIDTH)

# Draw O mark
def draw_O(row, col):
    x_center = col * CELL_SIZE + CELL_SIZE // 2
    y_center = row * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, CIRCLE_COLOR, (x_center, y_center), CIRCLE_RADIUS, CIRCLE_WIDTH)

# Check for a winner
def check_winner():
    global game_over, winner_message
    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] != "":
            pygame.draw.line(screen, 'blue', (0, (row + 0.5) * CELL_SIZE), (WIDTH, (row + 0.5) * CELL_SIZE), LINE_WIDTH)
            game_over = True
            winner_message = f"Player {board[row][0]} wins!"
            return board[row][0]
    
    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] != "":
            pygame.draw.line(screen, 'blue', ((col + 0.5) * CELL_SIZE, 0), ((col + 0.5) * CELL_SIZE, HEIGHT), LINE_WIDTH)
            game_over = True
            winner_message = f"Player {board[0][col]} wins!"
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != "":
        pygame.draw.line(screen, 'blue', (0, 0), (WIDTH, HEIGHT), LINE_WIDTH)
        game_over = True
        winner_message = f"Player {board[0][0]} wins!"
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != "":
        pygame.draw.line(screen, 'blue', (WIDTH, 0), (0, HEIGHT), LINE_WIDTH)
        game_over = True
        winner_message = f"Player {board[0][2]} wins!"
        return board[0][2]
    
    return None

# Check for a tie
def check_tie():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == "":
                return False
    return True


def restart_game():
    global board, current_player, game_over, winner_message
    board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    current_player = "X"
    game_over = False
    winner_message = ""
    screen.fill(BACKGROUND_COLOR)
    draw_lines()


def display_message():
    if winner_message:
        text = font.render(winner_message, True, 'yellow')
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    elif check_tie():
        text = font.render("It's a tie!", True, 'yellow')
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))


def handle_click(x, y):
    global current_player
    if game_over:
        return

    row = y // CELL_SIZE
    col = x // CELL_SIZE

    if board[row][col] == "":
        board[row][col] = current_player
        winner = check_winner()
        if winner:
            print(f"Player {winner} wins!")
        elif check_tie():
            print("It's a tie!")
        current_player = "O" if current_player == "X" else "X"

# Main game loop
def main():
    global game_over

    screen.fill(BACKGROUND_COLOR)
    draw_lines()

    while True:
        draw_marks()
        display_message()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                handle_click(x, y)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_game()

        pygame.display.update()

if __name__ == "__main__":
    main()
