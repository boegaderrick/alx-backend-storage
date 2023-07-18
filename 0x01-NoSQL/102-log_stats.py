#!/usr/bin/env python3
"""This script extracts details regarding http requests from a database"""
from pymongo import MongoClient

if __name__ == '__main__':
    collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx

    print(collection.estimated_document_count(), 'logs')

    print('Methods:')
    print('\tmethod GET:', collection.count_documents({"method": "GET"}))
    print('\tmethod POST:', collection.count_documents({"method": "POST"}))
    print('\tmethod PUT:', collection.count_documents({"method": "PUT"}))
    print('\tmethod PATCH:', collection.count_documents({"method": "PATCH"}))
    print('\tmethod DELETE:', collection.count_documents({"method": "DELETE"}))

    result = collection.count_documents({"method": "GET", "path": "/status"})
    print(result, 'status check')

    pipeline = [
            {"$group": {
                "_id": "$ip",
                "count": {"$sum": 1},
                }
             },
            {"$sort": {"count": -1}},
            {"$limit": 10}
            ]

    agg = collection.aggregate(pipeline)
    print('IPs')
    for ip in agg:
        print(f'\t{ip.get("_id")}: {ip.get("count")}')
