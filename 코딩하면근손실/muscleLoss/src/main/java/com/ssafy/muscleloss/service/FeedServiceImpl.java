package com.ssafy.muscleloss.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.ui.Model;

import com.ssafy.muscleloss.mapper.FeedMapper;
import com.ssafy.muscleloss.model.Feed;

@Service
public class FeedServiceImpl implements FeedService {

	@Autowired
	private FeedMapper feedMapper;

	@Override
	public int feedregister(Feed feed) {
		return feedMapper.feedregister(feed);
	}
	
	@Override
	public List<Feed> feedAll() {		
		return feedMapper.feedAll();
	}

	@Override
	public List<Feed> feedAllByUser(Feed feed) {
		return feedMapper.feedAllByUser(feed);
	}

	@Override
	public List<Feed> feedTagSearch(Feed feed) {
		return feedMapper.feedTagSearch(feed);
	}
	
	@Override
	public Feed getfeedimage(Feed feed) {
		return feedMapper.getfeedimage(feed);
	}

	@Override
	public int feedUpate(Feed feed) {
		return feedMapper.feedUpate(feed);
	}

	@Override
	public int feedDelete(String feedNo) {
		return feedMapper.feedDelete(feedNo);
	}
}
