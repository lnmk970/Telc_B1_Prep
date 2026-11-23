#!/bin/bash
# usage: run.sh S17 S18 ...   (expects full/SXX.js base and ext/SXX.js)
cd /tmp/claude-0/-home-user-Telc-B1-Prep/7bae1f57-d18b-57eb-9352-68181edabfc7/scratchpad
for id in "$@"; do
  base=full/$id.js; [ "$id" = S16 ] && base=full/S16b.js
  node expand.js $base ext/$id.js gen/$id.js || exit 1
done
node rebuild_body.js $(for id in "$@"; do echo gen/$id.js; done) || exit 1
cd /home/user/Telc_B1_Prep && node scripts/check_geschichten.js | tee /tmp/chk.txt | tail -3
grep -q "All stories passed" /tmp/chk.txt || { echo CHECK-FAILED; exit 1; }
