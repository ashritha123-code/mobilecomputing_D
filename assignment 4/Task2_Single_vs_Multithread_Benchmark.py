import time, math, os, statistics
from concurrent.futures import ThreadPoolExecutor
def work(a,b):
 s=0
 for n in range(a,b): s+=int(abs(math.sqrt(n)*math.sin(n%997))*1000)
 return s
def main():
 n=240000; w=min(4,os.cpu_count() or 1); size=n//w
 chunks=[(i*size,(i+1)*size if i<w-1 else n) for i in range(w)]
 st=[]; mt=[]; sr=mr=0
 print("TASK 2 - SERIAL VS THREAD-POOL BENCHMARK")
 print(f"Work items={n:,} | workers={w} | logical CPUs={os.cpu_count()}")
 for i in range(1,4):
  t=time.perf_counter(); sr=sum(work(a,b) for a,b in chunks); st.append(time.perf_counter()-t)
  t=time.perf_counter()
  with ThreadPoolExecutor(max_workers=w) as ex: mr=sum(ex.map(lambda ab:work(*ab),chunks))
  mt.append(time.perf_counter()-t)
  print(f"Run {i}: serial={st[-1]:.4f}s | thread-pool={mt[-1]:.4f}s")
 a=statistics.median(st); b=statistics.median(mt)
 print(f"Median serial={a:.4f}s | median thread-pool={b:.4f}s | ratio={b/a:.3f}x")
 print("Result equality:",sr==mr)
 print("Interpretation:","thread-pool slower in this run" if b>a else "thread-pool faster in this run")
 print("LIMITATION: desktop Python timing only; CPython GIL; no Android core placement, PSS, jank or energy data.")
if __name__=="__main__": main()
