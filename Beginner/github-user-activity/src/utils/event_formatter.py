def handle_push(event):
    repo = event.get("repo", {}).get("name", "unknown repo")
    return f"Pushed to {repo}"


def handle_create(event):
    repo = event.get("repo", {}).get("name", "unknown repo")
    payload = event.get("payload", {})

    ref_type = payload.get("ref_type")
    ref = payload.get("ref")

    if ref and ref_type:
        return f"Created {ref_type} '{ref}' in {repo}"
    elif ref_type:
        return f"Created {ref_type} in {repo}"
    else:
        return f"Created something in {repo}"


def handle_delete(event):
    repo = event.get("repo", {}).get("name", "unknown repo")
    payload = event.get("payload", {})

    ref_type = payload.get("ref_type", "something")
    ref = payload.get("ref", "")

    return f"Deleted {ref_type} '{ref}' from {repo}"


def handle_watch(event):
    repo = event.get("repo", {}).get("name", "unknown repo")
    return f"Starred {repo}"


def handle_fork(event):
    repo = event.get("repo", {}).get("name", "unknown repo")
    return f"Forked {repo}"


def handle_issues(event):
    repo = event.get("repo", {}).get("name", "unknown repo")
    payload = event.get("payload", {})

    action = payload.get("action", "updated")
    return f"{action.capitalize()} an issue in {repo}"


def handle_issue_comment(event):
    repo = event.get("repo", {}).get("name", "unknown repo")
    return f"Commented on an issue in {repo}"


def handle_pull_request(event):
    repo = event.get("repo", {}).get("name", "unknown repo")
    payload = event.get("payload", {})

    action = payload.get("action", "updated")
    return f"{action.capitalize()} a pull request in {repo}"


# 🔑 Handler registry
handlers = {
    "PushEvent": handle_push,
    "CreateEvent": handle_create,
    "DeleteEvent": handle_delete,
    "WatchEvent": handle_watch,
    "ForkEvent": handle_fork,
    "IssuesEvent": handle_issues,
    "IssueCommentEvent": handle_issue_comment,
    "PullRequestEvent": handle_pull_request,
}


# 🔁 Public function main file will call
def format_event(event):
    event_type = event.get("type")
    repo = event.get("repo", {}).get("name", "unknown repo")

    handler = handlers.get(event_type)

    if handler:
        return handler(event)
    else:
        return f"{event_type} in {repo}"