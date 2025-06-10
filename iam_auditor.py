import boto3
import json
import csv

iam = boto3.client('iam')

# Added list of roles
escalation_actions = [
	"iam:CreateUser",
	"iam:PutUserPolicy",
	"iam:AddUserToGroup",
	"iam:PassRole",
	"iam:CreateAccessKey"
]
# Function to list and export results


def list_roles():
	with open("'iam_audit_results.csv", mode = "w", newline="") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(["RoleName","Wildcard","EscalationRisks"])
        response = iam.list_roles()

	for role in response['Roles']:
        equal_wildcards = []
	equal_escalations = []

	inline_policy = iam.list_role_policy(RoleName = role_name)["PolicyNames"]
	for policy_name in  inline_policy:
	policy_doc = iam.get_role_policy(RoleName= role_name, PolicyName = policy_name)['PolicyDocument']
	statments = policy_doc.get("Statement",[])
	if isinstance(statements, dict)
		statements = [statements]

	for statement in statements:
		actions = statement.get("Action", [])
		if isinstance(actions, str):
			actions = [actions]
		for action in actions:
			if "*" in action:
			found_wildcards.append(action)
			if action.lower() in [e.lower() for e in escalation_actions]:
			found_escalation_risks.append(action)

#print(f"Role: {role['RoleName']}")

if __name__ == "__main__":
    list_roles()
