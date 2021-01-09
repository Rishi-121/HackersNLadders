import pygame
import math

black=(10,10,10)
white=(250,250,250)
red= (200,0,0)
b_red=(240,0,0)
green=(0,200,0)
b_green=(0,230,0)
blue=(0,0,200)
grey=(50,50,50)
yellow=(150,150,0)
purple=(43,3,132)
b_purple=(60,0,190)

def get_coord(pos, index):
    x_val = pos%20
    if x_val == 0:
        x_val=20
    x = (min(x_val, 21-x_val)-1)*81+40
    y_val = math.ceil(pos/10)
    y = (10-y_val)*79+40
    # print(f'pos: {pos} x_val: {x_val} y_val: {y_val}' )
    x_offset = 20 # 45 for board, 25 for the goti
    y_offset = -10*index # to give a shift so that the gotis don't overlap
    return (x+x_offset, y+y_offset)

SNAKES = {
    16: 8,
    52: 28,
    78: 25,
    99: 21,
    95: 75,
    93: 89
}

LADDERS = {
    2: 45,
    4: 27,
    9: 31,
    47: 84,
    70:87,
    71:91
}

class Game():
    def __init__(self):
        pygame.init()
        w=900
        h=900

        # icon=pygame.image.load("icon.jpg")
        self.GD=pygame.display.set_mode((w,h))
        pygame.display.set_caption("Snakes And Ladders")
        pygame.display.update()

        self.board= pygame.image.load("assets/board.jpg")
        self.GD.fill(white)
        self.GD.blit(self.board, (45, 0))
        

        self.player_states = [
            {"pos": 1, "image": pygame.image.load("assets/gotis/redgoti.png")},
            {"pos": 1, "image": pygame.image.load("assets/gotis/bluegoti.png")},
            {"pos": 1, "image": pygame.image.load("assets/gotis/greengoti.png")},
            {"pos": 1, "image": pygame.image.load("assets/gotis/yellowgoti.png")}
        ]
        for index, player in enumerate(self.player_states):
            self.GD.blit(player["image"], get_coord(player["pos"], index))

        pygame.display.update()

    def update_display(self):
        self.GD.fill(white)
        self.GD.blit(self.board, (45, 0))
        for index, player in enumerate(self.player_states):
            self.GD.blit(player["image"], get_coord(player["pos"], index))
        # self.GD.blit(self.player_states["image"], (40, 769))
        pygame.display.update()

    def display_player(self, player_id, value=""):
        self.update_display()
        font = pygame.font.Font('freesansbold.ttf', 25)
        text_display = f'Player {str(player_id+1)} threw: {value}'
        text = font.render(text_display, True, black)
        text_rect = text.get_rect()
        text_rect.center = (450, 860)
        self.GD.blit(text, text_rect)

    def make_move(self, player_id, dice_val):
        final_pos = self.player_states[player_id]["pos"]+int(dice_val)
        if(final_pos == 100):
            print(f'Player {str(player_id+1)} WINS!')
            Quit()
        elif (final_pos > 100):
            return
        elif final_pos in SNAKES.keys():
            print(f'Player {str(player_id+1)} lands on snake!')
            self.player_states[player_id]["pos"] = SNAKES[final_pos]
        elif final_pos in LADDERS.keys():
            print(f'Player {str(player_id+1)} lands on ladder!!')
            self.player_states[player_id]["pos"] = LADDERS[final_pos]
        else:
            self.player_states[player_id]["pos"] = final_pos

 
def Quit():
    pygame.quit()
    quit()

def main():
    GAME_LOOP = True
    g = Game()
    g.display_player(0)
    CURR_MOVE=0
    PLAYERS=4
    while GAME_LOOP:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    Quit()
                if event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_ESCAPE:
                        Quit()
        
        print(f'Player {str(CURR_MOVE+1)}: ')
        value = input()
        if value=='q':
            Quit()
        g.make_move(CURR_MOVE, value)
        g.display_player(CURR_MOVE, value)
        pygame.display.update()

        CURR_MOVE = (CURR_MOVE+1)%PLAYERS

main()

