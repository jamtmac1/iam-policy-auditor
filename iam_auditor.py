import boto3
import json

iam = boto3.client('iam')

# Added list of roles
escalation_actions = [
	"iam:CreateUser",
	"iam:PutUserPolicy",
	"iam:AddUserToGroup",
	"iam:PassRole"
	"iam:Createaccesskey"

# Function to list and export results
]
def list_roles():
    response = iam.list_roles()

with open('iam_audit_results.csv', mode='w', newline= '') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["roleName", "Wildcards", "EscalationRisks"])

	for role in response['Roles']:
        print(f"Role: {role['RoleName']}")

if __name__ == "__main__":
    list_roles()
