ADVERTISERS_FILE = "advertisers.txt"
RULES_FILE = "dist/rules.txt"

REPO_URL = "https://github.com/xetera/this-tweet-took-off"

TEMPLATE = f"""
! Title: Viral tweet piggyback list
! Description: Block paid tweets that promote useless products on the replies of viral tweets
! Expires: 4 days
! Homepage: {REPO_URL}
"""


def build_rule(match):
    return f"twitter.com##article[data-testid='tweet']:has(a:has-text({match}))"


def advertisers(ad_file):
    with open(ad_file, "r") as ads:
        return (ad.strip() for ad in ads.readlines())


def build_rules(ad_file=ADVERTISERS_FILE):
    for line in advertisers(ad_file):
        # Ublock uses ! for comments
        if line.startswith("#"):
            yield line.replace("#", "!")
        else:
            yield build_rule(line)


if __name__ == "__main__":
    rules = "\n".join(build_rules())
    with open(RULES_FILE, "w") as output:
        output.write(TEMPLATE.strip() + "\n\n")
        output.write(rules)
