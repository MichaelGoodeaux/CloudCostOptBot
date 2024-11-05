# Cloud Cost Optimization Bot

[![Apache License](https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square)](https://www.apache.org/licenses/LICENSE-2.0)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)

This project is a Cloud Cost Optimization Bot designed to monitor cloud costs and alert teams when thresholds are exceeded. The bot is capable of working with AWS, Azure, and GCP in a modular setup, allowing end users to choose the cloud provider(s) they want to deploy to. The project supports cost aggregation, filtering high costs, and configuring alerts through cloud-specific deployments.


## Authors

- [@MichaelGoodeaux](https://github.com/MichaelGoodeaux)


## Features

- Cost Aggregation: Aggregates costs across services within each cloud provider.
- Alerting: Alerts teams if costs exceed specified thresholds.
- Multi-Cloud Support: Modular design supports AWS, Azure, and GCP.
- Automation: Uses IaC and containerization for streamlined deployments.


## Folder Structure

```
.
├── bin/                          # Helper scripts
│   ├── build                     # Build script for Docker images
│   └── bootstrap.sh              # Initializes cloud resources
├── infrastructure/               # IaC files for each cloud provider
│   ├── aws/                      # AWS setup (CDK)
│   ├── azure/                    # Azure setup (Bicep)
│   └── gcp/                      # GCP setup (Deployment Manager)
├── python/                       # Main application code and dependencies
│   ├── core/                     # Core processing functions
│   ├── providers/                # Cloud provider-specific implementations
│   ├── config/                   # Configuration files
│   ├── requirements.txt          # Production dependencies
│   └── requirements-dev.txt      # Development dependencies
├── tests/                        # Unit tests
│   ├── core/                     # Tests for core functions
│   ├── providers/                # Tests for each cloud provider
│   └── config/                   # Tests for config settings
└── Dockerfile                    # Production Dockerfile
└── Dockerfile.dev                # Development Dockerfile
└── bitbucket-pipelines.yml       # CI/CD pipeline configuration
```
## Environment Variables

The following environment variables are required to run the Cost Optimization Bot. These variables should be set based on your environment (e.g., in Bitbucket as repository variables or in an .env file for local testing).

### General Variables
- `COST_THRESHOLD`: The cost threshold for filtering high-cost resources. Resources with costs above this value will trigger alerts.
- `SLACK_WEBHOOK_URL`: The webhook URL for sending notifications to Slack. This is required if you want alerts sent to a Slack channel.

### AWS Environment Variables
- `ENABLE_AWS`: Set to true to enable AWS processing; omit or set to false if not using AWS.
- `AWS_REGION`: The AWS region where resources are managed (e.g., us-east-1).
- `AWS_ACCOUNT_ID`: The AWS account ID for your environment.
- `AWS_BUCKET_NAME`: The name of the S3 bucket for storing Lambda code or other artifacts.

### Azure Environment Variables
- `ENABLE_AZURE`: Set to true to enable Azure processing; omit or set to false if not using Azure.
- `AZURE_REGION`: The Azure region for deployment (e.g., eastus).
- `AZURE_RESOURCE_GROUP`: The name of the Azure resource group where resources will be deployed.
- `AZURE_STORAGE_ACCOUNT_NAME`: The name of the Azure storage account used for storing function code and other resources.
- `AZURE_FUNCTION_APP_NAME`: The name of the Azure Function App for deploying serverless functions.
- `AZURE_CLIENT_ID`: Azure Service Principal client ID for authentication.
- `AZURE_CLIENT_SECRET`: Azure Service Principal client secret for authentication.
- `AZURE_TENANT_ID`: Azure Active Directory tenant ID for authentication.
- `AZURE_REGISTRY_NAME`: The Azure Container Registry (ACR) name where Docker images will be stored.

### GCP Environment Variables
- `ENABLE_GCP`: Set to true to enable GCP processing; omit or set to false if not using GCP.
- `GCP_REGION`: The GCP region for resource deployment (e.g., us-central1).
- `GCP_BUCKET_NAME`: The name of the Google Cloud Storage bucket for storing function code and artifacts.
- `GCP_FUNCTION_NAME`: The name of the Google Cloud Function for deploying serverless functions.
- `GCP_PROJECT_ID`: The GCP project ID where resources are managed.
- `GOOGLE_APPLICATION_CREDENTIALS_JSON`: Base64-encoded JSON credentials for a GCP service account with appropriate permissions. This is required for authentication.

## Run Locally

### Requirements

- **Python 3.9+**
- **Docker**
- **AWS CLI, Azure CLI, Google Cloud SDK** (used for deployment and resource setup)

To install dependencies:
```bash
pip install -r python/requirements.txt  # Production dependencies
pip install -r python/requirements-dev.txt  # Development dependencies
```

### Setup

1. **Clone the Repository**

```bash
git clone git@github.com:MichaelGoodeaux/CloudCostOptBot.git
cd CloudCostOptBot
```

2. **Set Environment Variables**:
 
Define environment variables for each provider in your environment or as repository variables in your code repository. This project requires:

- **AWS**: AWS_REGION, AWS_ACCOUNT_ID, AWS_BUCKET_NAME
- **Azure**: AZURE_REGION, AZURE_RESOURCE_GROUP, AZURE_STORAGE_ACCOUNT_NAME, AZURE_FUNCTION_APP_NAME
- **GCP**: GCP_BUCKET_NAME, GCP_REGION, GCP_FUNCTION_NAME

3. **Run Bootstrap Script**:  This script initializes required resources for each cloud provider (e.g., storage buckets).

```bash
chmod +x ./bin/bootstrap.sh
./bin/bootstrap.sh
```

## Usage/Examples

**Core Functions**

The core functions in python/core/ perform cost aggregation and filtering:
- `aggregate_costs(data)`: Aggregates costs by service.
- `filter_high_costs(data, threshold)`: Filters costs that exceed a defined threshold.

### Running the Cost Optimization Bot

To run the bot, use `main.py` as the entry point

```bash
python python/main.py
```

## Running Tests

To run tests using `pytest`, ensure you have the `tests` folder and `pytest.ini` configured.

```bash
pytest tests/
```

Alternatively, you can run tests within Docker using the `./bin/build` script:

1. Build the development container with ./bin/build:
```bash
chmod +x ./bin/build
./bin/build -t dev
```

2. Run tests in the development container:
```bash
docker run --rm your_app_dev pytest tests/
```

## Docker

The project supports Docker for both development and production environments, managed through the `./bin/build` script. This script ensures consistent builds across environments by specifying the appropriate Dockerfile and dependencies.

### Docker for Development

1. **Build the Development Container:**
```bash
chmod +x ./bin/build
./bin/build -t dev
```

2. **Run Tests and Linting**: After building, you can run tests and linting directly within the container:
```bash
docker run --rm your_app_dev pytest tests/  # Run tests
docker run --rm your_app_dev flake8 python/ tests/  # Run linting
```
This approach ensures that all necessary dependencies for development are included in the container.

### Docker for Production

The production build is optimized for deployment with only essential dependencies. Use `./bin/build` with the prod target to build the production image.

1. Build the Production Container:
```bash
./bin/build -t prod
```

2. Run the Production Container:
```bash
docker run --rm your_app_prod
```

## Deployment

### AWS Deployment

To deploy to AWS, ensure you’re logged into AWS CLI and run:
```bash
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
docker tag your_app_prod $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/your_app_prod:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/your_app_prod:latest
```

### Azure Deployment

To deploy to Azure, login to Azure CLI and push the image to Azure Container Registry (ACR):
```bash
az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
az acr login --name $AZURE_REGISTRY_NAME
docker tag your_app_prod $AZURE_REGISTRY_NAME.azurecr.io/your_app_prod:latest
docker push $AZURE_REGISTRY_NAME.azurecr.io/your_app_prod:latest
```

### GCP Deployment

For GCP deployment, authenticate and push the image to Google Container Registry (GCR):
```bash
echo $GOOGLE_APPLICATION_CREDENTIALS_JSON | gcloud auth activate-service-account --key-file=-
gcloud auth configure-docker
docker tag your_app_prod gcr.io/$GCP_PROJECT_ID/your_app_prod:latest
docker push gcr.io/$GCP_PROJECT_ID/your_app_prod:latest
```

## CI/CD Configuration

An example .yaml pipeline file has been included. The code is commented out, so it will not run as-is. You are free to uncomment out what you need or make it your own. 

The example pipeline (example-pipeline.yml) is set up with:

- **Install Dependencies**: Installs requirements.
- **Bootstrap Project**: Initializes resources using bootstrap.sh.
- **Build and Test**: Builds and tests the app in Docker.
- **Lint and Quality Check**: Runs flake8.
- **Deployment Steps** for AWS, Azure, and GCP.

## License

This project is licensed with [apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contributing

Contributions are always welcome!

See [CONTRIBUTING.md](CONTRIBUTING.md) for ways to get started.

## Code of Conduct

We are committed to fostering a welcoming and inclusive environment. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand our expectations for respectful participation.

By contributing to this project, you agree to abide by its terms.