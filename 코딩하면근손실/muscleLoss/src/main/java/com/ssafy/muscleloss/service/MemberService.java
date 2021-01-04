package com.ssafy.muscleloss.service;

import java.util.List;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;

import com.ssafy.muscleloss.model.Member;

public interface MemberService {

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
