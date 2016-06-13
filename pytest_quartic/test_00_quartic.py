#!/usr/bin/env python
# coding=UTF-8

# import unittest as t, time
import quartic.core as q
reload(q)


"""
Tests for Quartic.
"""

class TestQuartic:
    """
    Tests for Quartic.
    """

    def test_quartic(self):
        p = q.Project("pytest_quartic/test_data/Database_catastro.qgs")

        print
        print p.getDifferentConnections()

        assert p.getDifferentConnections()==set(["'catastro' localhost 5435 'catastro_admin' 'catastro_admin'"])
        
        newConn = q.Connection({"dbname": "a_database", "host": "the_host", "port": "5432",
                                "user": "the_user", "password": "the_pass"})

        oldConn = q.Connection({"dbname": "'catastro'", "host": "localhost", "port": "5435",
                                "user": "'catastro_admin'", "password": "'catastro_admin'"})
        
        p.reconnect(oldConn, newConn)

        print p.getDifferentConnections()

        assert p.getDifferentConnections()==set(["'a_database' the_host 5432 'the_user' 'the_pass'"])

        p.write("pytest_quartic/test_data/Rewritten.qgs")
