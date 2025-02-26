import sys
import requests
import re

# Sicherstellen, dass UTF-8 verwendet wird
sys.stdout.reconfigure(encoding="utf-8")

USERNAME = "johannes-pries"
API_URL = f"https://leetcode-stats-api.herokuapp.com/{USERNAME}"

response = requests.get(API_URL)
data = response.json()

leetcode_content = f"""
<!-- LEETCODE-STATS-START -->
## 🚀 My LeetCode progress 🚀

- **Total Solved:** {data['totalSolved']} / {data['totalQuestions']}
- **Easy:** {data['easySolved']} / {data['totalEasy']}
- **Medium:** {data['mediumSolved']} / {data['totalMedium']}
- **Hard:** {data['hardSolved']} / {data['totalHard']}
- **Ranking:** {data['ranking']}

<!-- LEETCODE-STATS-END -->
"""

# 🔹 README einlesen und Marker ersetzen
with open("README.md", "r", encoding="utf-8") as file:
    readme_content = file.read()

# Falls die Marker noch nicht existieren, einfach am Ende hinzufügen
if "<!-- LEETCODE-STATS-START -->" not in readme_content:
    readme_content += "\n" + leetcode_content
else:
    readme_content = re.sub(
        r"<!-- LEETCODE-STATS-START -->(.*?)<!-- LEETCODE-STATS-END -->",
        leetcode_content,
        readme_content,
        flags=re.DOTALL
    )

# 🔹 README speichern
with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme_content)

print("✅ README.md erfolgreich aktualisiert!")
