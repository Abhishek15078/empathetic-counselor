import { useEffect, useState } from "react";

import {

    createSession,

    sendMessage as sendMessageAPI,

    getMessageHistory,

    getSummary,

    downloadConversation

} from "../services/api";

function useChat() {

    const [messages, setMessages] = useState([]);

    const [sessionId, setSessionId] = useState(null);

    const [input, setInput] = useState("");

    const [isLoading, setIsLoading] = useState(false);

    const [error, setError] = useState(null);

    const [safetyTriggered, setSafetyTriggered] = useState(false);

    const [lastMessage, setLastMessage] = useState("");

    const [emotion, setEmotion] = useState(null);

    const [trajectory, setTrajectory] = useState(null);

    const [processingTime, setProcessingTime] = useState(null);

    const [summary, setSummary] = useState(null);

    useEffect(() => {
        initializeSession();
    }, []);

    // =======================================
    // Initialize Session
    // =======================================

    async function initializeSession() {

        try {

            const savedSession = localStorage.getItem("sessionId");

            if (savedSession) {

                console.log("Loaded existing session:", savedSession);

                setSessionId(savedSession);

                try {

                    const history =
                        await getMessageHistory(savedSession);

                    if (history.messages) {

                        setMessages(history.messages);

                    }

                }

                catch (err) {

                    console.error(
                        "Failed to load history.",
                        err
                    );

                }

                return;

            }

            const response =
                await createSession();

            console.log(
                "Session Created:",
                response.session_id
            );

            setSessionId(response.session_id);

            localStorage.setItem(
                "sessionId",
                response.session_id
            );

        }

        catch (err) {

            console.error(err);

            setError(
                "Unable to create session."
            );

        }

    }

    // =======================================
    // Send Message
    // =======================================

    async function sendMessage(messageText = null) {

        const text = (messageText ?? input).trim();
        setLastMessage(text);

        if (text === "") return;

        if (isLoading) return;

        setError(null);

        setSafetyTriggered(false);

        setIsLoading(true);

        const userMessage = {

            id: Date.now(),

            role: "user",

            content: text

        };

        setMessages(previous => [

            ...previous,

            userMessage

        ]);

        setInput("");

        try {

            const response =
                await sendMessageAPI(
                    sessionId,
                    text
                );

            const assistantMessage = {

                id: Date.now() + 1,

                role: "assistant",

                content: response.response_text

            };
            setEmotion(response.emotion);

            setTrajectory(response.trajectory);
 
            setProcessingTime(response.processing_time_ms);

            setMessages(previous => [

                ...previous,

                assistantMessage

            ]);

            if (response.safety_triggered) {

                setSafetyTriggered(true);

            }

        }

        catch (err) {

            console.error(
                "Message API Error:",
                err
            );

            setError(
                err.message ||
                "Something went wrong."
            );

        }

        finally {

            setIsLoading(false);

        }

    }
    async function retryLastMessage() {

    if (!lastMessage) {

        return;

    }

    await sendMessage(lastMessage);

   }
   async function loadSummary() {

    if (!sessionId) return;

    try {

        const result = await getSummary(

            sessionId

        );

        setSummary(result);

    }

    catch (err) {

        console.error(

            err

        );

    }

}
   async function exportConversation() {

    if (!sessionId) {

        return;

    }

    try {

        await downloadConversation(sessionId);

    }

    catch (err) {

        console.error(err);

        setError("Unable to download conversation.");

    }

}

// =======================================
// Start New Conversation
// =======================================

async function startNewConversation() {

    try {

        // Remove previous session
        localStorage.removeItem("sessionId");

        // Clear UI
        setMessages([]);
        setSummary(null);

        setEmotion(null);
        setTrajectory(null);
        setProcessingTime(null);

        setSafetyTriggered(false);
        setError(null);

        setInput("");

        // Create brand new backend session
        const response = await createSession();

        setSessionId(response.session_id);

        localStorage.setItem(

            "sessionId",

            response.session_id

        );

        console.log(

            "New session created:",

            response.session_id

        );

    }

    catch (err) {

        console.error(err);

        setError(

            "Unable to start a new conversation."

        );

    }

}

    return {

    sessionId,

    messages,

    input,

    setInput,

    sendMessage,

    retryLastMessage,

    isLoading,

    error,

    safetyTriggered,

    emotion,

    trajectory,

    processingTime,

    summary,

    loadSummary,

    exportConversation,

    startNewConversation

};

}

export default useChat;