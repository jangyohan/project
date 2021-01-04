package com.ssafy.muscleloss.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.muscleloss.mapper.MeetMapper;
import com.ssafy.muscleloss.model.Meet;

@Service
public class MeetServiceImpl implements MeetService{

	@Autowired
	private MeetMapper meetMapper;
	
	@Override
	public int meetregister(Meet meet) {
		return meetMapper.meetregister(meet);
	}

	@Override
	public List<Meet> meetAll() {
		return meetMapper.meetAll();
	}

	@Override
	public List<Meet> meetAllByCategory(Meet meet) {
		return meetMapper.meetAllByCategory(meet);
	}

	@Override
	public List<Meet> meetSearch(Meet meet) {
		return meetMapper.meetSearch(meet);
	}

	@Override
	public int meetUpdate(Meet meet) {
		return meetMapper.meetUpdate(meet);
	}

	@Override
	public int meetDelete(String meetNo) {
		return meetMapper.meetDelete(meetNo);
	}

}
