



def decide_risk_level(score):
    if score >= 8:
        return "danger"
    elif score >= 4:
        return "suspicious"
    else:
        return "safe"
