package com.ssafy.muscleloss.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.muscleloss.mapper.FeedMapper;
import com.ssafy.muscleloss.mapper.ShareMapper;
import com.ssafy.muscleloss.model.Feed;
import com.ssafy.muscleloss.model.Share;

@Service
public class ShareServiceImpl implements ShareService{

	@Autowired
	ShareMapper shareMapper;
	
	@Autowired
	FeedMapper feedMapper;

	@Override
	public int registershare(Share share) {
		return shareMapper.registershare(share);
	}

	@Override
	public int deleteshare(Share share) {
		return shareMapper.deleteshare(share);
	}

	@Override
	public int checkshare(Share share) {
		return shareMapper.checkshare(share);
	}

	@Override
	public List<Feed> feedByShare(Feed feed) {
		return shareMapper.feedByShare(feed);
	}

}
