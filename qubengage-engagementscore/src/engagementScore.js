const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 4000; 

// Middleware
app.use(cors());
app.use(bodyParser.json());

function calculateStudentEngagementScore(lab, lecture, support, canvas) {

    lab = parseInt(lab)
    lecture = parseInt(lecture)
    support = parseInt(support)
    canvas = parseInt(canvas)

    const lectureTotalhours = 33
    const lectureWeight = 0.3;
    const labTotalHours = 22
    const labWeight = 0.4;
    const supportTotalHours = 44
    const supportWeight = 0.15;
    const canvasTotalHours = 55
    const canvasWeight = 0.15;

    const lectureTotalWeighted = lecture * lectureWeight / lectureTotalhours;
    const labTotalWeighted = lab * labWeight / labTotalHours;
    const supportTotalWeighted = support * supportWeight / supportTotalHours;
    const canvasTotalWeighted = canvas * canvasWeight / canvasTotalHours;

    engagementScore = (lectureTotalWeighted + labTotalWeighted + supportTotalWeighted + canvasTotalWeighted)*100;
    const engagementScore = Number(engagementScore.toFixed(2))

    return engagementScore;
}

// GET endpoint for calculating student engagement score
app.get('/calculate_engagement_score', (req, res) => {
    const { lab, lecture, support, canvas } = req.query;

    // Check if all required parameters are provided
    if (!lab || !lecture || !support || !canvas) {
        return res.status(400).json({ error: 'Please provide values for lab, lecture, support, and canvas.' });
    }

    // Calculate the engagement score using the provided parameters
    const engagementScore = calculateStudentEngagementScore(lab, lecture, support, canvas);

    // Send the calculated engagement score as the response
    res.json({ engagementScore });
});

// Start the server
if (process.env.NODE_ENV !== 'test') {
    app.listen(port, () => {
        console.log(`Server is running on port ${port}`);
    });
}

module.exports = app;
