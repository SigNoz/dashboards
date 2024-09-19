# Contributing Guide for SigNoz Dashboards Repository

Thank you for your interest in contributing to the SigNoz Dashboards repository! This repository hosts SigNoz dashboard templates in JSON format for common services like MySQL, MongoDB, APM, JVM, and more. Your contributions help the community monitor and visualize their services more effectively.

This guide will help you understand how to contribute a new dashboard template to the repository. Please follow the instructions below to ensure consistency and quality across all contributions.

## Table of Contents

- [Getting Started](#getting-started)
- [Dashboard JSON File Naming Convention](#dashboard-json-file-naming-convention)
- [Creating the Dashboard JSON File](#creating-the-dashboard-json-file)
- [Writing the README File](#writing-the-readme-file)
  - [README Structure](#readme-structure)
  - [Example README](#example-readme)
- [Adding Screenshots](#adding-screenshots)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

---

## Getting Started

Before you begin, please make sure you have:

- A GitHub account.
- Familiarity with Git for version control.
- Basic understanding of SigNoz and how dashboard templates work.
- Installed any necessary tools for creating and exporting dashboards in JSON format.

## Dashboard JSON File Naming Convention

When adding a new dashboard JSON file, please follow the naming convention below:

```
name-of-dashboard-source-version.json
```

- **name-of-dashboard**: Use lowercase letters and hyphens to separate words.
- **source**: Indicate the data source, such as `otlp` or `prometheus`.
- **version**: Start with `v1` and increment for subsequent versions (`v2`, `v3`, etc.).

**Examples:**

- `mysql-otlp-v1.json`
- `mongodb-prometheus-v1.json`

## Setup SigNoz
If you don't have [SigNoz setup on your local](https://signoz.io/docs/install/docker/) then you get invited to test tenant from us.
1. Join SigNoz [Slack Community](https://signoz.io/slack)
2. Please ping `@vishal-signoz` or ask in the [`#contributing`](https://signoz-community.slack.com/archives/C01LWQ8KS7M) channel in our [Slack Community](https://signoz.io/slack) and we will invite you to test tenant.

## Creating the Dashboard JSON File

1. Create your dashboard in SigNoz.
2. Export the dashboard to a JSON file.
3. Ensure that the JSON file follows the naming convention.
4. Place the JSON file in an appropriate subdirectory if one exists.

## Writing the README File

Each dashboard should be accompanied by a README file that provides essential information for users. The README should be clear, concise, and formatted in Markdown.

### README Structure

Your README file should include the following sections:

1. **Title**

   - The title should include the name of the dashboard and the data source.
   - Example: `# MySQL Dashboard - OTLP`

2. **Metrics Ingestion**

   - Explain how to ingest metrics for the dashboard.
   - Provide configuration snippets (e.g., `otel-config.yaml`).
   - Include instructions for setting up receivers and pipelines.

3. **Variables**

   - List and describe any variables used in the dashboard.
   - Example:

     ```markdown
     ## Variables

     - `{{deployment_environment}}`: Deployment environment
     - `{{mysql_instance_endpoint}}`: MySQL instance endpoint
     ```

4. **Dashboard Panels**

   - Describe each section and panel in the dashboard.
   - Mention the metrics used for each panel.
   - Include screenshots stored in the `assets/` directory.

5. **Screenshots**

   - Add relevant screenshots to illustrate the dashboard sections.
   - Reference the images in the README using Markdown syntax.
   - Example:

     ```markdown
     ![Resources Screenshot 1](assets/resources_1.png)
     ```

### Example README

For an example of how your README should look, please refer to the [MySQL Dashboard README](https://github.com/SigNoz/dashboards/blob/main/mysql/readme.md) provided in this repository.

## Adding Screenshots

Screenshots enhance the readability of your README and help users understand the dashboard's appearance and functionality.

- Store all screenshots in the `assets/` directory.
- Name the images using the format `name-of-section.png`.
- Reference the images in your README using relative paths.

**Example:**

```markdown
![Resources Section](assets/resources.png)
```

## Submitting a Pull Request

Once you have prepared your dashboard JSON file, README, and screenshots, you're ready to submit a pull request.

1. **Fork the Repository**

   - Click the "Fork" button at the top right corner of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your-username/dashboards.git
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b add-my-dashboard-source-version
   ```

4. **Add Your Files**

   - Add your dashboard JSON file, README, and assets to the repository.

5. **Commit Your Changes**

   ```bash
   git add .
   git commit -m "Add [Name of Dashboard] dashboard - source, version"
   ```

6. **Push to Your Fork**

   ```bash
   git push origin add-my-dashboard-source-version
   ```

7. **Create a Pull Request**

   - Go to the original repository.
   - Click on "New Pull Request".
   - Select your fork and the branch you just pushed.
   - Provide a clear and descriptive title and description for your pull request.
   - Add the link of GitHub issue for requested dashboard in the PR description

8. **Address Review Comments**

   - Be responsive to any feedback or requested changes from maintainers.

## Code of Conduct

By participating in this project, you agree to abide by the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions will be licensed under the [Apache License 2.0](LICENSE).

---

Thank you for your contribution! Your effort helps improve the SigNoz community and makes monitoring more accessible for everyone.
