package com.ssafy.muscleloss.controller;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.muscleloss.model.Alarm;
import com.ssafy.muscleloss.model.Reply;
import com.ssafy.muscleloss.service.AlarmService;
import com.ssafy.muscleloss.service.ReplyService;
import com.ssafy.muscleloss.controller.ReplyController;

import io.swagger.annotations.ApiOperation;

@CrossOrigin("*")
@Controller
@RequestMapping("/api/reply")
public class ReplyController {

	private static final Logger logger = LoggerFactory.getLogger(ReplyController.class);
	private static final String SUCCESS = "success";
	private static final String FAIL = "fail";

	@Autowired
	private ReplyService replyService;

	@Autowired
	private AlarmService alarmService;

	@ApiOperation(value = "답글 정보를 보여준다. 그리고 DB입력 성공여부에 따라 'success' 또는 'fail' 문자열을 반환한다.", response = List.class)
	@ResponseBody
	@PostMapping("/listReply/{feedNo}")
	public List<Reply> listReply(@RequestBody Reply reply) {
		List<Reply> list = replyService.listReply(reply.getFeedNo_fk());
		return list;
	}

	@ApiOperation(value = "새로운 답글 정보를 입력한다. 그리고 DB입력 성공여부에 따라 'success' 또는 'fail' 문자열을 반환한다.", response = String.class)
	@ResponseBody
	@PostMapping("/insertReply/{uid}")
	public String insertReply(@RequestBody Reply reply, @PathVariable String uid) {
		System.out.println(reply);
		String answer;
		int cnt = replyService.insertReply(reply);
		if (cnt == 1) {
			System.out.println("답글달기 성공!!");

			Alarm alarm = new Alarm();
			String uid_fk_from = reply.getUid_fk();
			String uid_fk_to = uid;
			alarm.setMessage(uid_fk_from + "님이 댓글을 달았습니다.");
			alarmService.registerAlarm(uid_fk_to, uid_fk_from, alarm.getMessage(), "false");

			answer = "success";
		} else {
			System.out.println("답글달기 실패!!");
			answer = "fail";
		}
		return answer;
	}

	@ApiOperation(value = "글번호에 해당하는 답글의 정보를 수정한다. 그리고 DB수정 성공여부에 따라 'success' 또는 'fail' 문자열을 반환한다.", response = String.class)
	@ResponseBody
	@PutMapping("updateReply/{rNo}")
	public int updateReply(@RequestBody Reply reply, @PathVariable int rno) {
		int answer = replyService.updateReply(reply);
		if (answer == 1) {
		}
		return answer;
	}

	@ApiOperation(value = "글번호에 해당하는 답글의 정보를 삭제한다. 그리고 DB삭제 성공여부에 따라 'success' 또는 'fail' 문자열을 반환한다.", response = String.class)
	@ResponseBody
	@PostMapping("deleteReply/{rNo}")
	public String deleteReply(@PathVariable int rNo) {
		System.out.println(rNo);
		String answer;
		int cnt = replyService.deleteReply(rNo);
		if (cnt == 1) {
			System.out.println("답글삭제 성공!!");
			answer = "success";
		} else {
			System.out.println("답글삭제 실패!!");
			answer = "fail";
		}
		return answer;
	}

}
