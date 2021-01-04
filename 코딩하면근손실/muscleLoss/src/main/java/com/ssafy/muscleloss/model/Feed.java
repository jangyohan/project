package com.ssafy.muscleloss.model;

public class Feed implements Comparable<Feed>{
	private int feedNo;
	private String uid_fk;
	private String userimage;
	private String title;
	private String content;
	private String regdate;
	private String moddate;
	private int likeCount;
	private int replyCount;
	private String fileName;
	private String imgtype;
	
	public int getFeedNo() {
		return feedNo;
	}
	public void setFeedNo(int feedNo) {
		this.feedNo = feedNo;
	}
	public String getUid_fk() {
		return uid_fk;
	}
	public void setUid_fk(String uid_fk) {
		this.uid_fk = uid_fk;
	}
	public String getUserimage() {
		return userimage;
	}
	public void setUserimage(String userimage) {
		this.userimage = userimage;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	public String getRegdate() {
		return regdate;
	}
	public void setRegdate(String regdate) {
		this.regdate = regdate;
	}
	public String getModdate() {
		return moddate;
	}
	public void setModdate(String moddate) {
		this.moddate = moddate;
	}
	public int getLikeCount() {
		return likeCount;
	}
	public void setLikeCount(int likeCount) {
		this.likeCount = likeCount;
	}
	public int getReplyCount() {
		return replyCount;
	}
	public void setReplyCount(int replyCount) {
		this.replyCount = replyCount;
	}
	public String getFileName() {
		return fileName;
	}
	public void setFileName(String fileName) {
		this.fileName = fileName;
	}
	public String getImgtype() {
		return imgtype;
	}
	public void setImgtype(String imgtype) {
		this.imgtype = imgtype;
	}
	@Override
	public String toString() {
		return "Feed [feedNo=" + feedNo + ", uid_fk=" + uid_fk + ", userimage=" + userimage + ", title=" + title
				+ ", content=" + content + ", regdate=" + regdate + ", moddate=" + moddate + ", likeCount=" + likeCount
				+ ", replyCount=" + replyCount + ", fileName=" + fileName + ", imgtype=" + imgtype + "]";
	}
	@Override
	public int compareTo(Feed o) {
		return o.feedNo - this.feedNo;
	}
}