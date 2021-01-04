<template>
   <div>
      <nav class="navbar navbar-toggleable-md fixed-top navbar-transparent sticky-navigation">
         <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
               <span class="ion-grid"></span>
         </button>
         <div class="container">
               <a class="navbar-brand" href="#">
                  <img src="@/components/Test/img/logo-w60.png" class="nav-brand-logo" />
               </a>
               <div class="collapse navbar-collapse" id="navbarCollapse">
                  <ul class="navbar-nav ml-auto">
                     <li class="nav-item">
                           <a class="nav-link page-scroll" href="#home">Home</a>
                     </li>
                     <li class="nav-item">
                           <a class="nav-link page-scroll" href="#features">Features</a>
                     </li>
                     <li class="nav-item">
                           <a class="nav-link page-scroll" href="#team">Team</a>
                     </li>
                     <li class="nav-item">
                           <a class="nav-link page-scroll" href="#contact">Contact</a>
                     </li>
                  </ul>
               </div>
         </div>
      </nav>      
      
      <div class="wrapper">
         <!--header section-->
         <section class="hero-header" id="home" style="background-image: url(../img/slide1.jpg)">
               <div class="container">
                  <div class="row">
                     <div class="col-md-8 offset-md-2">
                           <div class="brand">
                              <h1 class="heading-light">One Account. Complete Control.</h1>
                              <p class="lead mb-5">
                                 Authority gives you one secure account for all your applications and complete 
                                 administrative control. 
                              </p>
                              <a href="#features" class="btn btn-outline-white btn-round btn-md page-scroll">
                                 <em class="ion-play"></em> Watch A Video
                              </a>
                           </div>
                     </div>
                  </div>
               </div>
         </section>

         <!--features-->
         <section class="bg-alt" id="features">
               <div class="container">
                  <div class="row">
                     <div class="col-md-8 offset-md-2">
                           <div class="title text-center">
                              <h2 class="heading-semi-bold text-primary">Authority</h2>
                              <p class="lead text-muted">
                                 Write a short but precise description of your product here. This paragraph is 
                                 helpful to explain your product in detail.
                              </p>
                           </div>
                     </div>
                  </div>
                  <div class="row text-center mt-4">
                     <div class="col-sm-4">
                           <div class="card border-none">
                              <div class="card-block">
                                 <div class="mb-3">
                                       <em class="ion-ios-checkmark-outline icon-lg text-primary"></em>
                                 </div>
                                 <h4>100% Secure</h4>
                                 <p class="text-muted">
                                       Explain each individual feature here in more detail - write at least 3-4
                                       sentences. Do not talk about irrelevant stuff.
                                 </p>
                              </div>
                           </div>
                     </div>
                     <div class="col-sm-4">
                           <div class="card border-none">
                              <div class="card-block">
                                 <div class="mb-3">
                                       <em class="ion-ios-infinite icon-lg text-success"></em>
                                 </div>
                                 <h4>Unlimited Accounts</h4>
                                 <p class="text-muted">
                                       Explain each individual feature here in more detail - write at least 3-4
                                       sentences. Do not talk about irrelevant stuff.
                                 </p>
                              </div>
                           </div>
                     </div>
                     <div class="col-sm-4">
                           <div class="card border-none">
                              <div class="card-block">
                                 <div class="mb-3">
                                       <em class="ion-ios-heart-outline icon-lg text-danger"></em>
                                 </div>
                                 <h4>Customer Support</h4>
                                 <p class="text-muted">
                                       Explain each individual feature here in more detail - write at least 3-4
                                       sentences. Do not talk about irrelevant stuff.
                                 </p>
                              </div>
                           </div>
                     </div>
                  </div>
               </div>
         </section>

         <!--team-->
         <section class="bg-faded" id="team">
               <div class="container">
                  <div class="row">
                     <div class="col-md-8 offset-md-2">
                           <div class="title text-center">
                              <h2 class="heading-semi-bold text-primary">Meet Our Team</h2>
                              <p class="lead">
                                 Write a short description of your team here.
                              </p>
                           </div>
                     </div>
                  </div>
                  <div class="row text-center mt-4">
                     <div class="col-sm-4">
                           <div class="mb-4">
                              <img src="@/components/Test/img/team-1.jpg" class="mx-auto d-block rounded-circle img-fluid img-team" alt="Team" />
                           </div>
                           <h5>John Doe</h5>
                           <p class="heading-semi-bold text-muted">Co-Founder</p>
                           <p class="text-muted">
                              Write here about your team member - what is his/her expertise and how he/she has 
                              participated in product development life-cycle.
                           </p>
                           <p>
                              <a href="#" class="mr-3"><em class="fa fa-facebook"></em></a>
                              <a href="#" class="mr-3"><em class="fa fa-twitter"></em></a>
                              <a href="#"><em class="fa fa-instagram"></em></a>
                           </p>
                     </div>
                     <div class="col-sm-4">
                           <div class="mb-4">
                              <img src="@/components/Test/img/avatar.jpg" class="mx-auto d-block rounded-circle img-fluid img-team" alt="Team" />
                           </div>
                           <h5>Inza Deol</h5>
                           <p class="heading-semi-bold text-muted">Head Support</p>
                           <p class="text-muted">
                              Write here about your team member - what is his/her expertise and how he/she has 
                              participated in product development life-cycle.
                           </p>
                           <p>
                              <a href="#" class="mr-3"><em class="fa fa-facebook"></em></a>
                              <a href="#" class="mr-3"><em class="fa fa-twitter"></em></a>
                              <a href="#"><em class="fa fa-instagram"></em></a>
                           </p>
                     </div>
                     <div class="col-sm-4">
                           <div class="mb-4">
                              <img src="@/components/Test/img/team-2.jpg" class="mx-auto d-block rounded-circle img-fluid img-team" alt="Team" />
                           </div>
                           <h5>Sameer Stein</h5>
                           <p class="heading-semi-bold text-muted">CTO</p>
                           <p class="text-muted">
                              Write here about your team member - what is his/her expertise and how he/she has 
                              participated in product development life-cycle.
                           </p>
                           <p>
                              <a href="#" class="mr-3"><em class="fa fa-facebook"></em></a>
                              <a href="#" class="mr-3"><em class="fa fa-twitter"></em></a>
                              <a href="#"><em class="fa fa-instagram"></em></a>
                           </p>
                     </div>
                  </div>
               </div>
         </section>

         <!--team-->
         <section class="bg-alt" id="contact">
               <div class="container">
                  <div class="row">
                     <div class="col-md-8 offset-md-2">
                           <div class="title text-center">
                              <h2 class="heading-semi-bold text-primary">Contact Us</h2>
                              <p class="lead text-muted">
                                 W'd love to hear from you!
                              </p>
                           </div>
                     </div>
                  </div>
                  <div class="row text-center mt-4">
                     <div class="col-md-8 offset-md-2">
                           <div class="row">
                              <div class="col-sm-6">
                                 <div class="form-group">
                                       <input type="text" class="form-control" placeholder="Your Name" />
                                 </div>
                              </div>
                              <div class="col-sm-6">
                                 <div class="form-group">
                                       <input type="text" class="form-control" placeholder="Your Email Adress" />
                                 </div>
                              </div>
                           </div>
                           <div class="form-group mt-4">
                              <textarea class="form-control" placeholder="What's in your mind?" rows="5"></textarea>
                           </div>
                           <div class="form-group mt-4">
                              <input type="submit" class="btn btn-primary btn-round" value="Send Message" />
                           </div>
                     </div>
                  </div>
               </div>
         </section>

         <!--footer-->
         <section class="colored-section bg-inverse footer pt-5">
               <div class="container">
                  <div class="row">
                     <div class="col-sm-6 offset-sm-3 text-center">
                           <ul class="nav justify-content-center">
                              <li class="nav-item">
                                 <a class="nav-link active" href="#">About</a>
                              </li>
                              <li class="nav-item">
                                 <a class="nav-link" href="#">License</a>
                              </li>
                              <li class="nav-item">
                                 <a class="nav-link" href="#">Privacy Policy</a>
                              </li>
                              <li class="nav-item">
                                 <a class="nav-link" href="#">Terms and Conditions</a>
                              </li>
                           </ul>
                           <p class="mt-4 text-muted">
                              &copy; 2017 Wired UI Kit. A FREE Bootstrap 4 UI Kit by 
                              <a href="https://wireddots.com">Wired Dots</a>. Designed by <a href="https://twitter.com/attacomsian">@attacomsian</a>
                           </p>
                     </div>
                  </div>
               </div>
         </section>
      </div>
   </div>
</template>

<script>
export default {
   name: 'Test',
}
</script>

<style>

</style>