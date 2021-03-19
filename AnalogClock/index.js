setInterval(() => {
    date = new Date()
    htime = date.getHours();
    mtime = date.getMinutes();
    stime = date.getSeconds();
    hrotation = (30*htime)+(mtime/2);
    mrotation = 6*mtime;
    srotation = 6*stime;
    
    hour.style.transform = `rotate(${hrotation}deg)`;
    minute.style.transform = `rotate(${mrotation}deg)`;
    second.style.transform = `rotate(${srotation}deg)`;

    if(mtime == 59 && stime == 59){
        var audio = document.createElement('audio');
        audio.setAttribute('src','Alarm-ringtone.mp3');
        audio.play();
    }
},1000);
