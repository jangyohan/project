package com.ssafy.muscleloss.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.muscleloss.model.Alarm;

@Mapper
public interface AlarmMapper {

	public int registerAlarm(String uid_fk_to, String uid_fk_from, String message, String alarmCheck);

	public int countAlarm(String uid_fk_to);

	public List<Alarm> listAlarm(String uid_fk_to);

	public int updateAlarm(String no);

	public int deleteAlarm(String no);

}
