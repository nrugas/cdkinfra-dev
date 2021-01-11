#!/usr/bin/env python3

from aws_cdk import core

from cdkinfra_dev.cdkinfra_dev_stack import CdkinfraDevStack


app = core.App()
CdkinfraDevStack(app, "cdkinfra-dev", env={'region': 'us-west-2'})

app.synth()
