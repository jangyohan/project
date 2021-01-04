package com.ssafy.muscleloss.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.muscleloss.mapper.LikeMapper;
import com.ssafy.muscleloss.model.Feed;
import com.ssafy.muscleloss.model.Like;

@Service
public class LikeServiceImpl implements LikeService{

	@Autowired
	LikeMapper likeMapper;
	
	@Override
	public int checklike(Like like) {
		return likeMapper.checklike(like);
	}

	@Override
	public int updatelike(Like like) {
		return likeMapper.updatelike(like);
	}

	@Override
	public int deletelike(Like like) {
		return likeMapper.deletelike(like);
	}

	@Override
	public int countlike(int feedno) {
		return likeMapper.countlike(feedno);
	}

}
