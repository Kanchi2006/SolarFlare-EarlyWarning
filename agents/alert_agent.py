def generate_alert(risk):

    if risk == "HIGH":
        return "⚠️ High Solar Flare Risk"

    elif risk == "MEDIUM":
        return "🟡 Moderate Solar Flare Risk"

    else:
        return "🟢 Low Solar Flare Risk"