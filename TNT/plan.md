### The 60-Minute Daily Execution Blueprint

Every single day is structured into three dedicated segments so you never waste time deciding what to do once the timer starts:

```
┌─────────────────────────┬───────────────────────────────┬────────────────────────────┐
│  00 – 10 min (10 min)   │     10 – 45 min (35 min)      │    45 – 60 min (15 min)    │
│  Flash Recall & Review  │  Deep Concept / Syntax Study  │ Hands-on / Drill / Cheats  │
└─────────────────────────┴───────────────────────────────┴────────────────────────────┘

```

* **Minutes 00–10:** Active recall of the previous day's formula, command flags, or algorithm without looking at notes.
* **Minutes 10–45:** Focused study of that day's specific theory, mechanics, or syntax.
* **Minutes 45–60:** Terminal command execution, manual tracing of pointer/scheduling problems, or writing 3 targeted queries. Record any non-obvious quirks into an **Exam-Day Cheat Binder**.

---

### Phase 1: Linux CLI, System Administration & Shell Scripting

*(Covers Stage 2 Trade Test + Operating System practical foundations)*

| Day | Primary Subject | Minutes 10–45: Deep Concept Study | Minutes 45–60: Practical / Problem Drill |
| --- | --- | --- | --- |
| **Day 1** | Filesystem & Navigation | Filesystem hierarchy standard (`/`, `/bin`, `/etc`, `/var`, `/proc`, `/dev`); absolute vs. relative paths. | Execute in terminal: `pwd`, `cd`, `ls -lah`, `tree`, `mkdir -p dir1/dir2`, `rmdir`, `touch file{1..5}.txt`. |
| **Day 2** | File Manipulation | Inode metadata concepts; file creation and moving mechanisms. | Execute: `cp -riv`, `mv -iv`, `rm -rf`, verify inode IDs with `ls -i` and examine file signatures with `file *`. |
| **Day 3** | Content Inspection | Streaming file contents; paging utilities vs. direct dumping. | Practice: `cat -n`, `tac`, navigate large system logs using `less` and `more`; test `head -n 20` and live tracking via `tail -f /var/log/syslog`. |
| **Day 4** | Permissions & Umask | Octal values (4, 2, 1) and symbolic representations (r, w, x, u, g, o, a); default creation permissions and `umask` arithmetic. | Calculate umask changes (`umask 027`); apply `chmod 755`, `chmod u=rwx,go=rx`, and practice recursive ownership with `chown -R user:group`. |
| **Day 5** | Special Bits & Links | SUID (`4000`), SGID (`2000`), and Sticky Bit (`1000`, `/tmp` mechanics); Hard links vs. Symbolic (soft) links. | Create hard and soft links with `ln` and `ln -s`; delete source targets to observe link behaviors; verify link counts via `ls -l`. |
| **Day 6** | System File Searching | Index-based searching vs. recursive directory traversal; search constraints by size, modification date, and ownership. | Execute: `find /etc -type f -name "*.conf"`, find files larger than 10M (`-size +10M`), and execute actions: `find . -type f -name "*.tmp" -exec rm {} \;`. |
| **Day 7** | Regex & Pattern Matching | Regular expression syntax: anchors (`^`, `$`), wildcards (`.`), quantifiers (`*`, `+`, `?`), character classes (`[a-z]`, `[^0-9]`). | Execute: `grep -E` patterns on `/etc/passwd`; practice flags: `-i` (case-insensitive), `-v` (invert), `-c` (count), `-n` (line numbers), `-r` (recursive). |
| **Day 8** | Streams, Pipes & Filters | Standard streams: stdin (0), stdout (1), stderr (2); redirecting and appending (`>`, `>>`, `2>`, `&>`); pipes (`|`). | Chain commands: `cat /etc/passwd | cut -d: -f1,7 | sort | uniq -c | sort -nr`; practice translations with `tr '[a-z]' '[A-Z]'`. |
| **Day 9** | Stream Editing (Sed & Awk) | Non-interactive stream editing: syntax of substitute command `s/find/replace/g`; Awk record and field processing (`$0`, `$1`, `NF`, `NR`). | Run: `sed -i.bak 's/localhost/127.0.0.1/g' test.txt`; process process tables: `ps aux | awk '{if ($3 > 5.0) print $1, $2, $3}'`. |
| **Day 10** | Process Lifecycle & Signals | Process hierarchy (PID, PPID, init/systemd); process states (Running, Sleeping, Zombie, Orphan); Linux signals (`SIGTERM 15`, `SIGKILL 9`, `SIGHUP 1`). | Inspect system load with `top` and `ps -ef`; simulate background process (`sleep 200 &`), inspect using `jobs`, and terminate via `kill -9 <PID>`. |
| **Day 11** | Storage & User Management | `/etc/passwd`, `/etc/shadow`, `/etc/group` structures; mount points, partition tables, disk block usage. | Run `df -h`, `du -sh *`, `lsblk`, `fdisk -l`; create a test user: `useradd -m -s /bin/bash testuser`, modify via `usermod -aG sudo testuser`. |
| **Day 12** | Services & Automation | Systemd unit architecture; service lifecycle control; cron expression format (minute, hour, day-of-month, month, day-of-week). | Query services using `systemctl status/start/stop/restart/enable`; edit crontab with `crontab -e` to schedule a 5-minute health check script. |

---

### Phase 2: Operating Systems Architecture

*(Covers Stage 1 Paper 2 Theory)*

| Day | Primary Subject | Minutes 10–45: Deep Concept Study | Minutes 45–60: Practical / Problem Drill |
| --- | --- | --- | --- |
| **Day 13** | Kernel & Dual-Mode Ops | User mode vs. Kernel mode; Mode bit transitions; System calls vs. Library functions; Interrupts, traps, and context switches. | Trace system calls of simple binaries using `strace ls`; document the sequence of events during a software interrupt. |
| **Day 14** | Process Control Block & IPC | PCB structures (register states, open files, memory limits); Inter-Process Communication mechanisms: shared memory vs. message passing. | Write down the full 7-state process transition diagram from memory; trace PCB state changes on suspension and preemption. |
| **Day 15** | Non-Preemptive Scheduling | FCFS scheduling and the Convoy Effect; Shortest Job First (SJF) and its theoretical optimality for minimum average waiting time. | Draw Gantt charts and compute Turnaround Time (TAT) and Waiting Time (WT) for a 4-process set under FCFS and SJF. |
| **Day 16** | Preemptive CPU Scheduling | Shortest Remaining Time First (SRTF); Round Robin (time quantum trade-offs: context switch overhead vs. response latency). | Calculate TAT and WT for a given process table under Round Robin with quanta $q=2$ and $q=4$; identify thrashing due to small quanta. |
| **Day 17** | Priority & Multilevel Queues | Priority scheduling (preemptive vs. non-preemptive) and priority inversion; Multilevel Queue and Multilevel Feedback Queue (MLFQ) rules. | Solve a numerical problem involving priority-based preemption with aging mechanisms applied to prevent starvation. |
| **Day 18** | Concurrency & Critical Section | Race conditions; the Critical Section problem; the 3 mandatory criteria: Mutual Exclusion, Progress, and Bounded Waiting. | Analyze hardware-assisted solutions: Test-and-Set and Swap instructions; identify why disabling hardware interrupts fails on multiprocessors. |
| **Day 19** | Peterson's Algorithm & Mutex | Peterson’s two-process solution (code analysis, flags, turn variable); Spinlocks; Mutex locks and locking semantics. | Manually step through Peterson's solution showing mutual exclusion holds even when context switching occurs after flag assertion. |
| **Day 20** | Semaphores & Synchronization | Counting semaphores vs. Binary semaphores; Atomic definitions of `wait()` ($P$) and `signal()` ($V$); Busy waiting vs. Blocked queues. | Implement a pseudocode synchronization barrier for 3 cooperating threads using counting semaphores. |
| **Day 21** | Classical IPC Problems | Bounded-Buffer (Producer-Consumer) problem; Readers-Writers problem (reader-preference vs. writer-preference starvation). | Write the semaphore-based solution for the Producer-Consumer problem using `mutex`, `empty`, and `full` semaphores; verify deadlock freedom. |
| **Day 22** | Deadlock Conditions & Detection | 4 Coffman conditions: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait; Resource Allocation Graphs (RAG); cycle vs. knot rules. | Given a resource graph with single-unit vs. multi-unit resources, identify whether a knot exists and declare deadlock certainty. |
| **Day 23** | Deadlock Avoidance (Banker's) | Safe state vs. Unsafe state; Banker’s Algorithm matrices: Allocation, Max, Need ($Need = Max - Allocation$), and Available. | Calculate the Need Matrix and step through the Safety Algorithm for a 5-process, 3-resource instance; find the valid Safe Sequence. |
| **Day 24** | Memory: Contiguous Allocation | Base and Limit registers; Fixed vs. Dynamic partitioning; Internal vs. External fragmentation; Allocation strategies: First-Fit, Best-Fit, Worst-Fit. | Solve a memory allocation problem: Place a sequence of process requests into variable memory partitions using First-Fit and Best-Fit. |
| **Day 25** | Paging & Address Translation | Paging architecture; Logical address split (Page Number $p$, Offset $d$); Physical address computation (Frame Number $f$, Offset $d$); Page table sizing. | Calculate page sizes and total page table size given a 32-bit logical address space and 4 KB page frames. |
| **Day 26** | TLB & Effective Memory Access | Translation Lookaside Buffer (TLB); TLB hit ratio ($\alpha$), TLB access time, main memory access time; Effective Memory Access Time (EMAT) calculations. | Solve 3 EMAT numerical problems: Compute EMAT with 90% TLB hit ratio, 20 ns TLB search time, and 100 ns main memory access time. |
| **Day 27** | Virtual Memory & Inverted Tables | Multi-level paging index computation; Inverted page tables; Demand paging; Page fault service routine (PFSR) cycle. | Compute the effective access time of a demand-paged system given a page fault rate $p=0.002$ and disk service latency of 8 milliseconds. |
| **Day 28** | Page Replacement Algorithms | First-In-First-Out (FIFO) and Belady’s Anomaly; Optimal Page Replacement (OPT); Least Recently Used (LRU) and stack algorithms. | Trace a reference string of 12 page requests through 3 and 4 page frames using FIFO (demonstrating Belady's Anomaly) and LRU. |
| **Day 29** | Thrashing & Working Set Model | Cause of thrashing; Degree of multiprogramming; Page Fault Frequency; Working Set Model ($\Delta$ window sizing). | Draw the CPU utilization vs. degree of multiprogramming curve; solve a numerical problem finding working-set memberships at time $t$. |
| **Day 30** | Disk Scheduling & File Systems | Disk hardware geometry; Seek time, rotational latency, transfer time; Disk scheduling algorithms: FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK. | Calculate the total head movement in cylinders for a given cylinder request queue using SSTF and C-SCAN. |

---

### Phase 3: Computer Networks, Protocols & Network Administration

*(Covers Stage 1 Paper 2 Theory + Stage 2 Trade Test Cabling/Config)*

| Day | Primary Subject | Minutes 10–45: Deep Concept Study | Minutes 45–60: Practical / Problem Drill |
| --- | --- | --- | --- |
| **Day 31** | Network Models & Layering | OSI 7-Layer model vs. TCP/IP 4-Layer model; Service primitives; Encapsulation and Decapsulation through the stack. | Map 15 common network protocols (DNS, BGP, ARP, ICMP, TCP, OSPF, etc.) to their exact corresponding OSI layer. |
| **Day 32** | Physical Media & Cabling | Guided media: UTP/STP categories (CAT5e, CAT6), Coaxial, Single-mode vs. Multimode Fiber; Straight-through vs. Crossover wiring standards. | Memorize T568A and T568B pinout color codes; document the exact wiring sequences for connecting PC-to-Switch vs. PC-to-PC. |
| **Day 33** | Framing & Error Detection | Character count, byte stuffing, bit stuffing (01111110 delimiter); Parity checks, Checksum calculation, Cyclic Redundancy Check (CRC). | Perform a step-by-step polynomial division for a 7-bit data block using CRC generator polynomial $G(x) = x^3 + x + 1$. |
| **Day 34** | Flow Control & MAC Protocols | Stop-and-Wait ARQ; Go-Back-N ARQ; Selective Repeat ARQ (window sizes, buffer requirements, link utilization formulas). | Calculate link utilization and optimal sender window size given bandwidth, round-trip time, and packet size. |
| **Day 35** | Medium Access Control | Pure ALOHA vs. Slotted ALOHA (throughput derivations $S = G e^{-2G}$ and $S = G e^{-G}$); CSMA/CD collision detection mechanics; CSMA/CA. | Calculate maximum throughput efficiency of slotted ALOHA; determine minimum frame size needed in CSMA/CD to detect collisions. |
| **Day 36** | IPv4 Structure & Classes | Classful addressing ranges (A, B, C, D, E); Default masks; Reserved addresses: Loopback (`127.0.0.0/8`), Private subnets (RFC 1918 ranges). | Identify class, network address, and host portion for 6 distinct IP strings; calculate maximum usable hosts per class. |
| **Day 37** | Subnetting Fundamentals (FLSM) | Fixed-Length Subnet Masking; Borrowing host bits for network identification; Subnet mask binary representation; Usable host formulas ($2^h - 2$). | Given IP `192.168.10.0/24`, divide it into 4 equal subnets: compute the subnet mask, network ID, first/last host, and broadcast ID for each. |
| **Day 38** | CIDR & VLSM Problem Solving | Classless Inter-Domain Routing notation; Variable-Length Subnet Masking; Route summarization (Supernetting) principles. | Solve a departmental VLSM layout problem: Assign subnets for 3 departments needing 60, 28, and 12 hosts from a single `/24` pool. |
| **Day 39** | IPv4 Header & Packet Analysis | Detailed header fields: Version, IHL, Type of Service, Total Length, Identification, Flags (DF, MF), Fragment Offset, TTL, Header Checksum. | Calculate packet fragmentation: Determine fragments, offset values, and MF flags for a 4000-byte datagram passing through an MTU of 1500 bytes. |
| **Day 40** | Address Resolution & ICMP | ARP cache mechanics; Gratuitous ARP; RARP; ICMP error message types (`Destination Unreachable`, `Time Exceeded`, `Redirect`). | Execute `arp -a` in the terminal; clear cache using `arp -d`; trace the exact round-trip ARP exchange before the first ping packet fires. |
| **Day 41** | Routing Architectures (Intra-AS) | Distance Vector Routing (Bellman-Ford equation, Count-to-Infinity flaw, Split Horizon, Poison Reverse); Link State Routing (OSPF Dijkstra SPF). | Step through Dijkstra’s algorithm on a 5-node graph to derive the least-cost routing table for Node A. |
| **Day 42** | Autonomous Routing & NAT | Border Gateway Protocol (BGP) Path Vector mechanics; Network Address Translation (Static NAT, Dynamic NAT, Port Address Translation/PAT). | Diagram how a home router PAT table maps multiple internal private IP requests to a single public IP using unique source port numbers. |
| **Day 43** | Transport: TCP Connections | TCP segment anatomy; Port demultiplexing; 3-Way Handshake (`SYN`, `SYN-ACK`, `ACK`); 4-Way Connection Teardown; Sequence & ACK tracking. | Trace sequence and acknowledgment numbers for a 3-segment TCP exchange; explain the purpose and duration of the `TIME_WAIT` state. |
| **Day 44** | TCP Flow & Congestion Control | TCP sliding window (advertised receiver window `rwnd`); TCP Congestion Window (`cwnd`); Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery. | Draw the classic TCP Sawtooth curve; calculate the `cwnd` progression across transmission rounds when a timeout vs. 3 duplicate ACKs occur. |
| **Day 45** | UDP & Application Protocols | UDP header fields and zero-overhead utility; DNS hierarchy (Iterative vs. Recursive lookups, A, AAAA, CNAME, MX, PTR records); DHCP DORA process. | Run `dig` and `nslookup` on a domain; inspect DNS query responses and identify authoritative name server records. |
| **Day 46** | Network Devices, VLANs & CLI | Hubs vs. Layer 2 Switches vs. Layer 3 Switches; Collision vs. Broadcast domains; Virtual LANs (VLAN 802.1Q tagging); Diagnostic CLI. | Run and interpret outputs: `ping -c 4`, `traceroute`, `netstat -tulnp`, `ss -s`, `ip addr show`, `ip route show`. |

---

### Phase 4: Database Management Systems & Relational Design

*(Covers Stage 1 Paper 2 Theory + Stage 2 Trade Test SQL Tasks)*

| Day | Primary Subject | Minutes 10–45: Deep Concept Study | Minutes 45–60: Practical / Problem Drill |
| --- | --- | --- | --- |
| **Day 47** | Architecture & ER Modeling | 3-Schema Architecture; Logical vs. Physical Data Independence; Entity types, Attributes (simple, composite, multivalued, derived), Keys. | Draw an ER diagram for a University Lab Inventory system; correctly mark cardinality ratios (1:1, 1:N, M:N) and participation constraints. |
| **Day 48** | Relational Model & Mapping | Relational schemas; Candidate Keys, Super Keys, Primary Keys, Foreign Keys, Referential Integrity; Converting ER diagrams to tables. | Convert an M:N relationship with multi-valued attributes into relational schemas, minimizing redundant tables. |
| **Day 49** | Relational Algebra Operations | Fundamental operators: Selection ($\sigma$), Projection ($\pi$), Cartesian Product ($\times$), Union ($\cup$), Set Difference ($-$), Rename ($\rho$). | Write relational algebra expressions to retrieve student names enrolled in "Operating Systems" but not enrolled in "Database Systems". |
| **Day 50** | Joins & Calculus | Join operations: Natural Join ($\bowtie$), Theta Join, Equi-Join, Outer Joins (Left, Right, Full); Tuple Relational Calculus (TRC) basics. | Formulate relational queries on a standard Employee-Department schema comparing Natural Join vs. Cartesian Product with Selection. |
| **Day 51** | SQL: Table Creation & Constraints | DDL commands: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`; Integrity constraints (`PRIMARY KEY`, `FOREIGN KEY ON DELETE CASCADE`, `CHECK`, `NOT NULL`). | Write a clean SQL script to create two relational tables (`Departments` and `Employees`) enforcing referential integrity and checks. |
| **Day 52** | SQL: Data Filtering & Aggregation | DQL/DML: `INSERT`, `UPDATE`, `DELETE`; `SELECT` clauses: `WHERE`, `ORDER BY`, `DISTINCT`, `LIMIT`; Aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`). | Write SQL queries to find total salary paid per department where employee count exceeds 5, using `GROUP BY` and `HAVING`. |
| **Day 53** | SQL: Complex Joins & Set Ops | Multi-table joins; Syntax and operational differences between `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`, `UNION`, `UNION ALL`. | Write a query to list all departments alongside their employees, ensuring departments with zero active employees still appear in the output. |
| **Day 54** | SQL: Nested & Correlated Queries | Subqueries in `WHERE` and `FROM` clauses; Subquery operators: `IN`, `EXISTS`, `NOT EXISTS`, `ALL`, `ANY`; Correlated subquery mechanics. | Write a query to find the 2nd highest salary in an organization without using the `LIMIT` or `TOP` keywords. |
| **Day 55** | Functional Dependencies & Closure | Functional Dependency (FD) definition; Armstrong’s Axioms; Attribute closure algorithm ($X^+$); Deriving Candidate Keys from FD sets. | Given relational schema $R(A, B, C, D, E)$ and FD set $\{A \rightarrow BC, CD \rightarrow E, B \rightarrow D\}$, find all candidate keys. |
| **Day 56** | Normalization (1NF, 2NF, 3NF) | Anomalies (Insertion, Deletion, Update); Normal forms definitions: 1NF (atomic values), 2NF (no partial dependency), 3NF (no transitive dependency). | Given a relation with functional dependencies, identify its highest normal form and decompose it step-by-step into 3NF. |
| **Day 57** | BCNF & Decomposition Testing | Boyce-Codd Normal Form (BCNF); Lossless/Non-additive Join Decomposition test; Dependency Preservation test. | Test whether decomposing relation $R(A,B,C)$ with $\{AB \rightarrow C, C \rightarrow B\}$ into $R_1(A,C)$ and $R_2(B,C)$ is lossless and dependency preserving. |
| **Day 58** | Transactions & Concurrency Control | ACID properties; Transaction states; Conflict serializability (testing via Precedence Graphs); Two-Phase Locking (Strict 2PL vs. Rigorous 2PL). | Draw a precedence graph for an interleaved schedule of 3 transactions; evaluate whether the schedule is conflict serializable. |

---

### Phase 5: C Programming, Pointer Mechanics & Data Structures

*(Covers Stage 1 Paper 2 Theory + Trade Test Debugging)*

| Day | Primary Subject | Minutes 10–45: Deep Concept Study | Minutes 45–60: Practical / Problem Drill |
| --- | --- | --- | --- |
| **Day 59** | C Basics, Types & Bitwise Ops | Variable types, modifiers (`unsigned`, `short`), Type casting rules; Operator precedence and associativity; Bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`). | Solve 5 tricky precedence and bitwise expression evaluations: e.g., checking if an integer is a power of 2 using `(x & (x - 1)) == 0`. |
| **Day 60** | Control Flow & Storage Classes | Loop controls (`break`, `continue`, `goto`); Storage classes: `auto`, `register`, `static` (local vs. global scope), and `extern`. | Predict the output of nested recursive loops and static variable increments across repeated function calls. |
| **Day 61** | Pointer Mechanics & Memory | Memory addresses; Pointer declaration, dereferencing (`*`, `&`); Pointer arithmetic rules (scaling by `sizeof(T)`); Pointers to pointers (`**ptr`). | Manually trace pointer address increments and value updates across a 2D integer array; write down the memory grid layout. |
| **Day 62** | Arrays, Strings & Char Pointers | Array decay to pointers; Multidimensional array row-major addressing; String termination (`\0`); `strcpy`, `strlen`, `strcmp` internals. | Write a custom, pointer-based implementation of string copy (`void my_strcpy(char *dest, const char *src)`) without library functions. |
| **Day 63** | Dynamic Memory Management | Dynamic allocation on the heap: `malloc()`, `calloc()`, `realloc()`, `free()`; Dangling pointers, Memory leaks, and Segmentation faults. | Write a C snippet allocating a dynamic 2D array, ensuring every row is allocated and properly freed in reverse sequence. |
| **Day 64** | Structures & Union Mechanics | Struct padding, memory alignment rules, structure offsets; Bit-fields; Unions and memory sharing. | Calculate the exact `sizeof` a struct containing mixed data types (char, int, double) considering 32-bit and 64-bit alignment boundaries. |
| **Day 65** | OOP Concepts (C++ / Python) | Encapsulation, Abstraction, Inheritance (single, multiple, diamond problem), Polymorphism (function overloading vs. virtual functions/overriding). | Trace virtual table (`vtable`) and virtual pointer (`vptr`) lookups during runtime polymorphism in C++. |
| **Day 66** | Linear Structures: Lists & Stacks | Singly linked list operations (insertion, deletion, traversal); Stack LIFO mechanics; Array vs. linked list representations of stacks. | Write code to reverse a singly linked list iteratively in $O(n)$ time and $O(1)$ extra auxiliary memory space. |
| **Day 67** | Stack Applications & Queues | Infix, Postfix, and Prefix conversions; Postfix expression evaluation using a stack; Queues (FIFO), Circular Queues, and Priority Queues. | Manually convert an infix expression containing parenthesis and exponentiation into its equivalent postfix string using an operator stack. |
| **Day 68** | Trees, Traversals & BST | Binary Tree terminology; Tree traversals (Inorder, Preorder, Postorder); Binary Search Tree (BST) property, search, and insertion. | Construct a unique Binary Tree given its Inorder and Preorder traversal sequences; compute its maximum height. |
| **Day 69** | Heap, Priority Queues & Sorting | Complete Binary Tree; Min-Heap and Max-Heap array mapping; Heapify operation; Sorting algorithms: Bubble, Insertion, Selection, Merge, Quick Sort. | Trace Quick Sort partition steps on an array of 8 integers; determine best, average, and worst-case time complexities. |
| **Day 70** | Asymptotic Complexity Analysis | Asymptotic notations ($O$, $\Omega$, $\Theta$); Recurrence relations: Substitution method, Recursion Tree method, Master Theorem for divide-and-conquer. | Solve 4 recurrence relations using the Master Theorem: e.g., $T(n) = 2T(n/2) + n$, $T(n) = 4T(n/2) + n^2$, $T(n) = 2T(n/2) + n \log n$. |

---

### Phase 6: Digital Logic, Computer Organization & Hardware

*(Covers Stage 1 Paper 2 Theory + Stage 2 Lab Maintenance)*

| Day | Primary Subject | Minutes 10–45: Deep Concept Study | Minutes 45–60: Practical / Problem Drill |
| --- | --- | --- | --- |
| **Day 71** | Number Systems & Codes | Conversions between Binary, Octal, Decimal, Hexadecimal; 1's and 2's complement representations; Overflow rules in signed arithmetic. | Perform 8-bit 2's complement subtraction; identify whether arithmetic overflow has occurred based on carry-in and carry-out of the MSB. |
| **Day 72** | Boolean Algebra & K-Maps | Boolean theorems; Sum of Products (SOP) and Product of Sums (POS); Karnaugh Maps (2, 3, and 4 variables); Implicants and Essential Prime Implicants. | Minimize a 4-variable boolean function with don't-care conditions using a 4x4 K-Map. |
| **Day 73** | Combinational Circuit Modules | Half Adder, Full Adder, Ripple Carry Adder; Multiplexers (MUX) as universal logic modules; Demultiplexers, Decoders, Encoders. | Implement an XOR gate and a Full Adder using exclusively 4:1 Multiplexers. |
| **Day 74** | Sequential Circuits & Flip-Flops | Latches vs. Flip-Flops; SR, JK, D, and T Flip-Flops; Race-around condition in JK; Master-Slave Flip-Flops; Setup and Hold times. | Complete the characteristic tables, excitation tables, and state transition equations for D and JK Flip-Flops. |
| **Day 75** | Registers & Counters | Shift Registers (SISO, SIPO, PISO, PIPO); Asynchronous (Ripple) Counters vs. Synchronous Counters; Modulo-$N$ counter design. | Design a Mod-6 synchronous counter using JK Flip-Flops; derive the next-state table and flip-flop excitation inputs. |
| **Day 76** | Computer Organization Basics | Von Neumann vs. Harvard architecture; Instruction cycle (Fetch, Decode, Execute phases); Program Counter, Instruction Register, Accumulator. | Trace data bus and address bus contents during an indirect memory-reference instruction execution cycle. |
| **Day 77** | Cache Memory Architecture | Cache mapping techniques: Direct Mapped, Fully Associative, Set-Associative; Cache replacement policies (LRU); Write-through vs. Write-back. | Calculate Tag, Set Index, and Word Offset bit fields for a 64 KB 4-way set-associative cache connected to a 32-bit physical address space. |
| **Day 78** | PC Hardware & Diagnostics | Motherboard anatomy: Chipsets, PCIe lanes, RAM channels (DDR4 vs. DDR5), SATA vs. M.2 NVMe; BIOS/UEFI; MBR vs. GPT; RAID 0, 1, 5, 10. | Document troubleshooting procedures for: (1) System powering on with no display (beep codes), (2) Corrupted GRUB dual-bootloader recovery. |

---

### Phase 7: Paper 1 — Aptitude, Reasoning, English & Institutional Framework

*(Mandatory Stage 1 Screening & Merit Paper)*

| Day | Primary Subject | Minutes 10–45: Deep Concept Study | Minutes 45–60: Practical / Problem Drill |
| --- | --- | --- | --- |
| **Day 79** | Quant: Percentages & Ratios | Percentages, Profit and Loss, Marked Price, Discount formulations; Ratio, Proportion, and Mixtures. | Solve 8 timed arithmetic problems on successive percentage discounts and cost-price/selling-price ratios. |
| **Day 80** | Quant: Time, Work & Distance | Work efficiency formulas; Pipes & Cisterns; Time, Speed, Distance; Relative speed problems (trains passing platforms and opposite trains). | Solve 8 standard problems on pipes with alternate leaking and relative speeds of moving trains. |
| **Day 81** | Quant: Averages & Basic Algebra | Simple & Compound Interest (annual vs. half-yearly compounding); Weighted Averages; Ages; Arithmetic and Geometric Progressions. | Solve 6 compound interest rate difference calculations and average age transition problems. |
| **Day 82** | Reasoning: Logic & Sequences | Coding-Decoding logic; Direction Sense tests; Blood Relations (family tree mapping). | Solve 10 questions on complex coded blood relations and multi-point directional pathways. |
| **Day 83** | Reasoning: Analytical Deductions | Syllogisms (Venn diagram deduction rules, "Some", "All", "No", "Possibility" cases); Number & Alphabetical series completion. | Solve 8 three-statement syllogism problems, testing validity using Venn diagrams. |
| **Day 84** | Reasoning: Non-Verbal & Puzzles | Seating arrangements (Linear and Circular facing inward/outward); Matrix puzzles; Mirror images and paper folding patterns. | Solve 2 circular seating arrangements involving 8 individuals with mixed facing directions. |
| **Day 85** | English: Grammar & Error Spotting | Subject-Verb agreement rules; Prepositions of time and place; Correct usage of tenses, conditional sentences. | Identify errors across 15 standard sentences testing misplaced modifiers and subject-verb disagreements. |
| **Day 86** | English: Vocabulary & Comprehension | Active & Passive Voice conversion rules; Direct & Indirect Speech rules; Common idioms, phrases, and one-word substitutions. | Convert 10 complex sentences between voices and narrative speech; review 20 high-frequency institutional English vocabulary terms. |
| **Day 87** | General Awareness: Indian Polity | Key Articles of the Indian Constitution: Fundamental Rights (Art 12–35), DPSPs, Parliament (Lok Sabha/Rajya Sabha), President, Judiciary. | Solve 15 MCQs on Constitutional bodies, parliamentary quorum, and constitutional amendment procedures. |
| **Day 88** | General Awareness: Science & ICT | Milestones in Indian Science and Technology; Space missions; National supercomputing mission; Basics of cyber laws (IT Act 2000). | Review and memorize 25 factual questions on modern Indian scientific institutions and digital public infrastructure. |
| **Day 89** | Institutional Rules: CCS Conduct | Central Civil Services (Conduct) Rules 1964: General obligations, integrity, maintenance of secrecy, private trade/employment restrictions. | Read official summary notes on CCS Conduct Rules; solve 8 administrative case-scenario MCQs. |
| **Day 90** | Institutional Rules: CCS Leave | Central Civil Services (Leave) Rules 1972: Earned Leave (EL), Half Pay Leave (HPL), Commuted Leave, Maternity/Paternity Leave, Casual Leave (CL). | Solve 10 scenario-based MCQs on leave accumulation limits, encashment, and maximum continuous absence rules. |
| **Day 91** | Financial Rules: GFR 2017 & GeM | General Financial Rules (GFR 2017): Basic principles of public procurement; Government e-Marketplace (GeM) purchase thresholds and procurement modes. | Memorize direct purchase financial ceilings on GeM, L1 bidding thresholds, and tender types (Limited vs. Open Tenders). |
| **Day 92** | Institute Governance (NIT/IIT Acts) | NITSER Act 2007 & Institutes of Technology Act: Structure of the Board of Governors (BoG), Senate, Director's powers, Registrar's functions. | Review the statutory administrative hierarchy of NITs and IITs; solve 10 questions on institute-level decision-making bodies. |

---

### Phase 8: Trade Test Drills, Mock Exams & Synthesis

*(Consolidation & Final Polish)*

| Day | Primary Subject | Minutes 10–45: Deep Concept Study | Minutes 45–60: Practical / Problem Drill |
| --- | --- | --- | --- |
| **Day 93** | Trade Test Drill: Linux Bash | Scripting review: Command-line arguments (`$1`, `$#`), conditional loops, and exit status monitoring. | Write a full Bash script from scratch: Scan a directory, archive files older than 30 days into a compressed `.tar.gz`, and log the output. |
| **Day 94** | Trade Test Drill: Network Setup | Diagnostics review: Static IP configuration on Linux via `/etc/netplan` or `nmcli`; routing tables; DNS debugging. | Configure a virtual network interface with a static IP and gateway; verify packet route traces using `traceroute` and `ping`. |
| **Day 95** | Trade Test Drill: Advanced SQL | Multi-table joins and subquery syntax review; indexing for query optimization. | Under a 20-minute timer, write and execute 4 complex SQL queries on an employee-project-department relational database. |
| **Day 96** | Paper 1 Aptitude Mini-Mock | Timed test condition: 30 Questions across Quant, Reasoning, English, and CCS/GFR Rules. | Review every incorrect question; document specific formula mistakes in the cheat binder. |
| **Day 97** | Paper 2 CSE Core Mini-Mock | Timed test condition: 40 Questions across OS, Networks, DBMS, C Programming, and Hardware. | Analyze conceptual gaps; re-verify missed questions in OS and Networking. |
| **Day 98** | Full Comprehensive CBT Mock | Timed simulation: 100 Questions covering Paper 1 (30%) + Paper 2 (70%). | Score assessment and detailed error analysis; identify weak areas. |
| **Day 99** | Cheat Binder Review | Comprehensive read-through of all recorded formulas, Linux flags, and normal form conditions. | Rapid-fire flashcard session covering all networking port numbers, protocol headers, and scheduling algorithms. |
| **Day 100** | Final System Inspection | Complete mental walk-through of the Stage 2 Trade Test laboratory routine. | Physical bench check: RJ-45 crimping review, bootable USB preparation sequence, and final formula sheet sign-off. |

---
