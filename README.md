# 🌩️ Cloud Updates Tracker

Stay ahead of the curve with the **Cloud Updates Tracker**—your go-to automation tool for tracking the latest announcements, features, and updates from major cloud providers. Designed for developers, engineers, and cloud enthusiasts, this project ensures you're always informed about what's new in the cloud ecosystem.

---

## 🚀 Features

- **Automated Updates**: Fetches daily updates from Azure, AWS, Google Cloud, Linode, and DigitalOcean.
- **Custom Filters**: Tracks Azure updates based on specific categories, including Kubernetes, Virtual Machines, and AI services.
- **Readable Markdown Output**: Saves updates in an easy-to-read `cloud-updates.md` file.
- **GitHub Actions Workflow**: Fully automated using GitHub Actions—set it up and forget it!

---

## 📂 How It Works

1. **Daily Automation**: A GitHub Actions workflow runs daily to fetch updates from cloud providers' RSS feeds.
2. **RSS Feeds**: Pulls updates from provider-specific feeds:
   - Azure (filtered by categories like AKS, Virtual Machines, AI services)
   - AWS What's New
   - Google Cloud Release Notes
   - Linode Blog
   - DigitalOcean Updates
3. **Markdown File**: The updates are saved in a structured `cloud-updates.md` file in the repository.

---

## 🎯 Why Use This?

- **Stay Updated**: Never miss a critical update or feature release from your favorite cloud providers.
- **Save Time**: Automate the process of checking multiple blogs and feeds.
- **Customizable**: Add more providers or fine-tune the filters for your specific needs.

---

## 🛠️ Getting Started

### Prerequisites
- A GitHub account
- Basic knowledge of Git and GitHub Actions

### Clone the Repository
```bash
git clone https://github.com/CloudCraftWithFranck/cloud-updates-tracker
cd cloud-updates-tracker
