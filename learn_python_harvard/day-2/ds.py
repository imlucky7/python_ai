from typing import Any


students = {
    "Hiya": 45,
    "Pranab": 34
}

def main():
    spacecraft = {"name": "James Webb Telescope"}
    spacecraft["distance"] = "2"
    spacecraft.update({"orbit": "Sun"})
    print(createReport(spacecraft))

    for name in students.keys(): #students.values()
        print(f"{name} got marks in math {students.get(name)}")
    
    for name, marks in students.items():
        print(f"{name} got marks {marks}") 

def createReport(spacecraft: Any):
    return f"""
    ============ REPORT ============
    Name: {spacecraft["name"]}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}
    ================================
    """

main()