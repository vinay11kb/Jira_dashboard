import csv
import config
from jira_client import connect_to_jira, fetch_issues

def write_to_csv(issues, filename='jira_issues.csv'):
    fieldnames = ['Issue Key', 'Summary', 'Status', 'Assignee', 'Reporter', 'Created', 'Updated']
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for issue in issues:
                writer.writerow({
                    'Issue Key': issue.key,
                    'Summary': issue.fields.summary,
                    'Status': issue.fields.status.name,
                    'Assignee': issue.fields.assignee.displayName if issue.fields.assignee else 'Unassigned',
                    'Reporter': issue.fields.reporter.displayName,
                    'Created': issue.fields.created,
                    'Updated': issue.fields.updated
                })
        print(f"Data extraction complete. Check '{filename}' for results.")
    except Exception as e:
        print(f"Failed to write CSV file: {e}")

def main():
    jira = connect_to_jira()
    jql_query = f'project = {config.PROJECT_KEY} ORDER BY created DESC'
    issues = fetch_issues(jira, jql_query)
    write_to_csv(issues)

if __name__ == '__main__':
    main()
