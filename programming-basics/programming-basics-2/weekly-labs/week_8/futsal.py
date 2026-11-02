"""Temp"""

import random
from abc import ABC, abstractmethod


class BallPossessionError(Exception):
    """Ball Possession Error"""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class TeamOverflowError(Exception):
    """Team Overflow Error"""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class DistanceMixin:
    """Mixin for distance calculation"""

    def distance_to(self, other: 'Player') -> float:
        """Calculate distance to another player"""
        x1, y1 = self.game_position
        x2, y2 = other.game_position
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


class Player(ABC, DistanceMixin):
    """Abstract class Player"""

    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
        self._position_type = None
        self.game_position = [None, None]
        self.has_ball = False
        self.ball_possession = 0
        self.team = None

    @property
    def position_type(self):
        """Return position type"""
        return self._position_type

    @position_type.setter
    def position_type(self, value: str):
        """Set position type"""
        self._position_type = value

    def find_nearest_teammate(self):
        """Finds the nearest teammate from the player's team"""
        if self.team is None:
            return None
        teammates = [player for player in self.team.players if player != self]
        if not teammates:
            return None
        return min(teammates)

    @abstractmethod
    def ball_pass(self) -> None:
        """Ball pass"""

    def __lt__(self, other):
        return self.number < other.number


class FieldPlayer(Player):
    """Class FieldPlayer"""

    def ball_pass(self) -> None:
        """Pass the ball to the nearest teammate"""
        nearest = self.find_nearest_teammate()
        if nearest:
            self.has_ball = False
            nearest.has_ball = True


class Goalkeeper(Player):
    """Class Goalkeeper"""

    def __init__(self, name: str, number: int):
        super().__init__(name, number)
        self.ball_possession = 0

    def ball_pass(self) -> None:
        if self.ball_possession > 4:
            raise BallPossessionError("A goalkeeper has only 4 seconds for a pass.")
        nearest = self.find_nearest_teammate()
        if nearest:
            self.has_ball = False
            nearest.has_ball = True


class Team:
    """Class Team"""

    def __init__(self, name: str):
        self.name = name
        self.match = None
        self.players = []
        self.players_by_position = {'goalkeeper': [], 'fieldplayer': []}

    def add_player(self, player: Player, position_type: str) -> None:
        """Adds a player to the team"""
        if position_type not in self.players_by_position:
            raise ValueError(f"Position must be one of: "
                             f"{', '.join(self.players_by_position.keys())}")
        if len(self.players) >= 5:
            raise TeamOverflowError("A futsal team can have only 5 players.")
        if position_type == 'goalkeeper' and len(self.players_by_position['goalkeeper']) >= 1:
            raise TeamOverflowError("A futsal team can have only 1 goalkeeper.")
        if position_type == 'fieldplayer' and len(self.players_by_position['fieldplayer']) >= 4:
            raise TeamOverflowError("A futsal team can have only 4 field players.")
        self.players.append(player)
        self.players_by_position[position_type].append(player)
        player.position_type = position_type
        player.team = self


class Match:
    """Class Match"""

    MATCH_FIELD_WIDTH = 20
    MATCH_FIELD_LENGTH = 40

    def __init__(self, date):
        self.date = date
        self.teams = []
        self.score = [0, 0]
        self.started = False
        self.finished = False
        self.title = ""

    def add_team(self, team: Team) -> None:
        """Adds a team"""
        if len(self.teams) >= 2:
            return
        self.teams.append(team)
        team.match = self
        if len(self.teams) == 2:
            self.title = f"{self.teams[0].name} vs. {self.teams[1].name}"

    def start_match(self) -> None:
        """Starts the match"""
        if len(self.teams) != 2:
            raise ValueError("A match must have two teams to start.")
        self.started = True
        for team in self.teams:
            for player in team.players:
                player.game_position = [random.randint(0, self.MATCH_FIELD_WIDTH - 1),
                                        random.randint(0, self.MATCH_FIELD_LENGTH - 1)]
        all_players = [player for team in self.teams for player in team.players]
        if all_players:
            chosen = random.choice(all_players)
            chosen.has_ball = True

    def finish_match(self) -> str:
        """Finish the match"""
        self.score = [random.randint(0, 10), random.randint(0, 10)]
        self.finished = True
        return "Match ended!"

    def __str__(self) -> str:
        if len(self.teams) < 2:
            return "Match does not have enough teams yet."
        if not self.started:
            return (f"Match between {self.teams[0].name} and "
                    f"{self.teams[1].name} hasn't started yet.")
        if self.started and not self.finished:
            return "Match in progress..."
        return (f"Match over. Score: {self.teams[0].name} "
                f"{self.score[0]} - {self.score[1]} {self.teams[1].name}")
