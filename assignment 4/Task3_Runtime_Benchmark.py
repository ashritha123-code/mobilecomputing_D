import time,gc,tracemalloc
def cpu(n=180000):
 x=0
 for i in range(n): x=(x+(i*17)%100003)%100003
 return x
def alloc(n=35000): return [{"id":i,"values":[i,i+1,i+2]} for i in range(n)]
def ui(n=12000): return sum(len(f"Row {i:05d} | status={i%4}") for i in range(n))
def measure(fn):
 gc.collect(); tracemalloc.start(); t=time.perf_counter(); r=fn(); dt=time.perf_counter()-t
 _,peak=tracemalloc.get_traced_memory(); tracemalloc.stop(); return dt,peak/1048576,r
def main():
 print("TASK 3 - RUNTIME WORKLOADS (PYTHON PROXY, NOT ART)")
 for name,fn in [("CPU loop",cpu),("Object allocation",alloc),("UI-list model",ui)]:
  cold,peak,_=measure(fn); warm,_,_=measure(fn)
  print(f"{name}: first={cold:.4f}s second={warm:.4f}s peak Python allocation={peak:.2f} MiB")
 print("\\nANDROID ART EVIDENCE COMMANDS (replace package name)")
 for c in ["adb shell dumpsys package <PACKAGE> | findstr /i compiler",
          "adb shell cmd package compile -m speed-profile <PACKAGE>",
          "adb shell cmd package compile -m verify <PACKAGE>",
          "adb logcat -d | findstr /i art-gc",
          "adb shell dumpsys meminfo <PACKAGE>"]:
  print(c)
 print("\\nLIMITATION: Python first/second invocation is not Android cold/warm launch; tracemalloc is not ART heap telemetry.")
if __name__=="__main__": main()
