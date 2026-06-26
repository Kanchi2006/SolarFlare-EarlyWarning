def get_recommendation(risk):

    if risk == "LOW":
        return """
        ✅ Continue normal operations.
        
        • No immediate threat detected.
        • Continue monitoring solar activity.
        """

    elif risk == "MEDIUM":
        return """
        ⚠️ Monitor critical systems.

        • Check satellite communication systems.
        • Watch GPS accuracy.
        • Increase monitoring frequency.
        """

    else:
        return """
        🚨 Activate mitigation protocols.

        • Notify satellite operators.
        • Monitor power grid stability.
        • Prepare for communication disruptions.
        """