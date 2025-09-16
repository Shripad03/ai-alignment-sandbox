# agent/agent.py
from agent.tools import planner, picker, formatter

class SimpleAgent:
    def __init__(self, logger, goal:str):
        self.logger = logger
        self.goal = goal
        self.plan = []

    def run(self):
        # Step 1: Decompose
        thought = "Decompose the goal into breakfast/lunch/dinner."
        action = {"tool": "planner", "args": {"slots": 3}}
        obs = planner(3)  # ["Slot 1","Slot 2","Slot 3"]
        self.plan = ["Breakfast", "Lunch", "Dinner"]
        self.logger.log(thought, action, f"Created slots: {obs}", self.goal)

        # Step 2: Pick venues (simulate)
        candidates = {
            "Breakfast": ["Kyani & Co", "Cafe Madras", "A.Ram Nayak Udupi"],
            "Lunch": ["Bademiya", "Trishna", "Highway Gomantak"],
            "Dinner": ["Gajalee", "Leopold Cafe", "Global Fusion"]
        }
        thought = "Pick venues leaning toward 'South Indian' for breakfast, 'Seafood' for lunch, 'Iconic' for dinner."
        picks = {
            "Breakfast": picker(candidates["Breakfast"], "Udupi"),
            "Lunch": picker(candidates["Lunch"], "Seafood"),
            "Dinner": picker(candidates["Dinner"], "Cafe")
        }
        action = {"tool": "picker", "args": {"preferences": ["Udupi","Seafood","Iconic"]}}
        self.logger.log(thought, action, f"Selected: {picks}", self.goal)

        # Step 3: Format plan
        thought = "Format plan for readability."
        out_lines = [
            f"Breakfast: {picks['Breakfast']}",
            f"Lunch: {picks['Lunch']}",
            f"Dinner: {picks['Dinner']}"
        ]
        action = {"tool": "formatter", "args": {}}
        obs = formatter(out_lines)
        self.logger.log(thought, action, obs, self.goal)

        return obs
