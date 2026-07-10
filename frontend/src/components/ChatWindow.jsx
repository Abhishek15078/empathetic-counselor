import { useEffect, useRef } from "react";

import "./ChatWindow.css";
import MessageBubble from "./MessageBubble";

function ChatWindow({ messages }) {

    const bottomRef = useRef(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth"
        });
    }, [messages]);

    return (

        <div className="chat-window">

            {
                messages.length === 0 ? (

                    <p>No messages yet.</p>

                ) : (

                    messages.map((message, index) => (

                        <MessageBubble
                            key={message.id ?? `${message.role}-${index}`}
                            message={message}
                        />

                    ))

                )
            }

            <div ref={bottomRef}></div>

        </div>

    );

}

export default ChatWindow;