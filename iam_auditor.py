import boto3
import csv

iam = boto3.client('iam')

## Escalations
escalation_actions = [
    "iam:CreateUser",
    "iam:PutUserPolicy",
    "iam:AddUserToGroup",
    "iam:PassRole",
    "iam:CreateAccessKey"
]
def calculate_risk_level(wildcards, escalations):
    score = 0
    if wildcards:
        score += 2
    if escalations:
        score += 2
    if any(a == "*" for a in wildcards):
        score += 3

    if score >= 4:
        return "High"
    elif score >= 2:
        return "Medium"
    else:
        return "Low"
def list_roles():
    with open("iam_audit_results.csv", mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["RoleName", "Wildcard", "EscalationRisks", "RiskScore", "AdmistratorAccess"])
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
            
            # Check for AdministratorAccess managed policy
            attached_policies = iam.list_attached_role_policies(RoleName=role_name)['AttachedPolicies']
            has_admin = any(p['PolicyName'] == 'AdministratorAccess' for p in attached_policies)
            
            if found_wildcards or found_escalations:
                risk_level = calculate_risk_level(found_wildcards, found_escalations)
                writer.writerow([
                    role_name,
                    ', '.join(found_wildcards),
                    ', '.join(found_escalations),
                    risk_level
                ])

if __name__ == "__main__":
    list_roles() 
#done
