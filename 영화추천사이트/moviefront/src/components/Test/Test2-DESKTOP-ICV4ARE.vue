<template>
  <vueper-slides
    class="no-shadow"
    :visible-slides="6"
    :slide-ratio="1 / 4"
    :gap="3"
    :bullets="false"
    :dragging-distance="70">
    <vueper-slide v-for="(slide, i) in slides" :key="i" :title="i.toString()" :image="slide.image" />
  </vueper-slides>
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

export default {
  data: () => ({
  slides: [
  {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
   {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
    image: require('@/views/static/00.jpg')
  },
  // Other slides.
]
}),
  name: 'MovieList',
  components: { 
    VueperSlides, 
    VueperSlide 
  },
//   data: () => ({
//   slides: [
//     {
//       title: 'Slide #1',
//       content: 'Slide content.'
//     },
//     {
//       title: 'Slide #2',
//       content: 'Slide content.'
//     }
//   ]
// }),
  props: {
  },
}
</script>

<style>
.no-shadow {
  width: 90%;
  margin-top: 50px;
  margin-left: auto;
  margin-right: auto;
}
</style>