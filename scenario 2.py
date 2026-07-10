# Email data
emails = [
    ["E1", 1, 3, 120, 0],
    ["E2", 6, 15, 300, 1],
    ["E3", 0, 1, 80, 0],
    ["E4", 4, 10, 250, 1],
    ["E5", 2, 5, 160, 0]
]

print("Training Data:")
for email in emails:
    print(email)

# New email
num_links = 5
num_caps_words = 12
email_length = 280

# Simple prediction rule
if num_links >= 4 or num_caps_words >= 10 or email_length >= 250:
    print("\nPrediction: Spam Email")
else:
    print("\nPrediction: Not Spam Email")
