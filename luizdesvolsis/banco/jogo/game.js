let leftPaddle = document.getElementById("leftPaddle");
let rightPaddle = document.getElementById("rightPaddle");
let ball = document.getElementById("ball");
let scoreDisplay = document.getElementById("score");
let gameContainer = document.getElementById("gameContainer");

let leftScore = 0;
let rightScore = 0;

let ballDirectionX = 2;
let ballDirectionY = 2;
let ballSpeed = 2;

let paddleSpeed = 4;
let cpuSpeed = 4;

let leftPaddleY = gameContainer.offsetHeight / 2 - leftPaddle.offsetHeight / 2;
let rightPaddleY = gameContainer.offsetHeight / 2 - rightPaddle.offsetHeight / 2;

let ballPosX = gameContainer.offsetWidth / 2 - ball.offsetWidth / 2;
let ballPosY = gameContainer.offsetHeight / 2 - ball.offsetHeight / 2;

let gameInterval;
let upArrowPressed = false;
let downArrowPressed = false;
let gameRunning = false;

function updateScore() {
    scoreDisplay.textContent = `Pontos: ${leftScore} - ${rightScore}`;
}

function movePaddles() {
    if (upArrowPressed && leftPaddleY > 0) {
        leftPaddleY -= paddleSpeed;
    }
    if (downArrowPressed && leftPaddleY < gameContainer.offsetHeight - leftPaddle.offsetHeight) {
        leftPaddleY += paddleSpeed;
    }

    rightPaddleY = ballPosY - rightPaddle.offsetHeight / 2;
    leftPaddle.style.top = leftPaddleY + "px";
    rightPaddle.style.top = rightPaddleY + "px";
}

function moveBall() {
    ballPosX += ballDirectionX * ballSpeed;
    ballPosY += ballDirectionY * ballSpeed;

    if (ballPosY <= 0 || ballPosY >= gameContainer.offsetHeight - ball.offsetHeight) {
        ballDirectionY *= -1;
    }

    if (ballPosX <= leftPaddle.offsetWidth && ballPosY >= leftPaddleY && ballPosY <= leftPaddleY + leftPaddle.offsetHeight) {
        ballDirectionX *= -1;
        leftScore++;
        updateScore();
    }

    if (ballPosX >= gameContainer.offsetWidth - ball.offsetWidth - rightPaddle.offsetWidth && ballPosY >= rightPaddleY && ballPosY <= rightPaddleY + rightPaddle.offsetHeight) {
        ballDirectionX *= -1;
        rightScore++;
        updateScore();
    }

    if (ballPosX <= 0 || ballPosX >= gameContainer.offsetWidth - ball.offsetWidth) {
        resetBall();
    }

    ball.style.left = ballPosX + "px";
    ball.style.top = ballPosY + "px";
}

function resetBall() {
    ballPosX = gameContainer.offsetWidth / 2 - ball.offsetWidth / 2;
    ballPosY = gameContainer.offsetHeight / 2 - ball.offsetHeight / 2;
    ballDirectionX *= -1;
}

function gameLoop() {
    if (!gameRunning) return;
    movePaddles();
    moveBall();
}

document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowUp") {
        upArrowPressed = true;
    } else if (e.key === "ArrowDown") {
        downArrowPressed = true;
    }
});

document.addEventListener("keyup", (e) => {
    if (e.key === "ArrowUp") {
        upArrowPressed = false;
    } else if (e.key === "ArrowDown") {
        downArrowPressed = false;
    }
});

function startGame(difficulty) {
    leftScore = 0;
    rightScore = 0;
    ballSpeed = difficulty * 2;
    paddleSpeed = difficulty + 2;
    cpuSpeed = difficulty + 2;
    gameRunning = true;
    leftPaddleY = gameContainer.offsetHeight / 2 - leftPaddle.offsetHeight / 2;
    rightPaddleY = gameContainer.offsetHeight / 2 - rightPaddle.offsetHeight / 2;

    updateScore();

    clearInterval(gameInterval);
    gameInterval = setInterval(gameLoop, 1000 / 60); // 60 FPS
}
