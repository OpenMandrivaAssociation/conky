#!/bin/sh
curl -s "https://github.com/brndnmtthws/conky/tags" |grep "tag/" |sed -e 's,.*tag/v,,;s,\".*,,;' |grep -E '^[0-9.]+$' |sort -V |tail -n1

