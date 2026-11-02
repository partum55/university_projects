import unittest
import random
from futsal import *


class TestFutsal(unittest.TestCase):
    def setUp(self):
        random.seed(42)

    def test_team_add_player_and_properties(self):
        team = Team("Test Team")
        keeper = Goalkeeper("Keeper", 1)
        team.add_player(keeper, "goalkeeper")
        self.assertEqual(team.players_by_position, {'goalkeeper': [keeper], 'fieldplayer': []})
        self.assertEqual(team.players, [keeper])
        self.assertEqual(keeper.position_type, "goalkeeper")
        self.assertEqual(keeper.team, team)

        # Додаємо кілька field players
        fp1 = FieldPlayer("FP1", 2)
        fp2 = FieldPlayer("FP2", 3)
        team.add_player(fp1, "fieldplayer")
        team.add_player(fp2, "fieldplayer")
        self.assertEqual(len(team.players), 3)
        self.assertEqual(team.players_by_position['fieldplayer'], [fp1, fp2])

    def test_team_invalid_position(self):
        team = Team("Test Team")
        fp = FieldPlayer("FP", 2)
        with self.assertRaises(ValueError) as context:
            team.add_player(fp, "invalid_position")
        expected_msg = "Position must be one of: goalkeeper, fieldplayer"
        self.assertEqual(str(context.exception), expected_msg)

    def test_team_overflow(self):
        team = Team("Overflow Team")
        # Додаємо 1 goalkeeper і 4 fieldplayer = 5 гравців
        keeper = Goalkeeper("Keeper", 1)
        team.add_player(keeper, "goalkeeper")
        for i in range(2, 6):
            fp = FieldPlayer(f"FP{i}", i)
            team.add_player(fp, "fieldplayer")
        with self.assertRaises(TeamOverflowError) as context:
            extra = FieldPlayer("Extra", 6)
            team.add_player(extra, "fieldplayer")
        self.assertEqual(context.exception.message, "A futsal team can have only 5 players.")

    def test_distance_calculation(self):
        fp1 = FieldPlayer("A", 1)
        fp2 = FieldPlayer("B", 2)
        fp1.game_position = [0, 0]
        fp2.game_position = [3, 4]
        self.assertEqual(fp1.distance_to(fp2), 5)

    def test_find_nearest_teammate(self):
        team = Team("Test Team")
        fp1 = FieldPlayer("A", 1)
        fp2 = FieldPlayer("B", 2)
        fp3 = FieldPlayer("C", 3)
        team.add_player(fp1, "fieldplayer")
        team.add_player(fp2, "fieldplayer")
        team.add_player(fp3, "fieldplayer")
        fp1.game_position = [0, 0]
        fp2.game_position = [1, 1]
        fp3.game_position = [5, 5]
        nearest = fp1.find_nearest_teammate()
        self.assertEqual(nearest, fp2)

    def test_fieldplayer_ball_pass(self):
        team = Team("Team A")
        fp1 = FieldPlayer("FP1", 1)
        fp2 = FieldPlayer("FP2", 2)
        team.add_player(fp1, "fieldplayer")
        team.add_player(fp2, "fieldplayer")
        fp1.has_ball = True
        fp1.game_position = [0, 0]
        fp2.game_position = [2, 2]
        fp1.ball_pass()
        self.assertFalse(fp1.has_ball)
        self.assertTrue(fp2.has_ball)

    def test_goalkeeper_ball_pass_success(self):
        team = Team("Team A")
        keeper = Goalkeeper("Keeper", 1)
        fp = FieldPlayer("FP", 2)
        team.add_player(keeper, "goalkeeper")
        team.add_player(fp, "fieldplayer")
        keeper.has_ball = True
        keeper.ball_possession = 4
        keeper.game_position = [0, 0]
        fp.game_position = [10, 0]
        keeper.ball_pass()
        self.assertFalse(keeper.has_ball)
        self.assertTrue(fp.has_ball)

    def test_goalkeeper_ball_pass_failure(self):
        team = Team("Team A")
        keeper = Goalkeeper("Keeper", 1)
        fp = FieldPlayer("FP", 2)
        team.add_player(keeper, "goalkeeper")
        team.add_player(fp, "fieldplayer")
        keeper.has_ball = True
        keeper.ball_possession = 5
        with self.assertRaises(BallPossessionError) as context:
            keeper.ball_pass()
        self.assertEqual(str(context.exception), "A goalkeeper has only 4 seconds for a pass.")

    def test_match_str_not_enough_teams(self):
        match = Match("2025-01-01")
        self.assertEqual(str(match), "Match does not have enough teams yet.")

    def test_match_str_not_started(self):
        match = Match("2025-01-01")
        team1 = Team("Team1")
        team2 = Team("Team2")
        match.add_team(team1)
        match.add_team(team2)
        expected = "Match between Team1 and Team2 hasn't started yet."
        self.assertEqual(str(match), expected)

    def test_match_str_in_progress(self):
        match = Match("2025-01-01")
        team1 = Team("Team1")
        team2 = Team("Team2")
        match.add_team(team1)
        match.add_team(team2)
        match.start_match()
        self.assertEqual(str(match), "Match in progress...")

    def test_match_str_finished(self):
        match = Match("2025-01-01")
        team1 = Team("Team1")
        team2 = Team("Team2")
        match.add_team(team1)
        match.add_team(team2)
        match.start_match()
        result = match.finish_match()
        self.assertEqual(result, "Match ended!")
        expected = f"Match over. Score: {team1.name} {match.score[0]} - {match.score[1]} {team2.name}"
        self.assertEqual(str(match), expected)

    def test_match_start_ball_assignment(self):
        match = Match("2025-01-01")
        team1 = Team("Team1")
        team2 = Team("Team2")
        p1 = FieldPlayer("P1", 1)
        p2 = FieldPlayer("P2", 2)
        p3 = Goalkeeper("GK1", 3)
        p4 = FieldPlayer("P3", 4)
        team1.add_player(p1, "fieldplayer")
        team1.add_player(p3, "goalkeeper")
        team2.add_player(p2, "fieldplayer")
        team2.add_player(p4, "fieldplayer")
        match.add_team(team1)
        match.add_team(team2)
        match.start_match()
        for team in match.teams:
            for player in team.players:
                self.assertIsNotNone(player.game_position[0])
                self.assertIsNotNone(player.game_position[1])
        all_players = team1.players + team2.players
        ball_holders = [player for player in all_players if player.has_ball]
        self.assertEqual(len(ball_holders), 1)


if __name__ == '__main__':
    unittest.main()
