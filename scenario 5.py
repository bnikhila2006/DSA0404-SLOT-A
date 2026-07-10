data = [
    ["A1", 45000, 720, 0, 1],
    ["A2", 30000, 650, 1, 0],
    ["A3", 60000, 780, 0, 1],
    ["A4", 28000, 620, 2, 0],
    ["A5", 52000, 710, 1, 1]
]
print("Loan Approval Dataset")
for row in data:
    print(row)
income = int(input("\nEnter Monthly Income (₹): "))
credit_score = int(input("Enter Credit Score: "))
existing_loans = int(input("Enter Existing Loans: "))
if credit_score >= 700:
    if income >= 45000:
        decision = "Approved"
    else:
        decision = "Rejected"
else:
    decision = "Rejected"
print("\nPrediction:", decision)
print("\nDecision Rules:")
print("1. If Credit Score >= 700")
print("      If Income >= 45000 --> Approved")
print("      Else --> Rejected")
print("2. If Credit Score < 700 --> Rejected")
