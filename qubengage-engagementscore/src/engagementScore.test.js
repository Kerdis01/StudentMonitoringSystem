const request = require('supertest');
const app = require('./engagementScore'); // Ensure this path is correct

describe('GET /calculate_engagement_score', () => {
  test('calculates the engagement score correctly', async () => {
    const response = await request(app)
      .get('/calculate_engagement_score')
      .query({ lab: '10', lecture: '20', support: '30', canvas: '40' });

    expect(response.statusCode).toBe(200);
    expect(response.body).toHaveProperty('engagementScore');
  });

  test('returns 400 if parameters are missing', async () => {
    const response = await request(app)
      .get('/calculate_engagement_score')
      .query({ lab: '10', lecture: '20' }); // Omitting support and canvas parameters

    expect(response.statusCode).toBe(400);
    expect(response.body).toHaveProperty('error');
  });
});
