package com.ssafy.muscleloss.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.ssafy.muscleloss.model.Alarm;
import com.ssafy.muscleloss.model.Like;
import com.ssafy.muscleloss.model.Reply;
import com.ssafy.muscleloss.service.AlarmService;
import com.ssafy.muscleloss.service.LikeService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = { "*" })@Controller
@RequestMapping("/api/like")
public class LikeController {

	@Autowired
	LikeService likeService;

	@Autowired
	private AlarmService alarmService;

	@ApiOperation(value = "좋아요 표시하기", response = String.class)
	@ResponseBody
	@PostMapping("/updatelike/{uid}")
	public String updatelike(@RequestBody Like like, @PathVariable String uid) {
		String answer;
		int cnt = likeService.updatelike(like);
		if (cnt == 1) {
			System.out.println("좋아요 성공!!");
			System.out.println(uid);

			Alarm alarm = new Alarm();
			String uid_fk_to = uid;
			String uid_fk_from = like.getUid_fk();
			alarm.setMessage(uid_fk_from + "님이 좋아요를 눌렀습니다.");
			alarmService.registerAlarm(uid_fk_to, uid_fk_from, alarm.getMessage(), "false");

			answer = "success";
		} else {
			System.out.println("좋아요 실패!!");
			answer = "fail";
		}
		return answer;
	}

	@ApiOperation(value = "좋아요 취소하기", response = String.class)
	@ResponseBody
	@PostMapping("/deletelike")
	public String deletelike(@RequestBody Like like) {
		String answer;
		int cnt = likeService.deletelike(like);
		if (cnt == 1) {
			System.out.println("좋아요취소 성공!!");
			answer = "success";
		} else {
			System.out.println("좋아요취소 실패!!");
			answer = "fail";
		}
		return answer;
	}

	@ApiOperation(value = "좋아요한 게시물인지 확인하기", response = String.class)
	@ResponseBody
	@PostMapping("/checklike")
	public String checklike(@RequestBody Like like) {
		String answer;
		int cnt = likeService.checklike(like);
		if (cnt >= 1) {
			System.out.println("이미 좋아요!!");
			answer = "success";
		} else {
			System.out.println("아직 좋아요 아님!!");
			answer = "fail";
		}
		return answer;
	}

	@ApiOperation(value = "좋아요 수 구하기", response = String.class)
	@ResponseBody
	@GetMapping("/countlike/{feedno}")
	public int countlike(@PathVariable int feedno) {
		int cnt = likeService.countlike(feedno);
		return cnt;
	}

}