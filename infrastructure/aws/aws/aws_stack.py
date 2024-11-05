# aws_stack.py - Main AWS CDK stack

import os
import shutil
from aws_cdk import (
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_events as events,
    aws_events_targets as targets,
    core
)

class CostOptimizationAwsStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the Lambda function with bundling
        cost_optimization_lambda = _lambda.Function(
            self, "CostOptimizationLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda.index.handler",
            code=_lambda.Code.from_asset(
                path="infrastructure/aws/lambda",
                bundling={
                    "image": _lambda.Runtime.PYTHON_3_8.bundling_docker_image,
                    "command": [
                        "bash", "-c",
                        # Copy both lambda and python directories into /asset-output
                        "cp -r /asset-input/. /asset-output/ && cp -r /asset-input/../../../python /asset-output/python"
                    ],
                }
            )
        )

        # Grant necessary permissions
        cost_optimization_lambda.add_to_role_policy(
            iam.PolicyStatement(
                actions=["ce:GetCostAndUsage", "s3:*", "ec2:DescribeInstances"],
                resources=["*"]
            )
        )

        # Schedule rule to trigger Lambda daily
        rule = events.Rule(
            self, "DailyCostOptimizationRule",
            schedule=events.Schedule.rate(core.Duration.days(1))
        )
        rule.add_target(targets.LambdaFunction(cost_optimization_lambda))
