def build_snippet(text: str, query_words: list[str], window: int = 350) -> str:
    text_lower = text.lower()

    first_match_index = -1

    for word in query_words:
        match_index = text_lower.find(word)
        if match_index != -1:
            first_match_index = match_index
            break

    if first_match_index == -1:
        return text[: window * 2].strip()

    start = max(first_match_index - window, 0)
    end = min(first_match_index + window, len(text))

    snippet = text[start:end].strip()

    if start > 0:
        snippet = "... " + snippet

    if end < len(text):
        snippet = snippet + " ..."

    return snippet


def search_pages(pages: list[dict], query: str, limit: int = 5) -> list[dict]:
    query_words = [
        word.lower()
        for word in query.split()
        if len(word.strip()) > 2
    ]

    results = []

    for page in pages:
        text = page.get("text", "")
        text_lower = text.lower()

        score = sum(1 for word in query_words if word in text_lower)

        if score > 0:
            snippet = build_snippet(text, query_words)

            results.append(
                {
                    "source": page.get("source"),
                    "page": page.get("page"),
                    "score": score,
                    "snippet": snippet
                }
            )

    results.sort(key=lambda item: item["score"], reverse=True)

    return results[:limit]