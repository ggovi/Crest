package hep.crest.data.config;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

import hep.crest.data.monitoring.repositories.IMonitoringRepository;
import hep.crest.data.monitoring.repositories.JdbcMonitoringRepository;
import hep.crest.data.repositories.IovDirectoryImplementation;
import hep.crest.data.repositories.IovGroupsCustom;
import hep.crest.data.repositories.IovGroupsImpl;
import hep.crest.data.repositories.PayloadDataBaseCustom;
import hep.crest.data.repositories.PayloadDataDBImpl;
import hep.crest.data.repositories.PayloadDataPostgresImpl;
import hep.crest.data.repositories.PayloadDataSQLITEImpl;
import hep.crest.data.repositories.PayloadDirectoryImplementation;
import hep.crest.data.repositories.TagDirectoryImplementation;

@Configuration
@ComponentScan("hep.crest.data.repositories")
public class RepositoryConfig {
	
	@Autowired
	private CrestProperties cprops;
	
    @Bean(name = "fstagrepository")
    public TagDirectoryImplementation tagdirectoryRepository() {
        return new TagDirectoryImplementation();
    }
    @Bean(name = "fsiovrepository")
    public IovDirectoryImplementation iovdirectoryRepository() {
        return new IovDirectoryImplementation();
    }
    @Bean(name = "fspayloadrepository")
    public PayloadDirectoryImplementation payloaddirectoryRepository() {
        return new PayloadDirectoryImplementation();
    }
    
    @Bean(name = "iovgroupsrepo")
    public IovGroupsCustom iovgroupsRepository(@Qualifier("dataSource") DataSource mainDataSource) {
    		IovGroupsImpl bean = new IovGroupsImpl(mainDataSource);
    		if (!cprops.getSchemaname().equals("none")) {
    			bean.setDefault_tablename(cprops.getSchemaname());
    		}
    		return bean;
    }

    /*
    @Profile({"prod","wildfly"})
    @Bean(name = "monitoringrepo")
    public IMonitoringRepository monitoringRepository(@Qualifier("daoDataSource") DataSource mainDataSource) {
    		IMonitoringRepository bean = new JdbcMonitoringRepository(mainDataSource);
    		return bean;
    }

    @Profile({"default","sqlite","h2","dev","mysql","postgres"})
    @Bean(name = "monitoringrepo")
    public IMonitoringRepository monitoringDefaultRepository(@Qualifier("daoDataSource") DataSource mainDataSource) {
    		IMonitoringRepository bean = new JdbcMonitoringRepository(mainDataSource);
    		return bean;
    }
    */

    @Profile({"test","default","prod","h2","wildfly","ssl","dev","mysql"})
    @Bean(name = "payloaddatadbrepo")
    public PayloadDataBaseCustom payloadDefaultRepository(@Qualifier("dataSource") DataSource mainDataSource) {
    		PayloadDataDBImpl bean = new PayloadDataDBImpl(mainDataSource);
		if (!cprops.getSchemaname().equals("none")) {
			bean.setDefault_tablename(cprops.getSchemaname());
		}
		return bean;
    }
    
    @Profile({"postgres"})
    @Bean(name = "payloaddatadbrepo")
    public PayloadDataBaseCustom payloadPostgresRepository(@Qualifier("dataSource") DataSource mainDataSource) {
    		PayloadDataPostgresImpl bean = new PayloadDataPostgresImpl(mainDataSource);
		if (!cprops.getSchemaname().equals("none")) {
			bean.setDefault_tablename(cprops.getSchemaname());
		}
		return bean;
    }
    
    @Profile("sqlite")
    @Bean(name = "payloaddatadbrepo")
    public PayloadDataBaseCustom payloadSqliteRepository(@Qualifier("dataSource") DataSource mainDataSource) {
    		PayloadDataSQLITEImpl bean = new PayloadDataSQLITEImpl(mainDataSource);
		if (!cprops.getSchemaname().equals("none")) {
			bean.setDefault_tablename(cprops.getSchemaname());
		}
		return bean;
    }

}