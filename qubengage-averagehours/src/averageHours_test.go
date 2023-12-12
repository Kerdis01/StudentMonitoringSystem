package main

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestCalculateAverageHoursHandler(t *testing.T) {
	tests := []struct {
		name           string
		totalHours     string
		wantStatusCode int
		want           ResponseData // Changed from wantResponse string to want ResponseData
	}{
		{
			name:           "valid total hours",
			totalHours:     "20",
			wantStatusCode: http.StatusOK,
			want:           ResponseData{AverageHours: 5},
		},
		{
			name:           "missing total hours",
			totalHours:     "",
			wantStatusCode: http.StatusBadRequest,
			want:           ResponseData{},
		},
		{
			name:           "invalid total hours",
			totalHours:     "invalid",
			wantStatusCode: http.StatusBadRequest,
			want:           ResponseData{},
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			req, err := http.NewRequest("GET", "/calculate_average_hours", nil)
			if err != nil {
				t.Fatal(err)
			}

			q := req.URL.Query()
			q.Add("total_hours", tc.totalHours)
			req.URL.RawQuery = q.Encode()

			rr := httptest.NewRecorder()
			handler := http.HandlerFunc(calculateAverageHoursHandler)

			handler.ServeHTTP(rr, req)

			if status := rr.Code; status != tc.wantStatusCode {
				t.Errorf("handler returned wrong status code: got %v want %v",
					status, tc.wantStatusCode)
			}

			// Only attempt to unmarshal if the status code was OK
			if tc.wantStatusCode == http.StatusOK {
				var got ResponseData
				err := json.Unmarshal(rr.Body.Bytes(), &got)
				if err != nil {
					t.Fatal("unable to unmarshal response:", err)
				}
				if got != tc.want {
					t.Errorf("handler returned unexpected body: got %v want %v",
						got, tc.want)
				}
			}
		})
	}
}
