# O(n) time | O(k) space
def tournamentWinner(competitions, results):
    teams_and_points = {}
    highest_score_team = ""

    for idx, match in enumerate(competitions):
        home = match[0]
        away = match[1]

        winner = home if results[idx] == 1 else away

        if winner in teams_and_points:
            teams_and_points[winner] += 3
        else:
            teams_and_points[winner] = 3

        if (
            highest_score_team == ""
            or teams_and_points[winner] > teams_and_points[highest_score_team]
        ):
            highest_score_team = winner

    return highest_score_team
