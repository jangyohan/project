package com.ssafy.muscleloss.controller;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.text.SimpleDateFormat;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.util.Base64;
import java.util.Collections;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Base64.Encoder;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
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
import org.springframework.web.multipart.MultipartFile;

import com.mysql.cj.xdevapi.Collection;
import com.ssafy.muscleloss.model.Alarm;
import com.ssafy.muscleloss.model.Feed;
import com.ssafy.muscleloss.model.Member;
import com.ssafy.muscleloss.model.Gallery;
import com.ssafy.muscleloss.service.AlarmService;
import com.ssafy.muscleloss.service.FeedService;
import com.ssafy.muscleloss.service.GalleryService;

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
@RequestMapping("/api/gallery")
public class GalleryController {

   @Autowired
   private GalleryService galleryService;

   @Autowired
   private MemberService memberService;

   @ResponseBody
   @PostMapping("/galleryAllByUserToday")
   public List<Gallery> galleryAllByUserToday(@RequestBody Gallery gallery) throws IOException, Exception {
      System.out.println(gallery); // 잘 받아왔는지 확인
      List<Gallery> list = galleryService.galleryAllByUser(gallery);
      Collections.reverse(list);
      
      // 날짜 작업
      for (int i = 0; i < list.size(); i++) {
         SimpleDateFormat format1 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
         Date now = new Date();

         String start = list.get(i).getRegdate();
         Date reg = format1.parse(start);

         long diff = now.getTime() - reg.getTime();
         System.out.println(list.get(i).getImageNo() + "번째 : " + diff);
         long min = diff / 60000;
//         System.out.println(min);

         // 만약 현재시간과 갤러리이미지 등록시간과의 차이가 24시간, 1시간은 60분. 즉 하루 이상 차이난다면 리스트에서 제거. 출력안할꺼임.
         if (min > (24 * 60)) {
            list.remove(i);
            i-=1;
         }
      }

      // 이미지 작업
      for (int i = 0; i < list.size(); i++) {
         System.out.println(list.get(i).getImageNo());
         String imgsrc = list.get(i).getImagesrc();
         // 이미지를 지정한 경로에서 불러와서(이미지가 저장되어있어야함) FileInputStream으로 읽은 후 InputStream으로 저장.
         InputStream imageStream = new FileInputStream(imgsrc);
         // InputStream으로 읽어들인 이미지를 ByteArray형태로 변환.
         byte[] imageByteArray = IOUtils.toByteArray(imageStream);
         imageStream.close();
         System.out.println(imageByteArray);
         // Base64형태로 인코딩해주는 encoder 객체를 생성.
         Encoder encoder = Base64.getEncoder();
         // 위에서 ByteArray형태로 변환된 이미지를 Base64형태로 인코딩.
         byte[] baseIncodingBytes = encoder.encode(imageByteArray);
         // Base64형태로 인코딩된 이미지 파일을 String으로 바꿈.
         String base64 = new String(baseIncodingBytes);
//            System.out.println(base64); // 잘 인코딩 됐는지 확인.
         // imgsrc라는 String 변수에 이미지의 총 src를 전부 작성. 이를 response.data를 읽어들인다면 그 자체로
         // 이미지파일이다.
         imgsrc = "data:" + list.get(i).getImgtype() + ";base64," + base64;
         list.get(i).setImagesrc(imgsrc);
      }
      return list;
   }

   @ResponseBody
   @PostMapping("/galleryAllByUserWeek")
   public List<Gallery> galleryAllByUserWeek(@RequestBody Gallery gallery) throws IOException, Exception {
      System.out.println(gallery); // 잘 받아왔는지 확인
      List<Gallery> list = galleryService.galleryAllByUser(gallery);
      Collections.reverse(list);

      // 날짜 작업
      for (int i = 0; i < list.size(); i++) {
         SimpleDateFormat format1 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
         Date now = new Date();

         String start = list.get(i).getRegdate();
         Date reg = format1.parse(start);

         long diff = now.getTime() - reg.getTime();
         long min = diff / 60000;
//               System.out.println(min);

         // 만약 현재시간과 갤러리이미지 등록시간과의 차이가 24시간, 1시간은 60분.에 곱하기 7. 즉 일주일 이상 차이난다면 리스트에서 제거. 출력안할꺼임.
         if (min > (24 * 60 * 7)) {
            list.remove(i);
            i-=1;
         }
      }

      // 이미지 작업
      for (int i = 0; i < list.size(); i++) {
         String imgsrc = list.get(i).getImagesrc();
         // 이미지를 지정한 경로에서 불러와서(이미지가 저장되어있어야함) FileInputStream으로 읽은 후 InputStream으로 저장.
         InputStream imageStream = new FileInputStream(imgsrc);
         // InputStream으로 읽어들인 이미지를 ByteArray형태로 변환.
         byte[] imageByteArray = IOUtils.toByteArray(imageStream);
         imageStream.close();
         System.out.println(imageByteArray);
         // Base64형태로 인코딩해주는 encoder 객체를 생성.
         Encoder encoder = Base64.getEncoder();
         // 위에서 ByteArray형태로 변환된 이미지를 Base64형태로 인코딩.
         byte[] baseIncodingBytes = encoder.encode(imageByteArray);
         // Base64형태로 인코딩된 이미지 파일을 String으로 바꿈.
         String base64 = new String(baseIncodingBytes);
//            System.out.println(base64); // 잘 인코딩 됐는지 확인.
         // imgsrc라는 String 변수에 이미지의 총 src를 전부 작성. 이를 response.data를 읽어들인다면 그 자체로
         // 이미지파일이다.
         imgsrc = "data:" + list.get(i).getImgtype() + ";base64," + base64;
         list.get(i).setImagesrc(imgsrc);
      }
      return list;
   }

   @ResponseBody
   @PostMapping("/galleryAllByUserMonth")
   public List<Gallery> galleryAllByUserMonth(@RequestBody Gallery gallery) throws IOException, Exception {
      System.out.println(gallery); // 잘 받아왔는지 확인
      List<Gallery> list = galleryService.galleryAllByUser(gallery);
      Collections.reverse(list);

      // 날짜 작업
      for (int i = 0; i < list.size(); i++) {
         SimpleDateFormat format1 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
         Date now = new Date();

         String start = list.get(i).getRegdate();
         Date reg = format1.parse(start);

         long diff = now.getTime() - reg.getTime();
         long min = diff / 60000;
//               System.out.println(min);

         // 만약 현재시간과 갤러리이미지 등록시간과의 차이가 24시간, 1시간은 60분.에 곱하기 7*30. 즉 한 달 이상 차이난다면 리스트에서 제거. 출력안할꺼임.
         if (min > (24 * 60 * 7 * 30)) {
            list.remove(i);
            i-=1;
         }
      }

      // 이미지 작업
      for (int i = 0; i < list.size(); i++) {
         String imgsrc = list.get(i).getImagesrc();
         // 이미지를 지정한 경로에서 불러와서(이미지가 저장되어있어야함) FileInputStream으로 읽은 후 InputStream으로 저장.
         InputStream imageStream = new FileInputStream(imgsrc);
         // InputStream으로 읽어들인 이미지를 ByteArray형태로 변환.
         byte[] imageByteArray = IOUtils.toByteArray(imageStream);
         imageStream.close();
         System.out.println(imageByteArray);
         // Base64형태로 인코딩해주는 encoder 객체를 생성.
         Encoder encoder = Base64.getEncoder();
         // 위에서 ByteArray형태로 변환된 이미지를 Base64형태로 인코딩.
         byte[] baseIncodingBytes = encoder.encode(imageByteArray);
         // Base64형태로 인코딩된 이미지 파일을 String으로 바꿈.
         String base64 = new String(baseIncodingBytes);
//            System.out.println(base64); // 잘 인코딩 됐는지 확인.
         // imgsrc라는 String 변수에 이미지의 총 src를 전부 작성. 이를 response.data를 읽어들인다면 그 자체로
         // 이미지파일이다.
         imgsrc = "data:" + list.get(i).getImgtype() + ";base64," + base64;
         list.get(i).setImagesrc(imgsrc);
      }
      return list;
   }

   @PostMapping(value = "/gallerysave", produces = MediaType.IMAGE_JPEG_VALUE)
   public @ResponseBody String gallerysave(@RequestParam MultipartFile image) throws IOException {
      String str = "";
      String dest3 = "";
      SimpleDateFormat format1 = new SimpleDateFormat("yyyyMMddHHmmss");
      Date time = new Date();
      String time1 = format1.format(time);
//      System.out.println(time1);
      if (image != null && !image.isEmpty()) {
         File dest1 = new File("/home/ubuntu/vue/dist/img/galleryupload/");
         File dest2 = new File("/home/ubuntu/vue/dist/img/galleryupload/" + time1 + "_" + image.getOriginalFilename());
         if (dest1.mkdirs()) {
            System.out.println("디렉토리 생성 성공");
         } else {
            System.out.println("디렉토리 생성 실패 또는 기존에 이미 디렉토리가 존재합니다.");
         }
         try {
            image.transferTo(dest2);
            str = "갤러리 저장성공";
            System.out.println(str);
            System.out.println("dest2 : " + dest2);
            dest3 = "" + dest2;
            System.out.println("dest3 : " + dest3);
         } catch (IllegalStateException e) {
            str = "갤러리 저장실패";
            System.out.println(str);
            e.printStackTrace();
         } catch (IOException e) {
            str = "갤러리 저장실패";
            System.out.println(str);
            e.printStackTrace();
         }
      }
      return (dest3);
   }

   // DB에 갤러리 이미지 저장.
   @ResponseBody
   @PostMapping("/galleryregister")
   public String galleryregister(@RequestBody Gallery gallery) throws IOException {
      System.out.println(gallery); // 잘 받아왔는지 확인.

      String answer;
      int cnt = galleryService.galleryregister(gallery);
      if (cnt == 1) {
         System.out.println("갤러리 이미지 DB에 등록 성공!!");
         answer = "success";
      } else {
         System.out.println("갤러리 이미지 DB에 등록 실패!!");
         answer = "fail";
      }
      return answer;
   }

   @ResponseBody
   @PostMapping("/galleryDelete/{imageNo}")
   public int galleryDelete(@PathVariable String imageNo) {
      // feed의 feedNo만 받아옴.
      System.out.println(imageNo);

      int isokgallerydelete = galleryService.galleryDelete(imageNo);
      if (isokgallerydelete != 1) {
         System.out.println("Gallery Image 삭제 실패");
      } else {
         System.out.println("Gallery Image 삭제 성공");
      }
      return isokgallerydelete;
   }

}