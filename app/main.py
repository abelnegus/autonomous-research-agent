"""
Autonomous Research & Intelligence Agent

Entry point for the research agent.
"""

from agents.planner import ResearchPlanner
from agents.researcher import Researcher


def main():
    question = input("What would you like me to research? ")

    planner = ResearchPlanner()
    researcher = Researcher()

    plan = planner.create_plan(question)

    print("\nResearch Plan:")
    for step in plan:
        print(f"- {step}")

    results = researcher.research(question, plan)

    print("\nResearch Results:")
    for result in results:
        print(f"- {result}")


if __name__ == "__main__":
    main()