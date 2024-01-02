import random
import math
from spade.agent import Agent
from spade.behaviour import State, FSMBehaviour
from GameAI import MiniMax

class GameLogic(Agent):
    #On a board players tokens are 1 and agents tokens are 2
    player = 1
    agent = 2
    
    class GameBehaviour(FSMBehaviour):
        async def on_start(self):
            print("Starting agent GameLogic...")

        async def on_end(self):
            print("Ending agent GameLogic...")
            
    class Player(State):
        async def run(self):
            self.agent.board.print_board()
            print("Player:")
            col = int(input("Choose column[0-6]: "))
            if col < 0 or col > 6:
                self.set_next_state("Player")
            else:
                if self.agent.board.column_not_full(col):
                    row = self.agent.board.get_next_free_row(col)
                    self.agent.board.place_token(row, col, self.agent.player)
                    if self.agent.board.check_result(self.agent.player):
                        print("Player won!")
                        self.agent.board.print_board()
                        await self.agent.stop()
                    else:
                        self.set_next_state("GameAgent")
                else:
                    self.set_next_state("Player")
                
    class GameAgent(State):
        async def run(self):
            self.agent.board.print_board()
            print("Game Agent:")
            col=0
            if(self.agent.mode == 0):
                col = random.randint(0,self.agent.board.column_count - 1)
            elif self.agent.mode == 1:
               col, value = MiniMax.minimax(MiniMax, self.agent.board, 5, True)
               
            if self.agent.board.column_not_full(col):
                row = self.agent.board.get_next_free_row(col)
                self.agent.board.place_token(row, col, self.agent.agent)
                if self.agent.board.check_result(self.agent.agent):
                    print("Game Agent won!")
                    self.agent.board.print_board()
                    await self.agent.stop()
                else:
                    self.set_next_state("Player")
            else:
                self.set_next_state("GameAgent")
                
    async def setup(self):
        fsmBeh = self.GameBehaviour()
        
        fsmBeh.add_state(name="Player", state=self.Player(), initial=True)
        fsmBeh.add_state(name="GameAgent", state=self.GameAgent())

        fsmBeh.add_transition(source="Player", dest="GameAgent")
        fsmBeh.add_transition(source="Player", dest="Player")
        fsmBeh.add_transition(source="GameAgent", dest="Player")
        fsmBeh.add_transition(source="GameAgent", dest="GameAgent")
        
        self.add_behaviour(fsmBeh)
        
    def __init__(self, jid, _pass, board, mode):
        super().__init__(jid, _pass)
        self.board = board
        self.mode = mode
