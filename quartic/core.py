#!/usr/bin/env python
# coding=UTF8

import xml.etree.ElementTree as et, collections as coll, sha


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
            
            if "'" not in self["dbname"]:
                self["dbname"] = "'%s'" % self["dbname"]
                
            self["host"] = initObject["host"]
            self["port"] = initObject["port"]
            self["user"] = initObject["user"]

            if "'" not in self["user"]:
                self["user"] = "'%s'" % self["user"]
            
            self["password"] = initObject["password"]

            if "'" not in self["password"]:
                self["password"] = "'%s'" % self["password"]

            
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

    xmlElement = None
    """XML ElementTree the datasource is defined in."""

    
    def __init__(self, datasource=None, xmlElement=None):
        """
        Constructor.

        :param datasource: Data source string of a QGIS project. Optional. If present, is parsed.
        :type datasource: String
        :param xmlElement: XML element the datasource is defined in.
        :type xmlElement: xml.etree.ElementTree
        """
        self.xmlElement = xmlElement
        
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

        if "sql" not in self.ds_keys.keys():
            self.ds_keys["sql"] = ""
            
        return self.ds_keys


    def getConnection(self):
        return Connection(self)

    
    def reconnect(self, connection):
        """
        Rebuilds the datasource string with new database parameters.

        :param connection: A Connection object with connection data.
        :type dbname: quartic.core.Connection
        """
        
        self["dbname"] = connection["dbname"]
        self["host"] = connection["host"]
        self["port"] = connection["port"]
        self["user"] = connection["user"]
        self["password"] = connection["password"]


    def getDataSourceString(self):
        """
        Outputs the datasource connection string.
        """

        out = ""
        
        for k,v in self.ds_keys.iteritems():
            out = out+(" %s=%s" % (k, v))

        return out.strip()

    

class Project(object):
    """
    Class containing functionality.
    """

    project = None
    """Project file to analyze."""

    tree = None
    """Project XML representation."""

    
    def __init__(self, project):
        """
        Constructor.

        :param project: Project path.
        :type project: String
        """
        self.project = project
        self.tree = et.parse(self.project)
        

    def getDataSources(self):
        """
        Get all different data sources in project.
        """

        layers = self.tree.getroot().find("projectlayers").findall("maplayer")
        layerdatasource = []
        
        for i in layers:
            provider = i.find("provider")

            if provider is not None:
                if provider.text=="postgres":
                    datasource = i.find("datasource").text
                    ds = DataSource(datasource, i.find("datasource"))
                    layerdatasource.append(ds)
                    
        return layerdatasource


    def getDifferentDataSources(self):
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


    def getDifferentConnections(self):
        """
        Prints all different connections.
        """

        return set([str(i) for i in self.getConnections()])


    def reconnect(self, oldConn, newConn):
        """
        Reconnect DataSources with a given connection to a new connection.

        :param oldConn: Old connection to replace.
        :type oldConn: quartic.core.Connection
        :param newConn: New connection.
        :type newConn: quartic.core.Connection
        """

        for i in self.getDataSources():
            if i.getConnection()==oldConn:
                i.reconnect(newConn)
                i.xmlElement.text=i.getDataSourceString()


    def write(self, fileName):
        """
        Rewrites the project file.

        :param fileName: File name.
        :type fileName: String
        """
        
        self.tree.write(fileName)
