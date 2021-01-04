package com.ssafy.muscleloss.controller;

import java.util.Collections;
import java.util.List;

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
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.muscleloss.model.Alarm;
import com.ssafy.muscleloss.model.Follow;
import com.ssafy.muscleloss.model.Like;
import com.ssafy.muscleloss.model.Member;
import com.ssafy.muscleloss.model.Reply;
import com.ssafy.muscleloss.service.AlarmService;
import com.ssafy.muscleloss.service.FollowService;
import com.ssafy.muscleloss.service.MemberService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin("*")
@Controller
@RequestMapping("/api/follow")
public class FollowController {

	@Autowired
	FollowService followService;
	
	@Autowired
	private AlarmService alarmService;
	
	/* follow 하기 */
	@ApiOperation(value = "팔로우하기.", response = String.class)
	@ResponseBody
	@PostMapping("/registFollow")
	public String registFollow(@RequestBody Follow follow) {

		String answer = null;

//		follow.setFollower(follow.getFollower());
//		follow.setFollowing(follow.getFollowing());
		System.out.println(">>>>>>>>>>>>>>>>follower");
		int cnt = followService.registFollow(follow);
		System.out.println("<<<<<<<<<<<<<<<follower2");
		
		if (cnt == 1) {
			System.out.println("팔로우 성공!!");
			// follwer 가 follwing 에게 팔로우신청 알람으로 follwing 에게 알린다.

			 Alarm alarm = new Alarm();
	            String uid_fk_to = follow.getFollower();
	            String uid_fk_from = follow.getFollowing();
	            alarm.setMessage(uid_fk_from + "님이 당신을 팔로우했습니다.");
	            alarmService.registerAlarm(uid_fk_to, uid_fk_from, alarm.getMessage(), "false");
            
			answer = "success";
		} else {
			System.out.println("팔로우 실패!!");
			answer = "fail";
		}
		return answer;
	}

	/* unfollow 하기 */
	@ApiOperation(value = "언팔로우하기.", response = String.class)
	@ResponseBody
	@PostMapping("/deleteFollow")
	public String removeFollow(@RequestBody Follow follow) {

		String answer = null;

//		Follow follow = new Follow();
//		follow.setFollower(follower);
//		follow.setFollowing(following);
		int cnt = followService.deleteFollow(follow);

		if (cnt == 1) {
			System.out.println("언팔로우 성공!!");
			answer = "success";
		} else {
			System.out.println("언팔로우 실패!!");
			answer = "fail";
		}
		return answer;
	}

	/* follower 수 구하기 */
	@ApiOperation(value = "팔로워 수 구하기.", response = String.class)
	@ResponseBody
	@GetMapping("/follower/{uid}")
	public int getFollowerCount(@PathVariable String uid) {
		System.out.println(uid);
		int cnt = followService.getFollowerCount(uid);
		return cnt;
	}

	/* following 수 구하기 */
	@ApiOperation(value = "팔로잉 수 구하기.", response = String.class)
	@ResponseBody
	@GetMapping("/following/{uid}")
	public int getFollowingCount(@PathVariable String uid) {
		int cnt = followService.getFollowingCount(uid);
		return cnt;
	}
	
	/* follower 리스트 보여주기 */
	@ApiOperation(value = "팔로워 리스트 보여주기.", response = String.class)
	@ResponseBody
	@GetMapping("/followerlist/{uid}")
	public List<Follow> getFollowerList(@PathVariable String uid) { // Member 리스트를 model에 넣어서 반환한다
		List<Follow> list = followService.getFollowerList(uid);
		return list;
	}
	
	/* following 리스트 보여주기 */
	@ApiOperation(value = "팔로잉 리스트 보여주기.", response = String.class)
	@ResponseBody
	@GetMapping("/followinglist/{uid}")
	public List<Follow> getFollowingList(@PathVariable String uid) { // Member 리스트를 model에 넣어서 반환한다
		List<Follow> list = followService.getFollowingList(uid);
		return list;
	}
	
	/* following 하고 있는지 보여주기 */
	  @ApiOperation(value = "following 하고 있는지 보여주기", response = String.class)
	  @ResponseBody
	  @PostMapping("/isFollow/{uid}")
		public String isFollow(@RequestBody Follow follow) {
			String answer;
			int cnt = followService.isFollow(follow);
			if (cnt >= 1) {
				System.out.println("이미 팔로우한 상태!!");
				answer = "success";
			} else {
				System.out.println("아직 팔로우 하지 않은 상태!!");
				answer = "fail";
			}
		
			return answer;
		}
	

}
