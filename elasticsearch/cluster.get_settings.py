#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from pprint import pprint


def cluster_get_settings(es):
    """he Cluster Stats API allows to retrieve statistics from a cluster wide
    perspective. The API returns basic index metrics and information about
    the current nodes that form the cluster.
    """
    pprint(es.cluster.get_settings())


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    cluster_get_settings(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/cluster.py#L125