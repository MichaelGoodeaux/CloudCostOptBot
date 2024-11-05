# app.py - Entry point for AWS CDK app

from aws_cdk import core
from aws.aws_stack import CostOptimizationAwsStack

app = core.App()
CostOptimizationAwsStack(app, "CostOptimizationAwsStack")
app.synth()
