date = new Date();

year = date.getFullYear();
month = date.getMonth() + 1;
today = date.getDate();
tomorrow = today + 1;

document.getElementById("current_date").innerHTML = year + "." + month + "." + today + " 오늘의 수업은?";
document.getElementById("tomorrow_date").innerHTML = year + "." + month + "." + tomorrow + " 내일의 수업은?";