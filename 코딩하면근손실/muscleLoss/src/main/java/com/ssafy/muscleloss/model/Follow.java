package com.ssafy.muscleloss.model;

public class Follow {

	private String follower;
	private String following;
	private String uid;
	private boolean isFollow;
	
	public String getFollower() {
		return follower;
	}
	public void setFollower(String follower) {
		this.follower = follower;
	}
	public String getFollowing() {
		return following;
	}
	public void setFollowing(String following) {
		this.following = following;
	}
	public String getUid() {
		return uid;
	}
	public void setUid(String uid) {
		this.uid = uid;
	}
	public boolean isFollow() {
		return isFollow;
	}
	public void setFollow(boolean isFollow) {
		this.isFollow = isFollow;
	}
	
	@Override
	public String toString() {
		return "Follow [follower=" + follower + ", following=" + following + ", uid=" + uid + ", isFollow=" + isFollow
				+ "]";
	}
	
}
