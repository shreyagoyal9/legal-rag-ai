from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever  # your retriever file

model = OllamaLLM(model="llama3.2")

template = """
You are an expert crime lawyer and judge.
Based on the case provided, explain which legal articles and laws apply,
and describe the actions to be taken if the accused is found guilty.

Relevant laws:
{laws}

Case:
{question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n==============================")
    question = input("Enter case info (q to quit): ")
    if question.lower() == "q":
        break

    # Retrieve relevant laws from the vector store
    retrieved_docs = retriever.invoke(question)
    laws_text = "\n".join([doc.page_content for doc in retrieved_docs])

    # Generate the model's answer
    result = chain.invoke({"laws": laws_text, "question": question})

    # ✅ Display only the final answer
    print("\n--- AI Response ---")
    print(result)
