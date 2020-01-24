#!/bin/bash
TESTFILES="$*"
if [ "x$TESTFILES" = "x" ]
then
	TESTFILES="$(cd prometheus/etc/tests && ls *yml)"
fi

echo "Testing files; $TESTFILES"
docker run -it --init --rm --name "prometheus-test" -v `pwd`/prometheus/etc:/etc/prometheus:ro --entrypoint '' --workdir /etc/prometheus/tests prom/prometheus:latest /bin/promtool test rules ${TESTFILES}
