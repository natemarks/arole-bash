#!/usr/bin/env bash
aws cloudformation delete-stack --stack-name "test-arole-bash"

echo "Waiting for delete-stack to finish"
aws cloudformation wait stack-delete-complete --stack-name "test-arole-bash"

echo "Stack deleted: test-arole-bash"