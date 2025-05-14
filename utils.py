def check_collision(circle_x, circle_y, radius, rect_x, rect_y, rect_w, rect_h):
    # Verifica colisão entre círculo (tiro) e retângulo (inimigo)
    closest_x = max(rect_x, min(circle_x, rect_x + rect_w))
    closest_y = max(rect_y, min(circle_y, rect_y + rect_h))
    distance_x = circle_x - closest_x
    distance_y = circle_y - closest_y
    return (distance_x ** 2 + distance_y ** 2) < (radius ** 2)
