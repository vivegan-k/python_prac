from re import A


remote_endpoint ="http://10.0.208.159:80"
remote_access_key ="abc"
remote_secret_key ="abc"
a =    f"radosgw-admin zonegroup placement modify --rgw-zonegroup default\
         --placement-id default-placement --storage-class CLOUDTIER\
         --tier-type=cloud-s3\
         --tier-config=endpoint={remote_endpoint},"+\
         f"access_key={remote_access_key},secret={remote_secret_key},"+\
         f"target_path='test_bucket',"+\
         f"multipart_sync_threshold=44432,multipart_min_part_size=44432,"+\
         f"retain_head_object=true,region=us-east-1"
print(a)