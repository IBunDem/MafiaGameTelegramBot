import enum


class GameTimeEnum(enum.Enum):
    day = 1
    night = 2


# TODO add new roles
class GameStateEnum(enum.Enum):
    meeting = 0
    vote_act = 1
    mafia_act = 2
    # police_act = 4
    # doctor_act = 5
    # maniac_act = 6

