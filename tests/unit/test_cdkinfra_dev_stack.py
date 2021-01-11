import json
import pytest

from aws_cdk import core
from cdkinfra-dev.cdkinfra_dev_stack import CdkinfraDevStack


def get_template():
    app = core.App()
    CdkinfraDevStack(app, "cdkinfra-dev")
    return json.dumps(app.synth().get_stack("cdkinfra-dev").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
