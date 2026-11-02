"""
Using Python, you will have the opportunity to
simulate a futsal match.
Let's do it!
"""

from futsal import *

def test_futsal():
    print('Creating Match...')
    # each match has its date and match title
    match = Match('2025-03-07')
    assert match.date == '2025-03-07'
    assert match.teams == []
    # match has an empty title because the list of match teams is empty
    assert match.title == ''
    assert str(match) == "Match does not have enough teams yet."
    # size of the match field
    assert match.MATCH_FIELD_WIDTH == 20
    assert match.MATCH_FIELD_LENGTH == 40
    assert match.started is False
    assert match.finished is False
    assert match.score == [0, 0]

    # now we are ready to create and add teams
    print('Creating Teams...')
    team_1 = Team('Liverpool')
    assert team_1.name == 'Liverpool'
    # a team can    have up to 5 players in 2 different positions:
    # goalkeeper and fieldplayer
    assert team_1.players == []
    assert team_1.players_by_position == {'goalkeeper': [], 'fieldplayer': []}
    # this team does not belong to any match
    assert team_1.match is None

    # let's create some players
    print('Adding Players...')
    try:
        Player('Alisson', 1)
        assert False
    except TypeError as e:
        assert (
            e.args[0] == 
            "Can't instantiate abstract class Player without an implementation "
            "for abstract method 'ball_pass'"
        )
    player_1 = Goalkeeper('Alisson', 1)
    assert player_1.name == 'Alisson'
    assert player_1.number == 1
    assert player_1.position_type is None
    assert player_1.game_position == [None, None]
    # assert player_1.team is None
    assert player_1.has_ball is False
    # only goalkeeper control time of ball possession
    assert player_1.ball_possession == 0
    assert isinstance(player_1, Player)
    assert isinstance(Player.position_type, property)

    team_1.add_player(player_1, 'goalkeeper')
    assert team_1.players_by_position == {'goalkeeper': [player_1],
                                          'fieldplayer': []}
    assert team_1.players == [player_1]
    # the position type of the player is a position in the team
    assert player_1.position_type == 'goalkeeper'
    # assert player_1.team  == team_1

    # we also can create and add other player to the team
    team_1.add_player(FieldPlayer("Karavaev", 2), "fieldplayer")
    team_1.add_player(FieldPlayer("Popov", 3), "fieldplayer")
    team_1.add_player(FieldPlayer("Shaparenko", 10), "fieldplayer")

    # only the goalkeeper and fieldplayer positions are in the team
    try: 
        team_1.add_player(FieldPlayer("Besedin", 9), "player")
        assert False
    except ValueError as e:
        assert (
            e.args[0] == 
        f"Position must be one of: {', '.join(team_1.players_by_position.keys())}"
        )
    team_1.add_player(FieldPlayer("Besedin", 9), "fieldplayer")

    # a team can have only 5 players
    assert len(team_1.players) == 5
    try:
        team_1.add_player(FieldPlayer("Bondar", 5), "fieldplayer")
        assert False
    except TeamOverflowError as e:
        assert e.message == 'A futsal team can have only 5 players.'

    print('First team created!')

    # Create second team and add players
    team_2 = Team('Manchester United')
    player_2 = FieldPlayer("Traore", 9)
    team_2.add_player(Goalkeeper("Bushchan", 1), "goalkeeper")
    team_2.add_player(FieldPlayer("Matviyenko", 4), "fieldplayer")
    team_2.add_player(FieldPlayer("Bondar", 5), "fieldplayer")
    team_2.add_player(FieldPlayer("Stepanenko", 6), "fieldplayer")
    team_2.add_player(player_2, "fieldplayer")

    print('Second team created!')
    # Match add a team
    match.add_team(team_1)
    assert team_1.match == match, team_1.match
    assert match.title == ''

    # attempt to start the match
    try:
        match.start_match()
        assert False
    except ValueError as e:
        assert e.args[0] == "A match must have two teams to start."

    match.add_team(team_2)
    assert team_1.match == team_2.match
    assert match.title == 'Liverpool vs. Manchester United'
    assert (
        str(match) ==
        "Match between Liverpool and Manchester United hasn't started yet."
    )
    # start the match
    match.start_match()
    print("Match started!")
    assert str(match) == "Match in progress..."
    assert match.started is True
    assert match.finished is False
    assert match.score == [0, 0]

    # players randomly placed on the field
    # the player game_position is the list of two integers
    for team in match.teams:
        for player in team.players:
            assert player.game_position[0] is not None
            assert player.game_position[1] is not None

    # one random player took possession of ball 
    all_players = team_1.players + team_2.players
    players = [player for player in all_players if player.has_ball]
    assert len(players) == 1
    assert players[0].has_ball is True 
    players[0].has_ball is False

    player_1.has_ball = True
    player_1.ball_possession = 5

    # a goalkeeper has only 4 sec for pass
    try:
        player_1.ball_pass()
        assert False
    except BallPossessionError as e:
        assert e.args[0] == "A goalkeeper has only 4 seconds for a pass."

    # for a pass, the player seaches for the nearest teammate
    assert isinstance(player_1, DistanceMixin)
    assert isinstance(player_2, DistanceMixin)

    team_1.players[-1].game_position = [5, 5]
    team_1.players[-2].game_position = [10, 10]

    distance = ((10 - 5) ** 2 + (10 - 5) ** 2) ** 0.5
    assert team_1.players[-1].distance_to(team_1.players[-2]) == distance

    player_1.has_ball = False
    player_2.has_ball = True
    nearest = player_2.find_nearest_teammate()
    player_2.ball_pass()
    assert player_2.has_ball is False
    assert nearest.has_ball is True

    # end the match
    assert match.finish_match() == "Match ended!"
    assert match.finished is True
    assert (
        str(match) ==
        f"Match over. Score: {match.teams[0].name} {match.score[0]} - "
        f"{match.score[1]} {match.teams[1].name}"
    )
    print("Match ended!")

if __name__=='__main__':
    test_futsal()
