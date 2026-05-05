# GitHub User Activity CLI

A command-line application that fetches and displays a GitHub user's
recent activity in a clean, human-readable format. This project
demonstrates API consumption, data transformation, and CLI-based output
formatting.

🔗 Project Source: https://roadmap.sh/projects/github-user-activity

🔗 Repository: https://github.com/Mika0x/github-user-activity

---

## 📌 Overview

GitHub User Activity CLI is a lightweight tool that retrieves recent
public activity for any GitHub user using the GitHub API. Instead of
displaying raw JSON data, it summarizes activity into readable sentences
and optionally aggregates repeated events for better clarity.

---

## 🚀 Features

- Fetch recent GitHub activity using the GitHub API
- Display activity in a human-readable format
- Aggregate repeated events (e.g., multiple pushes to the same repo)
- Handle multiple event types:
  - Push events
  - Create/Delete events
  - Issues and Pull Requests
  - Stars (Watch events)
  - Forks
- Graceful handling of unknown event types
- Error handling for invalid users and network issues

---

## 🛠️ Tech Stack

- Python
- GitHub API
- requests library

---

## 📂 Project Structure

```bash
github-user-activity/
│── github-activity.py        # Entry point
│── utils/
│   └── event_formatter.py   # Event formatting logic
│── README.md
```

---

## ⚙️ Installation

1.  Clone the repository:

```bash
git clone https://github.com/yourusername/github-user-activity.git
cd github-user-activity
```

2.  Install dependencies:

```bash
pip install requests
```

3.  Ensure Python is installed:

```bash
python3 --version
```

---

## ▶️ Usage

Run the script with a GitHub username:

```bash
python3 github-activity.py <github-username>
```

### Example:

```bash
python3 github-activity.py Mika0x
```

---

## 📖 Example Output

```bash
----------------------------------------
GitHub Activity Summary for Mika0x
----------------------------------------
• Pushed to Mika0x/backend-projects — 5 times
• Created branch 'main' in Mika0x/backend-projects — 1 time
• Pushed to Mika0x/task-tracker-cli — 12 times
```

---

## 🧠 How It Works

1.  The CLI accepts a GitHub username as input
2.  Sends a request to: `https://api.github.com/users/<username>/events`
3.  Parses the JSON response
4.  Groups events by type and repository
5.  Converts events into readable sentences using a formatter module
6.  Outputs a summarized view

---

## 🧩 Supported Event Types

- PushEvent → Pushed to repository
- CreateEvent → Created branch or repository
- DeleteEvent → Deleted branch or tag
- IssuesEvent → Opened or closed an issue
- PullRequestEvent → Opened or closed a pull request
- WatchEvent → Starred repository
- ForkEvent → Forked repository

---

## 📝 Notes

- The GitHub API returns up to 30 recent events by default
- Some event types contain limited data depending on the endpoint
- Commit counts are not always available from the events endpoint
- Unknown event types are handled gracefully with fallback output

---

## 🔮 Future Improvements

- Add `--raw` and `--summary` modes
- Filter events by type (e.g., only pushes)
- Add timestamps to output
- Improve CLI formatting (colors or tables)
- Support pagination for more results

---

## 📄 License

This project is open-source and available under the MIT License.
