#from lambda.myLambda import handler
from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)

from hitcounter import HitCounter


class CdkinfraDevStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Lambda resource
        my_lambda = _lambda.Function(
            self, 'myLambdaHandler', 
            runtime=_lambda.Runtime.PYTHON_3_8,
            code = _lambda.Code.asset('lambda'),
            handler = 'myLambda.handler'
            )

        # hitcounter
        myLambda_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda,
        )
        
        #API GW resource
        apigw.LambdaRestApi(
            self, 'Endpoint', 
            handler = myLambda_with_counter.handler,
        )