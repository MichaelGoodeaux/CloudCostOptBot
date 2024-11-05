# Contributing to Cloud Cost Optimization Bot

Thank you for your interest in contributing to the Cloud Cost Optimization Bot! We welcome contributions from the community to improve and enhance this project. Please read the guidelines below to ensure a smooth collaboration process.

## Branching Strategy

This project follows a feature-based branching model to keep development organized and manageable. Please follow these steps for creating and working with branches:

1. **Development Branch**:
- The `development` branch is the main branch where all changes are tested before being merged into `main`.
- Always branch from `development` when creating a new feature or bug fix.

2. **Feature and Bug Branches**:
- For new features, create a branch prefixed with `feature/`:
```bash
git checkout -b feature/your-feature-name
```
- For bug fixes, create a branch prefixed with `bug/`:
```bash
git checkout -b bug/your-bugfix-description
```

3. **Merge into Development**:
- Once your work is complete and tested, submit a pull request (PR) to merge your branch into `development` for further testing and review.

## Setting Up Your Development Environment

1. **Fork the Repository**: Create a fork of this repository to your own GitHub account.
2. **Clone your Fork**: Clone your forked repository to your local machine.
```bash
git clone git@github.com:MichaelGoodeaux/CloudCostOptBot.git
```
3. **Install Dependencies**:
    - Install project dependencies from `requirements.txt` and `requirements-dev.txt` in the `python` directory.
```bash
pip install -r python/requirements.txt
pip install -r python/requirements-dev.txt
```
4. **Set Up Environment Variables**: Refer to the main `README` to set up the required environment variables.

## Making a Contribution

1. Create a Branch
    - Make sure to branch from `development` and use the `feature/` or `bug/` prefix as appropriate.
2. Implement Your Changes
    - Write clear, maintainable code and ensure it aligns with the project’s style.
3. Write Tests
    - Add or update tests in the `tests` folder to cover new functionality or bug fixes.
    - Run tests locally to verify that all functionality is working as expected.
    ```bash
    pytest tests/
    ```
4. Commit Your Changes
    - Use descriptive and consistent commit messages (see guidelines below).
    - Commit often to document your progress.

## Commit Message Guidelines

We follow the Angular commit message format for consistency and readability. Please structure your commit messages as follows:

### Commit Message Format
Each commit message should include a **type**, an optional **scope**, and a **description**:

```php
Copy code
<type>(<scope>): <description>
```

### Commit Types
- feat: A new feature.
- fix: A bug fix.
- docs: Documentation only changes.
- style: Changes that do not affect the code’s meaning (e.g., white-space, formatting).
- refactor: Code changes that neither fix a bug nor add a feature.
- test: Adding missing tests or correcting existing ones.
- chore: Changes to the build process or auxiliary tools and libraries.

### Examples
- Feature: `feat(cost-analysis): add automated notifications for high-cost resources`
- Bug Fix: `fix(azure): correct memory leak in cost aggregation`
- Documentation: `docs(README): update setup instructions`
- Refactor: `refactor(gcp): improve cost data aggregation efficiency`
- Chore: `chore(deps): update dependency versions`

### Additional Tips
- Use the Present Tense: “Fix” not “Fixed” or “Fixes.”
- Be Descriptive but Concise: Keep messages clear and to the point.

## Code Review Process

All PRs into development will go through a code review process to ensure high-quality contributions.
- Automated Checks: The Bitbucket pipeline will automatically run tests and linting on each PR. Ensure your PR passes all checks before requesting a review.
- Address Feedback: Reviewers may leave comments or suggest changes. Address all feedback by pushing additional commits to your branch.
- Merge: Once the PR is approved and all checks pass, it can be merged into development.

Thank you for your contributions! Following these guidelines will help maintain a high-quality, collaborative project.