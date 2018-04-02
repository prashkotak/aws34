 import json
 import gzip
#
# import boto3
# client = boto3.client('s3')
# # resp = client.list_buckets()
# # for r in resp['Buckets']:
# #     print(r['Name'])
# response = client.list_objects_v2(Bucket='jobanjola')
#
# aaa = "554906049655_CloudTrail_us-east-1_20180306T0640Z_9yNIXKqYIVznl2sf.json.gz"
# with gzip.open(aaa, "rb") as f:
#     d = json.loads(f.read().decode("ascii"))
#
# print(d)


with gzip.open(file_path, "rb") as f:
    d = json.loads(f.read().decode("ascii"))
    for nik in d['Records']:
        for aa in nik['eventName']:
            print(aa)

