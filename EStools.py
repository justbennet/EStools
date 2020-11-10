#!/usr/bin/env python3

from elasticsearch.connection import create_ssl_context
from elasticsearch import Elasticsearch, helpers, exceptions
import ssl
import requests
import pprint

requests.packages.urllib3

cert = '/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem'
ssl_context = create_ssl_context(cafile=cert)
ssl_context.check_hostname = True

client = Elasticsearch(['es.arc-ts.umich.edu'], scheme='https',
                       port='443', ssl_context=ssl_context)

def es_info():

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(client.info())


def get_syslog_index_names(clustername = 'greatlakes'):


    return(sorted(client.indices.get_alias(
        'logstash-hpc-' + clustername + '-sysloglogs*')))


def get_module_usage(index):

# Define the query to be used

    queryParam = {
        "_source": [ "host", "module", "path" ],
        "query":
            { "bool": { "must":
                    [
                      {"match": {"program": "ModuleUsageTracking"}},
                      # {"match": {"path": "matlab"}}
                    ]
                }
            }
        }

# from EStools import get_module_usage
# get_module_usage("logstash-hpc-greatlakes-sysloglogs-v3-2020.11.01")

    # call the helpers library's scan() method to scroll
    resp = helpers.scan(
        client,
        # index = "logstash-hpc-greatlakes-sysloglogs-v3-2020.09.22",
        index = index,
        # scroll is in units of time 3m is 3 microseconds, 3s is 3 seconds.
        # See docs.
        scroll = '3m',
        # I think (?) this is the number of records per scroll buffer
        # size = 1000,
        query = queryParam
    )

    total = 0

    return(list(resp))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cluster", help="Cluster name",
                        choices=["greatlakes", "lighthouse", "armis2"],
                        default="greatlakes")
    args = parser.parse_args()

    clustername = args.cluster

    indexes = get_syslog_index_names(clustername)
    oldest = indexes[0]
    newest = indexes[-1]
    print(f"Oldest entry:  {oldest}")
    print(f"Newest entry:  {newest}")
