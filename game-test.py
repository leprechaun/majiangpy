import majiang
import majiang.game
import majiang.player
import majiang.plays
import majiang.tiles
import majiang.wall
import majiang.cemetary
import majiang.accountant

import random
import pprint


wall = majiang.wall.Wall()
cemetary = majiang.cemetary.Cemetary()
accountant = majiang.accountant.Accountant()

players = []
players.append(majiang.player.Player("laurence"))
players.append(majiang.player.Player("liang pei"))
players.append(majiang.player.Player("qian qi"))
players.append(majiang.player.Player("cute lam"))


game = majiang.game.Game(players, wall, accountant, cemetary)
game.start()

pprint.pprint(game._log)
