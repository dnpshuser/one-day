This master taxonomy breaks down all **10 SDE-2 preparation workstreams** into a deep hierarchical tree (`Workstream → Pillar → Category → Subcategory → Atomic 1-Hour Leaf Node`).

Every leaf node at the end of a branch represents **strictly one specific 1-hour study, implementation, or design block** (`[1 Hr]`), totaling **200 atomic 1-hour units** across the entire curriculum.

---

## 1. Workstream 1: Data Structures & Algorithms (DSA) — [72 Hours]

### 1.1 Data Structures — [24 Hours]

* **Hash-Based & Eviction Structures**
* **Custom Hash Table**
* `[1 Hr]` Implement Custom Generic `HashMap` with Separate Chaining & Dynamic Rehashing


* **Cache Eviction Structures**
* `[1 Hr]` Implement `LRU Cache` from scratch using Doubly Linked List + HashMap
* `[1 Hr]` Implement `LFU Cache` from scratch using Frequency-Bucketed Doubly Linked Lists in $O(1)$


* **Temporal & Rate-Tracking Structures**
* `[1 Hr]` Implement `Time-Based Key-Value Store` (Timestamped Binary Search map)
* `[1 Hr]` Implement `Design Hit Counter` with fixed-size circular array bucket eviction




* **Linear Monotonic Structures**
* **Monotonic Stack**
* **Next Greater / Smaller Element**
* `[1 Hr]` Next Greater Element in Circular Array + Daily Temperatures


* **Histogram & Matrix Area Boundaries**
* `[1 Hr]` Largest Rectangle in Histogram (Single-pass index boundary calculation)
* `[1 Hr]` Maximal Rectangle in Binary Matrix


* **Subarray Contribution Counting**
* `[1 Hr]` Sum of Subarray Minimums (Handling duplicate boundary contribution safely)




* **Monotonic Deque**
* **Window Extremes**
* `[1 Hr]` Sliding Window Maximum ($O(N)$ Double-Ended Queue)
* `[1 Hr]` Shortest Subarray with Sum at Least K (Prefix Sum + Monotonic Deque)






* **Heaps & Priority Queues**
* **K-Way & Frequency Selection**
* `[1 Hr]` Top K Frequent Elements + Kth Largest Element (QuickSelect vs. Min-Heap trade-off)
* `[1 Hr]` Merge K Sorted Lists + Smallest Range Covering Elements from K Lists


* **Two-Heap Partitioning**
* `[1 Hr]` Find Median from Data Stream (Max-Heap + Min-Heap balancing)
* `[1 Hr]` Sliding Window Median (Two Heaps with Lazy Deletion hash table)


* **Greedy Heap Scheduling**
* `[1 Hr]` Task Scheduler with Cooldown + Reorganize String
* `[1 Hr]` Meeting Rooms II & III (Interval allocation with Free-Room and Busy-Room heaps)




* **Trees (Structural Representation)**
* **Serialization & Reconstruction**
* `[1 Hr]` Serialize and Deserialize Binary Tree (Preorder + Queue reconstruction)
* `[1 Hr]` Construct Binary Tree from Preorder and Inorder Traversal ($O(N)$ index map)




* **Prefix Tries (Digital Search Trees)**
* **Standard & Wildcard Trie**
* `[1 Hr]` Implement Prefix Trie + Design Add and Search Words Data Structure (DFS wildcard `.`)


* **Bitwise & Grid Trie**
* `[1 Hr]` Word Search II (2D Grid Backtracking with Trie pruning)
* `[1 Hr]` Maximum XOR of Two Numbers in an Array (Binary Trie bit-matching)




* **Disjoint Set Union (DSU / Union-Find)**
* **Path Compression & Union by Rank**
* `[1 Hr]` Implement DSU Template + Accounts Merge (Equivalence component grouping)
* `[1 Hr]` Number of Islands II (Dynamic grid connectivity queries)





---

### 1.2 Algorithms — [48 Hours]

* **Two Pointers & Sliding Window**
* **Converging & Partitioning Pointers**
* `[1 Hr]` 3Sum + 4Sum (Deduplication without HashSet overhead)
* `[1 Hr]` Trapping Rain Water (Two-pointer prefix/suffix max optimization)


* **Variable-Size Sliding Window**
* `[1 Hr]` Minimum Window Substring (Frequency map debt tracking)
* `[1 Hr]` Longest Repeating Character Replacement + Max Consecutive Ones III
* `[1 Hr]` Subarrays with K Different Integers (`atMost(K) - atMost(K-1)` transformation)




* **Binary Search**
* **Rotated & Modified Array Search**
* `[1 Hr]` Search in Rotated Sorted Array (With and without duplicate elements)
* `[1 Hr]` Median of Two Sorted Arrays ($O(\log(\min(M,N)))$ partition binary search)


* **Binary Search on Answer Space (Monotonic Predicate)**
* **Min-Max Partitioning**
* `[1 Hr]` Split Array Largest Sum / Book Allocation Problem
* `[1 Hr]` Capacity to Ship Packages Within D Days


* **Rate & Distance Optimization**
* `[1 Hr]` Minimize Max Distance to Gas Station / Magnetic Force Between Balls
* `[1 Hr]` Kth Smallest Number in Multiplication Table






* **Tree Algorithms**
* **Iterative & Level-Order Traversals**
* `[1 Hr]` Morris Inorder Traversal ($O(1)$ space) + Boundary Traversal of Binary Tree


* **Path & Distance Calculations**
* `[1 Hr]` Binary Tree Maximum Path Sum (Postorder subtree gain vs. split-path max)
* `[1 Hr]` All Nodes Distance K in Binary Tree (Parent pointer graph conversion + BFS)


* **Ancestry & BST Properties**
* `[1 Hr]` Lowest Common Ancestor (LCA) in Binary Tree + Binary Lifting concept overview
* `[1 Hr]` Validate BST + Recover Binary Search Tree (Swapped nodes detection)




* **Graph Algorithms**
* **Breadth-First Search (BFS)**
* **Multi-Source BFS**
* `[1 Hr]` Rotting Oranges + Walls and Gates (Simultaneous wave expansion)


* **State-Space & Bidirectional BFS**
* `[1 Hr]` Word Ladder (Bidirectional BFS optimization)
* `[1 Hr]` Shortest Path in a Grid with Obstacles Elimination `(row, col, remaining_k)`




* **Depth-First Search (DFS)**
* **Cycle & Bipartite Detection**
* `[1 Hr]` Directed Cycle Detection (3-Color DFS) + Is Graph Bipartite?


* **Bridges & Articulation Points**
* `[1 Hr]` Critical Connections in a Network (Tarjan’s Low-Link Algorithm)




* **Topological Sort**
* **Indegree Queue & Ordering**
* `[1 Hr]` Kahn’s Algorithm Implementation + Course Schedule II
* `[1 Hr]` Alien Dictionary (Extracting character precedence graph + Topological Sort)


* **DAG Dynamic Programming**
* `[1 Hr]` Parallel Courses III (Completion time calculation across dependency DAG)




* **Shortest Path Algorithms**
* **Dijkstra’s Algorithm Variants**
* `[1 Hr]` Network Delay Time + Path with Maximum Probability
* `[1 Hr]` Cheapest Flights Within K Stops (Modified Dijkstra / Bellman-Ford state pruning)
* `[1 Hr]` Swim in Rising Water (Min-Max edge weight Dijkstra)


* **0-1 BFS & All-Pairs Shortest Path**
* `[1 Hr]` Minimum Cost to Make at Least One Valid Path in a Grid (0-1 Deque BFS)
* `[1 Hr]` Evaluate Division + Find the City With Smallest Neighbors (Floyd-Warshall)




* **Minimum Spanning Tree (MST)**
* `[1 Hr]` Min Cost to Connect All Points (Kruskal’s DSU vs. Prim’s Priority Queue)




* **Dynamic Programming (DP)**
* **1D & Kadane Variants**
* `[1 Hr]` Maximum Product Subarray + House Robber II (Circular array split)
* `[1 Hr]` Decode Ways + Word Break (Trie-accelerated 1D DP)


* **Knapsack Patterns**
* `[1 Hr]` 0/1 Knapsack: Partition Equal Subset Sum + Target Sum
* `[1 Hr]` Unbounded Knapsack: Coin Change I & II (Permutations vs. Combinations loop order)


* **String & Subsequence DP**
* `[1 Hr]` Longest Common Subsequence (LCS) + Edit Distance (Space-optimized to $O(N)$)
* `[1 Hr]` Longest Increasing Subsequence (LIS in $O(N \log N)$ Patience Sorting)
* `[1 Hr]` Regular Expression Matching / Wildcard Matching


* **Grid & Multi-Dimensional DP**
* `[1 Hr]` Cherry Pickup II (Simultaneous 2-agent 3D DP)
* `[1 Hr]` Longest Increasing Path in a Matrix (Memoized DFS on Grid)


* **Interval / Partition DP**
* `[1 Hr]` Burst Balloons (Last-element-to-pop interval transition)
* `[1 Hr]` Minimum Cost to Cut a Stick / Matrix Chain Multiplication


* **DP on Trees & State Machine DP**
* `[1 Hr]` House Robber III + Binary Tree Cameras (3-state subtree DP)
* `[1 Hr]` Best Time to Buy and Sell Stock with Cooldown & At Most K Transactions




* **Intervals, Backtracking & Plain-Editor Drills**
* **Interval Sweepline**
* `[1 Hr]` Merge Intervals + Insert Interval + Employee Free Time (Line Sweep)


* **Backtracking**
* `[1 Hr]` N-Queens + Palindrome Partitioning (State mutation and restoration)


* **Plain-Editor Timed Drills (No Autocomplete / No Compiler)**
* `[1 Hr]` Plain-Editor Drill 1: Solve 1 Unseen Graph + 1 Unseen DP Problem in 45 mins + Line-by-Line Dry Run
* `[1 Hr]` Plain-Editor Drill 2: Solve 1 Unseen Tree + 1 Unseen Sliding Window Problem in 45 mins
* `[1 Hr]` Plain-Editor Drill 3: Solve 1 Unseen Binary Search + 1 Unseen Heap Problem in 45 mins





---

## 2. Workstream 2: Low-Level Design (LLD) & Machine Coding — [27 Hours]

### 2.1 Object-Oriented Principles & Dependency Injection — [2 Hours]

* **SOLID & Clean Architecture**
* `[1 Hr]` Refactor a 200-line procedural payment script into Single-Responsibility & Open-Closed classes
* `[1 Hr]` Implement Constructor Dependency Injection & Interface Segregation across `Controller → Service → Repository`



### 2.2 Core Design Patterns (From-Memory Coding Templates) — [6 Hours]

* **Behavioral Patterns**
* `[1 Hr]` Strategy Pattern: Pluggable Dynamic Pricing & Discount Engine
* `[1 Hr]` Observer Pattern: Asynchronous Order Status Notification Bus
* `[1 Hr]` State Pattern: Strict Lifecycle State Machine (Order / Parcel Transitions)


* **Creational & Structural Patterns**
* `[1 Hr]` Factory & Abstract Factory Pattern: Multi-Channel Notification / Parser Instantiation
* `[1 Hr]` Decorator Pattern: Composable Pizza / Coffee / Insurance Add-On Cost Calculator
* `[1 Hr]` Thread-Safe Singleton & Builder Pattern: Double-Checked Locking + Immutable Request Builder



### 2.3 Machine Coding Harness & Testing Template — [3 Hours]

* **Skeleton & Validation Architecture**
* `[1 Hr]` Build Reusable Local IDE Skeleton (`Models`, `Repositories`, `Services`, `Exceptions`, `Driver`)
* `[1 Hr]` Build Custom Domain Exception Hierarchy & Input Validator Utility
* `[1 Hr]` Build 10-Minute Unit Test Template (Happy Path, Boundary Exception, `CountDownLatch` Concurrency Test)



### 2.4 End-to-End Machine Coding Builds & Twist Drills — [16 Hours]

* **Problem 1: Splitwise (Expense Sharing)**
* `[1 Hr]` Build Core: Equal, Exact, and Percentage splits + User balance sheet ledger
* `[1 Hr]` Twist & Test: Add Expense Group Simplification (Min-Cash-Flow graph) + Unit Tests


* **Problem 2: Parking Lot System**
* `[1 Hr]` Build Core: Multi-floor spot hierarchy, vehicle types, and Nearest-Spot Allocation Strategy
* `[1 Hr]` Twist & Test: Add Concurrent Multi-Gate Ticket Issuance + Hourly Surge Pricing Strategy


* **Problem 3: BookMyShow / Ticket Booking**
* `[1 Hr]` Build Core: Show seat layout, temporary Seat Lock with TTL expiry, and booking confirmation
* `[1 Hr]` Twist & Test: Add Thread-Safe Double-Booking Prevention under simultaneous requests + Unit Tests


* **Problem 4: In-Memory Multi-Level Cache**
* `[1 Hr]` Build Core: L1/L2 cache hierarchy with pluggable eviction interface and Read/Write-Through latency tracking
* `[1 Hr]` Twist & Test: Add Dynamic Capacity Resizing & Thread-Safe ReadWriteLocks + Unit Tests


* **Problem 5: Distributed Task / Job Scheduler**
* `[1 Hr]` Build Core: One-time and recurring Cron job registration, priority queue, and worker pool execution
* `[1 Hr]` Twist & Test: Add Exponential Backoff Retry Policy + Dead-Job Queue + Unit Tests


* **Problem 6: Food Delivery / E-Commerce Cart (Swiggy/Flipkart)**
* `[1 Hr]` Build Core: Restaurant catalog, inventory capacity check, and pluggable Search/Filter strategies
* `[1 Hr]` Twist & Test: Add Atomic Inventory Deduction on Checkout + Coupon Rule Engine + Unit Tests


* **Problem 7: Vending Machine / ATM**
* `[1 Hr]` Build Core: Idle, HasMoney, Selection, and Dispensing State classes with Inventory Management
* `[1 Hr]` Twist & Test: Add Greedy Denomination Change Dispenser + Refund/Cancel Rollback + Unit Tests


* **Problem 8: Custom In-Memory Pub-Sub Queue (Kafka Clone)**
* `[1 Hr]` Build Core: Topic partitions, Consumer Groups, and independent per-subscriber offset tracking
* `[1 Hr]` Twist & Test: Add Multi-Threaded Subscriber Workers + Offset Reset / Replay API + Unit Tests



---

## 3. Workstream 3: High-Level System Design (HLD) — [30 Hours]

### 3.1 Database & Storage Internals — [8 Hours]

* **Storage Engines & Indexing**
* `[1 Hr]` Storage Engines: B+ Trees (PostgreSQL/MySQL) vs. LSM Trees + SSTables (Cassandra/RocksDB)
* `[1 Hr]` Composite Indexing: The ESR Rule (Equality, Sort, Range) & Covering Indexes
* `[1 Hr]` Query Execution: Reading `EXPLAIN ANALYZE` plans & Eliminating ORM N+1 Queries
* `[1 Hr]` Pagination at Scale: Offset Pagination degradation vs. Cursor/Keyset Pagination


* **Partitioning, Replication & Migrations**
* `[1 Hr]` Database Sharding: Consistent Hashing with Virtual Nodes vs. Range-Based Sharding
* `[1 Hr]` Replication Topologies: Leader-Follower, Multi-Leader, and Leaderless Quorum ($R + W$ greater than $N$)
* `[1 Hr]` NoSQL Selection Matrix: Document vs. Wide-Column vs. Key-Value vs. Graph trade-offs
* `[1 Hr]` Zero-Downtime Schema Migrations: Expand-and-Contract (Parallel Change) Pattern



### 3.2 Caching, Messaging & Distributed Reliability — [10 Hours]

* **Caching Architecture**
* `[1 Hr]` Cache Topologies: Cache-Aside, Write-Through, Write-Back, and Refresh-Ahead
* `[1 Hr]` Redis Internals: Sorted Sets (ZSET), Geospatial Indexes, Streams, and HyperLogLog
* `[1 Hr]` Cache Failure Modes: Mitigating Cache Stampede (Singleflight/Mutex), Penetration (Bloom Filters), and Hot Keys


* **Asynchronous Messaging & Streaming**
* `[1 Hr]` Kafka Architecture: Brokers, Partitions, Partition Keys, Consumer Groups, and Offset Commits
* `[1 Hr]` Broker Trade-Offs: Kafka Log Streaming vs. RabbitMQ AMQP Routing vs. AWS SQS + Dead Letter Queues (DLQ)


* **Distributed Transactions & Coordination**
* `[1 Hr]` Consistency Models: CAP Theorem, PACELC Theorem, and Tunable Eventual Consistency
* `[1 Hr]` Distributed Transactions: 2-Phase Commit (2PC) bottlenecks vs. Saga Pattern (Orchestration vs. Choreography)
* `[1 Hr]` Dual-Write Elimination: Transactional Outbox Pattern with Change Data Capture (Debezium)
* `[1 Hr]` Distributed Locking: Redis Redlock vs. ZooKeeper Ephemeral Nodes vs. Etcd Leases + Fencing Tokens
* `[1 Hr]` Rate Limiting Algorithms: Token Bucket, Leaky Bucket, Fixed Window, and Sliding Window Log/Counter



### 3.3 End-to-End HLD System Blueprints (Excalidraw Drills) — [12 Hours]

* **Foundational & High-Throughput Systems**
* `[1 Hr]` Blueprint 1: Distributed URL Shortener & Pastebin (Snowflake 64-bit ID generator + Read caching)
* `[1 Hr]` Blueprint 2: Distributed Rate Limiter & Multi-Channel Notification Engine


* **High-Contention & Transactional Systems**
* `[1 Hr]` Blueprint 3: Ticket Booking / Flash Sale System (BookMyShow / IRCTC virtual waiting queue + seat lock)
* `[1 Hr]` Blueprint 4: Payment Gateway & Digital Wallet (Double-entry ledger, idempotency, PSP reconciliation)
* `[1 Hr]` Blueprint 5: E-Commerce Inventory & Cart Checkout Service (Soft vs. Hard inventory reservation)


* **Real-Time & Geo-Spatial Systems**
* `[1 Hr]` Blueprint 6: Hyperlocal Ride/Food Matching (Uber/Swiggy Geohash/QuadTree + Location ingestion pipeline)
* `[1 Hr]` Blueprint 7: Real-Time Chat Application (WhatsApp/Slack WebSocket Gateway, presence, message ordering)
* `[1 Hr]` Blueprint 8: Live Video Streaming & Real-Time View/Like Counters (Write buffering + CDN fan-out)


* **Feed, Search & Scheduling Systems**
* `[1 Hr]` Blueprint 9: Social Media News Feed (Twitter/Instagram hybrid Push/Pull fan-out for celebrities)
* `[1 Hr]` Blueprint 10: Typeahead Search Autocomplete (Distributed Trie partitioning + Kafka aggregation pipeline)
* `[1 Hr]` Blueprint 11: Distributed Task Scheduler at Scale (DB partitioning + Lease heartbeat + Worker recovery)


* **AI & Streaming Infrastructure**
* `[1 Hr]` Blueprint 12: GenAI Conversational Streaming System (SSE token streaming, Semantic Vector Cache, Token Rate Limiter)



---

## 4. Workstream 4: Concurrency & Core CS Internals — [12 Hours]

### 4.1 Multithreaded Coding Implementations — [5 Hours]

* **Synchronization Primitives**
* `[1 Hr]` Master Language Primitives: Mutexes, `ReentrantLock`, Condition Variables, Semaphores, and `AtomicInteger`/`CAS`


* **Classic Concurrency Coding Problems**
* `[1 Hr]` Implement `Bounded Blocking Queue` from scratch using Locks and Wait/Notify Conditions
* `[1 Hr]` Implement `Thread-Safe Token Bucket Rate Limiter` supporting high-concurrency bursts
* `[1 Hr]` Implement `Custom Read-Write Lock` with Writer-Preference (Preventing writer starvation)
* `[1 Hr]` Implement `Multi-Threaded Sequence Printer` (Odd-Even / FizzBuzz / Dining Philosophers deadlock avoidance)



### 4.2 Database Concurrency & Locking — [3 Hours]

* **Isolation & Row Locking**
* `[1 Hr]` Read/Write Anomalies: Dirty Reads, Non-Repeatable Reads, Phantom Reads, and Write Skew
* `[1 Hr]` ACID Isolation Levels: Read Uncommitted, Read Committed, Repeatable Read (MVCC snapshots), and Serializable
* `[1 Hr]` Locking Execution: Optimistic Concurrency (`version` column check) vs. Pessimistic Locking (`SELECT ... FOR UPDATE SKIP LOCKED`)



### 4.3 Networking & Communication Protocols — [4 Hours]

* **Transport & Application Protocols**
* `[1 Hr]` Transport Layer: TCP 3-Way Handshake, Congestion Control, TLS 1.3 Handshake vs. UDP
* `[1 Hr]` HTTP Evolution: HTTP/1.1 Keep-Alive vs. HTTP/2 Multiplexing (Head-of-Line blocking) vs. HTTP/3 (QUIC over UDP)
* `[1 Hr]` RPC Frameworks: gRPC (Protobuf binary serialization + HTTP/2 streams) vs. REST JSON
* `[1 Hr]` Real-Time Transport: WebSockets vs. Server-Sent Events (SSE) vs. Long Polling



---

## 5. Workstream 5: Resume Architecture & Behavioral Matrix (HM / Bar Raiser) — [12 Hours]

### 5.1 Resume Architecture Deep-Dives — [4 Hours]

* **Project 1 (Primary Flagship System)**
* `[1 Hr]` Draw Complete End-to-End Architecture on Excalidraw (API Gateway, Services, DB Schemas, Queues)
* `[1 Hr]` Document Quantitative Bottlenecks, Failure Modes, Trade-Offs (Why X over Y), and 10x Scale Redesign


* **Project 2 (Secondary System / Migration)**
* `[1 Hr]` Draw Complete End-to-End Architecture on Excalidraw & Isolate Personal Contribution ("I" vs. "We")
* `[1 Hr]` Document Quantitative Impact Metrics (p99 Latency, Throughput, Cost Reduction) & Live Q&A Defense



### 5.2 Behavioral STAR Story Matrix — [8 Hours]

* **Technical Ownership & Crisis Management**
* `[1 Hr]` Draft & Refine Story 1: Critical Production Outage (Root-cause diagnosis under pressure + Post-mortem fix)
* `[1 Hr]` Draft & Refine Story 2: Performance / Cost Optimization (Profiling bottleneck + Before/After metrics)
* `[1 Hr]` Draft & Refine Story 3: Ambiguous Requirement Ownership (Taking a vague problem to production launch)


* **Conflict, Trade-Offs & Leadership**
* `[1 Hr]` Draft & Refine Story 4: Technical Disagreement with Senior/Manager (Using POC/Benchmarks to align)
* `[1 Hr]` Draft & Refine Story 5: Tight Deadline Trade-Off (Incurring calculated technical debt + Repayment plan)
* `[1 Hr]` Draft & Refine Story 6: Mentorship & Operational Excellence (Code review standards, CI/CD, onboarding SDE-1s)
* `[1 Hr]` Draft & Refine Story 7: Hard Engineering Failure / Mistake (Owning a flawed design decision + Remediation)
* `[1 Hr]` Draft & Refine Story 8: GenAI Engineering Workflow (Accelerating delivery while enforcing quality/verification guardrails)



---

## 6. Workstream 6: Environment, Tooling & Resume Engineering — [5 Hours]

### 6.1 Local Coding & Whiteboard Setup — [3 Hours]

* **IDE & Build Readiness**
* `[1 Hr]` Configure Local IDE Project Template with Dependencies, Linter, and One-Click Unit Test Runner
* `[1 Hr]` Configure Live Code Templates / Snippets for Boilerplate (Fast I/O, Custom Exceptions, Test Setup)


* **Whiteboard Speed Setup**
* `[1 Hr]` Build Excalidraw Custom Shape Library (Load Balancers, Kafka, DB Cylinders, Cache) & Memorize Hotkeys



### 6.2 Resume & Profile Engineering — [2 Hours]

* **Impact-Driven Rewrite**
* `[1 Hr]` Rewrite Resume Experience Bullets using `[Action Verb] + [Architecture/Mechanism] + [Quantified Metric]`
* `[1 Hr]` Optimize LinkedIn Headline, Skills Matrix, and Referral Pitch Templates for Target Companies



---

## 7. Workstream 7: Code Review, Bug Hunting & Refactoring — [8 Hours]

### 7.1 Pull Request Audit Pillars — [5 Hours]

* **Systematic Bug Detection Drills**
* `[1 Hr]` Audit Drill 1 (Concurrency Bugs): Spot Check-Then-Act races, unsafe collections, and lock-ordering deadlocks
* `[1 Hr]` Audit Drill 2 (Resource & Transaction Leaks): Spot unclosed streams and HTTP calls inside `@Transactional` blocks
* `[1 Hr]` Audit Drill 3 (Performance Bottlenecks): Spot DB/RPC calls inside loops, unbounded queries, and memory bloat
* `[1 Hr]` Audit Drill 4 (Data Precision & Edge Cases): Spot floating-point currency errors, timezone bugs, and null traps
* `[1 Hr]` Audit Drill 5 (Security Flaws): Spot SQL injection concatenation, PII log leaks, and broken object-level auth (IDOR)



### 7.2 Hands-On Legacy Debugging & Refactoring — [3 Hours]

* **Live Codebase Drills**
* `[1 Hr]` Clone an unfamiliar multi-file repo, run failing test suite, and trace stack traces/breakpoints to fix 3 bugs
* `[1 Hr]` Refactor a legacy 300-line God Class into modular, unit-tested Strategy and Service classes under a 45-min timer
* `[1 Hr]` Add a new feature to an existing legacy codebase using Test-Driven Development (TDD) without breaking existing tests



---

## 8. Workstream 8: Production Operations, Observability & Resilience — [10 Hours]

### 8.1 Observability Stack — [4 Hours]

* **Telemetry & Service Health**
* `[1 Hr]` Metrics Engineering: Counter vs. Gauge vs. Histogram, and calculating p50, p95, and p99 latencies in Prometheus
* `[1 Hr]` Structured Logging: JSON log schemas, log levels, PII masking, and ELK/Loki indexing rules
* `[1 Hr]` Distributed Tracing: OpenTelemetry spans, propagating `Trace-ID`/`Correlation-ID` across HTTP and Kafka headers
* `[1 Hr]` Reliability Contracts: Defining SLIs, SLOs, SLAs, Error Budgets, and Actionable Alert Thresholds



### 8.2 Safe Deployment & Release Mechanics — [2 Hours]

* **Zero-Blast-Radius Releases**
* `[1 Hr]` Deployment Strategies: Rolling vs. Blue-Green vs. Automated Canary Rollouts with metric-based auto-rollback
* `[1 Hr]` Feature Flag Architecture: Dynamic percentage rollouts, user-cohort targeting, and instant kill-switches



### 8.3 Fault Tolerance & Chaos Engineering — [4 Hours]

* **Resilience Patterns**
* `[1 Hr]` Circuit Breaker Pattern: Implementing Closed → Open → Half-Open state transitions (Resilience4j / Hystrix concepts)
* `[1 Hr]` Retry Engineering: Exponential Backoff with Full Jitter & Preventing Retry Storms / Thundering Herds
* `[1 Hr]` Bulkhead Pattern: Isolating thread pools and connection pools per downstream dependency + Load Shedding
* `[1 Hr]` Graceful Degradation: Designing stale-cache fallbacks and default responses when critical dependencies fail



---

## 9. Workstream 9: API Engineering & Security Architecture — [9 Hours]

### 9.1 Production API Design — [5 Hours]

* **Resilient & Evolvable Contracts**
* `[1 Hr]` RESTful Resource Modeling: Proper HTTP verbs, status codes (`201`, `202`, `409`, `422`, `429`), and RFC 7807 error payloads
* `[1 Hr]` Idempotent API Engine: Designing `Idempotency-Key` middleware with Redis atomic locks and response caching
* `[1 Hr]` Webhook Architecture (Inbound & Outbound): HMAC-SHA256 signature verification, replay-attack timestamps, and retry queues
* `[1 Hr]` API Versioning & Deprecation: URI vs. Header versioning and zero-breakage contract transitions
* `[1 Hr]` Schema Evolution: Forward and backward compatibility rules in Protobuf (gRPC) and Apache Avro (Kafka Schema Registry)



### 9.2 Authentication & Authorization Architecture — [4 Hours]

* **Identity & Access Control**
* `[1 Hr]` OAuth 2.0 & OIDC Flows: Authorization Code Flow with PKCE vs. Client Credentials (Service-to-Service)
* `[1 Hr]` Token Architecture: Stateless JWT (Signature verification, short TTL, Refresh Token rotation) vs. Stateful Opaque Sessions
* `[1 Hr]` Access Control Models: Implementing RBAC (Role-Based) vs. ABAC (Attribute-Based) at Gateway and Service layers
* `[1 Hr]` Web & API Security Hardening: Mitigating CORS misconfigurations, CSRF, SSRF, and DDoS at the Edge/WAF



---

## 10. Workstream 10: Language Runtime Internals & Interview Funnel — [15 Hours]

### 10.1 Primary Language & Runtime Internals — [6 Hours]

* **Memory, Garbage Collection & Execution Engine**
* `[1 Hr]` Memory Model Internals: Stack vs. Heap generations (Eden, Survivor, Tenured / Escape Analysis) and Out-Of-Memory diagnosis
* `[1 Hr]` Garbage Collection Mechanics: Mark-and-Sweep, Generational GC (G1GC / ZGC / Tricolor Marking), and tuning GC pause spikes
* `[1 Hr]` Concurrency Runtime: OS Kernel Threads vs. Lightweight Runtime Threads (Virtual Threads / Goroutines / Event Loop phases)
* `[1 Hr]` Asynchronous Execution Internals: Futures / Promises / `async-await` state machines and non-blocking I/O multiplexing (`epoll`/`kqueue`)
* `[1 Hr]` Database Connection Pool Internals: Tuning max pool size, connection timeout, idle eviction, and detecting connection leaks
* `[1 Hr]` Memory Profiling & Thread Dumps: Analyzing Flamegraphs, Heap Dumps, and Thread Dumps to diagnose CPU spikes and deadlocks



### 10.2 Mock Interviews & Funnel Execution — [9 Hours]

* **Funnel Strategy & Scheduling**
* `[1 Hr]` Target Company Mapping: Categorize 30 companies into Tier B (Warm-up) and Tier A (Target) + Trigger Referral Outreach


* **Full-Length Timed Mock Interviews + Debriefs**
* `[1 Hr]` Live Mock 1: 60-Minute DSA Plain-Editor Round
* `[1 Hr]` Mock 1 Debrief: Fix communication gaps, edge-case blindness, and dry-run pacing
* `[1 Hr]` Live Mock 2: 90-Minute Machine Coding / LLD Round (Core build + live requirement twist)
* `[1 Hr]` Mock 2 Debrief: Refactor SOLID violations and optimize IDE typing speed
* `[1 Hr]` Live Mock 3: 60-Minute High-Level System Design (HLD) Round on Excalidraw
* `[1 Hr]` Mock 3 Debrief: Audit time allocation across Requirements, Schema, Architecture, and Deep-Dive bottlenecks
* `[1 Hr]` Live Mock 4: 60-Minute Hiring Manager (HM) / Bar Raiser Round (Project Whiteboard + STAR grilling)
* `[1 Hr]` Mock 4 Debrief: Sharpen metric articulation and "I vs. We" ownership framing



---

## Summary of the 200-Hour Atomic Tree

| Workstream | Pillars | Total 1-Hour Leaf Nodes |
| --- | --- | --- |
| **1. Data Structures & Algorithms (DSA)** | Data Structures (24) + Algorithms (48) | **72 Hours** |
| **2. Low-Level Design (LLD) & Machine Coding** | OOP (2) + Patterns (6) + Harness (3) + 8 Builds (16) | **27 Hours** |
| **3. High-Level System Design (HLD)** | DB Internals (8) + Infra Blocks (10) + 12 Blueprints (12) | **30 Hours** |
| **4. Concurrency & Core CS Internals** | Multithreading (5) + DB Locking (3) + Networking (4) | **12 Hours** |
| **5. Resume Architecture & Behavioral (HM)** | Project Deep-Dives (4) + 8 STAR Stories (8) | **12 Hours** |
| **6. Environment, Tooling & Resume** | IDE/Excalidraw Setup (3) + Resume Rewrite (2) | **5 Hours** |
| **7. Code Review, Bug Hunting & Refactoring** | 5 PR Audit Pillars (5) + Legacy Refactoring (3) | **8 Hours** |
| **8. Production Ops, Observability & Resilience** | Observability (4) + Releases (2) + Fault Tolerance (4) | **10 Hours** |
| **9. API Engineering & Security Architecture** | API Design (5) + AuthN/AuthZ Security (4) | **9 Hours** |
| **10. Runtime Internals & Interview Funnel** | Runtime Internals (6) + Mocks & Funnel (9) | **15 Hours** |
| **Total Curriculum** | **All 10 Workstreams** | **200 Hours** |