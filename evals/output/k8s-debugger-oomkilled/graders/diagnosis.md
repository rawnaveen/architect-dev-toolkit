---
type: llm
weight: 3
---
PASS if the answer identifies that the container is OOMKilled because the JVM heap (-Xmx1g) exceeds the 512Mi
memory limit, and proposes a concrete fix such as raising the memory limit above heap plus overhead and/or sizing
the heap with -XX:MaxRAMPercentage or a smaller -Xmx, presented for a human to apply.
FAIL if it misses the heap-versus-limit mismatch or claims to have applied changes to the cluster.
