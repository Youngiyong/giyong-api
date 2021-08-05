#!/bin/sh

aws deploy create-deployment-group \
--region ap-northeast-2 \
--application-name giyong-api-dev \
--deployment-group-name lastorder-api-dev-deploy-group \
--ec2-tag-filters Key=Name,Type=KEY_AND_VALUE,Value=dev-api \
--service-role-arn arn:aws:iam::299665028667:role/giyongDeployer
