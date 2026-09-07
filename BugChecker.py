severity = "High"

if severity == "critical":
    print("Fix immediately")
elif severity == "high":
    print("Fix Today")
elif severity == "medium":
    print("Fix This Sprint")
else:
    print("Low Priority")