import feedparser

# Cloud Provider RSS Feeds
feeds = {
    "Azure Updates": "https://azure.microsoft.com/en-us/updates?id=feed&filters=%5B%22Azure+Kubernetes+Service+%28AKS%29%22%2C%22Cloud+Services%22%2C%22Azure+VMware+Solution%22%2C%22Virtual+Machines%22%2C%22App+Service%22%2C%22Azure+Functions%22%2C%22Azure+Spot+Virtual+Machines%22%2C%22Virtual+Machine+Scale+Sets%22%2C%22Azure+Container+Instances%22%2C%22Azure+Compute+Fleet%22%2C%22Windows+Virtual+Machines%22%2C%22Azure+Spring+Apps%22%2C%22SQL+Server+on+Azure+Virtual+Machines%22%2C%22Linux+Virtual+Machines%22%2C%22Batch%22%2C%22Azure+CycleCloud%22%2C%22Azure+Dedicated+Host%22%2C%22Azure+VM+Image+Builder%22%2C%22Azure+Service+Fabric%22%2C%22Static+Web+Apps%22%2C%22Azure+Virtual+Desktop%22%2C%22Azure+Quantum%22%2C%22Azure+Modeling+and+Simulation+Workbench%22%2C%22Azure+Database+for+MySQL%22%2C%22Azure+Cache+for+Redis%22%2C%22Azure+Cosmos+DB%22%2C%22Azure+SQL+Database%22%2C%22Azure+Database+for+PostgreSQL%22%2C%22Azure+SQL+Managed+Instance%22%2C%22Azure+SQL%22%2C%22Azure+SQL+Edge%22%2C%22Azure+confidential+ledger%22%2C%22Azure+Database+for+MariaDB%22%2C%22Azure+Database+Migration+Service%22%2C%22Azure+Managed+Instance+for+Apache+Cassandra%22%2C%22Azure+AI+Studio%22%2C%22Azure+Machine+Learning%22%2C%22Azure+AI+Services%22%2C%22Azure+AI+Language%22%2C%22Azure+AI+Video+Indexer%22%2C%22Azure+AI+Personalizer%22%2C%22Azure+AI+Bot+Service%22%2C%22Azure+AI+Search%22%2C%22Azure+AI+Custom+Vision%22%2C%22QnA+Maker%22%2C%22Speaker+recognition%22%2C%22Azure+AI+Translator%22%2C%22Speech+translation%22%2C%22Health+Bot%22%2C%22Azure+AI+Content+Safety%22%2C%22Azure+OpenAI+Service%22%2C%22Speech+to+text%22%2C%22Text+to+speech%22%2C%22Language+Understanding+%28LUIS%29%22%2C%22Azure+Open+Datasets%22%2C%22Microsoft+Copilot+for+Security%22%2C%22AI+Anomaly+Detector%22%2C%22Data+Science+Virtual+Machines%22%2C%22Automation%22%2C%22Azure+Backup%22%2C%22Azure+Migrate%22%2C%22Microsoft+Copilot+for+Azure%22%2C%22Azure+Monitor%22%2C%22Azure+Site+Recovery%22%2C%22Network+Watcher%22%2C%22Azure+Automanage%22%2C%22Azure+Resource+Manager%22%2C%22Microsoft+Cost+Management%22%2C%22Traffic+Manager%22%2C%22Azure+Blueprints%22%2C%22Cloud+Shell%22%2C%22Microsoft+Azure+portal%22%2C%22Azure+Policy%22%2C%22Azure+Lighthouse%22%2C%22Azure+Advisor%22%2C%22Azure+Managed+Applications%22%2C%22Azure+mobile+app%22%2C%22Azure+Service+Health%22%2C%22Azure+Resource+Manager+templates%22%2C%22Azure+Managed+Grafana%22%2C%22Azure+Resource+Mover%22%2C%22Update+management+center%22%2C%22Azure+HDInsight+on+Azure+Kubernetes+Service%22%2C%22Azure+Stream+Analytics%22%2C%22Azure+Chaos+Studio%22%2C%22Azure+Data+Explorer%22%2C%22Microsoft+Fabric%22%2C%22Azure+Databricks%22%2C%22Azure+Synapse+Analytics%22%2C%22Azure+Data+Lake+Storage%22%2C%22Azure+Analysis+Services%22%2C%22Azure+Data+Factory%22%2C%22Data+Lake+Analytics%22%2C%22Azure+Data+Share%22%2C%22HDInsight%22%2C%22Event+Hubs%22%2C%22Power+BI+Embedded%22%2C%22Microsoft+Purview%22%2C%22Data+Catalog%22%2C%22Launched%22%5D",
    "AWS What's New": "https://aws.amazon.com/new/feed/",
    "Google Cloud Release Notes": "https://cloud.google.com/feeds/gcp-release-notes.xml",
    "Linode Blog": "https://www.linode.com/blog/feed/",
    "DigitalOcean Updates": "https://docs.digitalocean.com/release-notes/index.xml"
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
