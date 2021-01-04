package com.ssafy.muscleloss.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.ui.Model;

import com.ssafy.muscleloss.mapper.MemberMapper;
import com.ssafy.muscleloss.model.Member;

@Service
public class MemberServiceImpl implements MemberService {

	@Autowired
	private MemberMapper memberMapper;

	@Override
	public Member login(Member member) {
		return memberMapper.login(member);
	}
	
	@Override
	public int signUp(Member member) {
		return memberMapper.signUp(member);
	}
	
	@Override
	public Member findPwd(Member email) {
		return memberMapper.findPwd(email);
	}

	@Override
	public List<Member> searchAll() {		
		return memberMapper.searchAll();
	}

	@Override
	public int updateMem(Member member) {
		return memberMapper.updateMem(member);
	}
	
	@Override
	public int updateMemPw(Member member) {
		return memberMapper.updateMemPw(member);
	}

	@Override
	public int deleteMem(String userid) {
		return memberMapper.deleteMem(userid);
	}

	@Override
	public Member search(String userid) {	
		return memberMapper.search(userid);
	}

	@Override
	public int updateComment(Member member) {
		return memberMapper.updateComment(member);
	}

	@Override
	public int updateProfile(Member member) {
		return memberMapper.updateProfile(member);
	}
}
