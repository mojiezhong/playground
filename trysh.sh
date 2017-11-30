#!/usr/bin/env bash

S3BUILD="s3://ou-build-artifact-east/artifacts/webapp/01635cf89c00885936bdc2f98a68274fb270e1e0/dist"


if [[ $(aws s3 ls ${S3BUILD}) ]]
then
   echo  "find the file tht is correct"
else
   echo "not found"
fi

S3BUILD="s3://ou-build-artifact-east/artifacts/webapp/01635cf89c00885936bdc2f98a68274fb270e1esss0/dist"

if [[ $(aws s3 ls ${S3BUILD}) ]]
then

   echo  "find the file"
else
   echo "not existed that is correct"

fi


echo "gogogogogo"