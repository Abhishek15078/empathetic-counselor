import "./App.css";

import ChatWindow from "./components/ChatWindow";
import MessageInput from "./components/MessageInput";
import SafetyBanner from "./components/SafetyBanner";
import ErrorBanner from "./components/ErrorBanner";
import useChat from "./hooks/useChat";
import AnalyticsPanel from "./components/AnalyticsPanel";
import TypingIndicator from "./components/TypingIndicator";
function App() {

    const {

    messages,

    input,

    setInput,

    sendMessage,

    retryLastMessage,

    isLoading,

    safetyTriggered,

    error,

    emotion,

    trajectory,

    processingTime,

    summary,

    loadSummary,

    exportConversation,

    startNewConversation

} = useChat();

    return (

        <div className="app-container">

            <header className="app-header">

    <h1>

        Empathetic Counselor

    </h1>

    <button

        className="new-chat-btn"

        onClick={startNewConversation}

    >

        + New Chat

    </button>

</header>

            <main className="main-layout">

                <section className="chat-panel">

                    <SafetyBanner

                        visible={safetyTriggered}

                    />

                    <ChatWindow

                        messages={messages}

                    />

                    {

    isLoading && (

        <TypingIndicator />

    )

}

                    <ErrorBanner

    message={error}

    onRetry={retryLastMessage}

/>

                    <MessageInput

                        input={input}

                        setInput={setInput}

                        onSend={sendMessage}

                        disabled={isLoading}

                    />

                </section>

                <aside className="analytics-panel">

    <AnalyticsPanel

    emotion={emotion}

    trajectory={trajectory}

    processingTime={processingTime}

    safetyTriggered={safetyTriggered}

    summary={summary}

    onLoadSummary={loadSummary}

    onExportConversation={exportConversation}

/>

</aside>

            </main>

        </div>

    );

}

export default App;