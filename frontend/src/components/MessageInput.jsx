import "./MessageInput.css";

function MessageInput({

    input,

    setInput,

    onSend,

    disabled = false

}) {

    function handleKeyDown(event) {

        if (event.key === "Enter" && !event.shiftKey) {

            event.preventDefault();

            if (!disabled) {

                onSend();

            }

        }

    }

    function handleClick() {

        if (!disabled) {

            onSend();

        }

    }

    return (

        <div className="message-input-container">

            <input

                type="text"

                value={input}

                placeholder={

                    disabled

                        ? "Assistant is typing..."

                        : "Type your message..."

                }

                onChange={(event) =>

                    setInput(event.target.value)

                }

                onKeyDown={handleKeyDown}

                disabled={disabled}

                autoComplete="off"

            />

            <button

                onClick={handleClick}

                disabled={disabled}

            >

                {

                    disabled

                        ? "Sending..."

                        : "Send"

                }

            </button>

        </div>

    );

}

export default MessageInput;