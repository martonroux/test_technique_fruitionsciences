from error_gest import ErrorGest
from move_player import MovePlayer
import sys


def main():
    error_gest = ErrorGest()
    error_gest.len_gest()
    error_gest.h_flag()
    error_gest.file_check()

    file = sys.argv[1]
    move_player = MovePlayer(file)
    move_player.__init__(file)
    move_player.pilot()


main()
