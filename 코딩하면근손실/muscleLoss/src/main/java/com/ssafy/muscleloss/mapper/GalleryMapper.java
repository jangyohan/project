package com.ssafy.muscleloss.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.muscleloss.model.Gallery;

@Mapper
public interface GalleryMapper {

	List<Gallery> galleryAllByUser(Gallery gallery);

	int galleryregister(Gallery gallery);

	int galleryDelete(String imageNo);

}
