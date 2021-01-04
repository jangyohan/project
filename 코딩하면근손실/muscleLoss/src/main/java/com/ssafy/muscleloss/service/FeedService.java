package com.ssafy.muscleloss.service;

import java.util.List;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;

import com.ssafy.muscleloss.model.Feed;

public interface FeedService {
	public int feedregister(Feed feed);
	public List<Feed> feedAll();
	public List<Feed> feedAllByUser(Feed feed);
	public List<Feed> feedTagSearch(Feed feed);
	Feed getfeedimage(Feed feed);
	public int feedUpate(Feed feed);
	public int feedDelete(String feedNo);
}
