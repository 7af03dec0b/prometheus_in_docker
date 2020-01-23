# prometheus\_in\_docker

## Developing prometheus rules in docker
Simply execute `./docker.sh` and you'll get following setup:
* prometheus, reachable on port 9090, with configuration under `./prometheus/etc`
* alertmanager, reachable on port 9093, with configuration under `./alertmanager/etc`
* 3x node exporters, already configured in prometheus for scraping on port 9100, with custom file-based metrics examples, located under `./node_exporter/client-\*/`, where the client's name matches the name in docker. It's not necessary to restart the setup after you change the custom metrics files.

Preconfigured is simple example with fake\_load metrics (per host), alert thresholds (under `node_exporter/client-b1/limits.prom`) in prometheus and you can see the results either under prometheus or in alertmanager.

* Prometheus is http://localhost:9090/
* Alertmanager is http://localhost:9093/

## Testing Prometheus rules
Create your test files under `prometheus/etc/tests` (see example load.yml in this directory) and simply run `./run-tests.sh [filename.yml ...]`, eg. `./run-tests.sh load.yml`. If you do not specify filename, then all files matching `prometheus/etc/tests/\*.yml`  will be tested.
