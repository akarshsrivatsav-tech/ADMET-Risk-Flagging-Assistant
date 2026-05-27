class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


def print_report(r):

    # Risk color
    if r['risk'] == "Low Risk":
        color = Colors.GREEN
    elif r['risk'] == "Medium Risk":
        color = Colors.YELLOW
    else:
        color = Colors.RED

    # Score bar
    score_bar = "█" * r['score'] + "░" * (10 - r['score'])

    print(f"\n{Colors.MAGENTA}{'='*40}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}     MOLECULE ASSESSMENT REPORT{Colors.RESET}")
    print(f"{Colors.MAGENTA}{'='*40}{Colors.RESET}")

    print(f"\n{Colors.BOLD}🧪  Common Name:{Colors.RESET} {Colors.GREEN}{r['common_name']}{Colors.RESET}")
    print(f"{Colors.BOLD}🔬  Scientific Name:{Colors.RESET} {Colors.CYAN}{r['iupac_name']}{Colors.RESET}")
    print(f"{Colors.BOLD}🆔  CID:{Colors.RESET} {r['cid']}")

    print(f"\n{Colors.BOLD}📊  Molecular Formula:{Colors.RESET} {Colors.YELLOW}{r['formula']}{Colors.RESET}")
    print(f"{Colors.BOLD}⚖️  Molecular Weight:{Colors.RESET} {r['weight']}")
    print(f"{Colors.BOLD}🧬  SMILES:{Colors.RESET} {r['smiles']}")

    print(f"\n{Colors.BOLD}🚩  Risk Flags:{Colors.RESET}")
    if not r['flags']:
        print(f"{Colors.GREEN}✔ No risk flags detected{Colors.RESET}")
    else:
        for f in r['flags']:
            print(f"{Colors.RED}➤ {f}{Colors.RESET}")

    print(f"\n{Colors.BOLD}⚠️  Risk Level:{Colors.RESET} {color}{r['risk']}{Colors.RESET}")
    print(f"{Colors.BOLD}📈  Risk Score:{Colors.RESET} {score_bar} ({r['score']}/10)")

    print(f"\n{Colors.BOLD}💡  Recommendation:{Colors.RESET} {Colors.CYAN}{r['recommendation']}{Colors.RESET}")

    print(f"{Colors.MAGENTA}{'='*40}{Colors.RESET}")