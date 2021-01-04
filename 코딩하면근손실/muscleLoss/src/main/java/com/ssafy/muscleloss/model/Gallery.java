package com.ssafy.muscleloss.model;

public class Gallery {
	
	private int imageNo;
	private String uid_fk;
	private String regdate;
	private String moddate;
	private String imagesrc;
	private String imgtype;
	
	public int getImageNo() {
		return imageNo;
	}
	public void setImageNo(int imageNo) {
		this.imageNo = imageNo;
	}
	public String getUid_fk() {
		return uid_fk;
	}
	public void setUid_fk(String uid_fk) {
		this.uid_fk = uid_fk;
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
	public String getImagesrc() {
		return imagesrc;
	}
	public void setImagesrc(String imagesrc) {
		this.imagesrc = imagesrc;
	}
	public String getImgtype() {
		return imgtype;
	}
	public void setImgtype(String imgtype) {
		this.imgtype = imgtype;
	}
	@Override
	public String toString() {
		return "Gallery [imageNo=" + imageNo + ", uid_fk=" + uid_fk + ", regdate=" + regdate + ", moddate=" + moddate
				+ ", imagesrc=" + imagesrc + ", imgtype=" + imgtype + "]";
	}
}
