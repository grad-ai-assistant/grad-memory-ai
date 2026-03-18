# Grad Memory AI — System Architecture

## High-Level Architecture

Grad Memory AI follows a Retrieval-Augmented Generation (RAG) architecture designed for high-precision academic information retrieval.

User Documents → Parsing Layer → Chunking & Metadata → Embedding → Vector Database → Retrieval Engine → LLM → Response with Source

---

## Core Components

### 1. Document Ingestion Layer
Responsible for accepting and processing uploaded documents such as transcripts, SOPs, CVs, LORs, and certificates.

Functions:
- PDF text extraction
- Format normalisation
- Document classification

Tools:
- PyMuPDF
- Custom parsers (future)

---

### 2. Chunking & Metadata Layer
Documents are divided into semantically meaningful chunks.

Each chunk will be tagged with metadata such as:
- document_type
- semester
- subject
- year
- institution
- sop_version

This enables high-precision retrieval.

---

### 3. Embedding Layer
Each chunk is converted into a vector representation.

Model:
- OpenAI Embeddings (text-embedding-3-small)

---

### 4. Vector Storage
Embeddings are stored in a vector database.

Phase 1:
- Chroma (local)

Future:
- Pinecone / Weaviate

---

### 5. Retrieval Engine
Hybrid retrieval combining:
- Semantic vector search
- Metadata filtering
- Keyword search

---

### 6. LLM Reasoning Layer
The LLM receives:
- Retrieved chunks
- User question
- System prompt enforcing factual accuracy

Model:
- GPT-4o-mini

---

### 7. Response Layer
Outputs:
- Exact factual answer
- Structured form-answer mode
- Source citation

---

## System Principles

- Precision over verbosity
- No hallucination policy
- Source-grounded answers
- Persistent academic memory

---

## Future Architectural Extensions

- Multi-user authentication layer
- Cloud vector database
- Academic timeline engine
- Structured data extraction pipeline
- Application autofill API integrations
