package com.ssafy.muscleloss.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.muscleloss.model.Feed;

@Mapper
public interface FeedMapper {
	public int feedregister(Feed feed);
	public List<Feed> feedAll();
	public List<Feed> feedAllByUser(Feed feed);
	public List<Feed> feedTagSearch(Feed feed);
	Feed getfeedimage(Feed feed);
	public int feedUpate(Feed feed);
	public int feedDelete(String feedNo);
}