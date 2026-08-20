from application import create_application

def main():
  company = input("Enter the company name: ").strip()
  position = input("Enter the position you applied for: ").strip()
  status = input("Enter the application status (e.g., pending, accepted, rejected): ").strip()

  application = create_application(company, position, status)

  print(
      f"I applied to {application['company']} for the position of {application['position']}. "
      f"Application status: {application['status']}."
  )

if __name__ == "__main__":
  main()