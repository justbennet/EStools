#!/usr/bin/env python3

from EStools import es_info
from EStools import get_syslog_index_names
from EStools import get_module_usage

# Define cluster names and labels
clusters = {'greatlakes': "Great Lakes",
            'lighthouse': "Lighthouse",
            'armis2' : "Armis" }

# Print ES server information
es_info()

# For each cluster get the index names and print the oldest and newest
for cluster in sorted(clusters.keys()):
    cl_name = clusters[cluster]
    cl = get_syslog_index_names(cluster)
    oldest = cl[0]
    newest = cl[-1]
    print(f"\nIndexes for {cl_name}")
    print(f"Oldest entry:  {oldest}")
    print(f"Newest entry:  {newest}")

# For one index, get the name of the first and last module loaded.
# Data retrieved looks like this.
#
# { '_index': 'logstash-hpc-lighthouse-sysloglogs-v3-2020.11.09',
#    '_type': 'doc',
#    '_id': 't91wqnUBE2yvuKBLG5Co',
#    '_score': None,
#    '_source': {
#        'path': '/sw/arcts/centos7/modulefiles/Core/gcc/8.2.0.lua',
#        'module': 'gcc/8.2.0',
#        'host': 'lh-login1.arc-ts.umich.edu'
#        },
#    'sort': [0]
# }

# Request the data, and obtain the first and last records and print
print(f"\nPrinting example information about a specific module: gcc/8.2.0")
print(f"    from the {newest} index")
module_records = get_module_usage(newest)
oldest = module_records[0]['_source']['module']
newest = module_records[-1]['_source']['module']
print(f"Oldest module load record:  {oldest}")
print(f"Newest module load record:  {newest}")

# Print the number of loads for ARCTS provided gcc/8.2.0
# Match on the 'path' entry to disambiguate in case a user had a module called
#     gcc/8.2.0
count = 0
for item in module_records:
    if item['_source']['path'].find('/sw/arcts/centos7/modulefiles/Core/gcc/8.2.0.lua'):
        count += 1
print(f"The module gcc/8.2.0 was loaded {count} times")


