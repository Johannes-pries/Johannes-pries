import requests

USERNAME = "johannes-pries"
API_URL = f"https://leetcode-stats-api.herokuapp.com/{USERNAME}"

response = requests.get(API_URL)
data = response.json()

if response.status_code == 200:
    solved = data.get("totalSolved", 0)
    easy = data.get("easySolved", 0)
    medium = data.get("mediumSolved", 0)
    hard = data.get("hardSolved", 0)

    with open("README.md", "r") as file:
        readme = file.readlines()

    start_index = readme.index("<!-- LEETCODE-STATS-START -->\n")
    end_index = readme.index("<!-- LEETCODE-STATS-END -->\n")

    stats = f"""
<!-- LEETCODE-STATS-START -->
### 📊 LeetCode Statistiken

- **Gelöste Probleme**: {solved}
- **Einfach**: {easy}, **Mittel**: {medium}, **Schwer**: {hard}

[🔗 Mein LeetCode Profil](https://leetcode.com/{USERNAME}/)
<!-- LEETCODE-STATS-END -->
"""

    readme[start_index:end_index+1] = [stats]

    with open("README.md", "w") as file:
        file.writelines(readme)

    print("README erfolgreich aktualisiert!")
else:
    print("Fehler beim Abrufen der LeetCode-Daten")
