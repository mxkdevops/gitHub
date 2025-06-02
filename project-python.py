import pandas as pd

# Define project data
projects = [
    # Projects 26–50
    ("AI Infrastructure Cost Forecaster", "Forecast AWS costs using past billing data", "Time-series AI (LSTM/Prophet)", "Python, AWS Cost Explorer, Streamlit"),
    ("Natural Language S3 Query Tool", "Query S3 using plain English", "Prompt to Boto3 filter", "Python, CLI, Web UI"),
    ("AI Log Translator", "Explain Linux or AWS logs in plain English", "NLP log summarizer", "OpenAI, Python"),
    ("Auto System Doc Generator", "Generate README/docs from infra code", "LLM summarization", "Python, Terraform, GitHub"),
    ("AI DevOps Troubleshooter", "Explain CI/CD or cloud deployment failures", "Log parsing + GPT suggestions", "Python, GitHub Actions, CloudWatch"),
    ("Smart Task Automator", "Generate cron + script from natural language", "NLP to shell", "Python, CLI"),
    ("Project Complexity Estimator", "Estimate time/cost for technical ideas", "LLM + project templates", "Web tool, Python"),
    ("Smart Bash Explainer", "Explain Bash line-by-line", "NLP shell breakdown", "Python, CLI"),
    ("Resume Skills Extractor + AI-Match", "Match resumes with job requirements", "NLP + semantic match", "Python, embeddings"),
    ("AI Cloud Threat Detector", "Predict security threats in AWS logs", "Anomaly detection", "Python, GuardDuty"),
    ("Kubernetes Deployment Reviewer", "Check K8s YAMLs for best practices", "YAML NLP checker", "Python, OpenAI"),
    ("AI Cloud Visual Builder", "Generate infra diagrams or YAML from prompt", "Prompt to YAML + diagram", "Python, Mermaid/Diagrams.net"),
    ("API Status Dashboard Generator", "Live API status page generator", "AI-generated descriptions + scripts", "Python, Web UI"),
    ("Multi-Cloud Region Recommender", "Suggest best cloud region", "LLM + logic", "Python, Dash"),
    ("AI Email Reply Assistant", "Write professional replies to client emails", "AI writer", "OpenAI, Web UI"),
    ("AI Naming Assistant for Infra", "Suggest names for cloud resources", "LLM naming conventions", "Python, Web UI"),
    ("Linux Log Summarizer", "Summarize daily system logs", "NLP summarization", "Python, cron"),
    ("AI Terminal Assistant", "Chat with terminal commands", "Prompt to shell", "Python, CLI"),
    ("Auto Compliance Checklist Generator", "Create security/compliance checklists", "NLP checklist builder", "Python, Web"),
    ("AI System Uptime Reporter", "Human-readable uptime summaries", "uptime + GPT", "Bash, Python"),
    ("Smart Git Commit Reviewer", "Rewrite/summarize commit messages", "NLP on Git commits", "Python, Git CLI"),
    ("Tech Blog Rewriter / SEO Improver", "Improve blog SEO and formatting", "Prompt-tuned editor", "Python, OpenAI"),
    ("Server Benchmarking Bot", "Run tests, suggest tuning", "stress-ng + GPT", "Python, Linux"),
    ("Cloud Dashboard Prompt Builder", "Generate metrics queries from natural text", "Prompt to CloudWatch/Grafana", "Python, CLI"),
    ("Shell History Analyzer", "Summarize shell usage and tips", "NLP + command patterns", "Python, AI"),

    # Projects 51–60 (Linux/Security + AI)
    ("Linux Security Event Dashboard", "Visualize login/sudo/auth logs", "Log summarizer", "Python, Streamlit, Chart.js"),
    ("AI Threat Pattern Summarizer", "Summarize and group log-based threats", "Log NLP grouping", "Python, OpenAI"),
    ("Real-Time SSH Attack Visualizer", "Map SSH attack IPs live", "GeoIP + attack classifying", "Python, Mapbox"),
    ("File Integrity Monitor", "Detect abnormal file changes", "AI file change classifier", "Python, inotify, Web UI"),
    ("Kernel Alert Summarizer", "Summarize dmesg/journalctl alerts", "Kernel NLP analysis", "Python, AI"),
    ("AI Cron Job Analyzer", "Explain cron jobs and detect risks", "AI code reviewer", "Python, CLI"),
    ("System Summary Visual Report", "Visual system health report", "System stats + AI summary", "Python, psutil"),
    ("Port/Service Monitor + AI", "Track & analyze open ports/services", "Trend AI + visualizer", "Python, Dash"),
    ("Firewall Rule Optimizer", "Audit and improve iptables/UFW", "Prompt-based suggestions", "Python, CLI"),
    ("Linux Incident Timeline Generator", "Generate human-readable incident timeline", "Log → event NLP", "Python, Mermaid")
]

# Create DataFrame
df = pd.DataFrame(projects, columns=["Project Name", "Goal", "AI Feature", "Tech Stack"])

# Display the top rows
df.head()
