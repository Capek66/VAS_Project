import spade
import datetime

class Agent(spade.agent.Agent):
    class IspisVremena(spade.behaviour.PeriodicBehaviour):
        datum = None
        async def on_start(self):
            print("Pokrecem ispis vremena...\n")
            self.datum = datetime.datetime.now() + datetime.timedelta(days=100)
            self.datum = self.datum.replace(hour=0, minute=0, second=0, microsecond=0)

        async def run(self):
            diff = self.datum - datetime.datetime.now()
            seconds = diff.days * 24 * 60 * 60
            seconds = seconds + diff.seconds
            ispis = 'Preostalo sekundi do dana koji je udaljen 100 dana od danas (' + str(self.datum.day) + '.' + str(self.datum.month) + '.' + str(self.datum.year) + '.): ' + str(seconds)
            print(ispis)

        async def on_end(self):
            await self.agent.stop()

    async def setup(self):
        print("Agent: Pokrećem se!")
        vrijeme = self.IspisVremena(30)
        self.add_behaviour(vrijeme)

async def main():
    a = Agent("setup123@jabb.im","setup123")
    await a.start()
    
    await spade.wait_until_finished(a)
    print("Gotovo")


if __name__ == "__main__":
    spade.run(main())
