#!/usr/bin/env python
# coding=UTF-8

# import unittest as t, time
import quartic.core as q
import pytest_quartic.test_data.returned_data as rd
reload(q)
reload(rd)

"""
Tests for Quartic.
"""

class TestQuartic:
    """
    Tests for Quartic.
    """

    def test_quartic(self):
        p = q.Project("pytest_quartic/test_data/Database_catastro.qgs")

        new_conn = q.Connection({"dbname": "a_database", "host": "the_host", "port": "5432", "user": "the_user", "password": "the_pass"})

        c = q.Connection()

        # print c
        
        # print new_conn

        # print c==new_conn
        
        datasources = p.getDataSources()

        # print datasources[0]

        # print datasources[0].reconnect(new_conn)

        print set(p.getConnections())

        # print set(p.getDataSources())
        

        # reconnection = {"from": 
