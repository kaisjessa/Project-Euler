from math import atan2, tan, sqrt, dist


def ellipse_intersection(x0, y0, m):
    A = -m
    B = -m * x0 + y0
    a = 5
    b = 10
    x0 = (A * B * a**2 + a * b * sqrt(b**2 + (A * a) ** 2 - B**2)) / (
        b**2 + (A * a) ** 2
    )
    x1 = (A * B * a**2 - a * b * sqrt(b**2 + (A * a) ** 2 - B**2)) / (
        b**2 + (A * a) ** 2
    )
    y0 = (B * b**2 - (A * a) * b * sqrt(b**2 + (A * a) ** 2 - B**2)) / (
        b**2 + (A * a) ** 2
    )
    y1 = (B * b**2 + (A * a) * b * sqrt(b**2 + (A * a) ** 2 - B**2)) / (
        b**2 + (A * a) ** 2
    )

    return ((x0, y0), (x1, y1))


def get_new_point(a, b):
    x_a, y_a = a
    x_b, y_b = b
    m_ab = (y_b - y_a) / (x_b - x_a)
    m_tan = -4 * x_b / y_b
    m_norm = -1 / m_tan
    theta = atan2(abs(m_ab - m_norm), abs(1 + m_ab * m_norm))
    m_c = (m_norm - tan(-theta)) / (m_norm * tan(-theta) + 1)
    c0, c1 = ellipse_intersection(x_b, y_b, m_c)
    if dist(c0, (x_b, y_b)) < dist(c1, (x_b, y_b)):
        return c1
    return c0


if __name__ == "__main__":
    a = (0.0, 10.1)
    b = (1.4, -9.6)
    count = 1
    for i in range(1000):
        c = get_new_point(a, b)
        x, y = c
        if abs(x) <= 0.01 and y > 0:
            break
        count += 1
        a = b
        b = c
    print(count)
