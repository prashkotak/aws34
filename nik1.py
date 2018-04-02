import boto3

client = boto3.client('ce')
response = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2018-02-01',
        'End': '2018-02-28'
    },
    Granularity='DAILY',
    #Granularity='MONTHLY',
    Filter={
        'Dimensions': {
            'Key': 'INSTANCE_TYPE',
            'Values': ["t2.medium"]}},
    Metrics=[
        'BlendedCost',
    ],

)

print(response)

# response = client.get_dimension_values(
#     SearchString='string',
#     TimePeriod={
#         'Start': '2018-03-01',
#         'End': '2018-03-16'
#     },
#     Dimension='AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY',
#     Context='COST_AND_USAGE'|'RESERVATIONS',
#     NextPageToken='string'
# )
