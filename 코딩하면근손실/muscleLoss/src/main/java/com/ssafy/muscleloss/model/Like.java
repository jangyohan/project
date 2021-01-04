package com.ssafy.muscleloss.model;

public class Like {
   
   private int feedNo_fk;                   
   private String uid_fk;                 
   private int likeCheck;

   public int getFeedNo_fk() {
      return feedNo_fk;
   }
   public void setFeedNo_fk(int feedNo_fk) {
      this.feedNo_fk = feedNo_fk;
   }
   public String getUid_fk() {
      return uid_fk;
   }
   public void setUid_fk(String uid_fk) {
      this.uid_fk = uid_fk;
   }
   public int getLikeCheck() {
      return likeCheck;
   }
   public void setLikeCheck(int likeCheck) {
      this.likeCheck = likeCheck;
   }
   
   @Override
   public String toString() {
      return "Like [feedNo_fk=" + feedNo_fk + ", uid_fk=" + uid_fk + ", likeCheck=" + likeCheck + "]";
   }
   

}