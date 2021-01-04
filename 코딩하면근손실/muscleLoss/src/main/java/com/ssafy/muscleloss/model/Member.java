package com.ssafy.muscleloss.model;

public class Member {
	
	private String uid;
	private String email;
	private String password;
	private String create_date;
	private String interest1;
	private String interest2;
	private String interest3;
	private String avatarImage;
	private String imgtype;
	private String usercomment;
	private String usertoken;
	
	public String getUsertoken() {
		return usertoken;
	}
	public void setUsertoken(String usertoken) {
		this.usertoken = usertoken;
	}
	
	public String getUid() {
		return uid;
	}
	public void setUid(String uid) {
		this.uid = uid;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getCreate_date() {
		return create_date;
	}
	public void setCreate_date(String create_date) {
		this.create_date = create_date;
	}
	public String getInterest1() {
		return interest1;
	}
	public void setInterest1(String interest1) {
		this.interest1 = interest1;
	}
	public String getInterest2() {
		return interest2;
	}
	public void setInterest2(String interest2) {
		this.interest2 = interest2;
	}
	public String getInterest3() {
		return interest3;
	}
	public void setInterest3(String interest3) {
		this.interest3 = interest3;
	}
	public String getAvatarImage() {
		return avatarImage;
	}
	public void setAvatarImage(String avatarImage) {
		this.avatarImage = avatarImage;
	}
	public String getImgtype() {
		return imgtype;
	}
	public void setImgtype(String imgtype) {
		this.imgtype = imgtype;
	}
	public String getUsercomment() {
		return usercomment;
	}
	public void setUsercomment(String usercomment) {
		this.usercomment = usercomment;
	}
	@Override
	public String toString() {
		return "Member [uid=" + uid + ", email=" + email + ", password=" + password + ", create_date=" + create_date
				+ ", interest1=" + interest1 + ", interest2=" + interest2 + ", interest3=" + interest3
				+ ", avatarImage=" + avatarImage + ", imgtype=" + imgtype + ", usercomment=" + usercomment
				+ ", usertoken=" + usertoken + "]";
	}
}
