/**
 * 
 */
package hep.crest.data.runinfo.repositories.querydsl;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import com.querydsl.core.types.dsl.BooleanExpression;

import hep.crest.data.exceptions.CdbServiceException;
import hep.crest.data.repositories.querydsl.IFilteringCriteria;
import hep.crest.data.repositories.querydsl.SearchCriteria;


/**
 * @author aformic
 *
 */
@Component("runlumiFiltering")
public class RunLumiInfoFiltering implements IFilteringCriteria {

	private Logger log = LoggerFactory.getLogger(this.getClass());

	/*
	 * (non-Javadoc)
	 * 
	 * @see
	 * hep.phycdb.svc.querydsl.IFilteringCriteria#createFilteringConditions(java
	 * .util.List, java.lang.Object)
	 */
	@Override
	public List<BooleanExpression> createFilteringConditions(List<SearchCriteria> criteria) throws CdbServiceException {
		try {
			List<BooleanExpression> expressions = new ArrayList<>();
			for (SearchCriteria searchCriteria : criteria) {
				log.debug("search criteria " + searchCriteria.getKey() + " " + searchCriteria.getOperation() + " "
						+ searchCriteria.getValue());
				if (searchCriteria.getKey().equals("run")) {
					BooleanExpression runxthan = RunLumiInfoPredicates.isRunXThan(searchCriteria.getOperation(), searchCriteria.getValue().toString());
					expressions.add(runxthan);
				}  else if (searchCriteria.getKey().equals("lb")) {
					BooleanExpression lbxthan = RunLumiInfoPredicates
							.isLBXThan(searchCriteria.getOperation(), searchCriteria.getValue().toString());
					expressions.add(lbxthan);
				}  else if (searchCriteria.getKey().equals("insertionTime")) {
					BooleanExpression insertionTimexthan = RunLumiInfoPredicates
							.isInsertionTimeXThan(searchCriteria.getOperation(), searchCriteria.getValue().toString());
					expressions.add(insertionTimexthan);
				} else if (searchCriteria.getKey().equals("since")) {
					BooleanExpression isSinceXThan = RunLumiInfoPredicates
							.isSinceXThan(searchCriteria.getOperation(), searchCriteria.getValue().toString());
					expressions.add(isSinceXThan);
				} else if (searchCriteria.getKey().equals("starttime")) {
					BooleanExpression isStarttimeXThan = RunLumiInfoPredicates
							.isStarttimeXThan(searchCriteria.getOperation(), searchCriteria.getValue().toString());
					expressions.add(isStarttimeXThan);
				} else if (searchCriteria.getKey().equals("endtime")) {
					BooleanExpression isEndtimeXThan = RunLumiInfoPredicates
							.isEndtimeXThan(searchCriteria.getOperation(), searchCriteria.getValue().toString());
					expressions.add(isEndtimeXThan);
				}
			}
			return expressions;
		} catch (Exception e) {
			throw new CdbServiceException(e.getMessage());
		}
	}

}
