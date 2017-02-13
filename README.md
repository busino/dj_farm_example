# dj_farm_example

Simple Farm Application in Django to be used to evaluate docker

## Bug ##

The volumes have to be on local and remote host!!!

## Deploy with exoscale ##

```
export EXOSCALE_API_KEY=XXX
export EXOSCALE_API_SECRET=XXX
export EXOSCALE_DISK_SIZE=10
export EXOSCALE_SECURITY_GROUP=farm
export EXOSCALE_AFFINITY_GROUP=farm
export EXOSCALE_INSTANCE_PROFILE=tiny
export EXOSCALE_AVAILABILITY_ZONE=ch-gva-2 # use GV-2 because elastic IP is not available in dk-2

docker-machine create --driver exoscale --exoscale-security-group farm  farm
docker-machine env farm
eval $(docker-machine env farm)
docker-compose up --build
```
