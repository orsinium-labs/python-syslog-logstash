
# Python Syslog Logstash

Demonstration of logging system for Python projects. Fast and safe logs collecting.

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
1. Open Kibana: [127.0.0.1:5601/app/kibana](http://127.0.0.1:5601/app/kibana)
1. Go to Management -> Index patterns.
1. Click on "refresh fields". If "create" button still inactive then wait while ElasticSearch is ran.
1. Click "create"
1. Go to "Discover". This is your data :)

## Example

Example of one log message from ElasticSearch:

```json
{
  "@timestamp": "2018-04-27T12:18:39.199Z",
  "@version": "1",
  "message": {
    "name": "app_name",
    "module": "app",
    "lineno": 79,
    "message": null,
    "random_string": "ydrvlhdruj",
    "random_integer": 302
  },
  "facility_label": "user",
  "facility": "1",
  "hostname": "pythonsysloglogstash_psl-project_1.pythonsysloglogstash_default",
  "program": "",
  "relayhost": "pythonsysloglogstash_psl-project_1.pythonsysloglogstash_default",
  "relayip": "172.21.0.7",
  "severity_label": "crit",
  "severity": "2",
  "tag": "",
  "type": "syslog"
}
```
