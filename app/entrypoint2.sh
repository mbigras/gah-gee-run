#!/bin/bash
# Script entyrpoint2.sh runs entrypoint.sh which starts your app.

echo gah-gee-run: entrypoint2: running 1>&2
export ENTRYPOINT=entrypoint2.sh
exec ./entrypoint.sh $@
