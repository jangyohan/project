package com.ssafy.muscleloss.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.muscleloss.mapper.AlarmMapper;
import com.ssafy.muscleloss.model.Alarm;

@Service
public class AlarmServiceImpl implements AlarmService {

	@Autowired
	AlarmMapper alarmMapper;

	@Override
	public int registerAlarm(String uid_fk_to, String uid_fk_from, String message, String alarmCheck) {
		return alarmMapper.registerAlarm(uid_fk_to, uid_fk_from, message, alarmCheck);
	}

	@Override
	public int countAlarm(String uid_fk_to) {
		return alarmMapper.countAlarm(uid_fk_to);
	}

	@Override
	public List<Alarm> listAlarm(String uid_fk_to) {
		return alarmMapper.listAlarm(uid_fk_to);
	}

	@Override
	public int updateAlarm(String no) {
		return alarmMapper.updateAlarm(no);
	}

	@Override
	public int deleteAlarm(String no) {
		return alarmMapper.deleteAlarm(no);
	}

}
