class TabstackBrowserlessAutomationClient:
    def find_nodes(self, raw_html_body: str, query_selector: str) -> dict:
        # Simple simulated tag grabber
        tag = query_selector.strip(" .#")
        nodes = []
        start = 0
        while True:
            pos = raw_html_body.find(f"<{tag}", start)
            if pos == -1: break
            end = raw_html_body.find(f"</{tag}>", pos)
            if end == -1: break
            inner_start = raw_html_body.find(">", pos) + 1
            nodes.append(raw_html_body[inner_start:end].strip())
            start = end + len(tag) + 3
        return {"matched_nodes_text": nodes}