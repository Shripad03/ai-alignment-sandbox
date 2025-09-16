# agent/tools.py
def planner(slots:int=3):
    return [f"Slot {i+1}" for i in range(slots)]

def picker(options, preference):
    for o in options:
        if preference.lower() in o.lower():
            return o
    return options[0] if options else "N/A"

def formatter(plan:list):
    return "\n".join(f"- {p}" for p in plan)
