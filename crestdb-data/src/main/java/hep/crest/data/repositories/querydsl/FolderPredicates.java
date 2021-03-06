/**
 * 
 */
package hep.crest.data.repositories.querydsl;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.querydsl.core.types.Predicate;
import com.querydsl.core.types.dsl.BooleanExpression;

import hep.crest.data.security.pojo.QCrestFolders;

/**
 * @author aformic
 *
 */
public class FolderPredicates {

	private static Logger log = LoggerFactory.getLogger(FolderPredicates.class);

	private FolderPredicates() {

	}

	public static BooleanExpression hasNodeFullpathLike(String nfp) {
		log.debug("hasNodeFullpathLike: argument " + nfp);
		BooleanExpression pred = QCrestFolders.crestFolders.nodeFullpath.like("%" + nfp + "%");
		return pred;
	}
	public static BooleanExpression hasTagPatternLike(String tagpt) {
		log.debug("hasTagPatternLike: argument " + tagpt);
		BooleanExpression pred = QCrestFolders.crestFolders.tagPattern.like("%" + tagpt + "%");
		return pred;
	}
	public static BooleanExpression hasGroupRoleLike(String gr) {
		log.debug("hasGroupRoleLike: argument " + gr);
		BooleanExpression pred = QCrestFolders.crestFolders.groupRole.like("%" + gr + "%");
		return pred;
	}

	public static Predicate where(BooleanExpression exp) {
		Predicate pred = exp;
		return pred;
	}
}
