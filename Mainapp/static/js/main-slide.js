// date = new Date();

// year = date.getFullYear();
// month = date.getMonth() + 1;
// today = date.getDate();
// tomorrow = today + 1;

// document.getElementById("current_date").innerHTML = year + "." + month + "." + today + " 오늘의 수업은?";
// document.getElementById("tomorrow_date").innerHTML = year + "." + month + "." + tomorrow + " 내일의 수업은?";

// var imgs = 3;
// var now = 0;

// function slide() {
//     now = now == imgs ? 0: now += 1;

//     $(".slidewrap .slidelist .slideitem").eq(now - 1).css({"margin-left": "-500px"});
//     $(".slidewrap .slidelist .slideitem").eq(now).css({"margin-left": "0px"});
// }

// function start() {
//     $(".slidewrap .slidelist .slideitem").eq(0).siblings().css({"margin-left": "-500px"});

//     setInterval(function () { slide() }, 2000);
// }

// start()

// var idx_lgth = $(".slidewrap .slidelist .slideitem").length;
// var srt = 1;

// setInterval(AutoRun, 3000);
  
// function AutoRun(){
//   if(srt == idx_lgth){
//       srt = 0;  
//   }
//   $("section>a").eq(srt).addClass('on').siblings().removeClass('on');
//   $("#visual>div").eq(srt).addClass('on').siblings().removeClass('on');
//   srt++;  
// }