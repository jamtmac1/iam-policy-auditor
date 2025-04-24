import boto3

iam = boto3.client('iam')
def list_roles():
    response = iam.list_roles()
    for role in response['Roles']:
        print(f"Role: {role['RoleName']}")

if __name__ == "__main__":
    list_roles()