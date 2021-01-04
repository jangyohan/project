package com.ssafy.muscleloss.model;

import java.util.Date;

public class Reply {
	
	private Integer rno;
	private Integer feedNo_fk;
	private String replytext;
	private String uid_fk;
	private Date regdate;
	private Date moddate;
	
	public Integer getRno() {
		return rno;
	}
	public void setRno(Integer rno) {
		this.rno = rno;
	}
	public Integer getFeedNo_fk() {
		return feedNo_fk;
	}
	public void setFeedNo_fk(Integer feedNo_fk) {
		this.feedNo_fk = feedNo_fk;
	}
	public String getReplytext() {
		return replytext;
	}
	public void setReplytext(String replytext) {
		this.replytext = replytext;
	}
	public String getUid_fk() {
		return uid_fk;
	}
	public void setUid_fk(String uid_fk) {
		this.uid_fk = uid_fk;
	}
	public Date getRegdate() {
		return regdate;
	}
	public void setRegdate(Date regdate) {
		this.regdate = regdate;
	}
	public Date getModdate() {
		return moddate;
	}
	public void setModdate(Date moddate) {
		this.moddate = moddate;
	}
	
	@Override
	public String toString() {
		return "Reply [rno=" + rno + ", feedNo_fk=" + feedNo_fk + ", replytext=" + replytext + ", uid_fk=" + uid_fk
				+ ", regdate=" + regdate + ", moddate=" + moddate + "]";
	}	
	
}
