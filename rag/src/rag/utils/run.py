from src.rag.services.indexing.index import chunking
from src.rag.services.indexing.index import chromaEmbeded

document = """
Artificial intelligence has rapidly transformed the way people interact with technology and how businesses operate in the modern world. Machine learning allows computers to learn patterns from large amounts of data and make predictions or decisions without being explicitly programmed for every possible situation. Deep learning is a specialized branch of machine learning that uses neural networks with multiple layers to understand complex relationships in data such as images, audio, text, and video. Natural language processing enables computers to understand, interpret, summarize, and generate human language, making it useful for chatbots, translation systems, search engines, and automated assistants.

Retrieval augmented generation, commonly known as RAG, combines information retrieval with language generation to provide more relevant and grounded answers. In a typical RAG system, documents are first collected from different sources such as websites, PDFs, videos, or text files. The collected information is then cleaned and divided into smaller chunks because processing an entire large document at once can be inefficient. Each chunk is converted into a numerical representation called an embedding, which captures some of the semantic meaning of the text. These embeddings are stored in a vector database such as Chroma, allowing the system to retrieve relevant chunks when a user asks a question.

When a user submits a query, the query is also converted into an embedding using the same embedding model that was used during indexing. The vector database compares the query embedding with the stored embeddings and retrieves the chunks that are semantically similar to the query. The retrieved information is then combined with the original question and passed to a language model. The language model uses this context to generate a response that is more relevant to the stored information. This process can reduce reliance on the model's general knowledge and allow it to answer questions about custom documents and private knowledge sources.

Building an effective RAG application requires careful attention to document processing, chunk size, chunk overlap, metadata, embedding quality, and retrieval strategies. Smaller chunks can provide more focused information but may lose important context, while larger chunks can preserve context but may contain irrelevant information. Metadata can be used to identify the original source, document title, page number, author, category, or upload date. Developers can use metadata filters to retrieve information from specific sources and prevent unnecessary searches across an entire collection. A well designed indexing and retrieval pipeline can make applications more efficient, maintainable, and useful for real world scenarios.
"""

chunks = chunking(document,"1")


chromaEmbeded(chunks,"1")
