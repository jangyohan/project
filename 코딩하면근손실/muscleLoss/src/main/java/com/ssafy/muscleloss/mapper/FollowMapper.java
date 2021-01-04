package com.ssafy.muscleloss.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.muscleloss.model.Follow;

@Mapper
public interface FollowMapper {
	
	public int registFollow(Follow follow);
	public int deleteFollow(Follow follow);
	public int isFollow(Follow follow);
	
	public List<Follow> getFollowerList(String uid);
	public List<Follow> getFollowingList(String uid);
	
	public int getFollowerCount(String uid);
	public int getFollowingCount(String uid);

}
