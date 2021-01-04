package com.ssafy.muscleloss.controller;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Base64;
import java.util.Collections;
import java.util.List;
import java.util.Base64.Encoder;

import org.apache.commons.io.IOUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.ssafy.muscleloss.model.Meet;
import com.ssafy.muscleloss.model.Member;
import com.ssafy.muscleloss.service.MeetService;
import com.ssafy.muscleloss.service.MemberService;

@CrossOrigin("*")
@Controller
@RequestMapping("/api/meet")
public class MeetController {

	@Autowired
	private MeetService meetService;

	@Autowired
	private MemberService memberService;

	@ResponseBody
	@GetMapping("/meetAll")
	public List<Meet> meetAll() {
		List<Meet> list = meetService.meetAll();
		Collections.reverse(list);
		return list;
	}

	@ResponseBody
	@PostMapping("/meetAllByCategory")
	public List<Meet> meetAllByCategory(@RequestBody Meet meet) throws IOException {
		System.out.println(meet);

		List<Meet> list2 = meetService.meetAllByCategory(meet);
		Collections.reverse(list2);

		for (int i = 0; i < list2.size(); i++) {
			// 이미지 작업
			String uid_fk = list2.get(i).getUid_fk();
			Member mem = memberService.search(uid_fk);
			
			if(mem.getAvatarImage().equals("/img/person.9f2af2d1.png")) {
				list2.get(i).setUserimage("/img/person.9f2af2d1.png"); 
			} else {
				InputStream imageStream2 = new FileInputStream(mem.getAvatarImage());
				// InputStream으로 읽어들인 이미지를 ByteArray형태로 변환.
				byte[] imageByteArray2 = IOUtils.toByteArray(imageStream2);
				imageStream2.close();
//				System.out.println(imageByteArray2);
				// Base64형태로 인코딩해주는 encoder 객체를 생성.
				Encoder encoder2 = Base64.getEncoder();
				// 위에서  ByteArray형태로 변환된 이미지를 Base64형태로 인코딩.
				byte[] baseIncodingBytes2 = encoder2.encode(imageByteArray2);
				// Base64형태로 인코딩된 이미지 파일을 String으로 바꿈.
				String base64 = new String(baseIncodingBytes2);
//				System.out.println(base642); // 잘 인코딩 됐는지 확인.
				// imgsrc라는 String 변수에 이미지의 총 src를 전부 작성. 이를 response.data를 읽어들인다면 그 자체로 이미지파일이다.
				
				String imgsrc2 = "data:" + mem.getImgtype() + ";base64," + base64;
				// 이미지 파일의 src를 반환하면 끝.
//				System.out.println(imgsrc2);
				list2.get(i).setUserimage(imgsrc2);
			}
		}

		return list2;
	}

	@ResponseBody
	@PostMapping("/meetSearch")
	public List<Meet> meetSearch(@RequestBody Meet meet) {
		System.out.println(meet);
		List<Meet> list3 = meetService.meetSearch(meet);
		Collections.reverse(list3);
		return list3;
	}

	@ResponseBody
	@PostMapping("/meetregister")
	public String meetregister(@RequestBody Meet meet) {
		System.out.println(meet);
		String answer;
		int cnt = meetService.meetregister(meet);
		if (cnt == 1) {
			System.out.println("등록 성공!!");
			answer = "success";
		} else {
			System.out.println("등록 실패!!");
			answer = "fail";
		}
		return answer;
	}

	@ResponseBody
	@PostMapping("/meetUpdate")
	public int meetUpdate(@RequestBody Meet meet) {
		int isokmeetchange = meetService.meetUpdate(meet);
		if (isokmeetchange != 1) {
			System.out.println("meet 업데이트 실패");
		}
		return isokmeetchange;
	}

	@ResponseBody
	@PostMapping("/meetDelete/{meetNo}")
	public int feedDelete(@PathVariable String meetNo) {
		System.out.println(meetNo);
		int isokmeetdelete = meetService.meetDelete(meetNo);
		if (isokmeetdelete != 1) {
			System.out.println("meet 삭제 실패");
		} else {
			System.out.println("meet 삭제 성공");
		}
		return isokmeetdelete;
	}

}
