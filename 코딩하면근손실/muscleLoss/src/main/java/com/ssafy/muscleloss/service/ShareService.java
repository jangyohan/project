package com.ssafy.muscleloss.service;

import java.util.List;

import com.ssafy.muscleloss.model.Feed;
import com.ssafy.muscleloss.model.Share;

public interface ShareService {
	
	public int checkshare(Share share);
	public int registershare(Share share);
	public int deleteshare(Share share);
	
	public List<Feed> feedByShare(Feed feed);

	
	
}
