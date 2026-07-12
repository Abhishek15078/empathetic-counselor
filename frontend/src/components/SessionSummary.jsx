import "./SessionSummary.css";
import TrajectoryIndicator from "./TrajectoryIndicator";

const emotionColors = {
    joy: "#FFD54F",
    sadness: "#42A5F5",
    anger: "#EF5350",
    fear: "#7E57C2",
    surprise: "#FF7043",
    disgust: "#66BB6A",
    neutral: "#90A4AE"
};

function capitalize(word) {

    if (!word) return "";

    return word.charAt(0).toUpperCase() + word.slice(1);

}

function SessionSummary({ summary }) {

    if (!summary) {

        return null;

    }

    const emotionArc = summary?.emotion_arc ?? [];
    const keyMoments = summary?.key_moments ?? [];

    const dominantEmotion =
    emotionArc.length
        ? emotionArc.at(-1)
        : "Unknown";

    return (

        <div className="summary-card">

            <h3>
                Conversation Summary
            </h3>

            <div className="summary-grid">

                <div className="summary-item">

                    <span className="summary-icon">

                        😊

                    </span>

                    <div>

                        <small>

                            Dominant Emotion

                        </small>

                        <h4>

                            {capitalize(dominantEmotion)}

                        </h4>

                    </div>

                </div>

                <div className="summary-item">

                    <span className="summary-icon">

                        📈

                    </span>

                    <div>

                        <small>

                            Final Trajectory

                        </small>

                        <TrajectoryIndicator
                        trajectory={summary?.trajectory}
                        />

                    </div>

                </div>

                <div className="summary-item">

                    <span className="summary-icon">

                        💬

                    </span>

                    <div>

                        <small>

                            Total Turns

                        </small>

                        <h4>

                            {summary?.turn_count ?? 0}

                        </h4>

                    </div>

                </div>

            </div>

            <hr />

            <h4>

                Emotion Journey

            </h4>

            <div className="emotion-journey">

                {

                    emotionArc.map(

                        (emotion, index) => (

                            <span

                                key={index}

                                className="emotion-badge"

                                style={{

                                    backgroundColor:

                                        emotionColors[emotion] ||

                                        "#999"

                                }}

                            >

                                {capitalize(emotion)}

                            </span>

                        )

                    )

                }

            </div>

            <hr />

            <h4>

                Important Moments

            </h4>

            <ul className="key-moments">

                {

                    keyMoments.map(

                        (moment, index) => (

                            <li key={index}>

                                ✓ {moment}

                            </li>

                        )

                    )

                }

            </ul>

        </div>

    );

}

export default SessionSummary;