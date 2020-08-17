<!DOCTYPE html>
<html lang="ru">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<meta name="description" content="">
		<meta name="author" content="">
		<meta name="yandex-verification" content="a8f5b9cc475858db" />
		<link rel="icon" href="../../../../favicon.ico">
			<title>Pandora Search</title>
			
			<!-- jQuery 1.8 or later, 33 KB -->
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>



			<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
			<link href="css/style.css" rel="stylesheet">
			<link  href="https://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.4/fotorama.css" rel="stylesheet">
			<script src="https://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.4/fotorama.js"></script>
	</head>
	<body>
	<div class="menu">
<nav class="navbar navbar-expand-md bg-dark navbar-dark">
  <!-- Brand -->
  <a class="navbar-brand" href="index.php">Pandora</a>

  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>

  <!-- Navbar links -->
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="how_it_works.html">Как это работает</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="how_to_join.html">Как присоединиться</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="company.html">О компании/Контакты</a>
      </li>
    </ul>
  </div>
</nav>
</div>
	<br>
	<main>
		<div class="container" style="margin-top: 8%;">
		<div class="row main_area">
		<!-- <div class="col-1">
			<div class="pic_box">
			<img src="img/logo.png" alt="Логотип" class="logo_pic">
			</div>
		</div> -->

		<div class="col-12 search_box">     
		<div id="logo" >
		<h1> <a class="title_link" href="index.php">Pandora Search</a></h1><p>Найди поблизости</p>
		</div>

		<form role="form" id="form-buscar" method="get" action="back.php" class="search_form form">
		<div class="form-group">
		<div class="input-group">
		<input id="1" class="form-control" type="search" name="search" placeholder="Введите для поиска" required/>
		<span class="input-group-btn">
		<button class="btn btn-success" type="submit">
		<i class="glyphicon glyphicon-search" aria-hidden="true"></i> Поиск
		</button>
		</span>
		</div>
		</div>
		</form>
		</div> 
		</div>
		
		<div class="row">
		<div class="col-10 offset-1 accordion">
        <ul>
          <li>
            <input type="checkbox" checked>
            <i></i>
            <h2 class="title_block">Что это такое и как работает поиск?</h2>
            <div class="msg">
                <br>
                <p>Это поиск по товарам магазинов вашего города (пока что работает только по магазинам г.Пензы). Для поиска необходимо вбить название интересующего Вас товара. Вам будет выведена таблица с найденными товарами, магазинами города, где можно их преобрести, а также ценами и временем, на какой момент цена была актуальна.<p>
                
            </div>
          </li>
        </ul>
   		</div>


		<!-- <div class="description">
			<h2>Поиск по товарам в магазинах ващего города.</h2>
			<p>Введите названия продукта для поиска</p>
			<p>Вам будет выведен список всех найденных товаров с ценами и магазинами, где их можно купить.</p>
		</div> -->

		</div>
		</div>
			
	</main>



		<!-- Bootstrap core JavaScript ================================================== -->
		<!-- Placed at the end of the document so the pages load faster -->
		<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
		<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
		<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
	
	</body>
</html>

