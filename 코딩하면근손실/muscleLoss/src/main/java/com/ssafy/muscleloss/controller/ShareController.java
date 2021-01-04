package com.ssafy.muscleloss.controller;

import java.util.Collections;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.ssafy.muscleloss.model.Alarm;
import com.ssafy.muscleloss.model.Feed;
import com.ssafy.muscleloss.model.Like;
import com.ssafy.muscleloss.model.Share;
import com.ssafy.muscleloss.service.AlarmService;
import com.ssafy.muscleloss.service.FeedService;
import com.ssafy.muscleloss.service.ShareService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin("*")
@Controller
@RequestMapping("/api/share")
public class ShareController {

	@Autowired
	private ShareService shareService;

	@Autowired
	private FeedService feedService;

	@Autowired
	private AlarmService alarmService;

	@ApiOperation(value = "공유하기 표시하기", response = String.class)
	@ResponseBody
	@PostMapping("/registershare/{uid}")
	public String registershare(@RequestBody Share share, @PathVariable String uid) {
		String answer;
		int cnt = shareService.registershare(share);
		if (cnt == 1) {
			System.out.println("공유 성공!!");

	            Alarm alarm = new Alarm();
	            String uid_fk_from = share.getUid_fk();
	            String uid_fk_to = uid;
	            alarm.setMessage(uid_fk_from + "님이 당신의 게시물을 공유했습니다.");
	            alarmService.registerAlarm(uid_fk_to, uid_fk_from, alarm.getMessage(), "false");

			answer = "success";
		} else {
			System.out.println("공유 실패!!");
			answer = "fail";
		}
		return answer;
	}

	@ApiOperation(value = "공유하기 취소하기", response = String.class)
	@ResponseBody
	@PostMapping("/deleteshare")
	public String deleteshare(@RequestBody Share share) {
		String answer;
		int cnt = shareService.deleteshare(share);
		if (cnt == 1) {
			System.out.println("공유취소 성공!!");
			answer = "success";
		} else {
			System.out.println("공유취소 실패!!");
			answer = "fail";
		}
		return answer;
	}

	@ApiOperation(value = "공유한 게시물인지 확인하기", response = String.class)
	@ResponseBody
	@PostMapping("/checkshare")
	public String checkshare(@RequestBody Share share) {
		String answer;
		int cnt = shareService.checkshare(share);
		if (cnt >= 1) {
			System.out.println("이미 공유된 게시물!!");
			answer = "success";
		} else {
			System.out.println("아직 되지않았음!!");
			answer = "fail";
		}
		return answer;
	}

	@ApiOperation(value = "공유한 게시물 리스트 보여주기", response = String.class)
	@ResponseBody
	@PostMapping("/feedByShare")
	public List<Feed> feedByShare(@RequestBody Feed feed) { // Feed 리스트를 model에 넣어서 반환한다
		System.out.println(feed);
		List<Feed> list = shareService.feedByShare(feed);
		Collections.reverse(list);
		return list;
	}

}
