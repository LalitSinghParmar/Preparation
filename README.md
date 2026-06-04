# 🚀 6-Month Dual-Track Technical Upskilling Roadmap (With MCP & AI Agent Frameworks)

## 🗓️ Phase 1: Asynchronous Architecture & Linux (Weeks 1–4)

### Week 1: Groundwork & The Synchronous Audit
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Contains Duplicate* & *Valid Anagram* in Python.
* [ ] **Daily Personal (System Design):** Study HTTP Methods (GET, POST, PUT, DELETE) and status codes (200, 400, 401, 500).
* [ ] **Daily Office:** Trace the flow of a certificate request. Document exactly how long a single request takes when calling VirusTotal and Gemini. Find the exact blocking code line.
* [ ] **Weekend Personal (CertPulse-AI):** Open Mac terminal, run `mkdir certpulse-ai`, set up a Python `venv`, install `fastapi` and `uvicorn`, and run a baseline "Hello World" API on localhost.

### Week 2: Native Parsing & Async Basics
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Two Sum* & *Group Anagrams*.
* [ ] **Daily Personal (System Design):** Read about the differences between Synchronous (Blocking) and Asynchronous (Non-blocking) code execution models.
* [ ] **Daily Office:** Create a duplicate branch of your office project. Use Cursor AI to rewrite just one third-party API call (like VirusTotal fetch) using Python's `asyncio` and `httpx` instead of `requests`.
* [ ] **Weekend Personal (CertPulse-AI):** Create a FastAPI endpoint that accepts a domain string, uses Python’s built-in `ssl` and `socket` libraries to grab the remote SSL certificate, and parses its SHA-1 hash.

### Week 3: Log Parsing & Advanced Terminal Commands
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Top K Frequent Elements* & *Valid Palindrome*.
* [ ] **Daily Personal (System Design):** Learn what an API Gateway does and why rate-limiting is crucial for public/AI endpoints.
* [ ] **Daily Office:** Expand your office async refactor. Apply `async/await` syntax to the Vertex AI / Gemini API call section of your Django app.
* [ ] **Weekend Personal (Secured Log Analyzer):** Create a second standalone FastAPI service repository. Write an endpoint that allows a user to upload a standard server `.log` file and saves it locally. Practice using Mac terminal tools (`grep`, `awk`) to manually filter that file.

### Week 4: Front-End Basics & Consolidating Phase 1
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Container With Most Water* & *Best Time to Buy/Sell Stock*.
* [ ] **Daily Personal (Linux):** Practice piping terminal commands together (e.g., `history | grep python` or `cat log.txt | grep "404"`).
* [ ] **Daily Office:** Benchmark your office refactor. Compare your new async branch against the old synchronous master branch to verify the UI doesn't lock up during spikes.
* [ ] **Weekend Personal (CertPulse-AI):** Build a basic HTML/CSS frontend with a simple input box and a display area. Use native JavaScript `fetch()` calls to display the parsed certificate details from your FastAPI backend.

---

## 🗓️ Phase 2: Docker, Databases & Task Queues (Weeks 5–8)

### Week 5: Database Migration & Postgres
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Longest Substring Without Repeating Characters* & *Valid Parentheses*.
* [ ] **Daily Personal (System Design):** Study Relational Databases (Postgres) vs. NoSQL (MongoDB). Master ACID properties.
* [ ] **Daily Office:** Inspect your office database schema. Check how Django manages model migrations and look for any unoptimized database queries in your certificate lookup history.
* [ ] **Weekend Personal (CertPulse-AI):** Install Docker Desktop on your Mac. Run a local PostgreSQL container via terminal (`docker run`). Install `SQLAlchemy` or `SQLModel` in your backend code and save analyzed certificate hashes to Postgres.

### Week 6: Full Containerization (Docker Compose)
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Min Stack* & *Binary Search*.
* [ ] **Daily Personal (System Design):** Learn how Docker containers isolate networking, environments, and host file systems.
* [ ] **Daily Office:** Analyze your office deployment architecture. If it uses Docker, read the `Dockerfile` and `docker-compose.yml` files line-by-line to understand how services communicate.
* [ ] **Weekend Personal (CertPulse-AI):** Write a production-ready `Dockerfile` for your backend. Create a `docker-compose.yml` file that orchestrates your FastAPI container and your PostgreSQL container together. Boot them with `docker-compose up --build`.

### Week 7: Enter the Message Broker (Redis Setup)
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Search a 2D Matrix* & *Reverse Linked List*.
* [ ] **Daily Personal (System Design):** Learn the Message Queues / Producer-Consumer pattern. Understand why they are used for tasks taking longer than 2 seconds.
* [ ] **Daily Office:** Introduce Celery to your office Django project. Configure its settings to point to your office Redis instance as the message broker.
* [ ] **Weekend Personal (CertPulse-AI):** Add a Redis container to your personal `docker-compose.yml` file. Install `Celery` or `Arq` in your FastAPI app. Rewrite your domain scanning endpoint to immediately hand tasks to the Redis queue and return a tracking `job_id` to the UI.

### Week 8: The Asynchronous Status Check
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Merge Two Sorted Lists* & *Reorder List*.
* [ ] **Daily Personal (Linux):** Practice viewing container resource footprints with `docker stats` and checking application print statements using `docker logs <container_id>`.
* [ ] **Daily Office:** Move the heavy VirusTotal threat checks and Gemini prompts inside your office app into your new Celery background tasks. Create a lightweight Django endpoint `/task-status/<task_id>/` for frontend polling.
* [ ] **Weekend Personal (CertPulse-AI):** Implement a matching status polling endpoint (`/status/{job_id}`) in your FastAPI codebase. Update your JavaScript frontend to query this endpoint every 2 seconds until the Redis worker finishes processing.

---

## 🗓️ Phase 3: AI Engineering, MCP, & Agentic Frameworks (Weeks 9–14)

### Week 9: Free-Tier AI Configurations & Model Context Protocol (MCP) Foundations
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Remove Nth Node From End of List* & *Linked List Cycle*.
* [ ] **Daily Personal (System Design):** Learn about Model Context Protocol (MCP) architecture. Understand how the host, client, and server communicate.
* [ ] **Daily Office:** Audit the prompt instructions passed to your office Vertex AI integration. Optimize the instruction tokens to see if you can speed up output response parsing.
* [ ] **Weekend Personal (CertPulse-AI):** Sign up for a free developer token on Google AI Studio for Gemini 2.5 Flash. Install the official `google-genai` Python SDK. Set up a basic open-source MCP server locally on your Mac to explore how Cursor IDE can natively use MCP to interact with local files.

### Week 10: Building Custom MCP Servers for Threat Intelligence
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Invert Binary Tree* & *Maximum Depth of Binary Tree*.
* [ ] **Daily Personal (System Design):** Study the difference between unstructured data formats and structured application outputs (like forced JSON Schemas).
* [ ] **Daily Office:** Refactor your office Gemini response handling. Use Pydantic or Django forms to validate that the response object matches a clean structural standard before exposing it to the UI.
* [ ] **Weekend Personal (CertPulse-AI):** Write a custom MCP server in Python. This server will connect your Mac terminal or Cursor IDE directly to the public crt.sh API. This allows your AI assistant (Cursor) to run real-time certificate subdomain lookups using your own custom protocol tool.

### Week 11: Orchestration Frameworks (LangChain & LangGraph Basics)
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Diameter of Binary Tree* & *Balanced Binary Tree*.
* [ ] **Daily Personal (System Design):** Study Data Caching patterns. Learn about Cache-Aside vs. Write-Through methodologies using Redis.
* [ ] **Daily Office:** Check your corporate data cache settings. See if you can cache repetitive threat intelligence API lookups (like clean files searched multiple times) inside Redis to reduce network overhead.
* [ ] **Weekend Personal (Secured Log Analyzer):** Install LangChain or LangGraph. Migrate your basic linear Python prompt logic into a stateful graph system. Define explicit application node states: (1) Accept Input $\rightarrow$ (2) Check Signatures $\rightarrow$ (3) Format Prompt $\rightarrow$ (4) AI Threat Evaluation.

### Week 12: Multi-Agent AI Systems (CrewAI / AutoGen)
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Same Tree* & *Subtree of Another Tree*.
* [ ] **Daily Personal (System Design):** Read about Asynchronous Workers scaling. How do multiple container workers grab jobs off a single Redis line?
* [ ] **Daily Office:** Scale up your office background pipeline by ensuring multiple Celery worker processing threads are active simultaneously without creating race conditions.
* [ ] **Weekend Personal (Secured Log Analyzer):** Re-engineer your analysis pipeline into a Multi-Agent system using CrewAI. Create two distinct AI agents: an "Incident Investigator Agent" (tasked with finding raw anomalies in log segments) and a "Security Officer Agent" (tasked with evaluating the investigator's findings and writing a final compliance report).

### Week 13: Introduction to Embeddings & Vector Stores
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Lowest Common Ancestor of a Binary Search Tree* & *Binary Tree Level Order Traversal*.
* [ ] **Daily Personal (System Design):** Learn the core tenants of Retrieval-Augmented Generation (RAG). What are embeddings and why are Vector Databases required?
* [ ] **Daily Office:** Explore if there are internal documentation layers or historical security records in your company that could eventually be queried via an LLM RAG setup.
* [ ] **Weekend Personal (CertPulse-AI):** Install a lightweight local vector library like ChromaDB or `pgvector` inside your local Postgres container. Practice converting historical security vulnerability logs into vector embeddings and running similarity queries against them.

### Week 14: Mid-Point Project Review & Optimization
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Kth Smallest Element in a BST* & *Validate Binary Search Tree*.
* [ ] **Daily Personal (Linux):** Practice checking hidden configurations and editing files using native terminal text editors (`nano` or `vim`).
* [ ] **Daily Office:** Ensure all environment variables on your corporate system are clean and that no experimental code changes affect the main stable branches.
* [ ] **Weekend Personal (Both Projects):** Run extensive testing loops across both personal applications. Ensure your multi-agent execution loops and MCP endpoints don't cause local runtime deadlocks. Clean up the application layout styling.

---

## 🗓️ Phase 4: DevSecOps, Cloud Simulation & Architecture Wrap-Up (Weeks 15–24)

### Week 15: Infrastructure as Code (IaC) Basics
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Implement Trie (Prefix Tree)* & *Design Add and Search Words Data Structure*.
* [ ] **Daily Personal (System Design):** Study the difference between Imperative infrastructure management (UI consoles/Scripts) and Declarative configuration (Terraform).
* [ ] **Daily Office:** Review your corporate system's configuration patterns. Identify how infrastructure deployment details are communicated across your dev and engineering teams.
* [ ] **Weekend Personal (Secured Log Analyzer):** Install the Terraform CLI on your Mac. Create a new infrastructure folder containing a basic `main.tf` configuration file targeting an AWS provider mockup.

### Week 16: Local Cloud Provisioning (LocalStack)
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Word Search II* & *K Closest Points to Origin*.
* [ ] **Daily Personal (System Design):** Study Cloud Object Storage (AWS S3) design paradigms and access permissions policies (IAM).
* [ ] **Daily Office:** Review the cloud storage strategies utilized by your QA automated environments for storing execution screenshots or test logs.
* [ ] **Weekend Personal (Secured Log Analyzer):** Add a **LocalStack** service block to your container orchestrator file. Write a Terraform template to programmatically spin up a simulated AWS S3 storage bucket on your local Mac environment.

### Week 17: Application Cloud Cloud-Storage Integrations
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Kth Largest Element in an Array* & *Last Stone Weight*.
* [ ] **Daily Personal (System Design):** Understand the difference between storing data inside local stateful container storage versus remote cloud object file storage.
* [ ] **Daily Office:** Confirm that no confidential company credentials or production API authentication keys are stored inside tracking git files or codebase definitions.
* [ ] **Weekend Personal (Secured Log Analyzer):** Update your FastAPI app file storage logic using the `boto3` library. Ensure that uploaded `.log` files are archived straight into the local simulated AWS S3 bucket instead of the local Mac file system.

### Week 18: Continuous Integration Basics (GitHub Actions)
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Two Sum II - Input Array Is Sorted* & *3Sum*.
* [ ] **Daily Personal (System Design):** Study the core tenants of Continuous Integration (CI). Learn how remote build runners manage workflows.
* [ ] **Daily Office:** Audit your corporate Jenkins files line-by-line. Understand each phase: checkout, dependency preparation, execution, and artifact archiving.
* [ ] **Weekend Personal (CertPulse-AI):** Push your clean-room codebases into standalone, private or public GitHub repositories. Author your very first GitHub Actions configuration script under `.github/workflows/ci.yml`.

### Week 19: Pipeline Code Validation & Testing
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Evaluate Reverse Polish Notation* & *Generate Parentheses*.
* [ ] **Daily Personal (System Design):** Learn about standard code quality checking mechanisms, test coverage targets, and code style linters (`flake8`, `black`).
* [ ] **Daily Office:** Optimize test execution loops within your official Jenkins tasks by checking for unnecessary wait dependencies.
* [ ] **Weekend Personal (CertPulse-AI):** Write unified backend assertions using `pytest`. Configure your GitHub Actions workflow file to trigger your automated tests cleanly on every new code commit.

### Week 20: Automated Static Security Testing (SAST)
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Daily Temperatures* & *Car Fleet*.
* [ ] **Daily Personal (System Design):** Study standard vulnerability types like hardcoded credential leak risks and unverified raw string evaluations.
* [ ] **Daily Office:** Implement an initial automated step into a testing repository that scans codebases for hidden or plaintext security authorization tokens.
* [ ] **Weekend Personal (Both Projects):** Integrate **Bandit** (a Python SAST tool) into your GitHub Actions pipeline configuration. Test it by intentionally placing a mock vulnerability in a branch to see if the pipeline fails successfully.

### Week 21: Container Infrastructure Security Scanning
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Find Minimum in Rotated Sorted Array* & *Search in Rotated Sorted Array*.
* [ ] **Daily Personal (System Design):** Learn about container layer base image vulnerabilities and software supply chain dependency analysis.
* [ ] **Daily Office:** Review how your official infrastructure builds check third-party open-source components for underlying vulnerabilities.
* [ ] **Weekend Personal (Both Projects):** Add a container file testing step inside your CI workflow using **Trivy**. Configure it to scan your application's `Dockerfile` configurations automatically during construction.

### Week 22: Advanced Network and Security Hardening
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Time Based Key-Value Store* & *Subsets*.
* [ ] **Daily Personal (System Design):** Master the principles of Least Privilege Access, Cross-Origin Resource Sharing (CORS), and HTTPS encryption workflows.
* [ ] **Daily Office:** Document any network configuration improvements or performance gains discovered during your async refactoring sprints.
* [ ] **Weekend Personal (CertPulse-AI):** Restrict your application's CORS endpoints. Secure backend configuration processes by locking database and container network communication channels inside Docker.

### Week 23: Complete System Documentation Architecture
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Combination Sum* & *Permutations*.
* [ ] **Daily Personal (System Design):** Study methods for drafting concise technical documentation structures, including system architecture definitions and environmental setup instructions.
* [ ] **Daily Office:** Present your optimized asynchronous processing flow architecture blueprints to your team leads or engineering pairs.
* [ ] **Weekend Personal (Both Projects):** Write exhaustive production `README.md` documents for both of your portfolios. Include clear architecture drawings, system component layouts, and exact steps to run via Docker Compose.

### Week 24: Portfolio Launch & Interview Preparation
* [ ] **Daily Personal (DSA):** Solve NeetCode — *Subsets II* & *Combination Sum II*.
* [ ] **Daily Personal (System Design):** Conduct a holistic review of your design knowledge (Load balancers, Caching systems, Queue pipelines, Databases).
* [ ] **Daily Office:** Complete any remaining polish items within your office certificate automation code branch.
* [ ] **Weekend Personal (Final Step):** Make your personal GitHub repositories public. Host a working live recording or screenshots showcasing your async processing flow, Docker configurations, and Gemini AI outputs. Add these links directly to the top of your technical resume.
