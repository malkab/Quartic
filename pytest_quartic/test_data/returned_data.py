#!/usr/bin/env python
# coding=UTF-8


datasources = ['OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_centroide_parcela_grid_31_25" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'Key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_cent_pond_constru_grid_31_25" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'MULTIPOLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__constru_on_parcela_aggregate" (c_geom)\'), (\'sql\', \'"p_pu005" is not null or "p_pu029" is not null\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'MULTIPOLYGON\'), (\'table\', \'"fase_0"."catastro__c_parcela_residencial" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid_pkey\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"fase_0"."catastro__c_parcelas_andalucia" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"fase_0"."catastro_normalized_import_20150330__constru" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"context"."grid_125" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"context"."grid_250" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"context"."grid_31_25" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"context"."grid_62_5" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'MULTIPOLYGON\'), (\'table\', \'"context"."municipio" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POINT\'), (\'table\', \'"agregaciones_rejilla"."mvw__constru_on_parcela_aggregate" (wcent)\'), (\'sql\', \'"p_pu005" is not null or "p_pu029" is not null\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__constru_on_parcela_aggregate" (p_geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'MULTIPOLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__constru_on_parcela_aggregate" (c_geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POINT\'), (\'table\', \'"context"."mvw__grid_125_centroid" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POINT\'), (\'table\', \'"context"."mvw__grid_250_centroid" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POINT\'), (\'table\', \'"context"."mvw__grid_31_25_centroid" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POINT\'), (\'table\', \'"context"."mvw__grid_62_5_centroid" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__indicadores_parcelas_centroide_grid_125" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__indicadores_parcelas_centroide_grid_250" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__indicadores_parcelas_centroide_grid_31_25" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__indicadores_parcelas_centroide_grid_62_5" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_cent_pond_constru_grid_125" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_cent_pond_constru_grid_250" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_cent_pond_constru_grid_31_25" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_cent_pond_constru_grid_31_25" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_cent_pond_constru_grid_62_5" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_centroide_parcela_grid_125" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_centroide_parcela_grid_250" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_centroide_parcela_grid_31_25" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_centroide_parcela_grid_31_25" (geom)\')])', 'OrderedDict([(\'dbname\', "\'catastro\'"), (\'host\', \'localhost\'), (\'port\', \'5435\'), (\'user\', "\'catastro_admin\'"), (\'password\', "\'catastro_admin\'"), (\'sslmode\', \'disable\'), (\'key\', "\'gid\'"), (\'estimatedmetadata\', \'true\'), (\'srid\', \'25830\'), (\'type\', \'POLYGON\'), (\'table\', \'"agregaciones_rejilla"."mvw__pu005_pu029_centroide_parcela_grid_62_5" (geom)\')])']
