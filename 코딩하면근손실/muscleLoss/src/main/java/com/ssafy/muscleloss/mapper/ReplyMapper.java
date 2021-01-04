package com.ssafy.muscleloss.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.muscleloss.model.Reply;

@Mapper
public interface ReplyMapper {

	public List<Reply> listReply(int feedNo);	
	public int insertReply(Reply reply);
	public int updateReply(Reply reply);
	public int deleteReply(int rNo);

}
