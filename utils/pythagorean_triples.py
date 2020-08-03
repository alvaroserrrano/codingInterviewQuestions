def get_pyth_triples():
    return [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in\
            range(y, 30) if x**2 + y**2 == z**2]
print(get_pyth_triples())
