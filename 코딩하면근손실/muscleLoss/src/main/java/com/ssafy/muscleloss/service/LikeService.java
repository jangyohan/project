package com.ssafy.muscleloss.service;

import com.ssafy.muscleloss.model.Feed;
import com.ssafy.muscleloss.model.Like;

public interface LikeService {
	
	public int checklike(Like like);
	public int updatelike(Like like);
	public int deletelike(Like like);
	public int countlike(int feedno);

}
