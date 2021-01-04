package com.ssafy.muscleloss.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.muscleloss.mapper.FollowMapper;
import com.ssafy.muscleloss.model.Follow;
import com.ssafy.muscleloss.model.Member;

@Service
public class FollowServiceImpl implements FollowService{

	@Autowired
	private FollowMapper followMapper;
	
	@Override
	public int registFollow(Follow follow) {
		return followMapper.registFollow(follow);
	}

	@Override
	public int deleteFollow(Follow follow) {
		return followMapper.deleteFollow(follow);
	}

	@Override
	public int isFollow(Follow follow) {
		return followMapper.isFollow(follow);
	}

	@Override
	public List<Follow> getFollowerList(String uid) {
		return followMapper.getFollowerList(uid);
	}

	@Override
	public List<Follow> getFollowingList(String uid) {
		return followMapper.getFollowingList(uid);
	}

	@Override
	public int getFollowerCount(String uid) {
		return followMapper.getFollowerCount(uid);
	}

	@Override
	public int getFollowingCount(String uid) {
		return followMapper.getFollowingCount(uid);
	}

}
