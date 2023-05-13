from db.score_database import get_top3

def leaderboard_text():
    scores = get_top3("db")
    rank = 1
    scores_text = "\n"

    for score in scores:
        name = score[0]
        points = score[1]
        if len(name) > 9:
            name = name[0:8] + "..."
        scores_text += f"       {rank}. {name} –– {points} pistettä\n"
        rank += 1 

    return scores_text
