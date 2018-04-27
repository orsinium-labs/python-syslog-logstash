
# Python Syslog Logstash

Demonstration of logging system for Python projects.

## Scheme

1. **Python project** -- sent logs.
1. **Rsyslog** -- collect logs from projects (can be many rsyslogs on many servers).
1. **Redis** -- message queue between rsyslog and logstash.
1. **Logstash** -- retrieve data from Redis, select index and add into ElasticSearch.
1. **ElasticSearch** -- logs storage.
1. **Kibana** -- web-interface.

## Usage

1. Run:
    ```bash
    docker-compose up
    ```
1. Open Kibana:
    [127.0.0.1:5601/app/kibana](http://127.0.0.1:5601/app/kibana)
1. Go to Management -> Index patterns.
1. Click on "refresh fields". If "create" button still inactive then wait while ElasticSearch is ran.
1. Click "create"
1. Go to "Discover". This is your data :)
