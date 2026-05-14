const API_URL = "http://127.0.0.1:5000/analyze-message";

export async function sendToAPI(message) {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    if (!response.ok) {
        throw new Error("API request failed");
    }

    return await response.json();
}