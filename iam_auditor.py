import boto3
import json
import csv

iam = boto3.client('iam')

# Added list of roles
escalation_actions = [
	"iam:CreateUser",
	"iam:PutUserPolicy",
	"iam:AddUserToGroup",
<<<<<<< HEAD
	"iam:PassRole"
	"iam:Createaccesskey"
=======
	"iam:PassRole",
	"iam:CreateAccessKey"
>>>>>>> b7d1ac23766271c30a71d5696083186866796015

# Function to list and export results
]

def list_roles():
	with open("'iam_audit_results.csv", mode = "w", newline="") as csvfile:
		writer = csvwriter(csvfile)
		write.writerow(["RolenName","Wildcard","EscalationRisks". 
    response = iam.list_roles()

with open('iam_audit_results.csv', mode='w', newline= '') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["roleName", "Wildcards", "EscalationRisks"])

	for role in response['Roles']:
        print(f"Role: {role['RoleName']}")

if __name__ == "__main__":
    list_roles()
