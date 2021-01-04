package com.ssafy.muscleloss.service;

import java.util.List;

import com.ssafy.muscleloss.model.Reply;

public interface ReplyService {

	public List<Reply> listReply(int feedNo);	
	public int insertReply(Reply reply);
	public int updateReply(Reply reply);
	public int deleteReply(int rNo);
}
