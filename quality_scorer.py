def calculate_quality_score(blur_status, brightness_status, edge_status):
    score = 0

    if blur_status == "SHARP":
        score += 40

    if brightness_status == "NORMAL":
        score += 30

    if edge_status == "GOOD":
        score += 30

    return score


def get_recommendation(score):
    if score >= 80:
        return "GOOD QUALITY IMAGE"
    elif score >= 50:
        return "AVERAGE QUALITY IMAGE"
    else:
        return "LOW QUALITY IMAGE"
