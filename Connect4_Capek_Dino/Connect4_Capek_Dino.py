import spade
from GameStart import GameStart

async def main():
    print("Application is starting...")
    start_game = GameStart("start_agent@xmpp.social","VAS_Project_DC_2")
    await start_game.start()
    
    await spade.wait_until_finished(start_game)
    
    print("Application finished!")

if __name__ == '__main__':
    spade.run(main())