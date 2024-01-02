import spade
from spade.agent import Agent
from spade.behaviour import State, FSMBehaviour
from GameSetup import GameSetup

class GameStart(Agent):
    class StartBehaviour(FSMBehaviour):
        async def on_start(self):
            print("Starting agent GameStart...")       

        async def on_end(self):
            print("Ending agent GameStart...")
                
    class ValidGameSettings(State):
        async def run(self):
            print("Starting the game...")
            game_setup = GameSetup("setup_agent@xmpp.social", "VAS_Project_DC", self.agent.mode)
            
            await game_setup.start()
            await spade.wait_until_finished(game_setup)
            await self.agent.stop()


    class BadGameSettings(State):
        async def run(self):
            print("Game modes: [0 - random placement, 1 - minimax algorithm]")
            mode = int(input("Choose game mode: "))
            if(mode != 0 and mode != 1):
                print("Choose one of the available game modes!")
                self.set_next_state("Bad")
            else:
                self.agent.mode = mode
                self.set_next_state("Valid")

    async def setup(self):
        fsmBeh = self.StartBehaviour()
        
        fsmBeh.add_state(name="Valid", state=self.ValidGameSettings())
        fsmBeh.add_state(name="Bad", state=self.BadGameSettings(), initial=True)

        fsmBeh.add_transition(source="Bad",dest="Valid")
        fsmBeh.add_transition(source="Bad",dest="Bad")

        self.add_behaviour(fsmBeh)
