var section1Btn = document.getElementById("section1Btn"),
    section2Btn = document.getElementById("section2Btn"),
    section3Btn = document.getElementById("section3Btn");

    // set eastype to Linear
      TweenLite.defaultEase = Linear.easeNone;

      var sc = new TimelineMax({paused: true});
      sc.to(window, 650, {scrollTo:{y:0, offsetY:70}});

section1Btn.onclick = function() {
  // TweenLite.to(window, 200, {scrollTo:{y:"#section1", offsetY:70}});

  sc.play();
  sc.progress(1).progress(.75).progress(.5).progress(.25).progress(.15).progress(.05).progress(0);
  sc.play();
}

section2Btn.onclick = function() {
  TweenLite.to(window, 1, {scrollTo:{y:"#section2", offsetY:70}});
}

var tl = new TimelineMax({repeat: 0, paused:true});
tl.to(window, 1, {scrollTo:{y:"#section3", offsetY:70}});

tl.progress(1).progress(.75).progress(.5).progress(.25).progress(.15).progress(.05).progress(0);

section3Btn.onclick = function() {
  // TweenLite.to(window, 1, {scrollTo:{y:"#section3", offsetY:70}});
  tl.play();
}




/* or replace all code above with this jQuery snippet
$("button").each(function(index, element){
  $(this).click(function(){
    TweenLite.to(window, 1, {scrollTo:{y:"#section" + (index+1), offsetY:70}});
  })
})

*/
