import "./EmotionBadge.css";

function EmotionBadge({ emotion }) {

    if (!emotion) {

        return null;

    }

    return (

        <div className={`emotion-badge ${emotion.toLowerCase()}`}>

            {emotion.toUpperCase()}

        </div>

    );

}

export default EmotionBadge;