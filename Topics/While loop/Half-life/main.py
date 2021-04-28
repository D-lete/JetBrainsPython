class HalfLife:
    atoms_start = int(input())
    atoms_end = int(input())
    half_lives = 0
    half_lives_days = 0
    atoms = atoms_start

    while atoms >= atoms_end:
        atoms = atoms / 2
        half_lives += 1
        half_lives_days = half_lives * 12
    print(half_lives_days)


HalfLife()
