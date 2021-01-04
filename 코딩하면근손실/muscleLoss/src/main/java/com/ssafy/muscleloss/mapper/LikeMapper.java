package com.ssafy.muscleloss.mapper;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.muscleloss.model.Feed;
import com.ssafy.muscleloss.model.Like;

@Mapper
public interface LikeMapper {
	
	public int checklike(Like like);
	public int updatelike(Like like);
	public int deletelike(Like like);
	public int countlike(int feedno);
}
