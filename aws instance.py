import boto3
import os

def Header(head):
    header = ''
    header = header + '='.center(70,'=')   + "\n"
    header = header +repr(head).center(70) + "\n"
    header = header + '='.center(70,'=')   + "\n"
    return  header

ec2 = boto3.client('ec2')
regs = ec2.describe_regions()

def get_region():
    regionlist = list();
    for regions in regs['Regions']:
        allreg = regions['RegionName']
        regionlist.append(allreg)
    return  regionlist

def get_blank_vol():
    if os.path.exists('d:\Report.txt'):
        os.remove('d:\Report.txt')
    f = open('d:\Report.txt', 'a')
    rr = ''
    state = 'available'
    regionlist = get_region()
    volumelist = list();
    for def_region in regionlist:
      ec2 = boto3.client('ec2', region_name=def_region)
      vols = ec2.describe_volumes()
      for vol_id in vols['Volumes']:
        if vol_id['State'] == state:
           rr = rr +'\n'+ str(repr(vol_id['VolumeId']).rjust(15)+repr(vol_id['Size']).rjust(4)+"GB       "+repr(vol_id['VolumeType']).ljust(15)+repr(vol_id['AvailabilityZone']).rjust(14))

    head = Header('List of volumes')
    title = repr('VolumeId').center(20) + "   " + repr('Size').center(10) + repr('Type').center(10) + "         " + repr('Av-Zone1').center(14) + "\n"
    f.write(head+title+rr)


def get_securitygroup():
    regionlist = get_region()
    for def_region in regionlist:
        ec2 = boto3.client('ec2', region_name=def_region)
        response = ec2.describe_security_groups()
        for get_sec in response['SecurityGroups']:
          descrip = get_sec['Description']
          for get_grp in get_sec['IpPermissions']:
           if get_grp['IpProtocol'] == '-1':
             for cidr in get_grp['IpRanges']:
                 if cidr['CidrIp'] == '0.0.0.0/0':
                    print(descrip)

# xx= get_region()
# print(xx)
#get_blank_vol()
print(get_blank_vol())
#print(get_securitygroup())
