import feedparser

# Cloud Provider RSS Feeds
feeds = {
    "Azure Updates": "https://azure.microsoft.com/en-us/updates/feed/",
    "AWS What's New": "https://aws.amazon.com/new/feed/",
    "Google Cloud Release Notes": "https://cloud.google.com/release-notes.atom",
    "Linode Blog": "https://www.linode.com/blog/feed/",
    "DigitalOcean Updates": "https://www.digitalocean.com/blog/rss.xml"
}

# Fetch updates from each RSS feed
def fetch_updates():
    updates = {}
    for provider, url in feeds.items():
        print(f"Fetching updates from {provider}...")
        feed = feedparser.parse(url)
        updates[provider] = [{"title": entry.title, "link": entry.link} for entry in feed.entries[:3]]  # Top 3 updates
    return updates

# Write updates to a Markdown file
def write_to_markdown(updates):
    with open("cloud-updates.md", "w") as file:
        file.write("# 🌩️ Latest Cloud Updates\n\n")
        for provider, entries in updates.items():
            file.write(f"## {provider}\n")
            for entry in entries:
                file.write(f"- [{entry['title']}]({entry['link']})\n")
            file.write("\n---\n\n")  # Adds a separator between providers
    print("Updates written to 'cloud-updates.md'")

if __name__ == "__main__":
    updates = fetch_updates()
    write_to_markdown(updates)
