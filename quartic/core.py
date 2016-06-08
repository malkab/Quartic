#!/usr/bin/env python
# coding=UTF8

import xml.etree.ElementTree as et, collections as coll, copy, sha


class Connection(object):
    """
    Returns connection details.
    """

    c_keys = None
    """Dictionary with connection parameters."""

    
    def __init__(self, initObject=None):
        """
        Constructor.

        :param initObject: Object to initialize the connection from.
        :type initObject: quartic.core.DataSource or dictionary in the form {"dbname": "dbname", "host": "host", "port": "port", "user": "user", "password": "password"}
        """
        self.c_keys = {"dbname": None, "host": None, "port": None, "user": None, "password": None}
        
        if isinstance(initObject, DataSource) or isinstance(initObject, dict):
            self["dbname"] = initObject["dbname"]
            self["host"] = initObject["host"]
            self["port"] = initObject["port"]
            self["user"] = initObject["user"]
            self["password"] = initObject["password"]

            
    def __getitem__(self, key):
        """
        Returns a member of ds_keys.

        :param key: Key to return.
        :type key: String
        """
        return self.c_keys[key]


    def __hash__(self):
        """
        Computes the hash of the object. Used to create sets.
        """
        return int(sha.new(str(self)).hexdigest(), 16)
        

    def __setitem__(self, key, value):
        """
        Sets a member of ds_keys.

        :param key: Key to set.
        :type key: String
        :param value: Value to set the key to.
        :type value: String
        """
        self.c_keys[key]=value

            
    def __str__(self):
        """
        String representation of Connection.
        """
        return "%s %s %s %s %s" % (self["dbname"], self["host"], self["port"], self["user"], self["password"])


    def __eq__(self, conn):
        """
        Equality.

        :param conn: Another Connection.
        :type conn: quartic.core.Connection
        """
        if self.c_keys==conn.c_keys:
            return True
        else:
            return False

    
                
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

    
    def __hash__(self):
        """
        Computes the hash of the object. Used to create sets.
        """
        return int(sha.new(str(self)).hexdigest(), 16)
    

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

    
    def reconnect(self, connection):
        """
        Rebuilds the datasource string with new database parameters.

        :param connection: A Connection object with connection data.
        :type dbname: quartic.core.Connection
        :return: A new quartic.core.DataSource with connection parameters changed.
        """
        out = copy.deepcopy(self)

        out["dbname"] = connection["dbname"]
        out["host"] = connection["host"]
        out["port"] = connection["port"]
        out["user"] = connection["user"]
        out["password"] = connection["password"]

        return out

    

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


    def reconnect(self, 
