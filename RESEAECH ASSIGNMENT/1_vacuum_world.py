# Vacuum World - Simple Reflex Agent (two rooms: A and B)
# Percept = (location, status). The agent cleans if dirty, else moves to the other room.

def vacuum_agent(location, status):
    """Simple reflex agent: returns the action for the current percept."""
    if status == "Dirty":
        return "Suck"
    return "Right" if location == "A" else "Left"

def run_vacuum_world(location, rooms):
    cost = 0
    print(f"Initial State -> Location: {location}, Rooms: {rooms}\n")
    # Keep acting until both rooms are clean
    while "Dirty" in rooms.values():
        action = vacuum_agent(location, rooms[location])
        print(f"Location: {location} | Status: {rooms[location]:5} | Action: {action}")
        if action == "Suck":
            rooms[location] = "Clean"
        elif action == "Right":
            location = "B"
        else:
            location = "A"
        cost += 1
    print(f"\nFinal State   -> Location: {location}, Rooms: {rooms}")
    print(f"Both rooms are clean. Total actions (cost) = {cost}")

if __name__ == "__main__":
    loc = input("Enter starting location (A/B): ").strip().upper()
    a = input("Is room A Dirty or Clean? ").strip().capitalize()
    b = input("Is room B Dirty or Clean? ").strip().capitalize()
    run_vacuum_world(loc, {"A": a, "B": b})
