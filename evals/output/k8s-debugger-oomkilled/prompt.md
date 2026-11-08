---
description: 'k8s-debugger-oomkilled'
tags: [output, agent, k8s-debugger]
plugins: ['../../..']
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---
The payments-api pod in our staging EKS cluster keeps restarting. Here is the output of
`kubectl describe pod payments-api-7d9f8b6c5-x2k4q -n payments-staging`:

```
Containers:
  payments-api:
    Image:          123456789.dkr.ecr.ap-southeast-2.amazonaws.com/payments-api:2.8.1
    State:          Waiting
      Reason:       CrashLoopBackOff
    Last State:     Terminated
      Reason:       OOMKilled
      Exit Code:    137
    Restart Count:  14
    Limits:
      cpu:     1
      memory:  512Mi
    Requests:
      cpu:     250m
      memory:  512Mi
    Environment:
      JAVA_TOOL_OPTIONS:  -Xms1g -Xmx1g
Events:
  Warning  BackOff  2m (x60 over 30m)  kubelet  Back-off restarting failed container
```
Why is it failing and what should we change?
