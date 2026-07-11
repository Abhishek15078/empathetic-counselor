import "./TrajectoryIndicator.css";

function TrajectoryIndicator({ trajectory }) {

    if (!trajectory) {

        return null;

    }

    const config = {

        improving: {

            icon: "📈",

            color: "#2E7D32",

            label: "Improving"

        },

        stable: {

            icon: "➡",

            color: "#1565C0",

            label: "Stable"

        },

        worsening: {

            icon: "📉",

            color: "#C62828",

            label: "Worsening"

        }

    };

    const value =

        config[trajectory.toLowerCase()] ||

        {

            icon: "❓",

            color: "#666",

            label: trajectory

        };

    return (

        <div

            className="trajectory-indicator"

            style={{

                borderLeft: `6px solid ${value.color}`

            }}

        >

            <span

                className="trajectory-icon"

            >

                {value.icon}

            </span>

            <span

                className="trajectory-label"

                style={{

                    color: value.color

                }}

            >

                {value.label}

            </span>

        </div>

    );

}

export default TrajectoryIndicator;