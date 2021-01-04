package com.ssafy.muscleloss.controller;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.text.SimpleDateFormat;
import java.util.Base64;
import java.util.Base64.Encoder;
import java.util.Date;

import org.apache.commons.io.IOUtils;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;
import com.ssafy.muscleloss.model.Feed;
import com.ssafy.muscleloss.model.Like;
import com.ssafy.muscleloss.model.Reply;
import com.ssafy.muscleloss.service.LikeService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin("*")
@Controller
@RequestMapping("/api/file")
public class FileController {

//   @Autowired
//   LikeService likeService;
	// 단순히 이미지 파일 받아와서 백엔드로 정보만 출력하는 기능 
	@ResponseBody
	@PostMapping("/fileUpload")
	public String fileUpload(@RequestParam MultipartFile image) throws IOException {
		System.out.println("1. file : " + image);
		System.out.println("2. file의 파라미터 이름 : " + image.getName());
		System.out.println("3. file의 사이즈 : " + image.getSize());
		System.out.println("4. file의 실제이름 : " + image.getOriginalFilename());
		byte[] data = image.getBytes();
		System.out.println("5. file의 실제 내용 : " + data);
		System.out.println("6. file의 타입 : " + image.getContentType());
		String str = "";
		if (image.getName().equals("image") || image.getName().equals("png") || image.getName().equals("jpg")) {
			str = image.getName() + "업로드 성공!";
		}
		return str;
	}

	// 받아온 이미지 파일을 특정 경로에 저장. 경로 반환.
	@PostMapping(value="/profileimgsave", produces = MediaType.IMAGE_JPEG_VALUE)
	public @ResponseBody String profileimgsave(@RequestParam MultipartFile image) throws IOException {
		String str = "";
		String dest3 = "";
		SimpleDateFormat format1 = new SimpleDateFormat("yyyyMMddHHmmss");
		Date time = new Date();
		String time1 = format1.format(time);
//		System.out.println(time1);
		if (image != null && !image.isEmpty()) {
			File dest1 = new File("/home/ubuntu/vue/dist/img/fileupload/");
//			File dest1 = new File("/SSAFY/workspace_vue/frontend/frontend/src/assets/profile/");
			File dest2 = new File("/home/ubuntu/vue/dist/img/fileupload/" + time1 + "_" + image.getOriginalFilename());
//			File dest2 = new File("/SSAFY/workspace_vue/frontend/frontend/src/assets/profile/" + time1 + "_" + image.getOriginalFilename());
			if (dest1.mkdirs()) {
				System.out.println("디렉토리 생성 성공");
			} else {
				System.out.println("디렉토리 생성 실패 또는 기존에 이미 디렉토리가 존재합니다.");
			}
			try {
				System.out.println(dest2.getPath());
				image.transferTo(dest2);
				str = "저장성공";
				System.out.println(str);
				System.out.println("dest2 : " + dest2);
				dest3 = "" + dest2;
				System.out.println(dest3);
			} catch (IllegalStateException e) {
				str = "저장실패";
				System.out.println(str);
				e.printStackTrace();
			} catch (IOException e) {
				str = "저장실패";
				System.out.println(str);
				e.printStackTrace();
			}
		}
		
		// 이미지를 지정한 경로에서 불러와서(이미지가 저장되어있어야함) FileInputStream으로 읽은 후 InputStream으로 저장.
		InputStream imageStream = new FileInputStream("/home/ubuntu/vue/dist/img/fileupload/" + time1 + "_" + image.getOriginalFilename());
		// InputStream으로 읽어들인 이미지를 ByteArray형태로 변환.
		byte[] imageByteArray = IOUtils.toByteArray(imageStream);
		imageStream.close();
		System.out.println(imageByteArray);
		// Base64형태로 인코딩해주는 encoder 객체를 생성.
		Encoder encoder = Base64.getEncoder();
		// 위에서  ByteArray형태로 변환된 이미지를 Base64형태로 인코딩.
		byte[] baseIncodingBytes = encoder.encode(imageByteArray);
//		System.out.println(new String(baseIncodingBytes)); // 잘 인코딩 됐는지 확인.
		// Base64형태로 인코딩된 이미지 파일을 String으로 바꿈.
		String base64 = new String(baseIncodingBytes);
		// imgsrc라는 String 변수에 이미지의 총 src를 전부 작성. 이를 response.data를 읽어들인다면 그 자체로 이미지파일이다.
		String imgsrc = "data:" + image.getContentType() + ";base64," + base64;
		// 이미지 파일의 src를 반환하면 끝.
//		System.out.println(imgsrc);
		
		//그러나 이 단계에선 img파일의 전체src는 상당히 길다. DB저장 axios를 보내기 위해 지금은 이미지 저장 경로만 보낸다.
		return (dest3);
	}

	// 피드에서 사용자가 업로드한 이미지를 가져와 지정된 폴더에 저장하고, 경로를 반환.
		@PostMapping(value="/feedimgsave", produces = MediaType.IMAGE_JPEG_VALUE)
		public @ResponseBody String feedimgsave(@RequestParam MultipartFile image) throws IOException {
			String str = "";
			String dest3 = "";
			SimpleDateFormat format1 = new SimpleDateFormat("yyyyMMddHHmmss");
			Date time = new Date();
			String time1 = format1.format(time);
//			System.out.println(time1);
			if (image != null && !image.isEmpty()) {
				File dest1 = new File("/home/ubuntu/vue/dist/img/feedupload/");
				File dest2 = new File("/home/ubuntu/vue/dist/img/feedupload/" + time1 + "_" + image.getOriginalFilename());
				if (dest1.mkdirs()) {
					System.out.println("디렉토리 생성 성공");
				} else {
					System.out.println("디렉토리 생성 실패 또는 기존에 이미 디렉토리가 존재합니다.");
				}
				try {
					image.transferTo(dest2);
					str = "저장성공";
					System.out.println(str);
					System.out.println("dest2 : " + dest2);
					dest3 = "" + dest2;
					System.out.println(dest3);
				} catch (IllegalStateException e) {
					str = "저장실패";
					System.out.println(str);
					e.printStackTrace();
				} catch (IOException e) {
					str = "저장실패";
					System.out.println(str);
					e.printStackTrace();
				}
			}	
			
			return (dest3);
		}
	
}