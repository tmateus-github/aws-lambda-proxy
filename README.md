# AWS lambda proxy
Simple endpoint using AWS API GW and AWS LAMBDA
## Deploying
In order to deploy, we will need to run the following commands:
* This command is going to prepare the package and upload into S3 bucket.
```bash
aws cloudformation package --template-file template.yaml --s3-bucket <BUCKET_NAME> --output-template-file packaged-template.yaml
```
* This command will deploy all the stack.
```bash
aws --region eu-west-1 cloudformation deploy --template-file packaged-template.yaml --stack-name <STACK_NAME> --capabilities CAPABILITY_IAM
```
