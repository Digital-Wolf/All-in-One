## Script for All-in-One tool copy from lazymux
#By CjE##

import os, sys
import readline
from time import sleep as timeout
from Allincore import *

print("Digital-Wolf")
print("Authour:CjE")

def main():
	banner()
	print("   [01] Information Gathering")
	print("   [02] Vulnerability Analysis")
	print("   [03] Web Hacking")
	print("   [04] Database Assessment")
	print("   [05] Password Attacks")
	print("   [06] Wireless Attacks")
	print("   [07] Reverse Engineering")
	print("   [08] Exploitation Tools")
	print("   [09] Sniffing and Spoofing")
	print("   [10] Reporting Tools")
	print("   [11] Forensic Tools")
	print("   [12] Stress Testing")
	print("   [13] Install Linux Distro")
	print("   [14] Termux Utility")
	print("   [15] Shell Function [.bashrc]")
	print("   [16] Install CLI Games")
	print("\n   [00] Exit\n")
	lazymux = input(">>>:")

	# 01 - Information Gathering
	if lazymux.strip() == "1" or lazymux.strip() == "01":
		print("\n    [01] Nmap: Utility for network discovery and security auditing")
		print("    [02] Red Hawk: Information Gathering, Vulnerability Scanning and Crawling")
		print("    [03] D-TECT: All-In-One Tool for Penetration Testing")
		print("    [04] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [05] Infoga: Tool for Gathering Email Accounts Informations")
		print("    [06] ReconDog: Information Gathering and Vulnerability Scanner tool")
		print("    [07] AndroZenmap")
		print("    [08] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
		print("    [09] AstraNmap: Security scanner used to find hosts and services on a computer network")
		print("    [10] weeman: HTTP server for phishing in python")
		print("    [11] Easymap: Nmap Shortcut")
		print("    [12] BlackBox: A Penetration Testing Framework")
		print("    [13] XD3v: Powerful tool that lets you know all the essential details about your phone")
		print("    [14] Crips: This Tools is a collection of online IP Tools that can be used to quickly get information about IP Address's, Web Pages and DNS records")
		print("    [15] SIR: Resolve from the net the last known ip of a Skype Name")
		print("    [16] EvilURL: Generate unicode evil domains for IDN Homograph Attack and detect them")
		print("    [17] Striker: Recon & Vulnerability Scanning Suite")
		print("    [18] Xshell: ToolKit")
		print("    [19] OWScan: OVID Web Scanner")
		print("    [20] OSIF: Open Source Information Facebook")
		print("    [21] Devploit: Simple Information Gathering Tool")
		print("    [22] Namechk: Osint tool based on namechk.com for checking usernames on more than 100 websites, forums and social networks")
		print("    [23] AUXILE: Web Application Analysis Framework")
		print("    [24] inther: Information gathering using shodan, censys and hackertarget")
		print("    [25] GINF: GitHub Information Gathering Tool")
		print("    [26] GPS Tracking")
		print("    [27] ASU: Facebook Hacking ToolKit")
		print("    [28] fim: Facebook Image Downloader")
		print("    [29] MaxSubdoFinder: Tool for Discovering Subdomain")
		print("    [30] pwnedOrNot: OSINT Tool for Finding Passwords of Compromised Email Accounts")
		print("    [31] Mac-Lookup: Finds information about a Particular Mac address")
		print("    [32] BillCipher: Information Gathering tool for a Website or IP address")
		print("    [33] dnsrecon: Security assessment and network troubleshooting")
		print("    [34] zphisher: Automated Phishing Tool")
		print("    [35] Mr.SIP: SIP-Based Audit and Attack Tool")
		print("    [36] Sherlock: Hunt down social media accounts by username")
		print("    [37] userrecon: Find usernames across over 75 social networks")
		print("\n    [00] Back to main menu\n")
		infogathering = input(">>>:")
		if infogathering.strip() == "01" or infogathering.strip() == "1": nmap()
		elif infogathering.strip() == "02" or infogathering.strip() == "2": red_hawk()
		elif infogathering.strip() == "03" or infogathering.strip() == "3": dtect()
		elif infogathering.strip() == "04" or infogathering.strip() == "4": sqlmap()
		elif infogathering.strip() == "05" or infogathering.strip() == "5": infoga()
		elif infogathering.strip() == "06" or infogathering.strip() == "6": reconDog()
		elif infogathering.strip() == "07" or infogathering.strip() == "7": androZenmap()
		elif infogathering.strip() == "08" or infogathering.strip() == "8": sqlmate()
		elif infogathering.strip() == "09" or infogathering.strip() == "9": astraNmap()
		elif infogathering.strip() == "10": weeman()
		elif infogathering.strip() == "11": easyMap()
		elif infogathering.strip() == "12": blackbox()
		elif infogathering.strip() == "13": xd3v()
		elif infogathering.strip() == "14": crips()
		elif infogathering.strip() == "15": sir()
		elif infogathering.strip() == "16": evilURL()
		elif infogathering.strip() == "17": striker()
		elif infogathering.strip() == "18": xshell()
		elif infogathering.strip() == "19": owscan()
		elif infogathering.strip() == "20": osif()
		elif infogathering.strip() == "21": devploit()
		elif infogathering.strip() == "22": namechk()
		elif infogathering.strip() == "23": auxile()
		elif infogathering.strip() == "24": inther()
		elif infogathering.strip() == "25": ginf()
		elif infogathering.strip() == "26": gpstr()
		elif infogathering.strip() == "27": asu()
		elif infogathering.strip() == "28": fim()
		elif infogathering.strip() == "29": maxsubdofinder()
		elif infogathering.strip() == "30": pwnedOrNot()
		elif infogathering.strip() == "31": maclook()
		elif infogathering.strip() == "32": billcypher()
		elif infogathering.strip() == "33": dnsrecon()
		elif infogathering.strip() == "34": zphisher()
		elif infogathering.strip() == "35": mrsip()
		elif infogathering.strip() == "36": sherlock()
		elif infogathering.strip() == "37": userrecon()
		elif infogathering.strip() == "00" or infogathering.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 02 - Vulnerability Analysis
	elif lazymux.strip() == "2" or lazymux.strip() == "02":
		print("\n    [01] Nmap: Utility for network discovery and security auditing")
		print("    [02] AndroZenmap")
		print("    [03] AstraNmap: Security scanner used to find hosts and services on a computer network")
		print("    [04] Easymap: Nmap Shortcut")
		print("    [05] Red Hawk: Information Gathering, Vulnerability Scanning and Crawling")
		print("    [06] D-TECT: All-In-One Tool for Penetration Testing")
		print("    [07] Damn Small SQLi Scanner: A fully functional SQL injection vulnerability scanner (supporting GET and POST parameters) written in under 100 lines of code")
		print("    [08] SQLiv: massive SQL injection vulnerability scanner")
		print("    [09] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [10] sqlscan: Quick SQL Scanner, Dorker, Webshell injector PHP")
		print("    [11] Wordpresscan: WPScan rewritten in Python + some WPSeku ideas")
		print("    [12] WPScan: Free wordPress security scanner")
		print("    [13] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
		print("    [14] termux-wordpresscan")
		print("    [15] TM-scanner: websites vulnerability scanner for termux")
		print("    [16] Rang3r: Multi Thread IP + Port Scanner")
		print("    [17] Striker: Recon & Vulnerability Scanning Suite")
		print("    [18] Routersploit: Exploitation Framework for Embedded Devices")
		print("    [19] Xshell: ToolKit")
		print("    [20] SH33LL: Shell Scanner")
		print("    [21] BlackBox: A Penetration Testing Framework")
		print("    [22] XAttacker: Website Vulnerability Scanner & Auto Exploiter")
		print("    [23] OWScan: OVID Web Scanner")
		print("\n    [00] Back to main menu\n")
		vulnsys = input(">>>:")
		if vulnsys.strip() == "01" or vulnsys.strip() == "1": nmap()
		elif vulnsys.strip() == "02" or vulnsys.strip() == "2": androZenmap()
		elif vulnsys.strip() == "03" or vulnsys.strip() == "3": astraNmap()
		elif vulnsys.strip() == "04" or vulnsys.strip() == "4": easyMap()
		elif vulnsys.strip() == "05" or vulnsys.strip() == "5": red_hawk()
		elif vulnsys.strip() == "06" or vulnsys.strip() == "6": dtect()
		elif vulnsys.strip() == "07" or vulnsys.strip() == "7": dsss()
		elif vulnsys.strip() == "08" or vulnsys.strip() == "8": sqliv()
		elif vulnsys.strip() == "09" or vulnsys.strip() == "9": sqlmap()
		elif vulnsys.strip() == "10": sqlscan()
		elif vulnsys.strip() == "11": wordpreSScan()
		elif vulnsys.strip() == "12": wpscan()
		elif vulnsys.strip() == "13": sqlmate()
		elif vulnsys.strip() == "14": wordpresscan()
		elif vulnsys.strip() == "15": tmscanner()
		elif vulnsys.strip() == "16": rang3r()
		elif vulnsys.strip() == "17": striker()
		elif vulnsys.strip() == "18": routersploit()
		elif vulnsys.strip() == "19": xshell()
		elif vulnsys.strip() == "20": sh33ll()
		elif vulnsys.strip() == "21": blackbox()
		elif vulnsys.strip() == "22": xattacker()
		elif vulnsys.strip() == "23": owscan()
		elif vulnsys.strip() == "00" or vulnsys.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()

	# 03 - Web Hacking
	elif lazymux.strip() == "3" or lazymux.strip() == "03":
		print("\n    [01] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [02] WebDAV: WebDAV File Upload Exploiter")
		print("    [03] MaxSubdoFinder: Tool for Discovering Subdomain")
		print("    [04] Webdav Mass Exploit")
		print("    [05] Atlas: Quick SQLMap Tamper Suggester")
		print("    [06] sqldump: Dump sql result sites with easy")
		print("    [07] Websploit: An advanced MiTM Framework")
		print("    [08] sqlmate: A friend of SQLmap which will do what you always expected from SQLmap")
		print("    [09] inther: Information gathering using shodan, censys and hackertarget")
		print("    [10] HPB: HTML Pages Builder")
		print("    [11] Xshell: ToolKit")
		print("    [12] SH33LL: Shell Scanner")
		print("    [13] XAttacker: Website Vulnerability Scanner & Auto Exploiter")
		print("    [14] XSStrike: Most advanced XSS Scanner")
		print("    [15] Breacher: An advanced multithreaded admin panel finder")
		print("    [16] OWScan: OVID Web Scanner")
		print("    [17] ko-dork: A simple vuln web scanner")
		print("    [18] ApSca: Powerful web penetration application")
		print("    [19] amox: Find backdoor or shell planted on a site via dictionary attack")
		print("    [20] FaDe: Fake deface with kindeditor, fckeditor and webdav")
		print("    [21] AUXILE: Auxile Framework")
		print("    [22] xss-payload-list: Cross Site Scripting ( XSS ) Vulnerability Payload List")
		print("\n    [00] Back to main menu\n")
		webhack = input(">>>:")
		if webhack.strip() == "01" or webhack.strip() == "1": sqlmap()
		elif webhack.strip() == "02" or webhack.strip() == "2": webdav()
		elif webhack.strip() == "03" or webhack.strip() == "3": maxsubdofinder()
		elif webhack.strip() == "04" or webhack.strip() == "4": webmassploit()
		elif webhack.strip() == "05" or webhack.strip() == "5": atlas()
		elif webhack.strip() == "06" or webhack.strip() == "6": sqldump()
		elif webhack.strip() == "07" or webhack.strip() == "7": websploit()
		elif webhack.strip() == "08" or webhack.strip() == "8": sqlmate()
		elif webhack.strip() == "09" or webhack.strip() == "9": inther()
		elif webhack.strip() == "10": hpb()
		elif webhack.strip() == "11": xshell()
		elif webhack.strip() == "12": sh33ll()
		elif webhack.strip() == "13": xattacker()
		elif webhack.strip() == "14": xsstrike()
		elif webhack.strip() == "15": breacher()
		elif webhack.strip() == "16": owscan()
		elif webhack.strip() == "17": kodork()
		elif webhack.strip() == "18": apsca()
		elif webhack.strip() == "19": amox()
		elif webhack.strip() == "20": fade()
		elif webhack.strip() == "21": auxile()
		elif webhack.strip() == "22": xss_payload_list()
		elif webhack.strip() == "00" or webhack.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 04 - Database Assessment
	elif lazymux.strip() == "4" or lazymux.strip() == "04":
		print("\n    [01] DbDat: DbDat performs numerous checks on a database to evaluate security")
		print("    [02] sqlmap: Automatic SQL injection and database takeover tool")
		print("    [03] NoSQLMap: Automated NoSQL database enumeration and web application exploitation tool")
		print("    [04] audit_couchdb: Detect security issues, large or small, in a CouchDB server")
		print("    [05] mongoaudit: An automated pentesting tool that lets you know if your MongoDB instances are properly secured")
		print("\n    [00] Back to main menu\n")
		dbssm = input(">>>:")
		if dbssm.strip() == "01" or dbssm.strip() == "1": dbdat()
		elif dbssm.strip() == "02" or dbssm.strip() == "2": sqlmap()
		elif dbssm.strip() == "03" or dbssm.strip() == "3": nosqlmap
		elif dbssm.strip() == "04" or dbssm.strip() == "4": audit_couchdb()
		elif dbssm.strip() == "05" or dbssm.strip() == "5": mongoaudit()
		elif dbssm.strip() == "00" or dbssm.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 05 - Password Attacks
	elif lazymux.strip() == "5" or lazymux.strip() == "05":
		print("\n    [01] Hydra: Network logon cracker supporting different services")
		print("    [02] FMBrute: Facebook Multi Brute Force")
		print("    [03] HashID: Software to identify the different types of hashes")
		print("    [04] Facebook Brute Force 3")
		print("    [05] Black Hydra: A small program to shorten brute force sessions on hydra")
		print("    [06] Hash Buster: Crack hashes in seconds")
		print("    [07] FBBrute: Facebook Brute Force")
		print("    [08] Cupp: Common User Passwords Profiler")
		print("    [09] InstaHack: Instagram Brute Force")
		print("    [10] Indonesian Wordlist")
		print("    [11] Xshell")
		print("    [12] Aircrack-ng: WiFi security auditing tools suite")
		print("    [13] BlackBox: A Penetration Testing Framework")
		print("    [14] Katak: An open source software login brute-forcer toolkit and hash decrypter")
		print("    [15] Hasher: Hash cracker with auto detect hash")
		print("    [16] Hash-Generator: Beautiful Hash Generator")
		print("    [17] nk26: Nkosec Encode")
		print("    [18] Hasherdotid: A tool for find an encrypted text")
		print("    [19] Crunch: Highly customizable wordlist generator")
		print("    [20] Hashcat: World's fastest and most advanced password recovery utility")
		print("    [21] ASU: Facebook Hacking ToolKit")
		print("\n    [00] Back to main menu\n")
		passtak = input(">>>:")
		if passtak.strip() == "01" or passtak.strip() == "1": hydra()
		elif passtak.strip() == "02" or passtak.strip() == "2": fmbrute()
		elif passtak.strip() == "03" or passtak.strip() == "3": hashid()
		elif passtak.strip() == "04" or passtak.strip() == "4": fbBrute()
		elif passtak.strip() == "05" or passtak.strip() == "5": black_hydra()
		elif passtak.strip() == "06" or passtak.strip() == "6": hash_buster()
		elif passtak.strip() == "07" or passtak.strip() == "7": fbbrutex()
		elif passtak.strip() == "08" or passtak.strip() == "8": cupp()
		elif passtak.strip() == "09" or passtak.strip() == "9": instaHack()
		elif passtak.strip() == "10": indonesian_wordlist()
		elif passtak.strip() == "11": xshell()
		elif passtak.strip() == "12": aircrackng()
		elif passtak.strip() == "13": blackbox()
		elif passtak.strip() == "14": katak()
		elif passtak.strip() == "15": hasher()
		elif passtak.strip() == "16": hashgenerator()
		elif passtak.strip() == "17": nk26()
		elif passtak.strip() == "18": hasherdotid()
		elif passtak.strip() == "19": crunch()
		elif passtak.strip() == "20": hashcat()
		elif passtak.strip() == "21": asu()
		elif passtak.strip() == "00" or passtak.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 06 - Wireless Attacks
	elif lazymux.strip() == "6" or lazymux.strip() == "06":
		print("\n    [01] Aircrack-ng: WiFi security auditing tools suite")
		print("    [02] Wifite: An automated wireless attack tool")
		print("    [03] Wifiphisher: The Rogue Access Point Framework")
		print("    [04] Routersploit: Exploitation Framework for Embedded Devices")
		print("\n    [00] Back to main menu\n")
		wiretak = input(">>>:")
		if wiretak.strip() == "01" or wiretak.strip() == "1": aircrackng()
		elif wiretak.strip() == "02" or wiretak.strip() == "2": wifite()
		elif wiretak.strip() == "03" or wiretak.strip() == "3": wifiphisher()
		elif wiretak.strip() == "04" or wiretak.strip() == "4": routersploit()
		elif wiretak.strip() == "00" or wiretak.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 07 - Reverse Engineering
	elif lazymux.strip() == "7" or lazymux.strip() == "07":
		print("\n    [01] Binary Exploitation")
		print("    [02] jadx: DEX to JAVA Decompiler")
		print("    [03] apktool: A utility that can be used for reverse engineering Android applications")
		print("    [04] uncompyle6: Python cross-version byte-code decompiler")
		print("    [05] ddcrypt: DroidScript APK Deobfuscator")
		print("\n    [00] Back to main menu\n")
		reversi = input(">>>:")
		if reversi.strip() == "01" or reversi.strip() == "1": binploit()
		elif reversi.strip() == "02" or reversi.strip() == "2": jadx()
		elif reversi.strip() == "03" or reversi.strip() == "3": apktool()
		elif reversi.strip() == "04" or reversi.strip() == "4": uncompyle()
		elif reversi.strip() == "05" or reversi.strip() == "5": ddcrypt()
		elif reversi.strip() == "00" or reversi.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 08 - Exploitation Tools
	elif lazymux.strip() == "8" or lazymux.strip() == "08":
		print("\n    [01] Metasploit: Advanced open-source platform for developing, testing and using exploit code")
		print("    [02] commix: Automated All-in-One OS Command Injection and Exploitation Tool")
		print("    [03] BlackBox: A Penetration Testing Framework")
		print("    [04] Brutal: Payload for teensy like a rubber ducky but the syntax is different")
		print("    [05] TXTool: An easy pentesting tool")
		print("    [06] XAttacker: Website Vulnerability Scanner & Auto Exploiter")  
		print("    [07] Websploit: An advanced MiTM Framework")
		print("    [08] Routersploit: Exploitation Framework for Embedded Devices")
		print("\n    [00] Back to main menu\n")
		exploitool = input(">>>:")
		if exploitool.strip() == "01" or exploitool.strip() == "1": metasploit()
		elif exploitool.strip() == "02" or exploitool.strip() == "2": commix()
		elif exploitool.strip() == "03" or exploitool.strip() == "3": blackbox()
		elif exploitool.strip() == "04" or exploitool.strip() == "4": brutal()
		elif exploitool.strip() == "05" or exploitool.strip() == "5": txtool()
		elif exploitool.strip() == "06" or exploitool.strip() == "6": xattacker()
		elif exploitool.strip() == "07" or exploitool.strip() == "7": websploit()
		elif exploitool.strip() == "08" or exploitool.strip() == "8": routersploit()
		elif exploitool.strip() == "00" or exploitool.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 09 - Sniffing and Spoofing
	elif lazymux.strip() == "9" or lazymux.strip() == "09":
		print("\n    [01] KnockMail: Verify if Email Exists")
		print("    [02] tcpdump: A powerful command-line packet analyzer")
		print("    [03] Hac")
		print("    [04] hping3: hping is a command-line oriented TCP/IP packet assembler/analyzer")
		print("    [05] SocialFish: Educational Phishing Tool & Information Collector")
		print("    [06] santet-online: Social Engineering Tool")
		print("    [07] SpazSMS: Send unsolicited messages repeatedly on the same phone number")
		print("    [08] LiteOTP: Multi Spam SMS OTP")
		print("    [09] tshark: Network protocol analyzer and sniffer")
		print("    [10] Ettercap: Comprehensive suite for MITM attacks, can sniff live connections, do content filtering on the fly and much more")
		print("\n    [00] Back to main menu\n")
		sspoof = input(">>>:")
		if sspoof.strip() == "01" or sspoof.strip() == "1": knockmail()
		elif sspoof.strip() == "02" or sspoof.strip() == "2": tcpdump()
		elif sspoof.strip() == "03" or sspoof.strip() == "3": hac()
		elif sspoof.strip() == "04" or sspoof.strip() == "4": hping3()
		elif sspoof.strip() == "05" or sspoof.strip() == "5": socfish()
		elif sspoof.strip() == "06" or sspoof.strip() == "6": sanlen()
		elif sspoof.strip() == "07" or sspoof.strip() == "7": spazsms()
		elif sspoof.strip() == "08" or sspoof.strip() == "8": liteotp()
		elif sspoof.strip() == "09" or sspoof.strip() == "9": tshark()
		elif sspoof.strip() == "10": ettercap()
		elif sspoof.strip() == "00" or sspoof.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 10 - Reporting Tools
	elif lazymux.strip() == "10":
		print("\n    [01] dos2unix: Converts between DOS and Unix text files")
		print("    [02] exiftool: Utility for reading, writing and editing meta information in a wide variety of files")
		print("    [03] iconv: Utility converting between different character encodings")
		print("    [04] mediainfo: Command-line utility for reading information from media files")
		print("    [05] pdfinfo: PDF document information extractor")
		print("\n    [00] Back to main menu\n")
		reportls = input(">>>:")
		if reportls.strip() == "01" or reportls.strip() == "1": dos2unix()
		elif reportls.strip() == "02" or reportls.strip() == "2": exiftool()
		elif reportls.strip() == "03" or reportls.strip() == "3": iconv()
		elif reportls.strip() == "04" or reportls.strip() == "4": mediainfo()
		elif reportls.strip() == "05" or reportls.strip() == "5": pdfinfo()
		elif reportls.strip() == "00" or reportls.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 11 - Forensic Tools
	elif lazymux.strip() == "11":
		print("\n    [01] steghide: Embeds a message in a file by replacing some of the least significant bits")
		print("    [02] tesseract: Tesseract is probably the most accurate open source OCR engine available")
		print("    [03] sleuthkit: The Sleuth Kit (TSK) is a library for digital forensics tools")
		print("\n    [00] Back to main menu\n")
		forensc = input(">>>:")
		if forensc.strip() == "01" or forensc.strip() == "1": steghide()
		elif forensc.strip() == "02" or forensc.strip() == "2": tesseract()
		elif forensc.strip() == "03" or forensc.strip() == "3": sleuthkit()
		elif forensc.strip() == "00" or forensc.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 12 - Stress Testing
	elif lazymux.strip() == "12":
		print("\n    [01] Torshammer: Slow post DDOS tool")
		print("    [02] Slowloris: Low bandwidth DoS tool")
		print("    [03] Fl00d & Fl00d2: UDP Flood tool")
		print("    [04] GoldenEye: GoldenEye Layer 7 (KeepAlive+NoCache) DoS test tool")
		print("    [05] Xerxes: The most powerful DoS tool")
		print("    [06] Planetwork-DDOS")
		print("    [07] Xshell")
		print("    [08] santet-online: Social Engineering Tool")
		print("\n    [00] Back to main menu\n")
		stresstest = input(">>>:")
		if stresstest.strip() == "01" or stresstest.strip() == "1": torshammer()
		elif stresstest.strip() == "02" or stresstest.strip() == "2": slowloris()
		elif stresstest.strip() == "03" or stresstest.strip() == "3": fl00d12()
		elif stresstest.strip() == "04" or stresstest.strip() == "4": goldeneye()
		elif stresstest.strip() == "05" or stresstest.strip() == "5": xerxes()
		elif stresstest.strip() == "06" or stresstest.strip() == "6": planetwork_ddos()
		elif stresstest.strip() == "07" or stresstest.strip() == "7": xshell()
		elif stresstest.strip() == "08" or stresstest.strip() == "8": sanlen()
		elif stresstest.strip() == "00" or stresstest.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 13 - Install Linux Distro
	elif lazymux.strip() == "13":
		print("\n    [01] Ubuntu")
		print("    [02] Fedora")
		print("    [03] Kali Nethunter")
		print("    [04] Parrot")
		print("    [05] Arch Linux")
		print("\n    [00] Back to main menu\n")
		innudis = input(">>>:")
		if innudis.strip() == "01" or innudis.strip() == "1": ubuntu()
		elif innudis.strip() == "02" or innudis.strip() == "2": fedora()
		elif innudis.strip() == "03" or innudis.strip() == "3": nethunter()
		elif innudis.strip() == "04" or innudis.strip() == "4": parrot()
		elif innudis.strip() == "05" or innudis.strip() == "5": archlinux()
		elif innudis.strip() == "00" or innudis.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 14 - Termux Utility
	elif lazymux.strip() == "14":
		print("\n    [01] SpiderBot: Curl website using random proxy and user agent")
		print("    [02] Ngrok: tunnel local ports to public URLs and inspect traffic")
		print("    [03] Sudo: sudo installer for Android")
		print("    [04] google: Python bindings to the Google search engine")
		print("    [05] kojawafft")
		print("    [06] ccgen: Credit Card Generator")
		print("    [07] VCRT: Virus Creator")
		print("    [08] E-Code: PHP Script Encoder")
		print("    [09] Termux-Styling")
		print("    [11] xl-py: XL Direct Purchase Package")
		print("    [12] BeanShell: A small, free, embeddable Java source interpreter with object scripting language features, written in Java")
		print("    [13] vbug: Virus Maker")
		print("    [14] Crunch: Highly customizable wordlist generator")
		print("    [15] Textr: Simple tool for running text")
		print("    [16] heroku: CLI to interact with Heroku")
		print("    [17] RShell: Reverse shell for single listening")
		print("    [18] TermPyter: Fix all error Jupyter installation on termux")
		print("    [19] F4K3: Fake User Data Generator")
		print("    [20] shc: Shell script compiler")
		print("    [21] Octave: Scientific Programming Language")
		print("    [22] fp-compiler: Free Pascal is a 32, 64 and 16 bit professional Pascal compiler")
		print("    [23] Numpy: The fundamental package for scientific computing with Python")
		print("\n    [00] Back to main menu\n")
		moretool = input(">>>:")
		if moretool.strip() == "01" or moretool.strip() == "1": spiderbot()
		elif moretool.strip() == "02" or moretool.strip() == "2": ngrok()
		elif moretool.strip() == "03" or moretool.strip() == "3": sudo()
		elif moretool.strip() == "04" or moretool.strip() == "4": google()
		elif moretool.strip() == "05" or moretool.strip() == "5": kojawafft()
		elif moretool.strip() == "06" or moretool.strip() == "6": ccgen()
		elif moretool.strip() == "07" or moretool.strip() == "7": vcrt()
		elif moretool.strip() == "08" or moretool.strip() == "8": ecode()
		elif moretool.strip() == "09" or moretool.strip() == "9": stylemux()
		elif moretool.strip() == "10": passgencvar()
		elif moretool.strip() == "11": xlPy()
		elif moretool.strip() == "12": beanshell()
		elif moretool.strip() == "13": vbug()
		elif moretool.strip() == "14": crunch()
		elif moretool.strip() == "15": textr()
		elif moretool.strip() == "16": heroku()
		elif moretool.strip() == "17": rshell()
		elif moretool.strip() == "18": termpyter()
		elif moretool.strip() == "19": f4k3()
		elif moretool.strip() == "20": shc()
		elif moretool.strip() == "21": octave()
		elif moretool.strip() == "22": fpcompiler()
		elif moretool.strip() == "23": numpy()
		elif moretool.strip() == "00" or moretool.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 15 - Shell Function [.bashrc]
	elif lazymux.strip() == "15":
		print("\n    [01] FBVid (FB Video Downloader)")
		print("    [02] cast2video (Asciinema Cast Converter)")
		print("    [03] iconset (AIDE App Icon)")
		print("    [04] readme (GitHub README.md)")
		print("    [05] makedeb (DEB Package Builder)")
		print("    [06] quikfind (Search Files)")
		print("    [07] pranayama (4-7-8 Relax Breathing)")
		print("    [08] sqlc (SQLite Query Processor)")
		print("\n    [00] Back to main menu\n")
		myshf = input(">>>:")
		if myshf.strip() == "01" or myshf.strip() == "1": fbvid()
		elif myshf.strip() == "02" or myshf.strip() == "2": cast2video()
		elif myshf.strip() == "03" or myshf.strip() == "3": iconset()
		elif myshf.strip() == "04" or myshf.strip() == "4": readme()
		elif myshf.strip() == "05" or myshf.strip() == "5": makedeb()
		elif myshf.strip() == "06" or myshf.strip() == "6": quikfind()
		elif myshf.strip() == "07" or myshf.strip() == "7": pranayama()
		elif myshf.strip() == "08" or myshf.strip() == "8": sqlc()
		elif myshf.strip() == "00" or myshf.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	# 16 - Install CLI Games
	elif lazymux.strip() == "16":
		print("\n    [01] Flappy Bird")
		print("    [02] Street Car")
		print("    [03] Speed Typing")
		print("    [04] NSnake: The classic snake game with textual interface")
		print("    [05] Moon buggy: Simple game where you drive a car across the moon's surface")
		print("    [06] Nudoku: ncurses based sudoku game")
		print("    [07] tty-solitaire")
		print("    [08] Pacman4Console")
		print("\n    [00] Back to main menu\n")
		cligam = input(">>>:")
		if cligam.strip() == "01" or cligam.strip() == "1": flappy_bird()
		elif cligam.strip() == "02" or cligam.strip() == "2": street_car()
		elif cligam.strip() == "03" or cligam.strip() == "3": speed_typing()
		elif cligam.strip() == "04" or cligam.strip() == "4": nsnake()
		elif cligam.strip() == "05" or cligam.strip() == "5": moon_buggy()
		elif cligam.strip() == "06" or cligam.strip() == "6": nudoku()
		elif cligam.strip() == "07" or cligam.strip() == "7": ttysolitaire()
		elif cligam.strip() == "08" or cligam.strip() == "8": pacman4console()
		elif cligam.strip() == "00" or cligam.strip() == "0": restart_program()
		else: print("\nERROR: Wrong Input");timeout(1);restart_program()
	
	elif lazymux.strip() == "00":
		sys.exit()
	
	else:
		print("\nERROR: Wrong Input")
		timeout(1)
		restart_program()

if __name__ == "__main__":
	main()
