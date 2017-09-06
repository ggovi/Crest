package hep.crest.data.pojo;
// Generated Aug 2, 2016 3:50:25 PM by Hibernate Tools 3.2.2.GA

import java.sql.Timestamp;
import java.util.Date;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.PrePersist;
import javax.persistence.Table;

import hep.crest.data.config.*;
/**
 * Iov generated by hbm2java
 */
@Entity
@Table(name = "IOV", schema = DatabasePropertyConfigurator.SCHEMA_NAME)
public class Iov implements java.io.Serializable {

	/**
	* 
	*/
	private static final long serialVersionUID = 8775823880173022258L;
	private IovId id;
	private Tag tag;
	private String payloadHash;

	public Iov() {
	}

	public Iov(IovId id, Tag tag, String payloadHash) {
		this.id = id;
		this.tag = tag;
		this.payloadHash = payloadHash;
	}

	@EmbeddedId

	@AttributeOverrides({
			@AttributeOverride(name = "tagName", column = @Column(name = "TAG_NAME", nullable = false, length = 100)),
			@AttributeOverride(name = "since", column = @Column(name = "SINCE", nullable = false, precision = 38, scale = 0)),
			@AttributeOverride(name = "insertionTime", column = @Column(name = "INSERTION_TIME", nullable = false, length = 11)) })
	public IovId getId() {
		return this.id;
	}

	public void setId(IovId id) {
		this.id = id;
	}

	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "TAG_NAME", nullable = false, insertable = false, updatable = false)
	public Tag getTag() {
		return this.tag;
	}

	public void setTag(Tag tag) {
		this.tag = tag;
	}

	@Column(name = "PAYLOAD_HASH", nullable = false, length = 64)
	public String getPayloadHash() {
		return this.payloadHash;
	}

	public void setPayloadHash(String payloadHash) {
		this.payloadHash = payloadHash;
	}

	@PrePersist
	public void prePersist() {
		if (this.id.getInsertionTime() == null) {
			Timestamp now = new Timestamp(new Date().getTime());
			this.id.setInsertionTime(now);
		}
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() {
		return "Iov [id=" + id + ", tag=" + tag + ", payloadHash=" + payloadHash + "]";
	}

}
