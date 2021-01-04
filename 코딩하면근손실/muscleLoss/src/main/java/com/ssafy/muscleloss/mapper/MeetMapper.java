package com.ssafy.muscleloss.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.muscleloss.model.Meet;

@Mapper
public interface MeetMapper {
	
	public int meetregister(Meet meet);
	public List<Meet> meetAll();
	public List<Meet> meetAllByCategory(Meet meet);
	public List<Meet> meetSearch(Meet meet);
	public int meetUpdate(Meet meet);
	public int meetDelete(String meetNo);

}
