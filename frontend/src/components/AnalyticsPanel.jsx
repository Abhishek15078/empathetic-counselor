import "./AnalyticsPanel.css";

function AnalyticsPanel({

    emotion,

    trajectory,

    processingTime,

    safetyTriggered,

    summary,

    onLoadSummary,

    onExportConversation

}) {

    return (

        <div className="analytics-container">

            <h2>AI Insights</h2>

            {/* Emotion */}

            <div className="analytics-card">

                <h4>Emotion</h4>

                <p>

                    {emotion ?? "—"}

                </p>

            </div>

            {/* Trajectory */}

            <div className="analytics-card">

                <h4>Trajectory</h4>

                <p>

                    {trajectory ?? "—"}

                </p>

            </div>

            {/* Processing Time */}

            <div className="analytics-card">

                <h4>Processing Time</h4>

                <p>

                    {

                        processingTime != null

                            ? `${processingTime} ms`

                            : "—"

                    }

                </p>

            </div>

            {/* Safety */}

            <div className="analytics-card">

                <h4>Safety</h4>

                <p>

                    {

                        safetyTriggered

                            ? "⚠ Safety Triggered"

                            : "✅ Safe"

                    }

                </p>

            </div>

            {/* Generate Summary Button */}

            <div className="analytics-card">

                <button

                    onClick={onLoadSummary}

                >

                    Generate Summary

                </button>

            </div>

            {/* Download Conversation Button */}

            <div className="analytics-card">

                <button

                    onClick={onExportConversation}

                >

                    Download Conversation

                </button>

            </div>

            {/* Conversation Summary */}

            {

                summary && (

                    <div className="analytics-card">

                        <h4>

                            Conversation Summary

                        </h4>

                        <p>

                            <strong>

                                Turns:

                            </strong>{" "}

                            {summary.turn_count}

                        </p>

                        <p>

                            <strong>

                                Trajectory:

                            </strong>{" "}

                            {summary.trajectory}

                        </p>

                        <p>

                            <strong>

                                Emotion Arc

                            </strong>

                        </p>

                        <ul>

                            {

                                summary.emotion_arc.map(

                                    (item, index) => (

                                        <li key={index}>

                                            {item}

                                        </li>

                                    )

                                )

                            }

                        </ul>

                        <p>

                            <strong>

                                Key Moments

                            </strong>

                        </p>

                        <ul>

                            {

                                summary.key_moments.length > 0

                                    ? (

                                        summary.key_moments.map(

                                            (item, index) => (

                                                <li key={index}>

                                                    {item}

                                                </li>

                                            )

                                        )

                                    )

                                    : (

                                        <li>

                                            No key moments yet.

                                        </li>

                                    )

                            }

                        </ul>

                    </div>

                )

            }

        </div>

    );

}

export default AnalyticsPanel;