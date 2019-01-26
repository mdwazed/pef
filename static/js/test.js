// my custom js function

function log_item(){
    console.log('item logged');
}
function show_alert(){
    alert('hi');
}

window.onload = log_item;

var top_nav_projekt = document.getElementById('top-nav-projekt');
var top_nav_erganzung = document.getElementById('top-nav-erganzung');
var top_nav_progress = document.getElementById('top-nav-progress');
var left_nav_projekt = document.getElementsByClassName("left_nav_projekt");
var left_nav_erganzung = document.getElementsByClassName("left_nav_erganzung");

top_nav_projekt.addEventListener('click', function(){
    left_nav_erganzung.style.display = 'none';
});
top_nav_erganzung.addEventListener('click', function(){
    left_nav_projekt.style.display = 'none';
});