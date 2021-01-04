package com.ssafy.muscleloss.service;

import java.util.List;

import com.ssafy.muscleloss.model.Alarm;

public interface AlarmService {

	public int registerAlarm(String uid_fk_to, String uid_fk_from, String message, String alarmCheck);

	public int countAlarm(String uid_fk_to);

	public List<Alarm> listAlarm(String uid_fk_to);

	public int updateAlarm(String no);

	public int deleteAlarm(String no);
}
