package com.ssafy.muscleloss.service;

import java.util.List;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;

import com.ssafy.muscleloss.model.Gallery;

public interface GalleryService {
	public List<Gallery> galleryAllByUser(Gallery gallery);
	public int galleryregister(Gallery gallery);
	public int galleryDelete(String imageNo);
}
