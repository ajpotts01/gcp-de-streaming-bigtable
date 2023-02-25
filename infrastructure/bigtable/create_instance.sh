export INSTANCE_ID=bigtable-sandiego
export DISPLAY_NAME="San Diego Traffic Sensors"
export STORAGE_TYPE=SSD
export ID=sandiego-traffic-sensors-c1
export ZONE=australia-southeast1-a
export NUM_NODES=1

gcloud bigtable instances create ${INSTANCE_ID} \
--display-name="${DISPLAY_NAME}" \
--cluster-storage-type=${STORAGE_TYPE} \
--cluster-config=id=${ID},zone=${ZONE},nodes=${NUM_NODES}