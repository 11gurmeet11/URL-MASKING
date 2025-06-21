# 🎭 URL Masking Tool – Python

A Python tool that shortens a real URL and masks it using a fake domain and optional phishing-style keyword. This is commonly used in phishing awareness training and cybersecurity education.

> ⚠️ **For educational use only.** Misuse of this tool for malicious purposes such as phishing is illegal.

---

## 🚀 Features

- 🔗 URL Shortening using:
  - TinyURL
  - Dagd
  - Clck.ru
- 🕵️ URL masking with fake domains
- 🪝 Optional phishing-style keyword (e.g., "login", "free")
- 🎨 ASCII banner logo
- ❌ Input validation for phishing keyword, domain, and URL
- 📶 Internet connectivity check (optional)

---

## 🧪 Example

### Input:
```
Original URL: https://instagram.com
Service: TinyURL
Fake Domain: facebook.com
Keyword: login
```

### Output:
```
https://facebook.com-login@tinyurl.com/xyz123
```

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/url-masker.git
cd url-masker
pip install pyshorteners
```

---

## 🛠️ Usage

Run the script:

```bash
python urlmask.py
```

Optional `about` command:

```bash
python urlmask.py about
```

---

## 🔐 How URL Masking Works

This tool disguises the real destination like so:

```
https://[fake-domain]-[keyword]@[short-url]
```

Example:
```
https://facebook.com-login@tinyurl.com/abc123
```

This appears to point to Facebook, but the actual redirection is through TinyURL to any URL (e.g., Instagram).

---

## 📁 File Structure

```
urlmask.py       # Main script
README.md        # Documentation
```

---

## ⚠️ Disclaimer

This project is for:

- ✅ Cybersecurity training
- ✅ Ethical hacking labs
- ✅ Phishing awareness demos

🚫 Do NOT use this for phishing or illegal activities. Misuse may result in criminal charges under cyber laws.

---

## 🧑‍💻 Author

Name: GURMEET KAUR

---

## 📜 License

Licensed under the [MIT License](LICENSE).
