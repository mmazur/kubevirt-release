# kubevirt-release

You need `GITHUB_TOKEN` env var in the travis project settings for this to work

The end result is commited to the `gh-pages` branch and published via github pages mechanism as `$org.github.io/$project`.
So if this repo was called `kubevirt/release.git`, files would be accessible as e.g. `kubevirt.github.io/release/kubevirt/stable.txt` (or `kubevirt.io/release/kubevirt/stable.txt`).

Currently this is run from travis cron on a daily schedule, so it takes up to 24h for a new release to become visible.

