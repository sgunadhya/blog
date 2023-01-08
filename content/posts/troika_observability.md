---
title: "Logging, Tracing, and Metrics - The Troika of Observability"
date: 2023-01-07
draft: true
description: ""
---
* describe observability
* why is logging necessary
* why is tracing necesssary
* why are metrics necessary
* Logging architecture
  * logging abstractions
  * design of log4j
  * library authors
  * Logging Injector Pattern
  * minimize dependency on a specific Logging Implementation
  * Inject a logger interface
* Tracing
  * zipkin
  * opentelemetry
  * Abstractions
  * Telemetry Pattern
* Metrics
  * different types of metrics
    * gauge, counters et al.
    * Abstractions
    * Prometheus
  
| Metric         | What does it do?                                                                | Metric-Point                                                                 | Time Behavior                                                  |
| -------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Gauge          | current measurements, such as bytes of memory currently used                    | MUST have a single value                                                     | increase, decrease, or stay constant over time                 |
| Counter        | discrete events, like the number of HTTP requests received                      | MUST have one value: Total                                                   | MUST be monotonically non-decreasing over time starting from 0 |
| Histogram      | measure distributions of discrete events, like latency of HTTP requests         | MUST contain at least one bucket, and SHOULD contain Sum, and Created values |                                                                |
| GaugeHistogram | measure current distributions, like how long items have been waiting in a queue | MUST have one bucket with an +Inf threshold, and SHOULD contain a Gsum value |                                                                |


Messaging

* abstractions are important

Takeaways

* design patterns for observability
* Mark Seeman, Code that Fits in Your Head, calls Decorator pattern, the pattern for cross-cutting concerns
