package com.ssafy.muscleloss.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.muscleloss.mapper.FeedMapper;
import com.ssafy.muscleloss.mapper.ReplyMapper;
import com.ssafy.muscleloss.model.Reply;

@Service
public class ReplyServiceImpl implements ReplyService{

	
	@Autowired
	private ReplyMapper replyMapper;

	@Override
	public List<Reply> listReply(int feedNo) {
		return replyMapper.listReply(feedNo);
	}

	@Override
	public int insertReply(Reply reply) {
		return replyMapper.insertReply(reply);
	}

	@Override
	public int updateReply(Reply reply) {
		return replyMapper.updateReply(reply);
	}

	@Override
	public int deleteReply(int rNo) {
		return replyMapper.deleteReply(rNo);
	}
	
}
