# PROG8850-Final-Assignment

This brings up an "empty" signoz on port 3301 in a codespace. It also brings up wordpress on port 8000 and adminer on port 8001. Use this as a starting point for instrumenting your app.

https://docs.splunk.com/observability/en/gdi/opentelemetry/components/sqlquery-receiver.html should be helpful.

I also used this for a demo I was doing. To do this, I added an nginx proxy in the nginx folder and added the container with `../nginx/docker-compose.yml` in the `docker-compose.yml` file.
