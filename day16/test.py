from multiprocessing import Pool

# Function to run in multiple processes
def square(x):
    return x * x

if __name__ == "__main__":
    with Pool() as pool:
        # Map a function over data
        results = pool.map(square, range(10))
        print(results)
    dir = (-1,0)
    dir1 = (dir[1], dir[0])
    dir2 = (-dir[1], -dir[0])
    print(dir)
    print(dir1)
    print(dir2)