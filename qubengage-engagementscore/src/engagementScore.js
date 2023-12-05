const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000; 

// Middleware
app.use(cors());
app.use(bodyParser.json());

function calculateStudentEngagementScore(lab, lecture, support, canvas) {
    lab = parseInt(lab)
    lecture = parseInt(lecture)
    support = parseInt(support)
    canvas = parseInt(canvas)

    const totalHours = lab + lecture + support + canvas;
    const lectureWeight = 0.7;
    const labWeight = 0.8;
    const supportWeight = 0.3;
    const canvasWeight = 0.3;

    const lectureTotalWeighted = lecture * lectureWeight / totalHours;
    const labTotalWeighted = lab * labWeight / totalHours;
    const supportTotalWeighted = support * supportWeight / totalHours;
    const canvasTotalWeighted = canvas * canvasWeight / totalHours;

    const engagementScore = lectureTotalWeighted + labTotalWeighted + supportTotalWeighted + canvasTotalWeighted;

    return engagementScore;
}

// Endpoint for calculating student engagement score
app.post('/calculate_engagement_score', (req, res) => {
    const { lab, lecture, support, canvas } = req.body;

    if (typeof lab !== 'number' || typeof lecture !== 'number' || typeof support !== 'number' || typeof canvas !== 'number') {
        return res.status(400).json({ error: 'Invalid input. All values must be numbers.' });
    }

    const score = calculateStudentEngagementScore(lab, lecture, support, canvas);
    res.json({ engagementScore: score });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
