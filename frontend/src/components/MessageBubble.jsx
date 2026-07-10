import "./MessageBubble.css";

import EmotionBadge from "./EmotionBadge";

function MessageBubble({ message }) {

    return (

        <div

            className={

                message.role === "user"

                    ? "message-row user"

                    : "message-row assistant"

            }

        >

            <div className="message-bubble">

                {

                    message.role === "user" && (

                        <EmotionBadge

                            emotion={message.emotion}

                        />

                    )

                }

                {message.content}

            </div>

        </div>

    );

}

export default MessageBubble;