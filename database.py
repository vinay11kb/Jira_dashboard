# db_handler.py

import sqlite3

class DatabaseHandler:
    def __init__(self, db_name='jira_issues.db'):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS issues (
                id TEXT PRIMARY KEY,
                summary TEXT,
                status TEXT,
                assignee TEXT,
                reporter TEXT,
                created TEXT,
                updated TEXT
            )
        ''')

        conn.commit()
        conn.close()

    def insert_issues(self, issues):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        for issue in issues:
            cursor.execute('''
                INSERT OR REPLACE INTO issues (id, summary, status, assignee, reporter, created, updated)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                issue.key,
                issue.fields.summary,
                issue.fields.status.name,
                issue.fields.assignee.displayName if issue.fields.assignee else 'Unassigned',
                issue.fields.reporter.displayName,
                issue.fields.created,
                issue.fields.updated
            ))

        conn.commit()
        conn.close()
