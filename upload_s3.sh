export OUTPUTDIR=/Users/susrivas/code/blog/output
export S3_BUCKET=www.ssushant.in
s3cmd sync $OUTPUTDIR/ s3://$S3_BUCKET --acl-public --delete-removed --guess-mime-type
