import { useEffect, useState } from "react";

import {
    createSession,
    sendMessage as sendMessageAPI,
    getMessageHistory,
    getSummary,
    downloadConversation,
    getTimeline
} from "../services/api";

function useChat() {

    // -------------------------------
    // Chat
    // -------------------------------

    const [messages, setMessages] = useState([]);

    const [sessionId, setSessionId] = useState(null);

    const [input, setInput] = useState("");

    const [isLoading, setIsLoading] = useState(false);

    const [error, setError] = useState(null);

    const [safetyTriggered, setSafetyTriggered] = useState(false);

    const [lastMessage, setLastMessage] = useState("");

    // -------------------------------
    // AI Insights
    // -------------------------------

    const [emotion, setEmotion] = useState(null);

    const [trajectory, setTrajectory] = useState(null);

    const [processingTime, setProcessingTime] = useState(null);

    // -------------------------------
    // Summary
    // -------------------------------

    const [summary, setSummary] = useState(null);

    // -------------------------------
    // Timeline
    // -------------------------------

    const [timeline, setTimeline] = useState([]);

    useEffect(() => {

        initializeSession();

    }, []);

    // =======================================
    // Initialize Session
    // =======================================

    async function initializeSession() {

        try {

            const savedSession =
                localStorage.getItem("sessionId");

            if (savedSession) {

                setSessionId(savedSession);

                try {

                    const history =
                        await getMessageHistory(savedSession);

                    if (history.messages) {

                        setMessages(history.messages);

                    }

                    await loadTimeline(savedSession);

                }

                catch (err) {

                    console.error(err);

                }

                return;

            }

            const response =
                await createSession();

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

        if (!text) return;

        if (isLoading) return;

        setError(null);

        setSafetyTriggered(false);

        setIsLoading(true);

        const userMessage = {

            id: Date.now(),

            role: "user",

            content: text

        };

        setMessages(prev => [

            ...prev,

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

            setMessages(prev => [

                ...prev,

                assistantMessage

            ]);

            setEmotion(response.emotion);

            setTrajectory(response.trajectory);

            setProcessingTime(

                response.processing_time_ms

            );

            if (

                response.safety_triggered

            ) {

                setSafetyTriggered(true);

            }

            // Load newest timeline AFTER backend stores emotion

            await loadTimeline();

        }

        catch (err) {

            console.error(err);

            setError(

                err.message ||

                "Something went wrong."

            );

        }

        finally {

            setIsLoading(false);

        }

    }

    // =======================================
    // Retry
    // =======================================

    async function retryLastMessage() {

        if (!lastMessage) return;

        await sendMessage(lastMessage);

    }

    // =======================================
    // Summary
    // =======================================

    async function loadSummary() {

        if (!sessionId) return;

        try {

            const result =

                await getSummary(sessionId);

            setSummary(result);

        }

        catch (err) {

            console.error(err);

        }

    }

    // =======================================
    // Export Conversation
    // =======================================

    async function exportConversation() {

        if (!sessionId) return;

        try {

            await downloadConversation(

                sessionId

            );

        }

        catch (err) {

            console.error(err);

            setError(

                "Unable to download conversation."

            );

        }

    }

    // =======================================
    // Start New Conversation
    // =======================================

    async function startNewConversation() {

    try {

        setIsLoading(true);

        const response = await createSession();

        localStorage.setItem(
            "sessionId",
            response.session_id
        );

        setSessionId(response.session_id);

        setMessages([]);

        setSummary(null);

        setTimeline([]);

        setEmotion(null);

        setTrajectory(null);

        setProcessingTime(null);

        setSafetyTriggered(false);

        setError(null);

        setInput("");

    }

    catch (err) {

        console.error(err);

        setError(
            "Unable to start a new conversation."
        );

    }

    finally {

        setIsLoading(false);

    }

}

    // =======================================
    // Timeline
    // =======================================

    async function loadTimeline(id = sessionId) {

        if (!id) return;

        try {

            const result =

                await getTimeline(id);

            setTimeline(

                result.timeline

            );

        }

        catch (err) {

            console.error(

                "Timeline Error:",

                err

            );

        }

    }

    // =======================================

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

        startNewConversation,

        timeline,

        loadTimeline

    };

}

export default useChat;