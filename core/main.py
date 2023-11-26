import pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Pong-Game")

from core.objects import Paddle, Ball
from core.functions import draw_board, handle_collision, handle_paddle_movemoment

from core.constants import WIDTH, HEIGHT, WIN, FPS
from core.constants import PADDLE_WIDTH, PADDLE_HEIGHT, BALL_RADIUS
from core.constants import WIN_SCORE, FONT, WHITE


def run_pong():
    
    run = True
    clock = pygame.time.Clock()

    left_score, right_score = 0, 0

    left_paddle = Paddle(
        10, 
        HEIGHT//2 - PADDLE_HEIGHT//2, 
        PADDLE_WIDTH, 
        PADDLE_HEIGHT
    )
    right_paddle = Paddle(
        WIDTH - 10 - PADDLE_WIDTH, 
        HEIGHT//2 - PADDLE_HEIGHT//2, 
        PADDLE_WIDTH, 
        PADDLE_HEIGHT
    )
    ball = Ball(
        WIDTH//2, 
        HEIGHT//2,
        BALL_RADIUS
    )

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break
        
        keys = pygame.key.get_pressed()
        handle_paddle_movemoment(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        won = False
        if left_score >= WIN_SCORE:
            won = True
            win_text = "Left Player Won!!"
        elif right_score >= WIN_SCORE:
            won = True
            win_text = "Right Player Won!!"
        
        draw_board(WIN, [left_paddle, right_paddle], ball, (left_score, right_score))
        
        if won:
            text = FONT.render(win_text, 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            
            pygame.display.update()
            pygame.time.delay(5000)

            ball.reset()
            left_paddle.reset()
            right_paddle.reset()

            left_score = 0
            right_score = 0
    
    pygame.quit()


if __name__ == '__main__':
    pass