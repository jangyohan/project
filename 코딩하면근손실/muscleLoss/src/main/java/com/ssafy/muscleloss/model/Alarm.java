package com.ssafy.muscleloss.model;

import java.util.Date;

public class Alarm {
	private String no;
	private String message;
	private String uid_fk_to;
	private String uid_fk_from;
	private String alarmCheck;
	private Date date;
	
	
	public String getNo() {
		return no;
	}
	public void setNo(String no) {
		this.no = no;
	}
	public String getMessage() {
		return message;
	}
	public void setMessage(String message) {
		this.message = message;
	}
	public String getUid_fk_to() {
		return uid_fk_to;
	}
	public void setUid_fk_to(String uid_fk_to) {
		this.uid_fk_to = uid_fk_to;
	}
	public String getUid_fk_from() {
		return uid_fk_from;
	}
	public void setUid_fk_from(String uid_fk_from) {
		this.uid_fk_from = uid_fk_from;
	}
	public String getAlarmCheck() {
		return alarmCheck;
	}
	public void setAlarmCheck(String alarmCheck) {
		this.alarmCheck = alarmCheck;
	}
	public Date getDate() {
		return date;
	}
	public void setDate(Date date) {
		this.date = date;
	}
	
	@Override
	public String toString() {
		return "Alarm [no=" + no + ", message=" + message + ", uid_fk_to=" + uid_fk_to + ", uid_fk_from=" + uid_fk_from
				+ ", alarmCheck=" + alarmCheck + ", date=" + date + "]";
	}
	
}
