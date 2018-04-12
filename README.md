# AWS Sam python project sample
This is a sample project of how to manage development, testing, packaging and deployment for python serverless.


## Bundle dependencies 
You need to bundle 3rd party modules when you add new dependencies.

```
make bundle_deps
```

## Run function locally

```
# Append src files to the packaged zip
make bundle
sam local generate-event api | sam local invoke "SearchFunction"
```

or 

```
make bundle && sam local generate-event api | sam local invoke "SearchFunction"
```

## Deploy to AWS

```
# Create s3 bucket if you haven't created
# e.g. aws s3 mb s3://aws-sam-python-sample
make package deploy
```

## Make command reference

|Command|Description|
|---|---|
|`make bundle_deps`|Run docker and bundle 3rd party packages into `bundle.zip`|
|`make bundle`|Append src files to `bundle.zip`|
|`make bundle_all`|`make bundle_deps bundle`|
|`make package`|Upload `bundle.zip` to S3|
|`make deploy`|Update cloudfomation to update lambda functions and API Gateway|
|`make release`|`make bundle_all package deploy`. This should be used for CI|
