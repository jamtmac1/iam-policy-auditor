import boto3
import csv

iam = boto3.client('iam')

## Escalation
escalation_actions = [
    "iam:CreateUser",
    "iam:PutUserPolicy",
    "iam:AddUserToGroup",
    "iam:PassRole",
    "iam:CreateAccessKey"
]

def list_roles():
    with open("iam_audit_results.csv", mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["RoleName", "Wildcard", "EscalationRisks"])

        response = iam.list_roles()

        for role in response['Roles']:
            role_name = role['RoleName']
            found_wildcards = []
            found_escalations = []

            inline_policies = iam.list_role_policies(RoleName=role_name)["PolicyNames"]
            for policy_name in inline_policies:
                policy_doc = iam.get_role_policy(RoleName=role_name, PolicyName=policy_name)['PolicyDocument']
                statements = policy_doc.get("Statement", [])
                if isinstance(statements, dict):
                    statements = [statements]

                for statement in statements:
                    actions = statement.get("Action", [])
                    if isinstance(actions, str):
                        actions = [actions]
                    for action in actions:
                        if "*" in action:
                            found_wildcards.append(action)
                        if action.lower() in [e.lower() for e in escalation_actions]:
                            found_escalations.append(action)

            if found_wildcards or found_escalations:
                writer.writerow([
                    role_name,
                    ', '.join(found_wildcards),
                    ', '.join(found_escalations)
                ])

if __name__ == "__main__":
    list_roles()
