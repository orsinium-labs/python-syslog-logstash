

## Scheme

1. Python project -- sent logs.
1. Rsyslog -- collect logs from projects (can be many rsyslogs on many servers).
1. Redis -- message queue between rsyslog and logstash.
1. Logstash -- retrieve data from Redis, select index and add into ElasticSearch.
1. ElasticSearch -- logs storage.
1. Kibana -- web-interface.
