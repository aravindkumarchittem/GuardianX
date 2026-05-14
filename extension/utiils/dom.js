export function extractMessages(root) {
    const results = [];

    const nodes = root.querySelectorAll("div.message-in, div.message-out");

    nodes.forEach((node) => {
        const span = node.querySelector("span.selectable-text");

        if (span) {
            const text = span.innerText;
            results.push({ text, element: node });
        }
    });

    return results;
}