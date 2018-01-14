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

    <link href="/css/scrolling-nav.css" rel="stylesheet">

  </head>

  <body id="page-top">

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
      <div class="container">
        <a class="navbar-brand js-scroll-trigger" href="#page-top">Top Trending</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="#about">About</a>
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
<div class='container text-center' width="530px" style="max-width: 530px;"  >
    
      % for frame in emb:
        % if frame[0]=='fb':
          <iframe   src="{{frame[1]}}&width=500"  width="550px" height="500px" scrolling="no" frameborder="0" allowTransparency="true" style="min-height:100%;"></iframe> 
          

        
          
        % elif frame[0]=='insta':


    <iframe class="instagram-media instagram-media-rendered" id="instagram-embed-0" src="{{frame[1]}}embed/captioned/?cr=1&amp;v=8&amp;wp=440#%7B%22ci%22%3A0%2C%22os%22%3A6292.755%7D" allowtransparency="true" frameborder="0" height="814" data-instgrm-payload-id="instagram-media-payload-0" scrolling="no" style="background: rgb(255, 255, 255); border: 1px solid rgb(219, 219, 219); margin: 0 auto; max-width: 550px; width: calc(100% - 2px); border-radius: 4px; box-shadow: none; display: block; padding: 0px;"></iframe>
 


          


        

        % elif frame[0]=='twitter':
  
  <blockquote class="twitter-tweet instagram" data-lang="en"><a href="{{frame[1]}}">Tweet will appear here.</a></blockquote>
  

          



  % end
   % op=(frame[2]/frame[3])*100
      <div width="550px" style="border-style: solid ;border-width: 1px; border-radius: 3px;">
            <div  style="background-color: rgba(0, 255, 255, 1);width:{{op}}%; height: 100% ">{{frame[2]}}</div>

          </div>
          <br>
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



