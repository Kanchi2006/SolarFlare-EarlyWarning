def classify_flare(xray):

    if xray < 10:
        return "LOW"

    elif xray < 50:
        return "MEDIUM"

    else:
        return "HIGH"