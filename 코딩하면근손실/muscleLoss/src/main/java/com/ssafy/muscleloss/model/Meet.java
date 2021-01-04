package com.ssafy.muscleloss.model;

public class Meet implements Comparable<Meet> {

	private int meetNo;
	private String uid_fk;
	private String userimage;
	private String title;
	private String content;
	private String regdate;
	private String moddate;
	private String category;
	private String meetdate;
	private String kakao;
	private String map;
	private String imgtype;
	
	public int getMeetNo() {
		return meetNo;
	}

	public void setMeetNo(int meetNo) {
		this.meetNo = meetNo;
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

	public String getCategory() {
		return category;
	}

	public void setCategory(String category) {
		this.category = category;
	}

	public String getMeetdate() {
		return meetdate;
	}

	public void setMeetdate(String meetdate) {
		this.meetdate = meetdate;
	}

	public String getKakao() {
		return kakao;
	}

	public void setKakao(String kakao) {
		this.kakao = kakao;
	}

	public String getMap() {
		return map;
	}

	public void setMap(String map) {
		this.map = map;
	}

	public String getImgtype() {
		return imgtype;
	}

	public void setImgtype(String imgtype) {
		this.imgtype = imgtype;
	}

	@Override
	public String toString() {
		return "Meet [meetNo=" + meetNo + ", uid_fk=" + uid_fk + ", userimage=" + userimage + ", title=" + title
				+ ", content=" + content + ", regdate=" + regdate + ", moddate=" + moddate + ", category=" + category
				+ ", meetdate=" + meetdate + ", kakao=" + kakao + ", map=" + map + ", imgtype=" + imgtype + "]";
	}

	@Override
	public int compareTo(Meet o) {
		return o.meetNo - this.meetNo;
	}

}
