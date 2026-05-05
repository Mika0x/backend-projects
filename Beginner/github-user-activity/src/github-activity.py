import warnings

warnings.simplefilter("ignore")

import sys
import requests
from utils.event_formatter import format_event

LIMITER = 30  # limit for readability

def main():
    if len(sys.argv) != 2:
        print("Usage: python github-activity.py <github-username>")
        return

    username = sys.argv[1]
    print(f"\n{'-' * 40}\nGitHub Activity Summary for {username}\n{'-' * 40}")

    url = f"https://api.github.com/users/{username}/events"

    try:
        response = requests.get(url)
        response.raise_for_status()
        events = response.json()

        if not events:
            print("No recent activity found.")
            return

        # 🔹 Step 1: Count events by (type, repo)
        event_counts = {}

        for event in events[:LIMITER]:
            event_type = event.get("type")
            repo = event.get("repo", {}).get("name", "unknown repo")

            key = (event_type, repo)

            event_counts[key] = event_counts.get(key, 0) + 1

        # 🔹 Step 2: Print aggregated results
        for (event_type, repo), count in event_counts.items():

            # reuse formatter for consistency
            formatted = format_event({
                "type": event_type,
                "repo": {"name": repo},
                "payload": {}
            })

            times = "time" if count == 1 else "times"
            print(f"• {formatted} ({count} {times})")

    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print(f"User '{username}' not found.")
        else:
            print(f"HTTP error occurred: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error fetching GitHub activity: {e}")


if __name__ == "__main__":
    main()