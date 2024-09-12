from jira import JIRA
import logging

import config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_to_jira():
    try:
        options = {'server': config.JIRA_SERVER}
        jira = JIRA(options, basic_auth=(config.JIRA_USERNAME, config.JIRA_API_TOKEN))
        logger.info("Connected to Jira successfully.")
        return jira
    except Exception as e:
        logger.error(f"Failed to connect to Jira: {e}")
        raise

def fetch_issues(jira, jql_query, start_at=0, max_results=50):
    issues = []
    while True:
        try:
            batch = jira.search_issues(jql_query, startAt=start_at, maxResults=max_results)
            if not batch:
                break
            issues.extend(batch)
            start_at += max_results
        except Exception as e:
            logger.error(f"Error fetching issues: {e}")
            break
    return issues
