import "./AnalyticsPanel.css";
import EmotionTimeline from "./EmotionTimeline";
import SessionSummary from "./SessionSummary";

function AnalyticsPanel({

    emotion,

    trajectory,

    processingTime,

    safetyTriggered,

    summary,

    timeline,

    onLoadSummary,

    onExportConversation,

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

            <EmotionTimeline timeline={timeline ?? []} />

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

            <SessionSummary summary={summary ?? null} />

        </div>

    );

}

export default AnalyticsPanel;