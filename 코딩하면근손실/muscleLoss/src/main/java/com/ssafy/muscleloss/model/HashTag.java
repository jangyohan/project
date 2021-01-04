package com.ssafy.muscleloss.model;

public class HashTag {
	
	private Integer tag_id;
	private String tag_name;
	
	//getter,setter,toString
	public Integer getTag_id() {
		return tag_id;
	}
	public void setTag_id(Integer tag_id) {
		this.tag_id = tag_id;
	}
	public String getTag_name() {
		return tag_name;
	}
	public void setTag_name(String tag_name) {
		this.tag_name = tag_name;
	}
	
	@Override
	public String toString() {
		return "HashTagVO [tag_id=" + tag_id + ", tag_name=" + tag_name + "]";
	}
	
	@Override
	public int hashCode() {
		return tag_name.hashCode();
	}

}
