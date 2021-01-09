# import serial
import pygame
import math
from time import sleep

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
# si = serial.Serial('COM3',baudrate=9600,timeout=1)

def get_coord(pos, index):
    x_val = pos%20
    if x_val == 0:
        x_val=20
    x = (min(x_val, 21-x_val)-1)*81+40
    y_val = math.ceil(pos/10)
    y = (10-y_val)*79+40
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
        h=930

        # icon=pygame.image.load("icon.jpg")
        self.GD=pygame.display.set_mode((w,h))
        pygame.display.set_caption("Snakes And Ladders")
        pygame.display.update()

        self.board= pygame.image.load("assets/board.jpg")
        self.GD.fill(white)
        self.GD.blit(self.board, (45, 0))
        self.dices = [None]
        self.dices.extend([pygame.image.load(f"assets/dices/dice{str(index)}.png") for index in range(1, 7)])

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
        pygame.display.update()

    def display_player(self, player_id, value):
        self.update_display()
        font = pygame.font.Font('freesansbold.ttf', 25)
        text_display = f'Player {str(player_id+1)} threw: '
        text = font.render(text_display, True, black)
        text_rect = text.get_rect()
        text_rect.center = (450, 875)
        self.GD.blit(self.dices[int(value)], (540, 805))
        self.GD.blit(text, text_rect)

    def make_move(self, player_id, dice_val):
        final_pos = self.player_states[player_id]["pos"]+int(dice_val)
        if(final_pos == 100):
            self.player_states[player_id]["pos"] = final_pos
            print(f'Player {str(player_id+1)} WINS!')
            self.display_winner(player_id)
            sleep(6) # Wait for 6 secs then close. 
            Quit()
        elif (final_pos > 100):
            return
        elif final_pos in SNAKES.keys():
            print(f'Player {str(player_id+1)} lands on snake!')
            self.player_states[player_id]["pos"] = SNAKES[final_pos]
            # si.write('7'.encode())
        elif final_pos in LADDERS.keys():
            print(f'Player {str(player_id+1)} lands on ladder!!')
            self.player_states[player_id]["pos"] = LADDERS[final_pos]
            # si.write('6'.encode())
        else:
            self.player_states[player_id]["pos"] = final_pos

    def display_winner(self, player_id):
        self.update_display()
        font = pygame.font.Font('freesansbold.ttf', 25)
        text_display = f'Player {str(player_id+1)} WON !!'
        text = font.render(text_display, True, black)
        text_rect = text.get_rect()
        text_rect.center = (450, 875)
        self.GD.blit(text, text_rect)
        pygame.display.update()

    def display_turn(self, player_id):
        self.update_display()
        font = pygame.font.Font('freesansbold.ttf', 25)
        text_display = f'Player {str(player_id+1)}\'s turn now'
        text = font.render(text_display, True, black)
        text_rect = text.get_rect()
        text_rect.center = (450, 875)
        self.GD.blit(text, text_rect)
        pygame.display.update()
 
def Quit():
    pygame.quit()
    quit()

def main():
    GAME_LOOP = True
    g = Game()
    CURR_MOVE=0
    PLAYERS=4
    while GAME_LOOP:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    Quit()
                if event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_ESCAPE:
                        Quit()
        
        g.display_turn(CURR_MOVE)
        print(f'Player {str(CURR_MOVE+1)}\'s turn : ')
        # si.write('1'.encode())
        # while True:
        #     value = si.readline().decode('ascii')
        #     if value != '':
        #         value = int(value)
        #         if value > 0 and value < 7:
        #             print(value)
        #             break

        value = input()
        if value=='q':
            Quit()
        g.make_move(CURR_MOVE, value)
        g.display_player(CURR_MOVE, value)
        pygame.display.update()
        CURR_MOVE = (CURR_MOVE+1)%PLAYERS
        sleep(3) # to display what the player just threw

if __name__ == "__main__":
    main() 

