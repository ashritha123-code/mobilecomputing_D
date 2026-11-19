import shutil, subprocess
LAYERS={"Android":["Applications: Activities, services, receivers and app processes","Framework: ActivityManager, PackageManager and system services","ART: DEX loading, runtime compilation and garbage collection","Native libraries/HAL: native APIs and hardware abstraction","Linux kernel: scheduling, memory, drivers, Binder and security"],
"iOS":["Cocoa Touch: UIKit and application lifecycle","Media: graphics, audio, video and animation","Core Services: Foundation, networking and data services","Core OS: Darwin/XNU kernel, drivers and low-level security"]}
def main():
 print("TASK 1 - MOBILE OS ARCHITECTURE / DEVICE EVIDENCE")
 for os,layers in LAYERS.items():
  print("\\n"+os)
  for n,x in enumerate(layers,1): print(f" {n}. {x}")
 print("\\nPROCESS AND IPC")
 print("Android: Zygote forks app processes; Binder is the principal system IPC.")
 print("iOS: launchd coordinates launch; XPC and Mach ports support IPC.")
 print("\\nANDROID LIVE COMMAND EVIDENCE")
 if not shutil.which("adb"):
  print("NOT COLLECTED: adb unavailable. Install Android Platform Tools, connect device, enable USB debugging.")
 else:
  for label,cmd in [("devices",["adb","devices","-l"]),("version",["adb","shell","getprop","ro.build.version.release"]),("kernel",["adb","shell","uname","-a"]),("processes",["adb","shell","ps","-A"]),("memory",["adb","shell","dumpsys","meminfo"])]:
   try:
    p=subprocess.run(cmd,capture_output=True,text=True,timeout=10); print(f"\\n[{label}] exit={p.returncode}\\n{(p.stdout or p.stderr)[:700]}")
   except Exception as e: print(label,"ERROR",e)
 print("\\nLIMITATION: no iOS device or live Binder/XPC trace is inspected by this Python run.")
if __name__=="__main__": main()
