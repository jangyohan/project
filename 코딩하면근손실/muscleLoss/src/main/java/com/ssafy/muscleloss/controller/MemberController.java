package com.ssafy.muscleloss.controller;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.util.Base64;
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

import com.ssafy.muscleloss.model.Member;
import com.ssafy.muscleloss.service.MemberService;

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

@CrossOrigin("*")
@Controller
@RequestMapping("/api/member")
public class MemberController {
	
	@Autowired
	private MemberService memberService;
	
	@Autowired
    private KakaoAPI kakao;

	@ResponseBody
	@GetMapping("/userlist")	
	public List<Member> searchAll() { // Member 리스트를 model에 넣어서 반환한다
		List<Member> list = memberService.searchAll();
//		model.addAttribute("members", list);
		return list;
	}

	@ResponseBody
	@GetMapping("/{userid}")
	public Member mypage(@PathVariable String userid) throws IOException {
//		Member mem = (Member) session.getAttribute("userinfo");
//		model.addAttribute("member", mem);
		Member member = memberService.search(userid);
		if(member.getAvatarImage().equals("/img/person.9f2af2d1.png")) {
			member.setAvatarImage("/img/person.9f2af2d1.png");
		} else {
			// 이미지를 지정한 경로에서 불러와서(이미지가 저장되어있어야함) FileInputStream으로 읽은 후 InputStream으로 저장.
			InputStream imageStream = new FileInputStream(member.getAvatarImage());
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
			String imgsrc = "data:" + member.getImgtype() + ";base64," + base64;
			// 이미지 파일의 src를 반환하면 끝.
//			System.out.println(imgsrc);
			member.setAvatarImage(imgsrc);
		} 

		return member; 
	}

	@ResponseBody
	@PostMapping("/findPwd")
	public Member findPwd(@RequestBody Member email) {
		Member user = memberService.findPwd(email);
		if (user == null) {			
			System.out.println("userpwd가 null입니다.");
		}
		return user;
	}	
	
	@ResponseBody
	@PostMapping("/login")
	public ResponseEntity<JSONObject> login(@RequestBody Member member) throws IOException {
		// updated!!
		String uid = null;
		String email = null;
		String avatarImage = null;
		String usercomment = null;
		String token = null;		
		JSONObject jsonObject = new JSONObject();
		System.out.println("전달받은 데이터:" + member.toString());
		Member loginDto = memberService.login(member);		
		if (loginDto == null) {
			System.out.println("로그인 실패: " + loginDto);
			jsonObject = null;
		} else {
			uid = loginDto.getUid();
			email = loginDto.getEmail();
			avatarImage = loginDto.getAvatarImage();
			usercomment = loginDto.getUsercomment();
//			session.setAttribute("userinfo", loginDto);
			System.out.println("로그인 성공 : " + loginDto);
			Signer signer = HMACSigner.newSHA256Signer("too many secrets");
			System.out.println(signer);
			// Build a new JWT with an issuer(iss), issued at(iat), subject(sub) and expiration(exp)
			JWT jwt = new JWT().setIssuer("www.acme.com")
			                   .setIssuedAt(ZonedDateTime.now(ZoneOffset.UTC))
//			                   .setSubject("f1e33ab3-027f-47c5-bb07-8dd8ab37a2d3")
			                   .setSubject(email)
			                   .setExpiration(ZonedDateTime.now(ZoneOffset.UTC).plusMinutes(30));
			System.out.println(jwt);
			// Sign and encode the JWT to a JSON string representation
			String encodedJWT = JWT.getEncoder().encode(jwt, signer);
			System.out.println(encodedJWT);
			token = encodedJWT;	
			jsonObject.put("uid", uid);
			jsonObject.put("email", email);
			if(avatarImage.equals("/img/person.9f2af2d1.png")) {
				jsonObject.put("avatarImage", avatarImage);
			} else {
				// avatarImage 작업코드
				jsonObject.put("avatarImageSrc", avatarImage);
				// 이미지를 지정한 경로에서 불러와서(이미지가 저장되어있어야함) FileInputStream으로 읽은 후 InputStream으로 저장.
				InputStream imageStream = new FileInputStream(avatarImage);
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
				//imgsrc라는 String 변수에 이미지의 총 src를 전부 작성. 이를 response.data를 읽어들인다면 그 자체로 이미지파일이다.
				String imgsrc = "data:" + loginDto.getImgtype() + ";base64," + base64;
				// 이미지 파일의 src를 반환하면 끝.
//				System.out.println(imgsrc);
				jsonObject.put("avatarImage", imgsrc);
			}
			jsonObject.put("usercomment", usercomment);
			jsonObject.put("token", token);
			String jsonStr = jsonObject.toJSONString();
			System.out.println(jsonStr);
		}
		return new ResponseEntity<JSONObject>(jsonObject, HttpStatus.OK);	
	}
//	@ResponseBody
//	@RequestMapping("/login")
//	public String login(@RequestParam("code") String code, HttpSession session) {
//	    String access_Token = kakao.getAccessToken(code);
//	    HashMap<String, Object> userInfo = kakao.getUserInfo(access_Token);
//	    System.out.println("login Controller : " + userInfo);
//	    
//	    //    클라이언트의 이메일이 존재할 때 세션에 해당 이메일과 토큰 등록
//	    if (userInfo.get("email") != null) {
//	        session.setAttribute("userId", userInfo.get("email"));
//	        session.setAttribute("access_Token", access_Token);
//	    }
//	    return "index";
//	}

	
	@ResponseBody
	@PostMapping("/signUp")
	public String signUp(@RequestBody Member member) {
		System.out.println(member);
		
		String answer;
		int cnt = memberService.signUp(member);
		
		
		if (cnt == 1) {
			System.out.println("회원 가입 성공!!");
			answer = "success";
		} else {
			System.out.println("회원 가입 실패!!");
			answer = "fail";
		}
		//////////////////////////////
		return answer;
	}
	
	@ResponseBody
	@PostMapping("/checkSession")
	public boolean checkSession(@RequestBody Member member) {
		System.out.println(member);
		boolean answer;
		String encodedJWT = member.getUsertoken();
		System.out.println(encodedJWT);
		// Build an HMC verifier using the same secret that was used to sign the JWT
		Verifier verifier = HMACVerifier.newVerifier("too many secrets");

		// Verify and decode the encoded string JWT to a rich object
		JWT jwt = JWT.getDecoder().decode(encodedJWT, verifier);

		// Assert the subject of the JWT is as expected
//		assertEquals(jwt.subject, "f1e33ab3-027f-47c5-bb07-8dd8ab37a2d3");
		System.out.println(jwt.subject);
		System.out.println(member.getUid());
//		if(jwt.subject=="f1e33ab3-027f-47c5-bb07-8dd8ab37a2d3") {
		if(jwt.subject.equals(member.getUid())) {
			System.out.println("세션 인증 성공!!");
			answer = true;
		} else {
			System.out.println("세션 인증 실패!!");
			answer = false;
		}
		return answer;
	}

	@ResponseBody
	@PostMapping("/makeSession")
	public String makeSession(@RequestBody Member member) {
		System.out.println(member);
		Signer signer = HMACSigner.newSHA256Signer("too many secrets");
		System.out.println(signer);
		// Build a new JWT with an issuer(iss), issued at(iat), subject(sub) and expiration(exp)
		JWT jwt = new JWT().setIssuer("www.acme.com")
		                   .setIssuedAt(ZonedDateTime.now(ZoneOffset.UTC))
//		                   .setSubject("f1e33ab3-027f-47c5-bb07-8dd8ab37a2d3")
		                   .setSubject(member.getEmail())
		                   .setExpiration(ZonedDateTime.now(ZoneOffset.UTC).plusMinutes(30));
		System.out.println(jwt);
		// Sign and encode the JWT to a JSON string representation
		String encodedJWT = JWT.getEncoder().encode(jwt, signer);
		System.out.println(encodedJWT);
		return encodedJWT;
	}
	
	@ResponseBody
	@PutMapping(value = "/", consumes = "application/json")
	public int updateMem(@RequestBody Member member) {
		int num = memberService.updateMem(member);
		if (num == 1) { // 업데이트 성공
//			session.setAttribute("userinfo", member);
		}
		return num;
	}

	@ResponseBody
	@PostMapping("/updateMemPw")
	public int updateMemPw(@RequestBody Member member) {
		int isokpwchange = memberService.updateMemPw(member);
		if(isokpwchange == 1) {
			System.out.println("password 업데이트 성공");
		}
		if (isokpwchange != 1) {			
			System.out.println("password 업데이트 실패");
		}
		return isokpwchange;
	}
	
	@ResponseBody
	@PostMapping("/modifypw")
	public int modifypw(@RequestBody Member member) {
		int okpw = 0;
		Member oklogin = memberService.login(member);
		System.out.println(oklogin);
		if(oklogin != null) {
			okpw = 1;
		}
		if(oklogin == null) {
			System.out.println("oklogin.getPassword()가 null입니다.");
		}
		if(okpw == 1) {
			System.out.println("CurrentPassword 확인 완료.");
		}
		if (okpw != 1) {			
			System.out.println("CurrentPassword가 틀립니다.");
		}
		return okpw;
	}
	
	@ResponseBody
	@PostMapping("/modifyPW")
	public int modifyPW(@RequestBody Member member) {
		int isokpwchange = memberService.updateMemPw(member);
		if(isokpwchange == 1) {
			System.out.println("password 업데이트 성공");
		}
		if (isokpwchange != 1) {			
			System.out.println("password 업데이트 실패");
		}
		return isokpwchange;
	}
	
	@ResponseBody
	@PostMapping("/updateComment")
	public int updateComment(@RequestBody Member member) {
		int isokcommentchange = memberService.updateComment(member);
		if(isokcommentchange == 1) {
			System.out.println("comment 업데이트 성공");
		}
		if (isokcommentchange != 1) {			
			System.out.println("comment 업데이트 실패");
		}
		return isokcommentchange;
	}
	
	@ResponseBody
	@PostMapping("/updateProfile")
	public String updateProfile(@RequestBody Member member) throws IOException {
		System.out.println("member.getAvatarImage() : " + member.getAvatarImage()); // 잘 받아왔는지 확인.
		
		// 이미지를 지정한 경로에서 불러와서(이미지가 저장되어있어야함) FileInputStream으로 읽은 후 InputStream으로 저장.
		InputStream imageStream = new FileInputStream(member.getAvatarImage());
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
		
		int isokupdateProfile = memberService.updateProfile(member);
		if(isokupdateProfile == 1) {
			System.out.println("Profile 업데이트 성공");
		}
		if (isokupdateProfile != 1) {			
			System.out.println("Profile 업데이트 실패");
		}
		return base64;
	}
	
	@ResponseBody
	@PostMapping("/{userid}")
	public String deleteMem(@PathVariable String userid) {
		int num = memberService.deleteMem(userid);
		String answer;
		if (num == 0) {
			answer = "fail";
			System.out.println("삭제실패");
		} else {
			answer = "success";
			System.out.println("삭제성공");
		}
//		session.invalidate();
		return answer;
	}

}
// 확인