import "./ErrorBanner.css";

function ErrorBanner({

    message,

    onRetry

}) {

    if (!message) {

        return null;

    }

    return (

        <div className="error-banner">

            <span>

                {message}

            </span>

            <button

                onClick={onRetry}

            >

                Retry

            </button>

        </div>

    );

}

export default ErrorBanner;