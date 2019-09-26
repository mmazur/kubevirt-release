#!/usr/bin/env python3

OUTPUT_DIR='gh-pages'
GH_ORG='kubevirt'


from distutils.version import LooseVersion
from github import Github
import os
import re
import sys


def error(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


if len(sys.argv) != 2:
    error("usage: {0} <repo>".format(sys.argv[0]))

if 'GITHUB_TOKEN' not in os.environ:
    error("You need to define GITHUB_TOKEN env var for this to work.")


repo_name = sys.argv[1]

g = Github(os.environ['GITHUB_TOKEN'])
repo = g.get_repo('{0}/{1}'.format(GH_ORG, repo_name))

# TODO: stricter enforcement of version string pattern? To reduce chance of an accident?
releases = {r.tag_name: r for r in repo.get_releases() if r.tag_name and re.match('^v[0-9]+', r.tag_name)}

# TODO: what else other than v.draft?
full_releases = {k: v for k, v in releases.items() if re.match('^v[\.0-9]*$', k) and not v.draft}
sorted_full_versions = sorted(full_releases.keys(), key=LooseVersion, reverse=True)
latest = sorted_full_versions[0]

with open('{0}/{1}/stable.txt'.format(OUTPUT_DIR, repo_name), 'w') as stable:
    stable.write(latest)

