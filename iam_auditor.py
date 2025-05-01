import boto3
import json

iam = boto3.client('iam')

# Added list of roles
escalation_actions = [
	"iam:CreateUser",
	"iam:PutUserPolicy",
	"iam:AddUserToGroup",
	"iam:PassRole"
	"iam:create access key"

]
def list_roles():
    response = iam.list_roles()
    for role in response['Roles']:
        print(f"Role: {role['RoleName']}")

if __name__ == "__main__":
    list_roles()
