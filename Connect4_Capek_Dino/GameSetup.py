import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from GameBoard import GameBoard
from GameLogic import GameLogic

class GameSetup(Agent):
    class SetupBehaviour(OneShotBehaviour):
        async def on_start(self):
            print("Starting agent GameSetup...")

        async def run(self):
            board = GameBoard()
            game_logic = GameLogic("logic_agent@xmpp.social", "VAS_Project_DC_1", board, self.agent.mode)

            await game_logic.start()
            await spade.wait_until_finished(game_logic)
            await self.agent.stop()        

        async def on_end(self):
            print("Ending agent GameSetup...")
                
    async def setup(self):
        one_shot_beh = self.SetupBehaviour()
        self.add_behaviour(one_shot_beh)
        
    def __init__(self, jid, _pass, mode):
        super().__init__(jid, _pass)
        self.mode = mode
