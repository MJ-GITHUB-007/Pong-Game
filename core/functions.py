import pygame

from core.constants import WIDTH, HEIGHT, WHITE, BLACK, FONT


def draw_board(win, paddles, ball, scores):
    win.fill(BLACK)

    left_score, right_score = scores

    left_score_text = FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, ((1/4)*WIDTH - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, ((3/4)*WIDTH - right_score_text.get_width()//2, 20))

    for paddle in paddles:
        paddle.draw(win)
    
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 2, i, 4, HEIGHT//40))
    
    ball.draw(win)

    pygame.display.update()

def handle_collision(ball, left_paddle, right_paddle):
    if (
        ball.y + ball.radius >= HEIGHT or
        ball.y - ball.radius <= 0
    ):
        ball.y_vel *= -1
    
    if ball.x_vel < 0:
        if (
            ball.y >= left_paddle.y and
            ball.y <= left_paddle.y + left_paddle.height and
            ball.x - ball.radius <= left_paddle.x + left_paddle.width
        ):
            ball.x_vel *= -1

            middle_y = left_paddle.y + left_paddle.height/2
            delta_y = middle_y - ball.y
            reduction_factor = (left_paddle.height/2) / ball.MAX_VEL
            y_vel = delta_y / reduction_factor
            ball.y_vel = y_vel * (-1)
        
    else:
        if (
            ball.y >= right_paddle.y and
            ball.y <= right_paddle.y + right_paddle.height and
            ball.x + ball.radius >= right_paddle.x
        ):
            ball.x_vel *= -1

            middle_y = right_paddle.y + right_paddle.height/2
            delta_y = middle_y - ball.y
            reduction_factor = (right_paddle.height/2) / ball.MAX_VEL
            y_vel = delta_y / reduction_factor
            ball.y_vel = y_vel * (-1)

def handle_paddle_movemoment(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >=0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)
    
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >=0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)

if __name__ == '__main__':
    pass