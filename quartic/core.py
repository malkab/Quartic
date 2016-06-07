#!/usr/bin/env python
# coding=UTF8

import xml.etree.ElementTree as et, collections as coll


class Connection(object):
    """
    Returns connection details.
    """

    ds_dbname = None
    """DB name."""

    ds_host = None
    """Host."""

    ds_port = None
    """Port."""

    ds_user = None
    """User."""

    ds_password = None
    """Password."""

    def __init__(self, initObject=None):
        """
        Constructor.

        :param initObject: Object to initialize the connection from.
        :type initObject: quartic.core.DataSource
        """
        if isinstance(initObject, DataSource):
            self.ds_dbname = initObject["dbname"]
            self.ds_host = initObject["host"]
            self.ds_port = initObject["port"]
            self.ds_user = initObject["user"]
            self.ds_password = initObject["password"]


    def __str__(self):
        """
        String representation of Connection.
        """
        return "%s %s %s %s %s" % (self.ds_dbname, self.ds_host, self.ds_port, self.ds_user, self.ds_password)


    def __eq__(self, conn):
        """
        Equality.

        :param conn: Another Connection.
        :type conn: quartic.core.Connection
        """
        if self.ds_dbname<>conn.ds_dbname:
            return False
        if self.ds_host<>conn.ds_host:
            return False        
        if self.ds_port<>conn.ds_port:
            return False
        if self.ds_user<>conn.ds_user:
            return False                    
        if self.ds_password<>conn.ds_password:
            return False
        return True

    
                
class DataSource(object):
    """
    datasource representation in a QGIS project.
    """

    datasource = None
    """Original datasource string."""
    
    ds_keys = None
    """Dictionary with key/values of datasource string parsing."""

    
    def __init__(self, datasource=None):
        """
        Constructor.

        :param datasource: datasource string of a QGIS project. Optional. If present, is parsed.
        :type datasource: String
        """
        if datasource is not None:
            self.datasource = datasource
            self.ds_keys = coll.OrderedDict()
            self.parse(self.datasource)


    def __getitem__(self, key):
        """
        Returns a member of ds_keys.

        :param key: Key to return.
        :type key: String
        """
        return self.ds_keys[key]


    def __setitem__(self, key, value):
        """
        Sets a member of ds_keys.

        :param key: Key to set.
        :type key: String
        :param value: Value to set the key to.
        :type value: String
        """
        self.ds_keys[key]=value
    

    def __str__(self):
        """
        Return a string representation of the DataSource object. Prints the OrderedDict of parsed values.
        """
        return str(self.ds_keys)


    def __eq__(self, other):
        """
        Equality.

        :param other: Other DataSource object to compare with.
        :type other: quartic.core.DataSource
        """
        return self.ds_keys==other.ds_keys

    
    def parse(self, datasource):
        """
        Parses a datasource string.
        """
        self.datasource = datasource

        a = self.datasource.partition("=")

        while a[2]<>"":
            key = a[0]
            if key=="table":
                b = a[2].partition(")")
                value = b[0]+")"
            elif key==" sql":
                key = "sql"
                value = a[2]
                b = a[2].partition(" ")
            else:
                b = a[2].partition(" ")
                value = b[0]

            self.ds_keys[key] = value
            a = b[2].partition("=")

        return self.ds_keys


    def getConnection(self):
        return Connection(self)

    
    def rebuild(self, dbname=None, host=None, port=None, user=None, password=None):
        """
        Rebuilds the datasource string with new database parameters.

        :param dbname: New database name.
        :type dbname: String
        :param host: New database host.
        :type host: String
        :param port: New database port.
        :type port: String
        :param user: New database user.
        :type user: String
        :param password: New password.
        :type password: String
        """
        pass

    

class Project(object):
    """
    Class containing functionality.
    """

    project = None
    """Project file to analyze."""

    
    def __init__(self, project):
        """
        Constructor.

        :param project: Project path.
        :type project: String
        """
        self.project = project


    def getDataSources(self):
        """
        Get all different data sources in project.
        """

        tree = et.parse(self.project)
        layers = tree.getroot().find("projectlayers").findall("maplayer")
        layerdatasource = []
        
        for i in layers:
            provider = i.find("provider")

            if provider is not None:
                if provider.text=="postgres":
                    datasource = i.find("datasource").text
                    ds = DataSource(datasource)
                    layerdatasource.append(ds)
                    
        return layerdatasource


    def printDataSources(self):
        """
        Prints all different DataSources.
        """

        return set([str(i) for i in self.getDataSources()])


    def getConnections(self):
        """
        Get all connections in project.
        """

        ds = self.getDataSources()
        return [i.getConnection() for i in ds]


    def printConnections(self):
        """
        Prints all different connections.
        """

        return set([str(i) for i in self.getConnections()])
