import pyshorteners
import re
import sys
import socket


def validate_url(url: str) -> str:
    """Return the URL in lowercase if it already contains a scheme, else ''."""
    newurl = url.lower()
    return newurl if newurl.startswith(("http://", "https://")) else ""


def validate_domain(domain: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9.]+", domain))


def internet_connection() -> bool:          # (unused, but kept for completeness)
    try:
        socket.gethostbyname("www.google.com")
        return True
    except socket.gaierror:
        return False


def home_logo() -> None:                    # <‑‑ NEW ASCII BANNER
    print(
        r"""
                 ___====-_  _-====___
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \\//     ))#############\
   -###############\\    (oo)    //###############-
  -#################\\  / VV \  //#################-
 -###################\\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)
        """
    )


def validate_phishing_keyword(keyword: str) -> bool:
    return bool(re.fullmatch(r"[a-zA-Z0-9-_]+", keyword))


def shorting_url(short_obj, url: str) -> str:
    try:
        return short_obj.short(url)
    except Exception:
        print("An error occurred while shortening the URL.")
        return "error"


def shortener_service(url: str) -> str:
    print("1\ttinyurl\n2\tdagd\n3\tclckru")
    try:
        select = int(input("Select : "))
        shortner = pyshorteners.Shortener()
        mapping = {1: shortner.tinyurl, 2: shortner.dagd, 3: shortner.clckru}
        if select in mapping:
            return shorting_url(mapping[select], url)
        else:
            print("Please select between 1‑3")
    except ValueError:
        print("Please select between 1‑3")
    return "error"


def combiner(masked_url: str, domain_name: str, phishing_keyword: str) -> str:
    header, tail = masked_url.split("://", 1)
    middle = f"{domain_name}-{phishing_keyword}" if phishing_keyword else domain_name
    return f"{header}://{middle}@{tail}"


def urlmask():
    # “urlmask about” shows banner + (optional) about()
    if len(sys.argv) > 1 and sys.argv[1] == "about":
        home_logo()
        about()  # type: ignore  # about() assumed elsewhere in your codebase
        return

    home_logo()

    try:
        original_url = input("Enter original URL [Ex. https://google.com]: ").strip()
    except KeyboardInterrupt:
        print("\nExit by user")
        return

    if not original_url:
        print("Please enter a URL.")
        return

    if not (original_url := validate_url(original_url)):
        print("URL is not valid. Use the format https://example.com")
        return

    masked_url = shortener_service(original_url)
    if masked_url == "error":
        return

    try:
        domain_name = input(
            "Enter domain to display [Ex. google.com, facebook.com]: "
        ).strip().lower()
    except KeyboardInterrupt:
        print("\nExit by user")
        return

    if not domain_name or not validate_domain(domain_name):
        print("Please enter a correct domain name (letters, numbers, dots).")
        return

    try:
        want_keyword = input("Do you want to add a keyword? [yes/no]: ").strip().lower()
    except KeyboardInterrupt:
        print("\nExit by user")
        return

    phishing_keyword = ""
    if want_keyword == "yes":
        try:
            phishing_keyword = input(
                "Enter keyword [letters/digits/‑/_]: "
            ).strip().lower()
        except KeyboardInterrupt:
            print("\nExit by user")
            return
        if not validate_phishing_keyword(phishing_keyword):
            print("Invalid keyword; allowed: letters, numbers, '-' and '_'.")
            return

    result = combiner(masked_url, domain_name, phishing_keyword)
    print(f"\nMasked URL ⇒ {result}")


if __name__ == "__main__":
    urlmask()
