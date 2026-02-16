from turtle import Screen
from Snake.snake import Snake
import time,Snake.food as food,Snake.scoreboard as scoreboard
    
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0) # SCREEN WILL NOT BE UPDATED 
screen.title("MY SNAKE GAME")
screen.listen()

snake = Snake()
food = food.Food()
score = scoreboard.ScoreBoard()

screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update() # UPDATED AFTER ALL THE PIECES ARE MOVED 
    time.sleep(0.1)            
    snake.move()
    
    #Collision with food
    if snake.head.distance(food) < 15:
        score.increse_score()
        food.refresh()
        snake.extend()
    if snake.head.xcor() >300 or  snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:

        score.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()    
screen.exitonclick()

    


