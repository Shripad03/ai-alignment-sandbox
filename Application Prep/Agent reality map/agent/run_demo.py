# agent/run_demo.py
from agent.interceptor import RunLogger
from agent.agents import SimpleAgent

if __name__ == "__main__":
    goal = "Plan a 1-day Mumbai food crawl"
    logger = RunLogger(runs_dir="runs")
    agent = SimpleAgent(logger, goal)
    final = agent.run()
    print("\n=== FINAL PLAN ===\n" + final)
    print(f"\nLog written to: runs/{logger.run_id}.jsonl")