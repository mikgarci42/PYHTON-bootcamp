#!/Users/mikgarci/42Cursus/AI-py/42AI-mikgarci-env/bin/python
import sys
import time
from tqdm import trange

def ft_progress(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy, prefix="", size=60, out=sys.stdout):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)
