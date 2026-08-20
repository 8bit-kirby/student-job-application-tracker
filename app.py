company = input("Enter the company name: ").strip()
position = input("Enter the position you applied for: ").strip()
status = input("Enter the application status (e.g., pending, accepted, rejected): ").strip

application = {
    "company": company,
    "position": position,
    "status": status
}

print(
    f"I applied to {application['company']} for the position of {application['position']}. "
    f"Application status: {application['status']}."
)