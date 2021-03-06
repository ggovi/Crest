/**
 * 
 */
package hep.crest.data.repositories.querydsl;

import java.util.Date;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.querydsl.core.types.Predicate;
import com.querydsl.core.types.dsl.BooleanExpression;

import hep.crest.data.pojo.QTag;


/**
 * @author aformic
 *
 */
public class TagPredicates {

	private static Logger log = LoggerFactory.getLogger(TagPredicates.class);

	private TagPredicates() {

	}

	public static BooleanExpression hasNameLike(String name) {
		log.debug("hasNameLike: argument " + name);
		BooleanExpression pred = QTag.tag.name.like("%" + name + "%");
		return pred;
	}
	
	public static BooleanExpression hasTimeTypeLike(String ttype) {
		log.debug("hasTimeTypeLike: argument " + ttype);
		BooleanExpression pred = QTag.tag.timeType.like("%" + ttype + "%");
		return pred;
	}

	public static BooleanExpression hasObjectTypeLike(String objtype) {
		log.debug("hasObjectTypeLike: argument " + objtype);
		BooleanExpression pred = QTag.tag.objectType.like("%"+objtype+"%");
		return pred;
	}
	
	public static BooleanExpression isInsertionTimeXThan(String oper, String num) {
		log.debug("isInsertionTimeXThan: argument " + num + " operation " + oper);
		BooleanExpression pred = null;

		if (oper.equals("<")) {
			pred = QTag.tag.insertionTime.lt(new Date(new Long(num)));
		} else if (oper.equals(">")) {
			pred = QTag.tag.insertionTime.gt(new Date(new Long(num)));
		} else if (oper.equals(":")) {
			pred = QTag.tag.insertionTime.eq(new Date(new Long(num)));
		}
		return pred;
	}
	public static BooleanExpression isModificationTimeXThan(String oper, String num) {
		log.debug("isModificationTimeXThan: argument " + num + " operation " + oper);
		BooleanExpression pred = null;

		if (oper.equals("<")) {
			pred = QTag.tag.modificationTime.lt(new Date(new Long(num)));
		} else if (oper.equals(">")) {
			pred = QTag.tag.modificationTime.gt(new Date(new Long(num)));
		} else if (oper.equals(":")) {
			pred = QTag.tag.modificationTime.eq(new Date(new Long(num)));
		}
		return pred;
	}

	public static Predicate where(BooleanExpression exp) {
		Predicate pred = exp;
		return pred;
	}
}
