#!/usr/bin/env bash
set -euo pipefail
mkdir -p src/main/java/com/acme k8s
printf '<project><modelVersion>4.0.0</modelVersion><groupId>com.acme</groupId><artifactId>svc</artifactId><version>1.0</version></project>\n' > pom.xml
printf '#!/bin/sh\necho mvnw\n' > mvnw && chmod +x mvnw
printf 'DB_PASSWORD=supersecret\n' > .env
printf 'apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: svc\n' > k8s/deployment.yaml
printf 'class App {}\n' > src/main/java/com/acme/App.java
