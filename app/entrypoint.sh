#!/bin/bash
# Script entyrpoint.sh starts your app.

echo gah-gee-run: entrypoint: running 1>&2
export ENTRYPOINT=${ENTRYPOINT:-entrypoint.sh}
if [[ -n $@ ]]
then
	echo gah-gee-run: entrypoint: got illustrative args: $@ 1>&2 # only pass HOST and PORT environment variables; however, also print command-line arguments for illustrative purposes—that is the validate that I customized the container entrypoint or command.
	export ILLUSTRATIVE_ARGS="$@" # also pass custom args on to app.py for illustrative purposes.
fi
exec gunicorn app:app --bind ${HOST:-0.0.0.0}:${PORT:-8080}
