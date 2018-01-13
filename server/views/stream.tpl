<!DOCTYPE html>
<html lang="en">

  <head>
  

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Scrolling Nav - Start Bootstrap Template</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.min.css" rel="stylesheet">
<script async defer src="//platform.instagram.com/en_US/embeds.js"></script>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<script async defer src="//platform.instagram.com/en_US/embeds.js"></script>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<script async src="/js/facebook.js" charset="utf-8"></script>


    <!-- Custom styles for this template -->
    <link href="/css/scrolling-nav.css" rel="stylesheet">

  </head>

  <body id="page-top">

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
      <div class="container">
        <a class="navbar-brand js-scroll-trigger" href="#page-top">Start Bootstrap</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="#about">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="#services">Services</a>
            </li>
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="#contact">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <header class="bg-primary text-white">
      <div class="container text-center">
        <h1>Welcome to Scrolling Nav</h1>
        <p class="lead">A landing page template freshly redesigned for Bootstrap 4</p>
      </div>
    </header>
  <div  class='container text-center'>
<div class='container text-center' width="60%"  >
    
    	% for frame in emb:
    		% if frame[0]=='fb':
    			<iframe   src="{{frame[1]}}&width=648" width="648" height="648" scrolling="no" frameborder="0" allowTransparency="true"></iframe>
    		
  	
  
	<!-- <iframe   src="{{frame[1]}}&width=500"   scrolling="no" frameborder="0" allowTransparency="true"  ></iframe>  -->


		

    		% elif frame[0]=='insta':
    			<blockquote class="instagram-media  text-center instagram"  data-instgrm-captioned data-instgrm-permalink={{ frame[1]}} style="max-width:658px; width:99.375%; margin: 0 aut o!important;"> </blockquote> 

    		

    		% elif frame[0]=='twitter':
  
	<blockquote class="twitter-tweet" data-lang="en"><a href="{{frame[1]}}">Tweet will appear here.</a></blockquote>

	% end
	 % aria-expanded
</div>
</div>

 
    <!-- Footer -->
    <footer class="py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; Your Website 2017</p>
      </div>
      <!-- /.container -->
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="js/jquery.easing.min.js"></script>

    <!-- Custom JavaScript for this theme -->
    <script src="/js/scrolling-nav.js"></script>

  </body>

</html>



