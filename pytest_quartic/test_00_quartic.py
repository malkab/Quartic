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

        print p.printDataSources()
        print p.printConnections()
       
