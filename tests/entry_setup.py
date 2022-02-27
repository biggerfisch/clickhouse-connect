#!/usr/bin/env python

def add_test_entries():
    import pkg_resources
    dist = pkg_resources.Distribution('clickhouse-connect-test')
    ep = pkg_resources.EntryPoint.parse('clickhouse_connect = clickhouse_connect.sqlalchemy.dialect.ClickHouseDialect', dist=dist)
    entry_map = dist.get_entry_map()
    map_entry = entry_map.get_from_name('sqlalchemy.dialects')
    if map_entry is None:
        entry_map['sqlalchemy.dialects'] = {'clickhouse_connect': [ep]}
        pkg_resources.working_set.add(dist)
        print('test ep added to distribution')
    else:
        print('test ep already added')


if __name__ == '__main__':
    add_test_entries()
