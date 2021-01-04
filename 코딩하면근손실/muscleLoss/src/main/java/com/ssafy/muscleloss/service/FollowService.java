package com.ssafy.muscleloss.service;

import java.util.List;

import com.ssafy.muscleloss.model.Follow;

public interface FollowService {

	public int registFollow(Follow follow);
	public int deleteFollow(Follow follow);
	public int isFollow(Follow follow);
	
	public List<Follow> getFollowerList(String uid);
	public List<Follow> getFollowingList(String uid);
	
	public int getFollowerCount(String uid);
	public int getFollowingCount(String uid);

}
