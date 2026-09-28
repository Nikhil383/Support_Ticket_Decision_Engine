from laya import Router


class DecisionEngine:

    def __init__(self):
        self.router = Router()

    def analyze(self, message: str) -> dict:

        state = {
            "body": message
        }

        questions = {
            "department": {
                "type": "choice",
                "instructions": "Which department should handle this customer support ticket?",
                "criteria": {
                    "billing": "Charges, invoices, payments, refunds, or billing.",
                    "technical": "APIs, errors, outages, login problems, or technical failures.",
                    "sales": "Purchasing, pricing, or new-plan questions.",
                    "general": "Does not clearly belong to billing, technical, or sales.",
                },
            },

            "urgency": {
                "type": "score",
                "instructions": "How urgent is this customer support issue?",
                "criteria": [
                    "Not urgent and limited impact.",
                    "Needs attention soon but is not a major outage.",
                    "Critical, widespread, security-sensitive, or core production failure.",
                ],
            },

            "needs_human": {
                "type": "noul",
                "instructions": "Does this support ticket require human review?",
            },
        }

        result = self.router.predict(
            state,
            questions,
            model="typed-decisions",
        )

        # Current Laya returns answers inside `answers`.
        answers = result["answers"]

        department = answers["department"]
        urgency = answers["urgency"]
        human = answers["needs_human"]

        return {
            "department": department["choice"],
            "department_probability": department[
                "probabilities"
            ][department["choice"]],
            "urgency": urgency["score"],
            "human_probability": human["noul"],
            "raw": result,
        }