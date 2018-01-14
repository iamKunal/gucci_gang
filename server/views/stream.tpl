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
<!--    			<blockquote class="instagram-media  text-center instagram"  data-instgrm-captioned data-instgrm-permalink={{ frame[1]}} style="max-width:658px; width:100%; margin: 0 auto !important;"> </blockquote> -->
<!--<blockquote class="instagram-media text-center instagram" data-instgrm-captioned data-instgrm-permalink="{{ frame[1] }}" data-instgrm-version="8" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:658px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:37.5% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAMUExURczMzPf399fX1+bm5mzY9AMAAADiSURBVDjLvZXbEsMgCES5/P8/t9FuRVCRmU73JWlzosgSIIZURCjo/ad+EQJJB4Hv8BFt+IDpQoCx1wjOSBFhh2XssxEIYn3ulI/6MNReE07UIWJEv8UEOWDS88LY97kqyTliJKKtuYBbruAyVh5wOHiXmpi5we58Ek028czwyuQdLKPG1Bkb4NnM+VeAnfHqn1k4+GPT6uGQcvu2h2OVuIf/gWUFyy8OWEpdyZSa3aVCqpVoVvzZZ2VTnn2wU8qzVjDDetO90GSy9mVLqtgYSy231MxrY6I2gGqjrTY0L8fxCxfCBbhWrsYYAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/BdqJEePHbGi/" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by Suryaveer Singh (@_suryaveer)</a> on <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2018-01-07T18:34:02+00:00">Jan 7, 2018 at 10:34am PST</time></p></div></blockquote> <script async defer src="//platform.instagram.com/en_US/embeds.js"></script>-->

    <iframe class="instagram-media instagram-media-rendered" id="instagram-embed-0" src="{{frame[1]}}embed/captioned/?cr=1&amp;v=8&amp;wp=658#%7B%22ci%22%3A0%2C%22os%22%3A6292.755%7D" allowtransparency="true" frameborder="0" height="814" data-instgrm-payload-id="instagram-media-payload-0" scrolling="no" style="background: rgb(255, 255, 255); border: 1px solid rgb(219, 219, 219); margin: 0 auto; max-width: 658px; width: calc(100% - 2px); border-radius: 4px; box-shadow: none; display: block; padding: 0px;"></iframe>

<!--<iframe class="instagram-media instagram-media-rendered" id="instagram-embed-4" src='{{frame[1]}}embed/?cr=1&v=8wp=658%23%7b%22ci%22%3a0%2c%22os%22%3a6988.285%7d' allowtransparency="true" frameborder="0" height="556" data-instgrm-payload-id="instagram-media-payload-4" scrolling="no" style="background: rgb(255, 255, 255); border: 1px solid rgb(219, 219, 219); margin: 0 auto; max-width: 658px; width: calc(100% - 2px); border-radius: 4px; box-shadow: none; display: block; padding: 0px;"></iframe>-->
    		

    		% elif frame[0]=='twitter':
  
	<blockquote class="twitter-tweet instagram" data-lang="en"><a href="{{frame[1]}}">Tweet will appear here.</a></blockquote>
<!--<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">I woke up this morning in Hawaii with ten minutes to live. It was a false alarm, but a real psychic warning. If we allow this one-man Gomorrah and his corrupt Republican congress to continue alienating the world we are headed for suffering beyond all imagination. ;^\ <a href="https://t.co/Kwca91IIy2">pic.twitter.com/Kwca91IIy2</a></p>&mdash; Jim Carrey (@JimCarrey) <a href="https://twitter.com/JimCarrey/status/952284494257508352?ref_src=twsrc%5Etfw">January 13, 2018</a></blockquote>-->
<!--<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>-->


	% end
	% end
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



