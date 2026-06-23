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
            snippet = text[:700]

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