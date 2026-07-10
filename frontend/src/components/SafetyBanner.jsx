import "./SafetyBanner.css";

function SafetyBanner({ visible }) {

    if (!visible) {

        return null;

    }

    return (

        <div className="safety-banner">

            <h3>
                ⚠️ Crisis Support
            </h3>

            <p>

                It sounds like you may be going through
                something extremely difficult.

            </p>

            <p>

                If you are in immediate danger,
                please contact your local emergency
                services or a trusted person.

            </p>

            <strong>

                988 Suicide & Crisis Lifeline

            </strong>

        </div>

    );

}

export default SafetyBanner;