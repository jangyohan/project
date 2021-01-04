package com.ssafy.muscleloss.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.muscleloss.model.Member;

@Mapper
public interface MemberMapper {
	
	Member login(Member member);
	Member findPwd(Member email);
	public int signUp(Member member);
	public List<Member> searchAll();
	public int updateMem(Member member);
	public int deleteMem(String userid);
	Member search(String userid);
	public int updateMemPw(Member member);
	public int updateComment(Member member);
	public int updateProfile(Member member);
}
