package com.ssafy.muscleloss.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.muscleloss.model.Feed;
import com.ssafy.muscleloss.model.Share;

@Mapper
public interface ShareMapper {
	
	public int checkshare(Share share);
	public int registershare(Share share);
	public int deleteshare(Share share);
	
	public List<Feed> feedByShare(Feed feed);


}
