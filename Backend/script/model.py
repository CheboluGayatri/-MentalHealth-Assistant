class PHQ9DoctorModel:

    def __init__(self):
        pass

    def predict(self, responses):

        total_score = sum(responses)

        if total_score <= 4:
            severity = "Minimal"
            advice = "You are doing well. Maintain a healthy lifestyle."

        elif total_score <= 9:
            severity = "Mild"
            advice = "Try relaxation techniques and monitor your feelings."

        elif total_score <= 14:
            severity = "Moderate"
            advice = "Consider speaking with a counselor."

        elif total_score <= 19:
            severity = "Moderately Severe"
            advice = "Professional help is recommended."

        else:
            severity = "Severe"
            advice = "Please seek immediate medical attention."

        return {
            "total_score": total_score,
            "severity": severity,
            "doctor_advice": advice
        }