CONFIG={"platform":"Android","permissions":["CAMERA","ACCESS_FINE_LOCATION"],"token_storage":"Keystore-backed encrypted storage","network":"HTTPS + TLS validation","cleartext_allowed":False,"internal_component_exported":False,"app_signing":True}
THREATS=[
("Spoofing","Token theft/replay","Keystore key, short-lived token, server revocation","PARTIAL","An unlocked compromised device may use an active session."),
("Tampering","Local database modification","Authenticated encryption and integrity checks","PARTIAL","Rooted OS/app-process compromise remains."),
("Repudiation","Denying a submitted record","Server audit log with timestamp and UUID","PARTIAL","Client clock alone is not trusted."),
("Disclosure","Another app reads patient data","Sandbox UID separation and encrypted DB","BLOCKED in normal OS","Root/forensic compromise remains."),
("DoS","Repeated API requests","Rate limiting and exponential backoff","PARTIAL","Distributed abuse may remain."),
("Elevation","Launch internal activity externally","exported=false and signature permissions","BLOCKED","Misconfigured deep links may expose another route."),
("Network interception","Read/modify API traffic","TLS validation and optional certificate pinning","BLOCKED on valid TLS path","Compromised device trust remains.")]
def main():
 print("TASK 4 - STRIDE-STYLE MOBILE SECURITY AUDIT")
 print("Config:",CONFIG)
 for cat,attack,control,result,risk in THREATS:
  print(f"\\n[{cat}] {attack}\\n Control: {control}\\n Decision: {result}\\n Residual: {risk}")
 print("\\nASSET TRACE")
 for row in ["Auth token | token theft | Keystore + short-lived token | PARTIAL","Local DB | extraction | sandbox + encrypted DB | PARTIAL","API traffic | interception | TLS validation | BLOCKED on valid TLS","Internal activity | external launch | exported=false | BLOCKED"]: print(row)
 print("\\nVERDICT: conditionally acceptable for this example configuration; validate actual app.")
 print("LIMITATION: rule-based illustrative audit; no APK, manifest or network traffic was scanned.")
if __name__=="__main__": main()
