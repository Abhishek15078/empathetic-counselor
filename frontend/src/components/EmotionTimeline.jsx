import "./EmotionTimeline.css";

import {

ResponsiveContainer,
LineChart,
Line,
XAxis,
YAxis,
CartesianGrid,
Tooltip

} from "recharts";

const emotionColors={

joy:"#FFD54F",

sadness:"#42A5F5",

anger:"#EF5350",

fear:"#7E57C2",

surprise:"#FF7043",

disgust:"#66BB6A",

neutral:"#90A4AE"

};

function CustomDot(props){

const{

cx,

cy,

payload

}=props;

if(cx===undefined||cy===undefined){

return null;

}

return(

<circle

cx={cx}

cy={cy}

r={6}

stroke="#ffffff"

strokeWidth={2}

fill={

emotionColors[payload.emotion] ||

"#90A4AE"

}

/>

);

}

function CustomTooltip({

active,

payload

}){

if(

active &&

payload &&

payload.length

){

const data=payload[0].payload;

return(

<div className="timeline-tooltip">

<p>

<b>

Turn {data.turn}

</b>

</p>

<p>

Emotion :

{data.emotion}

</p>

<p>

Confidence :

{(data.score*100).toFixed(1)}%

</p>

</div>

);

}

return null;

}

function EmotionTimeline({

timeline=[]

}){

const data = timeline ?? [];

if (data.length < 2){

return(

<div className="timeline-placeholder">

📊

<p>

Emotion timeline will appear after a few messages.

</p>

</div>

);

}

return(

<div className="timeline-card">

<h4>

Emotion Timeline

</h4>

<ResponsiveContainer

width="100%"

height={280}

>

<LineChart data={data}>

<CartesianGrid

strokeDasharray="3 3"

/>

<XAxis

dataKey="turn"

label={{

value:"Turn",

position:"insideBottom",

offset:-5

}}

/>

<YAxis

domain={[0,1]}

label={{

value:"Confidence",

angle:-90,

position:"insideLeft"

}}

/>

<Tooltip

content={<CustomTooltip/>}

/>

<Line

type="monotone"

dataKey="score"

stroke="#3B82F6"

strokeWidth={3}

dot={<CustomDot/>}

isAnimationActive={true}

animationDuration={800}

/>

</LineChart>

</ResponsiveContainer>

</div>

);

}

export default EmotionTimeline;