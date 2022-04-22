def f(points, cost):
    result = cost / points
    print(f"{f'Cost: {cost:>6,} ':<13}", f"{f'Points: {points:>6,} ':<13}", f"->  {result*100:.4f} US cents/pt")


d = {
    600: 7.99,
    1600: 19.99,
    3150: 34.99,
    6300: 59.99,
    11000: 99.99,
    23000: 199.99
}

for points, cost in d.items():
    f(points, cost)


# Cost:   7.99  Points:    600  ->  1.3317 US cents/pt
# Cost:  19.99  Points:  1,600  ->  1.2494 US cents/pt
# Cost:  34.99  Points:  3,150  ->  1.1108 US cents/pt
# Cost:  59.99  Points:  6,300  ->  0.9522 US cents/pt
# Cost:  99.99  Points: 11,000  ->  0.9090 US cents/pt
# Cost: 199.99  Points: 23,000  ->  0.8695 US cents/pt
