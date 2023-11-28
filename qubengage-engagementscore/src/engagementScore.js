

function calculateStudentEngagementScore(lab, lecture, support, canvas) {
    const totalHours = lab + lecture + support + canvas;
    
    const lectureWeight = 0.3;
    const labWeight = 0.4;
    const supportWeight = 0.15;
    const canvasWeight = 0.15;

    const lectureTotalWeighted = lecture * lectureWeight / totalHours;
    const labTotalWeighted = lab * labWeight / totalHours;
    const supportTotalWeighted = support * supportWeight / totalHours;
    const canvasTotalWeighted = canvas * canvasWeight / totalHours;

    const engagementScore = lectureTotalWeighted + labTotalWeighted + supportTotalWeighted + canvasTotalWeighted;

    return engagementScore;
}

// Example usage:
const labHours = 10;
const lectureHours = 15;
const supportHours = 5;
const canvasHours = 8;

const score = calculateStudentEngagementScore(labHours, lectureHours, supportHours, canvasHours);
console.log('Student Engagement Score:', score);
