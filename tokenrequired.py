tokens = 50001

if tokens <= 10000:
    print("Use Small Context Model")
elif tokens > 10000 and tokens <=50000:
    print("Use Medium Context Model")
else:
    print("Use Large Context Model")