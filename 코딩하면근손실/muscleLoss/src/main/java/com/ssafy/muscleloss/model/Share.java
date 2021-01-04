package com.ssafy.muscleloss.model;

public class Share {
	
	private int feedNo_fk;                   
	private String uid_fk;                 
	private int shareCheck;
	
	public int getFeedNo_fk() {
		return feedNo_fk;
	}
	public void setFeedNo_fk(int feedNo_fk) {
		this.feedNo_fk = feedNo_fk;
	}
	public String getUid_fk() {
		return uid_fk;
	}
	public void setUid_fk(String uid_fk) {
		this.uid_fk = uid_fk;
	}
	public int getShareCheck() {
		return shareCheck;
	}
	public void setShareCheck(int shareCheck) {
		this.shareCheck = shareCheck;
	}
	
	@Override
	public String toString() {
		return "Share [feedNo_fk=" + feedNo_fk + ", uid_fk=" + uid_fk + ", shareCheck=" + shareCheck + "]";
	}

}
