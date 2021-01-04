package com.ssafy.muscleloss.controller;

import java.util.Collections;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.ssafy.muscleloss.model.Alarm;
import com.ssafy.muscleloss.service.AlarmService;

import io.swagger.annotations.ApiOperation;


@CrossOrigin("*")
@Controller
@RequestMapping("/api/alarm")
public class AlarmController {

	@Autowired
	private AlarmService alarmService;
	
    @ApiOperation(value = "알람 리스트 보여주기", response = String.class)
	@ResponseBody
	@GetMapping("/listAlarm/{uid}")
	public List<Alarm> listAlarm(@PathVariable String uid) { 
		List<Alarm> list = alarmService.listAlarm(uid); 
		Collections.reverse(list);
		return list;
	}
    
    @ApiOperation(value = "알람 읽은것 삭제하기", response = String.class)
   @ResponseBody
    @PostMapping("/deleteAlarm")
   public String deleteAlarm(@RequestBody Alarm alarm) {
      String answer;
      int cnt = alarmService.deleteAlarm(alarm.getNo());
      if (cnt == 1) {
         System.out.println("알람 삭제 성공!!");
         answer = "success";
      } else {
         System.out.println("알람 삭제 실패!!");
         answer = "fail";
      }
      return answer;
   }
	
	
}
