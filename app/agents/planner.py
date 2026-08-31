class ResearchPlanner:
    """Creates a research plan for a given question."""

    def create_plan(self, question: str) -> list[str]:
        return [
            f"Understand the research question: {question}",
            "Identify relevant sources",
            "Collect evidence",
            "Verify important claims",
            "Analyze the findings",
            "Generate the final report",
        ]