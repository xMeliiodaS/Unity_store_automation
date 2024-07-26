class Utils:
    @staticmethod
    def create_jira_issue(jira_handler, test_id, exception, project_key="AT", issue_type="Bug"):
        """
        Create a Jira issue for a failed test.

        :param jira_handler: An instance of JiraHandler.
        :param test_id: The ID of the test that failed.
        :param exception: The exception that was raised.
        :param project_key: The Jira project key. Defaults to "AT".
        :param issue_type: The type of Jira issue. Defaults to "Bug".
        """
        issue_summary = f"Assertion failed in test: {test_id}"
        issue_description = f"Test case {test_id} failed with exception: {str(exception)}"
        jira_handler.create_issue(
            project_key=project_key,
            summary=issue_summary,
            description=issue_description,
            issue_type=issue_type
        )
