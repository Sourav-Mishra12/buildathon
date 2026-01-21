def simplify_prompt(text, language):
    return f"""
You are an assistant that explains documents in very simple language.

Document:
{text}

Explain this document in very simple {language}.
Avoid technical terms.
Keep it short and clear.
"""


def question_prompt(summary, question, language):
    return f"""
You are helping a user understand a document.

Document summary:
{summary}

User question:
{question}

Answer clearly in {language}.
Keep answer short and simple.
"""
