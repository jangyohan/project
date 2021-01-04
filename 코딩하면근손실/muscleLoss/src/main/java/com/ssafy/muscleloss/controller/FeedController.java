package com.ssafy.muscleloss.controller;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.util.Base64;
import java.util.Collections;
import java.util.HashMap;
import java.util.List; 
import java.util.Base64.Encoder; 

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
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

import com.mysql.cj.xdevapi.Collection;
import com.ssafy.muscleloss.model.Alarm;
import com.ssafy.muscleloss.model.Feed;
import com.ssafy.muscleloss.model.Member;
import com.ssafy.muscleloss.service.AlarmService;
import com.ssafy.muscleloss.service.FeedService;

import io.fusionauth.jwt.Signer;
import io.fusionauth.jwt.Verifier;
import io.fusionauth.jwt.domain.JWT;
import io.fusionauth.jwt.hmac.HMACSigner;
import io.fusionauth.jwt.hmac.HMACVerifier;

import org.apache.commons.io.IOUtils;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import com.ssafy.muscleloss.service.KakaoAPI;
import com.ssafy.muscleloss.service.MemberService;


@CrossOrigin("*")
@Controller
@RequestMapping("/api/feed")
public class FeedController {

	@Autowired
	private FeedService feedService;
	
	@Autowired
	private AlarmService alarmService;
	
	@Autowired
	private MemberService memberService;

	@ResponseBody
	@GetMapping("/feedAll")
	public List<Feed> feedAll() { // Feed 리스트를 model에 넣어서 반환한다
		List<Feed> list = feedService.feedAll();
		Collections.reverse(list);
		
//		list.get(1).setUid_fk("테스트해볼게요");
//		for(int i = 0; i < list.size(); i++) {
//			System.out.println(list.get(i).getFeedNo() + " / " + list.get(i).getUid_fk());
//		}
		
		return list;
	}

	@ResponseBody
	@PostMapping("/feedAllByUser")
	public List<Feed> feedAllByUser(@RequestBody Feed feed) { // Feed 리스트를 model에 넣어서 반환한다
		System.out.println(feed); 
		List<Feed> list2 = feedService.feedAllByUser(feed);
		Collections.reverse(list2);
		return list2;
	}
	
	@ResponseBody
	@PostMapping("/feedTagSearch")
	public List<Feed> feedTagSearch(@RequestBody Feed feed) { // Feed 리스트를 model에 넣어서 반환한다
		System.out.println(feed); 
		List<Feed> list3 = feedService.feedTagSearch(feed); 
		Collections.reverse(list3);
		return list3;
	}
	
	@ResponseBody
	@PostMapping("/feedregister")
	public String feedregister(@RequestBody Feed feed) throws IOException {
		System.out.println(feed); // 잘 받아왔는지 확인.
		
		
		// 이미지를 지정한 경로에서 불러와서(이미지가 저장되어있어야함) FileInputStream으로 읽은 후 InputStream으로 저장.
		InputStream imageStream = new FileInputStream(feed.getFileName());
		// InputStream으로 읽어들인 이미지를 ByteArray형태로 변환.
		byte[] imageByteArray = IOUtils.toByteArray(imageStream);
		imageStream.close();
		System.out.println(imageByteArray);
		// Base64형태로 인코딩해주는 encoder 객체를 생성.
		Encoder encoder = Base64.getEncoder();
		// 위에서  ByteArray형태로 변환된 이미지를 Base64형태로 인코딩.
		byte[] baseIncodingBytes = encoder.encode(imageByteArray);
		// Base64형태로 인코딩된 이미지 파일을 String으로 바꿈.
		String base64 = new String(baseIncodingBytes);
		System.out.println(base64); // 잘 인코딩 됐는지 확인.
		// imgsrc라는 String 변수에 이미지의 총 src를 전부 작성. 이를 response.data를 읽어들인다면 그 자체로 이미지파일이다.
//		String imgsrc = "data:" + image.getContentType() + ";base64," + base64;
		// 이미지 파일의 src를 반환하면 끝. 위에서 src 전체 문장 만드는건 profile.vue에서 하자.
//		System.out.println(imgsrc);
		
		String answer;
		int cnt = feedService.feedregister(feed);
		if (cnt == 1) {
			System.out.println("피드 등록 성공!!");
//			alarmfunction.FeedAlarm(feed.getUid_fk());
			
//			 	Alarm alarm = new Alarm();
//	            String uid_fk_to = feed.getUid_fk();
//	            String uid_fk_from = uid;
//	            alarm.setMessage(uid_fk_from + "님이 피드를 올렸습니다.");
//	            alarmService.registerAlarm(uid_fk_to, uid_fk_from, alarm.getMessage(), "false");
	            
			answer = "success";
		} else {
			System.out.println("피드 등록 실패!!");
			answer = "fail";
		}
		return base64;
	}
	
	@ResponseBody
	@PostMapping("/getfeedimage")
	public ResponseEntity<JSONObject> getfeedimage(@RequestBody Feed feed) throws IOException {
		System.out.println(feed); // 잘 받아왔는지 확인.
		JSONObject jsonObject = new JSONObject();
		Feed realfeed = feedService.getfeedimage(feed);
		Member mem = memberService.search(realfeed.getUid_fk());
		if(realfeed.getFileName().equals(feed.getFileName())) {
			System.out.println("받아온 이미지 경로와 실제 존재하는 데이터베이스의 이미지 경로가 일치합니다. 작업을 계속합니다.");
		} else {
			System.out.println("받아온 이미지 경로와 실제 존재하는 데이터베이스의 이미지 경로가 일치하지않습니다.");
			System.out.println("받아온 이미지 feed.getFileName() : " + feed.getFileName());
			System.out.println("실제 DB이미지 realfeed.getFileName() : " + realfeed.getFileName());
		}
		// 이미지를 지정한 경로에서 불러와서(이미지가 저장되어있어야함) FileInputStream으로 읽은 후 InputStream으로 저장.
		InputStream imageStream = new FileInputStream(realfeed.getFileName());
		// InputStream으로 읽어들인 이미지를 ByteArray형태로 변환.
		byte[] imageByteArray = IOUtils.toByteArray(imageStream);
		imageStream.close();
		System.out.println(imageByteArray);
		// Base64형태로 인코딩해주는 encoder 객체를 생성.
		Encoder encoder = Base64.getEncoder();
		// 위에서  ByteArray형태로 변환된 이미지를 Base64형태로 인코딩.
		byte[] baseIncodingBytes = encoder.encode(imageByteArray);
		// Base64형태로 인코딩된 이미지 파일을 String으로 바꿈.
		String base64 = new String(baseIncodingBytes);
//		System.out.println(base64); // 잘 인코딩 됐는지 확인.
		// imgsrc라는 String 변수에 이미지의 총 src를 전부 작성. 이를 response.data를 읽어들인다면 그 자체로 이미지파일이다.
		String imgsrc = "data:" + realfeed.getImgtype() + ";base64," + base64;
		// 이미지 파일의 src를 반환하면 끝.
//		System.out.println(imgsrc);
		jsonObject.put("fileName", imgsrc);
		
		if(mem.getAvatarImage().equals("/img/person.9f2af2d1.png")) {
			jsonObject.put("userimage", "/img/person.9f2af2d1.png");
		} else {
			InputStream imageStream2 = new FileInputStream(mem.getAvatarImage());
			// InputStream으로 읽어들인 이미지를 ByteArray형태로 변환.
			byte[] imageByteArray2 = IOUtils.toByteArray(imageStream2);
			imageStream2.close();
			System.out.println(imageByteArray2);
			// Base64형태로 인코딩해주는 encoder 객체를 생성.
			Encoder encoder2 = Base64.getEncoder();
			// 위에서  ByteArray형태로 변환된 이미지를 Base64형태로 인코딩.
			byte[] baseIncodingBytes2 = encoder2.encode(imageByteArray2);
			// Base64형태로 인코딩된 이미지 파일을 String으로 바꿈.
			String base642 = new String(baseIncodingBytes2);
//			System.out.println(base642); // 잘 인코딩 됐는지 확인.
			// imgsrc라는 String 변수에 이미지의 총 src를 전부 작성. 이를 response.data를 읽어들인다면 그 자체로 이미지파일이다.
			
			String imgsrc2 = "data:" + mem.getImgtype() + ";base64," + base642;
			// 이미지 파일의 src를 반환하면 끝.
//			System.out.println(imgsrc2);
			jsonObject.put("userimage", imgsrc2);
		}
		String jsonStr = jsonObject.toJSONString();
//		System.out.println(jsonStr);
		
		return new ResponseEntity<JSONObject>(jsonObject, HttpStatus.OK);
	}
	 
	@ResponseBody
	@PostMapping("/feedUpate")
	public int feedUpate(@RequestBody Feed feed) {
		int isokfeedchange = feedService.feedUpate(feed);
		if (isokfeedchange != 1) {			
			System.out.println("password 업데이트 실패");
		}
		return isokfeedchange;
	}

	@ResponseBody
	@PostMapping("/feedDelete/{feedNo}")
	public int feedDelete(@PathVariable String feedNo) {
		// feed의 feedNo만 받아옴.
		System.out.println(feedNo);
		
		int isokfeeddelete = feedService.feedDelete(feedNo);
		if (isokfeeddelete != 1) {			
			System.out.println("feed 삭제 실패");
		} else {
			System.out.println("feed 삭제 성공");
		}
		return isokfeeddelete;
	}
	
	
}