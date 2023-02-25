export DEST_BUCKET_NAME=bigtable-streaming-bucket
export BUCKET_LOCATION=australia-southeast1
#export SOURCE_DATA_PATH=../../data
#export TARGET_DATA_PATH=data

gcloud storage buckets create gs://$DEST_BUCKET_NAME --location $BUCKET_LOCATION
#gsutil cp -r $SOURCE_DATA_PATH/* gs://$DEST_BUCKET_NAME/$TARGET_DATA_PATH