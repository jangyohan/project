package com.ssafy.muscleloss.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.ui.Model;

import com.ssafy.muscleloss.mapper.GalleryMapper;
import com.ssafy.muscleloss.model.Gallery;

@Service
public class GalleryServiceImpl implements GalleryService {

	@Autowired
	private GalleryMapper galleryMapper;
	
	@Override
	public List<Gallery> galleryAllByUser(Gallery gallery) {
		return galleryMapper.galleryAllByUser(gallery);
	}

	@Override
	public int galleryregister(Gallery gallery) {
		return galleryMapper.galleryregister(gallery);
	}

	@Override
	public int galleryDelete(String imageNo) {
		return galleryMapper.galleryDelete(imageNo);
	}
}
