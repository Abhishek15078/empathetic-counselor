const BASE_URL =
    import.meta.env.VITE_API_BASE_URL ||
    "http://localhost:8000";

console.log("BASE_URL =", BASE_URL);


// =======================================
// Create Session
// =======================================

export async function createSession() {

    const response =
        await fetch(

            `${BASE_URL}/api/session`,

            {

                method: "POST"

            }

        );

    if (!response.ok) {

        throw new Error(

            "Failed to create session."

        );

    }

    return await response.json();

}


// =======================================
// Send Message
// =======================================

export async function sendMessage(

    sessionId,

    message

) {

    const response =
        await fetch(

            `${BASE_URL}/api/message`,

            {

                method: "POST",

                headers: {

                    "Content-Type":
                        "application/json"

                },

                body: JSON.stringify({

                    session_id:
                        sessionId,

                    message:
                        message

                })

            }

        );

    if (!response.ok) {

        throw new Error(

            "Failed to send message."

        );

    }

    return await response.json();

}


// =======================================
// Load Conversation History
// =======================================

export async function getMessageHistory(

    sessionId

) {

    const response =
        await fetch(

            `${BASE_URL}/api/messages/${sessionId}`

        );

    if (!response.ok) {

        throw new Error(

            "Failed to load conversation history."

        );

    }

    return await response.json();

}


// =======================================
// Conversation Summary
// =======================================

export async function getSummary(sessionId) {

    const response = await fetch(

        `${BASE_URL}/api/session/${sessionId}/summary`

    );

    if (!response.ok) {

        throw new Error(
            "Failed to load summary."
        );

    }

    return await response.json();

}
// =======================================
// Download Conversation
// =======================================

export async function downloadConversation(

    sessionId

) {

    const response =

        await fetch(

            `${BASE_URL}/api/session/${sessionId}/export`

        );

    if (!response.ok) {

        throw new Error(

            "Failed to download conversation."

        );

    }

    const blob =

        await response.blob();

    const url =

        window.URL.createObjectURL(blob);

    const link =

        document.createElement("a");

    link.href = url;

    link.download =

        `conversation_${sessionId}.txt`;

    document.body.appendChild(link);

    link.click();

    link.remove();

    window.URL.revokeObjectURL(url);

}
// =======================================
// Emotion Timeline
// =======================================

export async function getTimeline(sessionId) {

    const response = await fetch(

        `${BASE_URL}/api/session/${sessionId}/timeline`

    );

    if (!response.ok) {

        throw new Error(

            "Failed to load timeline."

        );

    }

    return await response.json();

}