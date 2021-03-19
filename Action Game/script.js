score = 0;
cross = true;
document.onkeydown = function(e){
    console.log("Key Code is : ",e.keyCode);
    if(e.keyCode == 38){
        dino = document.querySelector('.dino');
        dino.classList.add('animatedino');
        setTimeout(() => {
            dino.classList.remove('animatedino');
        },700);
    }
    if(e.keyCode == 39){
        dino = document.querySelector('.dino');
        dinoX = parseInt(window.getComputedStyle(dino,null).getPropertyValue('left'));
        dino.style.left = (dinoX + 112) + "px";     
}
    if(e.keyCode == 37){
        dino = document.querySelector('.dino');
        dinoX = parseInt(window.getComputedStyle(dino,null).getPropertyValue('left'));
        dino.style.left = (dinoX - 112) + "px";     
    }
}
setInterval(() => {
    dino = document.querySelector('.dino');
    gameOver = document.querySelector('.gameOver');
    obstacle = document.querySelector('.obstacle');

    dx = parseInt(window.getComputedStyle(dino,null).getPropertyValue('top'));
    dy = parseInt(window.getComputedStyle(dino,null).getPropertyValue('left'));

    ox = parseInt(window.getComputedStyle(obstacle,null).getPropertyValue('top'));
    oy = parseInt(window.getComputedStyle(obstacle,null).getPropertyValue('left'));

    offsetX = Math.abs(dx-ox);
    offsetY = Math.abs(dy-oy);
    if(offsetX<93 && offsetY<52){
        gameOver.style.visibility = 'visible';
        obstacle.classList.remove('obstacleAni')
    }
    else if(offsetX < 145 && cross){
        score += 10;
        updateScore(score);
        cross = false;
        setTimeout(() => {
            cross = true;
        },1000);
    }
}, 100);

function updateScore(score){
    scoreCont.innerHTML = "Your Score : " + score;
}