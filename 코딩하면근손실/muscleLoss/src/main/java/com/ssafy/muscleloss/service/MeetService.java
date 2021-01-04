package com.ssafy.muscleloss.service;

import java.util.List;

import com.ssafy.muscleloss.model.Meet;

public interface MeetService {
	
	public int meetregister(Meet meet);
	public List<Meet> meetAll();
	public List<Meet> meetAllByCategory(Meet meet);
	public List<Meet> meetSearch(Meet meet);
	public int meetUpdate(Meet meet);
	public int meetDelete(String meetNo);

}
