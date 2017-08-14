from view import View
import sys
from curses import wrapper

class Main:
    view = View()
    game = Game()
    def run(self):
        self.view.start()
        while True:
            try:
                self.game.play()
            except Exception:
                break
        self.view.shut_down()
        sys.exit(0)

if __name__ == '__main__':
    Main().run()
