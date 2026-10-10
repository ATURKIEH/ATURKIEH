# Aref Turkieh
 
Computer Science student at Western University, interested in AI/ML engineering and software engineering. I like building real, working systems: RAG platforms, reinforcement learning agents, backend infrastructure, not just models in a notebook.
 
## Tech Stack
 
**Languages:** Python, Java, C++, JavaScript, TypeScript, Bash
 
**ML/AI:** TensorFlow, PyTorch, LangChain, LangGraph, LlamaIndex, Scikit-learn, Pandas, NumPy
 
**Backend:** FastAPI, PostgreSQL, SQLAlchemy, Redis, JWT Auth, WebSockets
 
**Frontend:** React, TypeScript, Tailwind
 
**Cloud & DevOps:** AWS, Azure, Docker, GitHub Actions
 
**Databases:** PostgreSQL, SQLite, Pinecone

## Experience
 
**OCS, AI & Software Engineer Intern (Dubai, UAE)** - Built a full-stack Cash Disbursement Voucher approval system deployed on Azure, now in company-wide pilot across 5 departments.
 
**FlyRank, Backend AI Engineer Intern (Remote, Part-time)** - Built an LLM usage metering and billing backend with Stripe integration and exactly-once usage recording.
 
**Mada Communications International, Penetration Testing Intern (OnSite)** - Enumerated hidden endpoints and built automated vulnerability triage tooling, uncovering 12 new attack surfaces.
 
## Featured Projects
 
### OCS - Cash Disbursement Voucher Approval System
Full-stack approval system (FastAPI, PostgreSQL, React/TypeScript) deployed on Azure, replacing a manual paper-based process across a company-wide pilot.
- Built a dynamic multi-level approval engine with automated backup and escalation handling
- Integrated Azure OpenAI and Document Intelligence for receipt processing, cutting per-receipt time 8x
### FlyRank - LLM Usage Metering & Billing Backend
Backend service (FastAPI, PostgreSQL, Docker) for metering AI/API usage and enforcing subscription quotas.
- Designed an idempotent metering pipeline guaranteeing exactly-once usage recording under retries via a database-level unique constraint
- Integrated Stripe for subscription billing with webhook signature verification and event deduplication
### Document Q&A - Multi-User RAG Platform
RAG platform (FastAPI, LangChain, Pinecone, PostgreSQL, React/TypeScript) supporting multi-format document ingestion.
- JWT-authenticated retrieval scope enforcing per-user document isolation via Pinecone metadata filtering
- Many-to-many chat-to-document schema enabling multi-threaded conversations across one or several documents
### AresScheduler - Adaptive Thread Pool Scheduler
Custom Java thread pool with FIFO, priority queue, and work-stealing scheduling policies.
- Work-stealing reduced latency by ~91% versus FIFO under high load
- Adaptive policy engine profiling live runtime metrics to recommend scheduling strategy
### StockSignal AI - Stock Movement Predictor
Two-model pipeline (PyTorch LSTM + FinBERT sentiment) predicting 5-day stock direction across 14 equities.
- Achieved 62% directional accuracy on held-out test data
- Deployed with FastAPI, Streamlit, Docker, and GitHub Actions CI/CD
### SOC Analyst AI - Anomaly Detection & Incident Reporting
Security tool combining an autoencoder for anomaly detection with a Random Forest classifier and LangChain-generated incident reports.
- 83% weighted F1 across attack types on the NSL-KDD dataset
- Deployed with FastAPI, SQLite, Streamlit, and Docker
### Algorithmic Trading Agent - Reinforcement Learning
Double DQN agent trading a 5-stock portfolio, backtested against a buy-and-hold benchmark with live paper trading.
- 418% backtest return vs. 98% for buy-and-hold, with an honestly documented drawdown tradeoff
- Debugged real RL failure modes, including Q-value overestimation and policy collapse
  
## 📊 GitHub Stats

![GitHub followers](https://img.shields.io/github/followers/ATURKIEH?label=Follow&style=social)
![GitHub stars](https://img.shields.io/github/stars/ATURKIEH?affiliations=OWNER&style=social)

---
## 📫 Connect With Me
- LinkedIn: https://www.linkedin.com/in/aref-turkieh/
- GitHub: https://github.com/ATURKIEH
- Email: turkieharef@gmail.com

![](https://komarev.com/ghpvc/?username=ATURKIEH&color=blue)
