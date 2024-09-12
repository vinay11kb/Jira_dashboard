# main.py

import logging
from jira_client import connect_to_jira, fetch_issues
from database import DatabaseHandler
import config

# Set up logging
logging.basicConfig(level=logging.INFO)


def main():
    try:


        # JQL query to fetch Jira issues
        jql_query = f'project = {config.PROJECT_KEY} ORDER BY created DESC'
        issues = fetch_issues(jql_query)

        # Initialize Database handler
        db_handler = DatabaseHandler()

        # Save Jira issues to the database
        db_handler.insert_issues(issues)

        logging.info("Data extraction and saving to the database complete.")

    except Exception as e:
        logging.error(f"Error occurred: {e}")


if __name__ == '__main__':
    main()
