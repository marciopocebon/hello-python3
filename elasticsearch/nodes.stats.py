#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from pprint import pprint


def nodes_stats(es):
    """The cluster nodes stats API allows to retrieve one or more (or all) of
    the cluster nodes statistics.
    """
    pprint(es.nodes.stats())


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    nodes_stats(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/nodes.py#L25